#!/usr/bin/env python3
import json
import time
import signal
from pathlib import Path

try:
    import smbus2
except Exception:
    smbus2 = None

try:
    import RPi.GPIO as GPIO
except Exception:
    GPIO = None

CONFIG_PATH = Path(__file__).with_name("powerstack_config.json")

DEFAULT_CONFIG = {
    "gpio": {
        "power_hold": 27,
        "shutdown_detect": 17
    },
    "i2c": {
        "bus": 1,
        "ina219_addr": 0x40,
        "ds3231_addr": 0x68
    },
    "thresholds": {
        "low_battery_voltage": 3.4,
        "shutdown_voltage": 3.3,
        "poll_interval_s": 2,
        "confirm_low_count": 3
    }
}

class FakeGPIO:
    BCM = OUT = IN = PUD_UP = LOW = 0
    HIGH = 1
    _pins = {}

    @classmethod
    def setmode(cls, *a, **k):
        pass

    @classmethod
    def setup(cls, pin, mode, pull_up_down=None):
        cls._pins[pin] = 0

    @classmethod
    def output(cls, pin, value):
        cls._pins[pin] = int(bool(value))

    @classmethod
    def input(cls, pin):
        return cls._pins.get(pin, 1)

    @classmethod
    def cleanup(cls):
        cls._pins.clear()

class PowerStack:
    def __init__(self, config=None):
        self.cfg = config or DEFAULT_CONFIG
        self.bus = None
        self.stop = False
        self.low_count = 0
        self.gpio = GPIO or FakeGPIO
        if smbus2 is not None:
            try:
                self.bus = smbus2.SMBus(self.cfg["i2c"]["bus"])
            except Exception:
                self.bus = None

    def setup_gpio(self):
        self.gpio.setmode(self.gpio.BCM)
        self.gpio.setup(self.cfg["gpio"]["power_hold"], self.gpio.OUT)
        self.gpio.setup(self.cfg["gpio"]["shutdown_detect"], self.gpio.IN, pull_up_down=self.gpio.PUD_UP)
        self.gpio.output(self.cfg["gpio"]["power_hold"], self.gpio.HIGH)

    def read_shutdown_request(self):
        return self.gpio.input(self.cfg["gpio"]["shutdown_detect"]) == 0

    def read_ina219_bus_voltage(self):
        return None

    def should_shutdown(self):
        if self.read_shutdown_request():
            return True
        v = self.read_ina219_bus_voltage()
        if v is None:
            return False
        if v <= self.cfg["thresholds"]["low_battery_voltage"]:
            self.low_count += 1
        else:
            self.low_count = 0
        return self.low_count >= self.cfg["thresholds"]["confirm_low_count"] or v <= self.cfg["thresholds"]["shutdown_voltage"]

    def shutdown(self):
        self.gpio.output(self.cfg["gpio"]["power_hold"], self.gpio.LOW)

    def run(self):
        self.setup_gpio()
        try:
            while not self.stop:
                if self.should_shutdown():
                    self.shutdown()
                    break
                time.sleep(self.cfg["thresholds"]["poll_interval_s"])
        finally:
            self.gpio.cleanup()

def load_config():
    if CONFIG_PATH.exists():
        return json.loads(CONFIG_PATH.read_text())
    return DEFAULT_CONFIG

def main():
    p = PowerStack(load_config())

    def _sig(*_):
        p.stop = True

    signal.signal(signal.SIGINT, _sig)
    signal.signal(signal.SIGTERM, _sig)
    p.run()

if __name__ == "__main__":
    main()