# Build a Marlin
[![Marlin Repo](https://img.shields.io/github/v/release/MarlinFirmware/Marlin?label=%20Marlin%20Version)](https://github.com/MarlinFirmware/Marlin)
[![Buy Me A Coffee](https://www.buymeacoffee.com/assets/img/custom_images/yellow_img.png)](https://www.buymeacoffee.com/pp8mnskrg2f)


[Marlin](https://github.com/MarlinFirmware/Marlin) comes pre-installed on most 3D printers and for non-programmers this can be a pain to build. Building is useful for those who want up to date firmware or features which aren't usually enabled.

Build A Marlin will download the latest supported Marlin, apply a selected configuration and build the firmware to flash onto your printer.

Feel free to [open an issue](https://github.com/markrossington/build-a-marlin/issues/new) if you are having problems.

# Disclaimer
I offer no warranty, support or guarantees. Any changes to your 3D printer firmware and the consequences of these changes are your responsibility. If you do not understand what you are doing then I suggest you do not continue.

# Lets just do this

## Build the Firmware

 1. Clone or [download a zip](https://github.com/markrossington/build-a-marlin/archive/refs/heads/main.zip) of this repository
 2. Unzip to a folder, for example: 
    * Windows: `C:/build-a-marlin/` 
    * Linux/Mac: `~/build-a-marlin/`
 3. Ensure you have Python 3.x installed. [Download here](https://www.python.org/downloads/).
 4. Open a command prompt on Windows or terminal on Linux/Mac
 5. Type (Note this is the same folder as in step 2): 
    * Windows: `cd C:/build-a-marlin/` 
    * Linux/Mac: `cd ~/build-a-marlin/` 
 6. Type:
    * Windows `python scripts/marlin_build.py`
    * Linux/Mac: `python3 scripts/marlin_build.py`
 7. There will be a lot of text flying past which is a good thing, once it's stopped firmware should be built and available in the `output` folder. Check for `firmware.bin`

# FAQ

  1. If you're going to flash a new firmware, why not just use [Klipper](https://www.klipper3d.org)?
     * Klipper will mean learning a whole new software ecosystem. This is a valuable learning project and **one I suggest to those who seek it**. However if you just want your printer to operate in the same way, but with better features: Marlin is the way to go. 
     * Feature wise Klipper used to be king, however the Marlin team are catching up with features such as linear advance and input shaping which are now both available. 
     * You absolutely need an additional computer (usually a Rapsberry Pi) constantly plugged into your printer. Not a problem for most of us who use Octoprint/OctoPi but still worth noting. Using Klipper your printer will not operate without this. 
     * The existing TFT screen will no longer work, there are great projects such as [Klipperscreen](https://klipperscreen.readthedocs.io) which will work with a screen plugged into your Raspberry Pi but this is extra hardware still. 
  2. Why Python and not X, Y or Z?
      * I wanted this to work on as many platforms as possible. Python allows for this and is often installed on many peoples machines anyway. It's worth noting that building Marlin doesn't work on a Raspberry Pi at this point in time, this is a limitation of the toolchains and nothing I can control.
 