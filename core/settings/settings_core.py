"""
- Creation Date: 01/27/2024 12:02 PM EST
- Last Updated: 05/25/2024 09:45 PM EDT
- Authors: Joseph Armstrong (armstrongjoseph08@gmail.com)
- file: `./core/settings/settings_core.py`
- Purpose: Core code for the settings of this application.
"""
###############################################################################
import json
import logging
from os import makedirs, mkdir
from os.path import exists, expanduser

from core.other.embedded import EmbeddedElements
from core.time import get_utc_and_local_time


class AppThemes:
    """ """
    def theme_names() -> list:
        """ """
        return [
            "Black",
            "Blue Mono",
            "Blue Purple",
            "Bright Colors",
            "Brown Blue",
            "Dark #1",
            "Dark #2",
            "Dark Amber",
            "Dark Black #1",
            "Dark Black #2",
            "Dark Blue #1",
            "Dark Blue #2",
            "Dark Blue #3",
            "Dark Blue #4",
            "Dark Blue #5",
            "Dark Blue #6",
            "Dark Blue #7",
            "Dark Blue #8",
            "Dark Blue #9",
            "Dark Blue #10",
            "Dark Blue #11",
            "Dark Blue #12",
            "Dark Blue #13",
            "Dark Blue #14",
            "Dark Blue #15",
            "Dark Blue #16",
            "Dark Blue #17",
            "Dark Blue #18",
            "Dark Brown #1",
            "Dark Brown #2",
            "Dark Brown #3",
            "Dark Brown #4",
            "Dark Brown #5",
            "Dark Brown #6",
            "Dark Brown #7",
            "Dark Brown #8",
            "Dark Green #1",
            "Dark Green #2",
            "Dark Green #3",
            "Dark Green #4",
            "Dark Green #5",
            "Dark Green #6",
            "Dark Green #7",
            "Dark Green #8",
            "Dark Grey #1",
            "Dark Grey #2",
            "Dark Grey #3",
            "Dark Grey #4",
            "Dark Grey #5",
            "Dark Grey #6",
            "Dark Grey #7",
            "Dark Grey #8",
            "Dark Grey #9",
            "Dark Grey #10",
            "Dark Grey #11",
            "Dark Grey #12",
            "Dark Grey #13",
            "Dark Grey #14",
            "Dark Grey #15",
            "Dark Grey #16",
            "Dark Purple #1",
            "Dark Purple #2",
            "Dark Purple #3",
            "Dark Purple #4",
            "Dark Purple #5",
            "Dark Purple #6",
            "Dark Purple #7",
            "Dark Purple #8",
            "Dark Red #1",
            "Dark Red #2",
            "Dark Red #3",
            "Dark Tan Blue",
            "Dark Teal #1",
            "Dark Teal #2",
            "Dark Teal #3",
            "Dark Teal #4",
            "Dark Teal #5",
            "Dark Teal #6",
            "Dark Teal #7",
            "Dark Teal #8",
            "Dark Teal #9",
            "Dark Teal #10",
            "Dark Teal #11",
            "Dark Teal #12",
            "Dark Teal #13",
            "Default",
            "GrayGrayGray",
            "Green",
            "Green Mono",
            "Green Tan",
            "Hot Dog Stand",
            "Kayak",
            "Light Blue #1",
            "Light Blue #2",
            "Light Blue #3",
            "Light Blue #4",
            "Light Blue #5",
            "Light Blue #6",
            "Light Blue #7",
            "Light Blue #8",
            "Light Brown #1",
            "Light Brown #2",
            "Light Brown #3",
            "Light Brown #4",
            "Light Brown #5",
            "Light Brown #6",
            "Light Brown #7",
            "Light Brown #8",
            "Light Brown #9",
            "Light Brown #10",
            "Light Brown #11",
            "Light Brown #12",
            "Light Brown #13",
            "Light Brown #14",
            "Light Gray",
            "Light Green #1",
            "Light Green #2",
            "Light Green #3",
            "Light Green #4",
            "Light Green #5",
            "Light Green #6",
            "Light Green #7",
            "Light Green #8",
            "Light Green #9",
            "Light Green #10",
            "Light Green #11",
            "Light Grey #1",
            "Light Grey #2",
            "Light Grey #3",
            "Light Grey #4",
            "Light Grey #5",
            "Light Grey #6",
            "Light Grey #7",
            "Light Purple",
            "Light Teal",
            "Light Yellow",
            "Material #1",
            "Material #2",
            "Neutral Blue",
            "Purple",
            "Python",
            "Python Plus",
            "Reddit",
            # "Reds",
            # "Sandy Beach",
            # "System Default",
            # "System Default Alt",
            # "System Default For Reals",
            # "Tan",
            # "Tan Blue",
            # "Teal Mono",
        ]

    def theme_conversion_dictionary() -> dict:
        """ """
        return {
            "Black": "Black",
            "Blue Mono": "BlueMono",
            "Blue Purple": "BluePurple",
            "Bright Colors": "BrightColors",
            "Brown Blue": "BrownBlue",
            "Dark #1": "Dark",
            "Dark #2": "Dark2",
            "Dark Amber": "DarkAmber",
            "Dark Black #1": "DarkBlack",
            "Dark Black #2": "DarkBlack1",
            "Dark Blue #1": "DarkBlue",
            "Dark Blue #2": "DarkBlue1",
            "Dark Blue #3": "DarkBlue2",
            "Dark Blue #4": "DarkBlue3",
            "Dark Blue #5": "DarkBlue4",
            "Dark Blue #6": "DarkBlue5",
            "Dark Blue #7": "DarkBlue6",
            "Dark Blue #8": "DarkBlue7",
            "Dark Blue #9": "DarkBlue8",
            "Dark Blue #10": "DarkBlue9",
            "Dark Blue #11": "DarkBlue10",
            "Dark Blue #12": "DarkBlue11",
            "Dark Blue #13": "DarkBlue12",
            "Dark Blue #14": "DarkBlue13",
            "Dark Blue #15": "DarkBlue14",
            "Dark Blue #16": "DarkBlue15",
            "Dark Blue #17": "DarkBlue16",
            "Dark Blue #18": "DarkBlue17",
            "Dark Brown #1": "DarkBrown",
            "Dark Brown #2": "DarkBrown1",
            "Dark Brown #3": "DarkBrown2",
            "Dark Brown #4": "DarkBrown3",
            "Dark Brown #5": "DarkBrown4",
            "Dark Brown #6": "DarkBrown5",
            "Dark Brown #7": "DarkBrown6",
            "Dark Brown #8": "DarkBrown7",
            "Dark Green #1": "DarkGreen",
            "Dark Green #2": "DarkGreen1",
            "Dark Green #3": "DarkGreen2",
            "Dark Green #4": "DarkGreen3",
            "Dark Green #5": "DarkGreen4",
            "Dark Green #6": "DarkGreen5",
            "Dark Green #7": "DarkGreen6",
            "Dark Green #8": "DarkGreen7",
            "Dark Grey #1": "DarkGrey",
            "Dark Grey #2": "DarkGrey1",
            "Dark Grey #3": "DarkGrey2",
            "Dark Grey #4": "DarkGrey3",
            "Dark Grey #5": "DarkGrey4",
            "Dark Grey #6": "DarkGrey5",
            "Dark Grey #7": "DarkGrey6",
            "Dark Grey #8": "DarkGrey7",
            "Dark Grey #9": "DarkGrey8",
            "Dark Grey #10": "DarkGrey9",
            "Dark Grey #11": "DarkGrey10",
            "Dark Grey #12": "DarkGrey11",
            "Dark Grey #13": "DarkGrey12",
            "Dark Grey #14": "DarkGrey13",
            "Dark Grey #15": "DarkGrey14",
            "Dark Grey #16": "DarkGrey15",
            "Dark Purple #1": "DarkPurple",
            "Dark Purple #2": "DarkPurple1",
            "Dark Purple #3": "DarkPurple2",
            "Dark Purple #4": "DarkPurple3",
            "Dark Purple #5": "DarkPurple4",
            "Dark Purple #6": "DarkPurple5",
            "Dark Purple #7": "DarkPurple6",
            "Dark Purple #8": "DarkPurple7",
            "Dark Red #1": "DarkRed",
            "Dark Red #2": "DarkRed1",
            "Dark Red #3": "DarkRed2",
            "Dark Tan Blue": "DarkTanBlue",
            "Dark Teal #1": "DarkTeal",
            "Dark Teal #2": "DarkTeal1",
            "Dark Teal #3": "DarkTeal2",
            "Dark Teal #4": "DarkTeal3",
            "Dark Teal #5": "DarkTeal4",
            "Dark Teal #6": "DarkTeal5",
            "Dark Teal #7": "DarkTeal6",
            "Dark Teal #8": "DarkTeal7",
            "Dark Teal #9": "DarkTeal8",
            "Dark Teal #10": "DarkTeal9",
            "Dark Teal #11": "DarkTeal10",
            "Dark Teal #12": "DarkTeal11",
            "Dark Teal #13": "DarkTeal12",
            "Default": "Default",
            "GrayGrayGray": "GrayGrayGray",
            "Green": "Green",
            "Green Mono": "GreenMono",
            "Green Tan": "GreenTan",
            "Hot Dog Stand": "HotDogStand",
            "Kayak": "Kayak",
            "Light Blue #1": "LightBlue",
            "Light Blue #2": "LightBlue1",
            "Light Blue #3": "LightBlue2",
            "Light Blue #4": "LightBlue3",
            "Light Blue #5": "LightBlue4",
            "Light Blue #6": "LightBlue5",
            "Light Blue #7": "LightBlue6",
            "Light Blue #8": "LightBlue7",
            "Light Brown #1": "LightBrown",
            "Light Brown #2": "LightBrown1",
            "Light Brown #3": "LightBrown2",
            "Light Brown #4": "LightBrown3",
            "Light Brown #5": "LightBrown4",
            "Light Brown #6": "LightBrown5",
            "Light Brown #7": "LightBrown6",
            "Light Brown #8": "LightBrown7",
            "Light Brown #9": "LightBrown8",
            "Light Brown #10": "LightBrown9",
            "Light Brown #11": "LightBrown10",
            "Light Brown #12": "LightBrown11",
            "Light Brown #13": "LightBrown12",
            "Light Brown #14": "LightBrown13",
            "Light Gray": "LightGray1",
            "Light Green #1": "LightGreen",
            "Light Green #2": "LightGreen1",
            "Light Green #3": "LightGreen2",
            "Light Green #4": "LightGreen3",
            "Light Green #5": "LightGreen4",
            "Light Green #6": "LightGreen5",
            "Light Green #7": "LightGreen6",
            "Light Green #8": "LightGreen7",
            "Light Green #9": "LightGreen8",
            "Light Green #10": "LightGreen9",
            "Light Green #11": "LightGreen10",
            "Light Grey #1": "LightGrey",
            "Light Grey #2": "LightGrey1",
            "Light Grey #3": "LightGrey2",
            "Light Grey #4": "LightGrey3",
            "Light Grey #5": "LightGrey4",
            "Light Grey #6": "LightGrey5",
            "Light Grey #7": "LightGrey6",
            "Light Purple": "LightPurple",
            "Light Teal": "LightTeal",
            "Light Yellow": "LightYellow",
            "Material #1": "Material1",
            "Material #2": "Material2",
            "Neutral Blue": "NeutralBlue",
            "Purple": "Purple",
            "Python": "Python",
            "Python Plus": "PythonPlus",
            "Reddit": "Reddit",
            # "Reds": "",
            # "Sandy Beach": "",
            # "System Default": "",
            # "System Default Alt": "",
            # "System Default For Reals": "",
            # "Tan": "",
            # "Tan Blue": "",
            # "Teal Mono": "",
        }


class AppSettings:
    """ """
    def __init__(self) -> None:
        """ """
        pass

    def generate_settings_data(self) -> dict:
        """
        Holds the default settings dictionary for this application.
        """

        home_dir = expanduser("~")
        home_dir = home_dir.replace("\\", "/")
        home_dir = f"{home_dir}/.sdv_pbp_fb"

        if exists(home_dir):
            pass
        else:
            logging.warning(
                "%s doesn't exist. ", home_dir +
                "Attempting to create the directory."
            )
            try:
                makedirs(home_dir)
            except Exception as e:
                logging.critical("An unhandled exception has occurred %e", e)
                raise NotADirectoryError(
                    "A directory for housing application " +
                    "data could not be made at \n"
                    + home_dir
                    + ".\nThis is a critical error, " +
                    "and the application must shut down.\n"
                    + "Full exception: "
                    + e
                )

        now_formatted, utc_time_formatted = get_utc_and_local_time()
        # print()
        default_settings = {
            "app_version": EmbeddedElements.app_version(),
            # Could be a feature in the future where someone could
            # chart out a historical game, and be able upload the
            # game's JSON file directly through GitHub.
            "app_theme": "DarkBlack",
            "user_identity": {
                "internet_identity": "Anonymous_Person",
                "first_name": None,
                "last_name": None,
                "contact": None,
                "github_username": None,
                "twitter_handle": None,
                "reddit_username": None,
                "email": None,
            },
            # This will default to ./{home}/.fb_pbp/
            "data": {
                "data_directory": home_dir,
                "sql_directory": home_dir,
                "sql_language": "sqlite",
                # Probably something to implement in the future
                "debug_log_to_file": False
            },
            "last_opened": now_formatted,
            "last_opened_utc": utc_time_formatted,
            "show_menubar": True,
            "defaults": {
                "default_league": "DEFL",
                "default_season": 2019,
                "default_team": "-ALL-",
                "default_week": 1
            },
        }
        return default_settings

    def load_settings(self) -> dict:
        """
        Loads the settings for this app,
        and re-creates the settings file if it doesn't exist.
        """
        home_dir = expanduser("~")

        try:
            mkdir(f"{home_dir}/.sdv_pbp_fb/")
        except FileExistsError:
            logging.info(f"{home_dir}/.sdv_pbp_fb/ already exists.")

        try:
            with open(f"{home_dir}/.sdv_pbp_fb/settings.json", "r") as f:
                json_str = f.read()
        except FileNotFoundError:
            logging.warning(
                "Settings file not found in "
                + f"`{home_dir}/.sdv_pbp_fb/`."
                + "Attempting to create a settings file."
            )
            self.create_settings_file()
            with open(f"{home_dir}/.sdv_pbp_fb/settings.json", "r") as f:
                json_str = f.read()

        json_arr = json.loads(json_str)

        now_formatted, utc_time_formatted = get_utc_and_local_time()
        json_arr["last_opened"] = now_formatted
        json_arr["last_opened_utc"] = utc_time_formatted
        return json_arr

    def create_settings_file(self) -> None:
        """ """
        settings_dict = self.generate_settings_data()

        home_dir = expanduser("~")
        home_dir = home_dir.replace("\\", "/")
        home_dir = f"{home_dir}/.sdv_pbp_fb"

        if exists(home_dir):
            pass
        else:
            logging.warning(
                f"{home_dir} doesn't exist. " +
                "Attempting to create the directory."
            )
            try:
                makedirs(home_dir)
            except Exception as e:
                logging.critical(f"An unhandled exception has occurred {e}")
                raise NotADirectoryError(
                    "A directory for housing application " +
                    "data could not be made at \n"
                    + home_dir
                    + ".\nThis is a critical error, " +
                    "and the application must shut down.\n"
                    + "Full exception: "
                    + e
                )

        with open(f"{home_dir}/settings.json", "w+") as f:
            f.write(json.dumps(settings_dict, indent=4))

    def save_settings(self, settings: dict):
        """ """
        home_dir = expanduser("~")

        try:
            mkdir(f"{home_dir}/.sdv_pbp_fb/")
        except FileExistsError:
            logging.info(f"{home_dir}/.sdv_pbp_fb/ already exists.")

        # with open(f"{home_dir}/.sdv_pbp_fb/settings.json", "w+") as f:
        #     f.write(
        #         json.dumps(
        #             settings,
        #             indent=4
        #         )
        #     )

        try:
            with open(f"{home_dir}/.sdv_pbp_fb/settings.json", "w+") as f:
                f.write(
                    json.dumps(
                        settings,
                        indent=4
                    )
                )
        except Exception as e:
            logging.critical(
                "Unhandled exception. "
                + "Could not write to settings file. "
                + f"Exception: {e}"
            )


if __name__ == "__main__":
    print(AppSettings.load_settings())
