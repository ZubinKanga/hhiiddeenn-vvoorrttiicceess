# hhiiddddeenn vvoorrttiicceess
## Rollercoaster simulator connector

This repository contains files to connect the rollercoaster simulation software [No Limits 2](https://www.nolimitscoaster.com/) to the iOS metronome app [The Metronome by Soundbrenner](https://www.soundbrenner.com/the-metronome-app/), with the goal to translate rollercoaster ride information like speed to metronome attributes like BPM. 

## Prerequisites

In order to run this software, you need to run a copy of [No Limits 2 on Steam](https://store.steampowered.com/app/301320/NoLimits_2_Roller_Coaster_Simulation/) on a computer running macOS. 

You also need to have Python 3 installed on your system. With newer versions of macOS, Python comes pre-installed, but may have the wrong version 2.7. If you have trouble running the script below, refer to "[Using Python on a Macintosh](https://docs.python.org/3/using/mac.html)". I recommend [pyenv](https://github.com/pyenv/pyenv) to keep track of all installed Python versions.

The script uses a library called `python-osc` which needs to be installed on your computer. You can install it using the Python package manager `pip` to install this dependency system-wide:

```
python3 -m pip install python-osc
```

## Usage


### No Limits 2
In Steam, right-click the installed No Limits 2 game and choose "Properties…". 

Under "Launch Options", enter

```
--telemetry --telemetryport=15151
```

Then start the game. 

### OSC Server
Open the Terminal application in Application > Utilities > Terminal. Navigate to a clone of this repository on your local harddrive. 
Run the Python script to receive the telemetry data from No Limits 2 and translate it to an [Open Sound Control](https://en.wikipedia.org/wiki/Open_Sound_Control) server by typing 

```
python hhvv_nl2_to_osc.py
```
and confirming with Enter.

### Max Patch

You can now open the [Max 8](https://cycling74.com/products/max) patch `hhvv_osc_to_midi.maxpat`. Its job is it to receive the OSC data and transform the speed value into a simple metronome. The metronome ticks are sent as individual MIDI note commands to an iPhone running The Metronome by Soundbrenner.

### MIDI Connection
For the The Metronome by Soundbrenner to receive the MIDI command, you need to connect the iOS device using a USB cable (Bluetooth MIDI is not recommended). Open the Audio MIDI Setup application under Applications > Utilities, navigate to the Audio Devices screen (⌘+1) and enable the iOS device for MIDI communication via USB by clicking the "Enable" button.
Inside The Metronome by Soundbrenner, navigate to the Settings tab and into the App Settings > MIDI. Select the MIDI Input IDEM Host (should be the only one) to receive MIDI commands.
