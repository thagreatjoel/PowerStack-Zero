from daemon import PowerStack, DEFAULT_CONFIG, FakeGPIO

class Dummy:
    def __init__(self, v=None, req=False):
        self.v = v
        self.req = req
        self.cfg = DEFAULT_CONFIG
        self.gpio = FakeGPIO
        self.low_count = 0

    def read_shutdown_request(self):
        return self.req

    def read_ina219_bus_voltage(self):
        return self.v


def test_shutdown_request_triggers():
    p = Dummy(req=True)
    assert PowerStack.should_shutdown(p)


def test_low_voltage_requires_confirmation():
    p = Dummy(v=3.35)
    assert not PowerStack.should_shutdown(p)
    assert not PowerStack.should_shutdown(p)
    assert PowerStack.should_shutdown(p)


def test_immediate_critical_voltage():
    p = Dummy(v=3.2)
    assert PowerStack.should_shutdown(p)