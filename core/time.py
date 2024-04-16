"""
# Creation Date: 02/11/2024 11:30 AM EDT
# Last Updated: 04/15/2024 10:25 AM EDT
# Authors: Joseph Armstrong (armstrongjoseph08@gmail.com)
# file: `./core/time.py`
# Purpose: Core code for the settings of this application.
###############################################################################
"""
from datetime import datetime, timezone

from tzlocal import get_localzone


def get_utc_and_local_time() -> datetime:
    """ """
    local_timezone = get_localzone()

    now = datetime.now()
    now = now.replace(tzinfo=local_timezone)
    utc_time = datetime.now(timezone.utc)
    now_formatted = now.isoformat()
    utc_time_formatted = utc_time.isoformat()

    return now_formatted, utc_time_formatted
