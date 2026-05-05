# ==== PlatformIO Settings ====
pio_download_url = "https://raw.githubusercontent.com/platformio/platformio-core-installer/master/get-platformio.py"

# ==== Building Marlin ====
marlin_ref = "cfbd8a2e3665585cecb749de6428c749f833273f"  # latest commit tested on bugfix-2.1.x
marlin_download_url = f"https://github.com/MarlinFirmware/Marlin/archive/{marlin_ref}.zip"

# This is the PlatformIO target (i.e. which board to build for)
# Artillery_Ruby is the name of the Artillery 3D 32bit printer mainboard
# This is good for: Artillery X1, X2, Genius, Genius Pro and Hornet printers
platformio_target = "Artillery_Ruby"

# Configuration sources can be remote URLs or local file paths.
# The defaults point to the Marlin project Artillery Sidewinder X2 example configuration.
configuration_h_source = "https://github.com/MarlinFirmware/Configurations/raw/bugfix-2.1.x/config/examples/Artillery/Sidewinder%20X2/Configuration.h"
configuration_adv_h_source = "https://github.com/MarlinFirmware/Configurations/raw/bugfix-2.1.x/config/examples/Artillery/Sidewinder%20X2/Configuration_adv.h"

# If the configurations live in a private GitHub repo, add your PAT here.
personal_access_token = ""  # Leave blank for public repos.
