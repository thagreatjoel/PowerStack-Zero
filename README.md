<div align="left" style="position: relative;">
  <img src="./images/logo.png" align="left" width="357" style="margin: 0 20px 0 0;">

  <div>
    <img src="./images/title1.png" alt="POWERSTACK ZERO" width="430" height="50">
    <p align="left">
      <em><code>❯ Raspberry Pi Zero 2W Smart UPS and Expansion Board</code></em>
    </p>
    <div>
      <a href="https://www.kicad.org/" style="margin-right: 15px; display: inline-block;">
        <img align="center" src="https://img.shields.io/badge/KiCad-2B5FC3?style=for-the-badge&logo=kicad&logoColor=white" style="border-radius: 30px;" alt="kicad">
      </a>
      <a href="https://easyeda.com/" style="margin-right: 15px; display: inline-block;">
        <img align="center" src="https://img.shields.io/badge/EasyEDA-1765F3?style=for-the-badge&logo=circuitboard&logoColor=white" style="border-radius: 30px;" alt="easyeda">
      </a>
        </a>
  <a href="https://www.raspberrypi.com/" style="display: inline-block;">
    <img align="center" src="https://img.shields.io/badge/Raspberry%20Pi-Zero%202W-A22846?style=for-the-badge&logo=raspberrypi&logoColor=white" style="border-radius: 30px;" alt="raspberry-pi">
  </a>
    </div>
    <br>
  <p align="left">
      A UPS and RTC system for Raspberry Pi Zero 2W, designed to provide stable power management, safe shutdown support, and future expansion with 4 USB ports for OTG use.
    </p>
  </div>
</div>
<br clear="left">


#  Getting Started

###  Usage

Run PowerStack-Zero as a Raspberry Pi Zero 2W UPS by connecting a battery and USB-C cable, then powering the Pi’s 5V/GND rail from the board.

Typical routine:
1. Charge the battery over USB-C.
2. Power runs from either the battery or external input.
3. INA219 monitors current and voltage.
4. The Pi can shut down safely with the MOSFET switch.
5. DS3231 keeps time and can handle wake-ups.


###  Testing

Run the test suite using the following command:

```sh
python3 -m pytest
```

Or, if you want to test hardware:
- Verify charging works.
- Check battery protection.
- Test 5V boost stability.
- Confirm INA219 readings.
- Make sure safe shutdown and RTC wake are reliable.

---

