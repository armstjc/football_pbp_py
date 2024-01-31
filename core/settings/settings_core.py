# Creation Date: 01/27/2024 12:02 PM EDT
# Updates:
# Authors: Joseph Armstrong (armstrongjoseph08@gmail.com)
# file: `./core/settings/settings_core.py`
# Purpose: Core code for the settings of this application.
################################################################################
from os.path import expanduser, exists
from os import makedirs
from datetime import datetime, timezone
import logging

from tzlocal import get_localzone


def generate_settings_data():
    """
    Holds the default settings dictionary for this application.
    """

    home_dir = expanduser("~")
    home_dir = home_dir.replace("\\", "/")
    home_dir = f"{home_dir}/.sdv_pbp"

    local_timezone = get_localzone()
    if exists(home_dir):
        pass
    else:
        logging.warning(f"{home_dir} doesn't exist. Attempting to create the directory.")
        try:
            makedirs(home_dir)
        except Exception as e:
            logging.critical(f"An unhandled exception has occured {e}")
            raise NotADirectoryError(
                "A directory for housing application data could not be made at \n"+
                home_dir+
                ".\nThis is a critical error, and the application must shut down.\n"+
                "Full exception: "+e
            )

    now = datetime.now()
    now = now.replace(tzinfo=local_timezone)
    utc_time = datetime.now(timezone.utc)
    now_formated = now.isoformat()
    utc_time_formated = utc_time.isoformat()
    
    # print()
    default_settings = {
        "app_version": "0.0.1",
        # Could be a feature in the future where someone could
        # chart out a historical game, and be able upload the
        # game's JSON file directly through GitHub.
        "user_identity": {
            "internet_identity": "Anonymous_Person",
            "first_name":None,
            "last_name":None,
            "contact":None,
            "github_username":None,
            "twitter_handle":None,
            "email": None
        },
        # This will default to ./{home}/.fb_pbp/
        "data": {
            "data_directory": home_dir,
            "sql_directory": home_dir,
            "sql_language": "sqlite",
        },
        "last_opened": now_formated,
        "last_opened_utc": utc_time_formated,
        "debug_log_to_file":False,

    }
    return default_settings


if __name__ == "__main__":
    settings_dict = generate_settings_data()
    print(settings_dict)
