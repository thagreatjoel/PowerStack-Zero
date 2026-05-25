
<div align="left" style="position: relative;">
  <img src="https://github.com/user-attachments/assets/59ad20dd-9f9b-4056-bc5f-69c52da3f1b7" align="left" width="357" style="margin: 0 20px 0 0;">

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

##  Usage

Run PowerStack-Zero as a Raspberry Pi Zero 2W UPS by connecting a battery and USB-C cable, then powering the Pi’s 5V/GND rail from the board.

Typical routine:
1. Charge the battery over USB-C.
2. Power runs from either the battery or external input.
3. INA219 monitors current and voltage.
4. The Pi can shut down safely with the MOSFET switch.
5. DS3231 keeps time and can handle wake-ups.

##  Installation
First, update your package list and install the GPIO library:

    sudo apt update
    sudo apt install python3-rpi.gpio

Next, clone the PowerStack-Zero repository and go to the firmware folder:

    git clone https://github.com/your-username/PowerStack-Zero.git
    cd PowerStack-Zero/Firmware

To start the daemon, run:
 
    python3 -u daemon.py

You’ll see the daemon fire up, set up GPIO, and go into its main loop. If you want to stop it safely, just hit Ctrl+C–that’ll kick off the cleanup process.
Watch for the loop to start and make sure GPIO initializes. When you exit, the cleanup should trigger properly. For hardware, check that charging works, battery protection engages, 5V boost stays stable, INA219 readings show up, and the daemon handles safe shutdowns.

## Project Structure

```sh
└── PowerStack-Zero/
    ├── Firmware/
    │   ├── __pycache__/
    │   ├── config.json
    │   ├── daemon.py
    │   ├── powerstack.service
    │   └── test_daemon.py
    ├── hardware/
    ├── docs/
    ├── LICENSE
    └── README.md
```



<h1 align="center">Layers</h1>
<div align="center"><img width="400" alt="Screenshot 2026-05-25 114533" src="https://github.com/user-attachments/assets/cc164947-622b-4c16-b0bf-31f212da57b7" /> <img width="402" alt="Screenshot 2026-05-25 114553" src="https://github.com/user-attachments/assets/039f7b22-fc7d-4370-8e5f-2f2daf245c32" />
</div>




<h1 align="center">Zine Page</h1>
<p align="center"><img width="500"" alt="Power Zine" src="https://github.com/user-attachments/assets/deea1ebb-6358-4765-b8e6-a19bc9d2a664" /></p>
