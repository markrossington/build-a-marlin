# ==== PlatformIO Settings ====
pio_download_url = "https://raw.githubusercontent.com/platformio/platformio-core-installer/master/get-platformio.py"

# ==== Building Marlin ====
marlin_version = "cfbd8a2e3665585cecb749de6428c749f833273f"  # latest commit tested on bugfix-2.1.x
marlin_download_url = f"https://github.com/MarlinFirmware/Marlin/archive/{marlin_version}.zip"

# This is the PlatformIO target (i.e. which board to build for)
# Artillery_Ruby is the name of the Artillery 3D 32bit printer mainboard
# This is good for: Artillery X1, X2, Genius, Genius Pro and Hornet printers
platformio_target = "Artillery_Ruby"

# Set to True if you want to use Configuration files from somewhere else, 
# you will need to specify marlin_configuration_h and marlin_configuration_adv_h below
# Set to False to use the default configuration found in the config/ folder
use_custom_config = False

# URL of Configuration.h file, only used if use_custom_config is True. This is the Marlin projects example.
marlin_configuration_h = "https://github.com/MarlinFirmware/Configurations/raw/bugfix-2.1.x/config/examples/Artillery/Sidewinder%20X2/Configuration.h"

# URL of Configuration_adv.h file, only used it use_custom_config is True. This is the Marlin projects example.
marlin_configuration_adv_h = "https://github.com/MarlinFirmware/Configurations/raw/bugfix-2.1.x/config/examples/Artillery/Sidewinder%20X2/Configuration_adv.h"

# If the configurations live in a private github repo, add your PAT here
personal_access_token = "" # Leave blank for public repos
