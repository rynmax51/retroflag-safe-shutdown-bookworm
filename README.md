# RetroFlag Safe Shutdown for Raspberry Pi OS Bookworm

Safe Shutdown Script for RetroFlag Cases (SuperPi Case tested)  
Designed for Raspberry Pi OS Bookworm (Debian 12) and newer GPIO handling.

---

## What This Project Does
- Provides clean shutdown support for RetroFlag Pi cases using physical power and reset buttons
- Safely powers down the Raspberry Pi to prevent SD card corruption
- Blinks the case's LED when the shutdown button is pressed
- Offers optional reset (reboot) button functionality

This version is **tested with the RetroFlag SuperPi Case** on a **Raspberry Pi 3B+** running **Raspberry Pi OS Bookworm**.

---

## Supported Hardware
- [SUPERPi CASE-U](https://retroflag.com/SUPERPi-CASE-U.html) ✅
- (Other RetroFlag cases like Nespi+, MegaPi, and Nespi 4 may work but are untested)

✅ **IMPORTANT:**  
Make sure the **"SAFE SHUTDOWN"** switch inside your RetroFlag case is turned **ON**.

---

## Supported Systems
- Raspberry Pi OS **Bookworm** (Debian 12)
- Tested on Raspberry Pi **3B+**

**Note:**  
This script is intended for **standard Raspberry Pi OS**.  
It has not been tested on RetroPie, RecalBox, Batocera, or Lakka.

---

## Installation

First, make sure you are connected to the internet and SSH (or local terminal) into your Pi.

1. Clone this repository:
```bash
git clone https://github.com/rynmax51/retroflag-safe-shutdown-bookworm.git
cd retroflag-safe-shutdown-bookworm
```

2. Make the installer executable:
```bash
chmod +x retroflag-install.sh
```

3. Run the installer:
```bash
sudo ./retroflag-install.sh
```

✅ This will:
- Copy the SafeShutdown script to `/opt/RetroFlag/`
- Create and enable a systemd service
- Start the Safe Shutdown service immediately

---

## How It Works
- **Power button** pressed → LED blinks → Raspberry Pi shuts down safely
- **Reset button** pressed → Raspberry Pi reboots safely
- **Service** auto-starts at boot

---

## Credits and Acknowledgements

This project was developed with technical guidance and writing assistance from OpenAI's ChatGPT, based on testing and integration on a Raspberry Pi 3B+ using a RetroFlag [SUPERPi CASE-U](https://retroflag.com/SUPERPi-CASE-U.html).

The original [RetroFlag Pi Case scripts](https://github.com/RetroFlag/retroflag-picase) were used as a starting point. However, during testing, it was discovered that the official scripts did not work correctly on Raspberry Pi OS Bookworm (Debian 12) due to system changes. This project adapts and updates the functionality to be compatible with Bookworm and newer GPIO handling.

Special thanks to the open-source community for providing the original inspiration.

---
