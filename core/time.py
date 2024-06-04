"""
# Creation Date: 02/11/2024 11:30 AM EDT
# Last Updated: 06/04/2024 03:25 PM EDT
# Authors: Joseph Armstrong (armstrongjoseph08@gmail.com)
# file: `./core/time.py`
# Purpose: Core code for the settings of this application.
###############################################################################
"""

from datetime import datetime, timezone

import pytz
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


def convert_datetime_into_utc_time(
    date_str: str,
    time_str: str,
    timezone: str
) -> str:
    """ """
    tzinfo_tz = pytz.timezone(timezone)
    utc_tz = pytz.timezone("Etc/UCT")
    datetime_formatted = datetime.strptime(
        f"{date_str}T{time_str}",
        "%Y-%m-%dT%H:%M"
    )
    datetime_formatted = datetime_formatted.replace(
        tzinfo=tzinfo_tz
    )
    day_formatted = datetime_formatted.strftime("%A")
    utc_datetime = datetime_formatted.astimezone(utc_tz)
    datetime_formatted = datetime_formatted.isoformat()
    utc_datetime = utc_datetime.isoformat()

    return utc_datetime, datetime_formatted, day_formatted


if __name__ == "__main__":
    date_str = "2020-01-01"
    time_str = "01:01"
    timezone_str = "America/New_York"
    dt, utc_dt, tz = convert_datetime_into_utc_time(
        date_str=date_str,
        time_str=time_str,
        timezone=timezone_str
    )
    print(dt)
    print(utc_dt)
    print(tz)
