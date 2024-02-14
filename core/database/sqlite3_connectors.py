# Creation Date: 02/10/2024 12:39 AM EDT
# Last Updated: 02/11/2024 11:50 AM EST
# Authors: Joseph Armstrong (armstrongjoseph08@gmail.com)
# file: `./core/settings/sqlite3_connectors.py`
# Purpose: Core code for the settings of this application.
###############################################################################
import logging
import sqlite3
from os.path import expanduser

from core.database.create_db_elements import create_app_sqlite3_db


def initialize_sqlite3_connectors(custom_dir: str = None):
    """
    asdf
    """
    home_dir = expanduser("~")
    sql_dir = ""
    if custom_dir is not None:
        sql_dir = custom_dir
    else:
        sql_dir = home_dir

    try:
        con = sqlite3.connect(f"{sql_dir}/.sdv_pbp/sdv_pbp_py.sqlite")
        cur = con.cursor()
    except sqlite3.OperationalError as e:
        create_app_sqlite3_db(custom_dir)
        logging.warning(
            "A SQLite3 Operational Error has been raised. " + f"Reason: {e}"
        )
        con = sqlite3.connect(f"{sql_dir}/.sdv_pbp/sdv_pbp_py.sqlite")
        cur = con.cursor()

    return con, cur
