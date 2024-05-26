"""
- Creation Date: 02/03/2024 02:54 PM EST
- Last Updated: 05/25/2024 09:45 PM EDT
- Author: Joseph Armstrong (armstrongjoseph08@gmail.com)
- File Name: ./core/database/create_sdv_pbp_db.py
- Purpose: Loads in data used by this application,
-   and rebuilds tables if data is lost/corrupted.
"""

###############################################################################

import logging
import sqlite3
from os.path import expanduser

import polars as pl

from core.database.create_db_elements import (
    SqliteSampleFiles, create_app_sqlite3_db
)

# class verify_db_integrity:
#     """ """

#     def __init__(self,db_engine:str) -> None:
#         if db_engine == "sqlite3":
#             self.validate_sqlite3_tables()


class SqliteLoadData:
    """ """

    def load_iso_nations(
        con: sqlite3.Connection, cur: sqlite3.Cursor
    ) -> pl.DataFrame:
        """ """
        try:
            df = pl.read_database(
                query="SELECT * FROM iso_nations",
                connection=cur,
                schema_overrides={
                    "nation_name": pl.String,
                    "nation_iso_alpha_2": pl.String,
                    "nation_iso_alpha_3": pl.String,
                    "nation_iso_numeric": pl.UInt16,
                    "iso_3166_2": pl.String,
                    "region": pl.String,
                    "subregion": pl.String,
                    "intermediate_region": pl.String,
                    "region_code": pl.UInt16,
                    "subregion_code": pl.UInt16,
                    "intermediate_region_code": pl.UInt16,
                },
            )
        except sqlite3.OperationalError as e:
            logging.warning(
                f"A SQLite3 Operational Error has been raised. Reason {e}"
            )
            cur.executescript(SqliteSampleFiles.iso_nations())
            con.commit()

            df = pl.read_database(
                query="SELECT * FROM iso_nations",
                connection=cur,
                schema_overrides={
                    "nation_name": pl.String,
                    "nation_iso_alpha_2": pl.String,
                    "nation_iso_alpha_3": pl.String,
                    "nation_iso_numeric": pl.UInt16,
                    "iso_3166_2": pl.String,
                    "region": pl.String,
                    "subregion": pl.String,
                    "intermediate_region": pl.String,
                    "region_code": pl.UInt16,
                    "subregion_code": pl.UInt16,
                    "intermediate_region_code": pl.UInt16,
                },
            )
        except Exception as e:
            logging.critical("An unhandled exception has occurred: %e", e)
            raise e

        if len(df) < 1:
            logging.error(
                "[sqlite3].[dbo].[iso_nations] has no data. "
                + "Recreating database table."
            )
        return df

    def load_iso_states(
        con: sqlite3.Connection, cur: sqlite3.Cursor
    ) -> pl.DataFrame:
        """ """
        try:
            df = pl.read_database(
                query="SELECT * FROM iso_3166_2",
                connection=cur,
                schema_overrides={
                    "nation_iso_alpha_2": pl.String,
                    "nation_iso_alpha_3": pl.String,
                    "nation_iso_numeric": pl.UInt16,
                    "subdivision_iso_3166_2_code": pl.String,
                    "subdivision_name": pl.String,
                    "subdivision_category": pl.String,
                    "subdivision_parent": pl.String,
                },
            )
        except sqlite3.OperationalError:
            logging.warning("A SQLite3 Operational Error has been raised. ")
            cur.executescript(SqliteSampleFiles.iso_3166_2_states())
            con.commit()
            cur.executescript(SqliteSampleFiles.iso_3166_2_data())
            con.commit()
            df = pl.read_database(
                query="SELECT * FROM iso_3166_2",
                connection=cur,
                schema_overrides={
                    "nation_iso_alpha_2": pl.String,
                    "nation_iso_alpha_3": pl.String,
                    "nation_iso_numeric": pl.UInt16,
                    "subdivision_iso_3166_2_code": pl.String,
                    "subdivision_name": pl.String,
                    "subdivision_category": pl.String,
                    "subdivision_parent": pl.String,
                },
            )
        except Exception as e:
            logging.critical("An unhandled exception has occurred: %e", e)
            raise e

        if len(df) < 1:
            # If for any reason
            logging.error(
                "[sqlite3].[dbo].[iso_3166_2] has no data. "
                + "Recreating database table."
            )
        return df

    def load_iso_timezones(
        con: sqlite3.Connection, cur: sqlite3.Cursor
    ) -> pl.DataFrame:
        """ """
        try:
            df = pl.read_database(
                query="SELECT * FROM iso_timezones",
                connection=cur,
                schema_overrides={
                    "timezone_name": pl.String,
                    "nation_iso_alpha_2": pl.String,
                },
            )
        except sqlite3.OperationalError:
            logging.warning(
                "A SQLite3 Operational Error has been raised. "
            )
            cur.executescript(SqliteSampleFiles.iso_timezones())
            con.commit()
            df = pl.read_database(
                query="SELECT * FROM iso_timezones",
                connection=cur,
                schema_overrides={
                    "timezone_name": pl.String,
                    "nation_iso_alpha_2": pl.String,
                },
            )
        except Exception as e:
            logging.critical("An unhandled exception has occurred: %e", e)
            raise e

        if len(df) < 1:
            logging.error(
                "[sqlite3].[dbo].[iso_timezones] has no data. "
                + "Recreating database table."
            )
        return df

    def load_leagues(
            con: sqlite3.Connection,
            cur: sqlite3.Cursor
    ) -> pl.DataFrame:
        """ """
        try:
            df = pl.read_database(
                query="SELECT * FROM fb_leagues",
                connection=cur,
                schema_overrides={
                    "league_id": pl.String,
                    "league_long_name": pl.String,
                    "league_short_name": pl.String,
                    "league_sport_type": pl.String,
                    # "league_default_sex": pl.String,
                    # "league_default_gender": pl.String,
                    "league_notes": pl.String,
                    "field_length": pl.UInt8,
                    "downs": pl.UInt8,
                    "first_down_yards": pl.UInt8,
                    "end_zone_length": pl.UInt8,
                    "kickoff_yardline": pl.UInt8,
                    "safety_kick_yardline": pl.UInt8,
                    "kickoff_touchback_yardline": pl.UInt8,
                    "punt_touchback_yardline": pl.UInt8,
                    "normal_touchback_yardline": pl.UInt8,
                    "kansas_ot_yardline": pl.UInt8,
                    "pat_yardline": pl.UInt8,
                    "1PC_yardline": pl.UInt8,
                    "2PC_yardline": pl.UInt8,
                    "3PC_yardline": pl.UInt8,
                    "quarters": pl.UInt8,
                    "timeouts_per_half": pl.UInt8,
                    "ot_period_seconds": pl.UInt16,
                    "game_seconds": pl.UInt16,
                    "half_seconds": pl.UInt16,
                    "quarter_seconds": pl.UInt16,
                    "ot_periods": pl.Int8,
                    "ot_periods_until_shootout": pl.Int8,
                    "min_xfl_ot_periods": pl.Int8,
                    "set_xfl_ot_periods": pl.Int8,
                    "touchdown_points": pl.UInt8,
                    "field_goal_points": pl.UInt8,
                    "safety_points": pl.UInt8,
                    "pat_points": pl.UInt8,
                    "pat_defense": pl.UInt8,
                    "pat_safety": pl.UInt8,
                    "players_on_field": pl.UInt8,
                    "xfl_pat": pl.Boolean,
                    "preseason_overtime_enabled": pl.Boolean,
                    "reg_season_ot_enabled": pl.Boolean,
                    "postseason_ot_enabled": pl.Boolean,

                    "preseason_ot_type": pl.String,
                    "reg_season_ot_type": pl.String,
                    "postseason_ot_type": pl.String,

                    "two_forward_passes": pl.Boolean,
                    "spikes_are_team_stats": pl.Boolean,
                    "sacks_are_rushes": pl.Boolean,
                    "kneeldowns_are_team_stats": pl.Boolean,
                    "kickoff_fc_always_goes_to_touchback": pl.Boolean,
                    "kickoffs_enabled": pl.Boolean,
                    "use_xfl_kickoff": pl.Boolean,
                    "drop_kick_enabled": pl.Boolean,
                    "drop_kick_bonus_point": pl.Boolean,
                    "fg_adds_ez_length": pl.Boolean,
                    "long_fg_bonus_point": pl.Boolean,
                    "xp_is_a_fg": pl.Boolean,
                    "rouges_enabled": pl.Boolean,
                    "punting_enabled": pl.Boolean,
                    "onside_punts_enabled": pl.Boolean,
                    "fair_catch_enabled": pl.Boolean,
                },
            )
        except sqlite3.OperationalError as e:
            logging.warning(
                "A SQLite3 Operational Error has been raised. " +
                f"Reason: {e}"
            )
            cur.executescript(SqliteSampleFiles.leagues_sql_file())
            con.commit()
            df = pl.read_database(
                query="SELECT * FROM fb_leagues",
                connection=cur,
                schema_overrides={
                    "league_id": pl.String,
                    "league_long_name": pl.String,
                    "league_short_name": pl.String,
                    "league_sport_type": pl.String,
                    "league_default_sex": pl.String,
                    "league_default_gender": pl.String,
                    "league_notes": pl.String,
                    "field_length": pl.UInt8,
                    "downs": pl.UInt8,
                    "first_down_yards": pl.UInt8,
                    "end_zone_length": pl.UInt8,
                    "kickoff_yardline": pl.UInt8,
                    "safety_kick_yardline": pl.UInt8,
                    "kickoff_touchback_yardline": pl.UInt8,
                    "punt_touchback_yardline": pl.UInt8,
                    "normal_touchback_yardline": pl.UInt8,
                    "kansas_ot_yardline": pl.UInt8,
                    "pat_yardline": pl.UInt8,
                    "1PC_yardline": pl.UInt8,
                    "2PC_yardline": pl.UInt8,
                    "3PC_yardline": pl.UInt8,
                    "quarters": pl.UInt8,
                    "timeouts_per_half": pl.UInt8,
                    "ot_period_seconds": pl.UInt16,
                    "game_seconds": pl.UInt16,
                    "half_seconds": pl.UInt16,
                    "quarter_seconds": pl.UInt16,
                    "ot_periods": pl.Int8,
                    "ot_periods_until_shootout": pl.Int8,
                    "min_xfl_ot_periods": pl.Int8,
                    "set_xfl_ot_periods": pl.Int8,
                    "touchdown_points": pl.UInt8,
                    "field_goal_points": pl.UInt8,
                    "safety_points": pl.UInt8,
                    "pat_points": pl.UInt8,
                    "pat_defense": pl.UInt8,
                    "pat_safety": pl.UInt8,
                    "players_on_field": pl.UInt8,
                    "preseason_ot_enabled": pl.Boolean,
                    "reg_season_ot_enabled": pl.Boolean,
                    "postseason_ot_enabled": pl.Boolean,

                    "preseason_ot_type": pl.String,
                    "reg_season_ot_type": pl.String,
                    "postseason_ot_type": pl.String,

                    "two_forward_passes": pl.Boolean,
                    "spikes_are_team_stats": pl.Boolean,
                    "sacks_are_rushes": pl.Boolean,
                    "kneeldowns_are_team_stats": pl.Boolean,
                    "kickoff_fc_always_goes_to_touchback": pl.Boolean,
                    "kickoffs_enabled": pl.Boolean,
                    "use_xfl_kickoff": pl.Boolean,
                    "drop_kick_enabled": pl.Boolean,
                    "drop_kick_bonus_point": pl.Boolean,
                    "fg_adds_ez_length": pl.Boolean,
                    "long_fg_bonus_point": pl.Boolean,
                    "xp_is_a_fg": pl.Boolean,
                    "rouges_enabled": pl.Boolean,
                    "punting_enabled": pl.Boolean,
                    "onside_punts_enabled": pl.Boolean,
                    "fair_catch_enabled": pl.Boolean,
                    "special_onside_play_enabled": pl.Boolean,
                },
            )
        except Exception as e:
            logging.critical(f"An unhandled exception has occurred: {e}")
            raise e

        if len(df) < 1:
            logging.error(
                "[sqlite3].[dbo].[fb_leagues] has no data. "
                + "Recreating database table."
            )
        return df

    def load_seasons(
            con: sqlite3.Connection,
            cur: sqlite3.Cursor
    ) -> pl.DataFrame:
        """ """
        try:
            df = pl.read_database(
                query="SELECT * FROM fb_seasons",
                connection=cur,
                schema_overrides={
                    "season": pl.UInt16,
                    "league_id": pl.String,
                    "season_notes": pl.String,
                    "field_length": pl.UInt8,
                    "downs": pl.UInt8,
                    "first_down_yards": pl.UInt8,
                    "end_zone_length": pl.UInt8,
                    "kickoff_yardline": pl.UInt8,
                    "safety_kick_yardline": pl.UInt8,
                    "kickoff_touchback_yardline": pl.UInt8,
                    "punt_touchback_yardline": pl.UInt8,
                    "normal_touchback_yardline": pl.UInt8,
                    "kansas_ot_yardline": pl.UInt8,
                    "pat_yardline": pl.UInt8,
                    "1PC_yardline": pl.UInt8,
                    "2PC_yardline": pl.UInt8,
                    "3PC_yardline": pl.UInt8,
                    "quarters": pl.UInt8,
                    "timeouts_per_half": pl.UInt8,
                    "ot_period_seconds": pl.UInt16,
                    "game_seconds": pl.UInt16,
                    "half_seconds": pl.UInt16,
                    "quarter_seconds": pl.UInt16,
                    "ot_periods": pl.Int8,
                    "ot_periods_until_shootout": pl.Int8,
                    "min_xfl_ot_periods": pl.Int8,
                    "set_xfl_ot_periods": pl.Int8,
                    "touchdown_points": pl.UInt8,
                    "field_goal_points": pl.UInt8,
                    "safety_points": pl.UInt8,
                    "pat_points": pl.UInt8,
                    "pat_defense": pl.UInt8,
                    "pat_safety": pl.UInt8,
                    "players_on_field": pl.UInt8,
                    "preseason_overtime_enabled": pl.Boolean,
                    "reg_season_ot_enabled": pl.Boolean,
                    "postseason_ot_enabled": pl.Boolean,
                    "preseason_ot_type": pl.String,
                    "reg_season_ot_type": pl.String,
                    "postseason_ot_type": pl.String,
                    "two_forward_passes": pl.Boolean,
                    "spikes_are_team_stats": pl.Boolean,
                    "sacks_are_rushes": pl.Boolean,
                    "kneeldowns_are_team_stats": pl.Boolean,
                    "kickoff_fc_always_goes_to_touchback": pl.Boolean,
                    "kickoffs_enabled": pl.Boolean,
                    "use_xfl_kickoff": pl.Boolean,
                    "drop_kick_enabled": pl.Boolean,
                    "drop_kick_bonus_point": pl.Boolean,
                    "fg_adds_ez_length": pl.Boolean,
                    "long_fg_bonus_point": pl.Boolean,
                    "xp_is_a_fg": pl.Boolean,
                    "rouges_enabled": pl.Boolean,
                    "punting_enabled": pl.Boolean,
                    "onside_punts_enabled": pl.Boolean,
                    "fair_catch_enabled": pl.Boolean,
                },
            )
        except sqlite3.OperationalError as e:
            logging.warning(
                "A SQLite3 Operational Error has been raised. " +
                f"Reason: {e}"
            )
            cur.executescript(SqliteSampleFiles.seasons_sql_file())
            con.commit()
            df = pl.read_database(
                query="SELECT * FROM fb_seasons",
                connection=cur,
                schema_overrides={
                    "season": pl.UInt16,
                    "league_id": pl.String,
                    "season_notes": pl.String,
                    "field_length": pl.UInt8,
                    "downs": pl.UInt8,
                    "first_down_yards": pl.UInt8,
                    "end_zone_length": pl.UInt8,
                    "kickoff_yardline": pl.UInt8,
                    "safety_kick_yardline": pl.UInt8,
                    "kickoff_touchback_yardline": pl.UInt8,
                    "punt_touchback_yardline": pl.UInt8,
                    "normal_touchback_yardline": pl.UInt8,
                    "kansas_ot_yardline": pl.UInt8,
                    "pat_yardline": pl.UInt8,
                    "1PC_yardline": pl.UInt8,
                    "2PC_yardline": pl.UInt8,
                    "3PC_yardline": pl.UInt8,
                    "quarters": pl.UInt8,
                    "timeouts_per_half": pl.UInt8,
                    "ot_period_seconds": pl.UInt16,
                    "game_seconds": pl.UInt16,
                    "half_seconds": pl.UInt16,
                    "quarter_seconds": pl.UInt16,
                    "ot_periods": pl.Int8,
                    "ot_periods_until_shootout": pl.Int8,
                    "min_xfl_ot_periods": pl.Int8,
                    "set_xfl_ot_periods": pl.Int8,
                    "touchdown_points": pl.UInt8,
                    "field_goal_points": pl.UInt8,
                    "safety_points": pl.UInt8,
                    "pat_points": pl.UInt8,
                    "pat_defense": pl.UInt8,
                    "pat_safety": pl.UInt8,
                    "players_on_field": pl.UInt8,
                    "preseason_overtime_enabled": pl.Boolean,
                    "reg_season_ot_enabled": pl.Boolean,
                    "postseason_ot_enabled": pl.Boolean,
                    "preseason_sudden_death_ot": pl.Boolean,
                    "reg_season_sudden_death_ot": pl.Boolean,
                    "postseason_sudden_death_ot": pl.Boolean,
                    "preseason_mod_sudden_death_ot": pl.Boolean,
                    "reg_season_mod_sudden_death_ot": pl.Boolean,
                    "postseason_mod_sudden_death_ot": pl.Boolean,
                    "preseason_super_modified_ot": pl.Boolean,
                    "reg_season_super_modified_ot": pl.Boolean,
                    "postseason_super_modified_ot": pl.Boolean,
                    "preseason_kansas_ot": pl.Boolean,
                    "reg_season_kansas_ot": pl.Boolean,
                    "postseason_kansas_ot": pl.Boolean,
                    "preseason_ncaa_ot": pl.Boolean,
                    "reg_season_ncaa_ot": pl.Boolean,
                    "postseason_ncaa_ot": pl.Boolean,
                    "preseason_xfl_ot": pl.Boolean,
                    "reg_season_xfl_ot": pl.Boolean,
                    "postseason_xfl_ot": pl.Boolean,
                    "preseason_full_period_ot": pl.Boolean,
                    "reg_season_full_period_ot": pl.Boolean,
                    "postseason_full_period_ot": pl.Boolean,
                    "two_forward_passes": pl.Boolean,
                    "spikes_are_team_stats": pl.Boolean,
                    "sacks_are_rushes": pl.Boolean,
                    "kneeldowns_are_team_stats": pl.Boolean,
                    "kickoff_fc_always_goes_to_touchback": pl.Boolean,
                    "kickoffs_enabled": pl.Boolean,
                    "use_xfl_kickoff": pl.Boolean,
                    "drop_kick_enabled": pl.Boolean,
                    "drop_kick_bonus_point": pl.Boolean,
                    "fg_adds_ez_length": pl.Boolean,
                    "long_fg_bonus_point": pl.Boolean,
                    "xp_is_a_fg": pl.Boolean,
                    "rouges_enabled": pl.Boolean,
                    "punting_enabled": pl.Boolean,
                    "onside_punts_enabled": pl.Boolean,
                    "fair_catch_enabled": pl.Boolean,
                },
            )
        except Exception as e:
            logging.critical(f"An unhandled exception has occurred: {e}")
            raise e

        if len(df) < 1:
            logging.error(
                "[sqlite3].[dbo].[fb_seasons] has no data. "
                + "Recreating database table."
            )
        return df

    def load_fb_teams(
            con: sqlite3.Connection,
            cur: sqlite3.Cursor
    ) -> pl.DataFrame:
        """ """
        try:
            df = pl.read_database(
                query="SELECT * FROM fb_teams",
                connection=cur,
                infer_schema_length=100,
                schema_overrides={
                    "season": pl.UInt16,
                    "league_id": pl.String,
                    "team_id": pl.String,
                    "pfr_team_id": pl.String,
                    "pfr_fran_id": pl.String,
                    "sr_team_id": pl.String,
                    # "ncaa_old_team_id": pl.Int32,
                    "ncaa_team_id": pl.Int32,
                    "stats_crew_team_id": pl.String,
                    "footballdb_team_id": pl.String,
                    "espn_team_id": pl.Int16,
                    "arenafan_team_id": pl.Int16,
                    "team_abv": pl.String,
                    "team_name": pl.String,
                    "team_location": pl.String,
                    "team_nickname": pl.String,
                    "team_city": pl.String,
                    "team_state": pl.String,
                    "team_nation": pl.String,
                    "team_conference": pl.String,
                    "team_division": pl.String,
                    "team_head_coach": pl.String,
                    "team_oc": pl.String,
                    "team_dc": pl.String,
                    "timezone_name": pl.String,
                    "team_notes": pl.String,
                    "stadium_id": pl.Int16
                },
            )
        except sqlite3.OperationalError as e:
            logging.warning(
                "A SQLite3 Operational Error has been raised. " +
                f"Reason: {e}"
            )
            cur.executescript(SqliteSampleFiles.teams_sql_file())
            con.commit()
            df = pl.read_database(
                query="SELECT * FROM fb_teams",
                connection=cur,
                infer_schema_length=100,
                schema_overrides={
                    "season": pl.UInt16,
                    "league_id": pl.String,
                    "team_id": pl.String,
                    "pfr_team_id": pl.String,
                    "pfr_fran_id": pl.String,
                    "sr_team_id": pl.String,
                    # "ncaa_old_team_id": pl.Int32,
                    "ncaa_team_id": pl.Int32,
                    "stats_crew_team_id": pl.String,
                    "footballdb_team_id": pl.String,
                    "espn_team_id": pl.Int64,
                    "arenafan_team_id": pl.Int64,
                    "team_abv": pl.String,
                    "team_name": pl.String,
                    "team_location": pl.String,
                    "team_nickname": pl.String,
                    "team_city": pl.String,
                    "team_state": pl.String,
                    "team_nation": pl.String,
                    "team_conference": pl.String,
                    "team_division": pl.String,
                    "team_head_coach": pl.String,
                    "team_oc": pl.String,
                    "team_dc": pl.String,
                    "timezone_name": pl.String,
                    "team_notes": pl.String,
                    "stadium_id": pl.Int16
                },
            )
        except Exception as e:
            logging.critical(f"An unhandled exception has occurred: {e}")
            raise e

        if len(df) < 1:
            logging.error(
                "[sqlite3].[dbo].[fb_teams] has no data. " +
                "Recreating database table."
            )
        return df

    def load_fb_rosters(
            con: sqlite3.Connection,
            cur: sqlite3.Cursor
    ) -> pl.DataFrame:
        """ """
        try:
            df = pl.read_database(
                query="SELECT * FROM fb_rosters",
                connection=cur,
                schema_overrides={
                    "season": pl.String,
                    "league_id": pl.String,
                    "team_id": pl.String,
                    "team_abv": pl.String,
                    "player_id": pl.Int64,
                    "position": pl.String,
                    "depth_chart_position": pl.String,
                    "jersey_number": pl.String,
                    "status": pl.String,
                    "player_full_name": pl.String,
                    "player_football_name": pl.String,
                    "player_first_name": pl.String,
                    "player_last_name": pl.String,
                    "player_bday": pl.Date,
                    "height": pl.UInt8,
                    "height_ft": pl.UInt8,
                    "height_in": pl.UInt8,
                    "weight": pl.UInt16,
                    "college": pl.String,
                    "gsis_id": pl.String,
                    "espn_id": pl.Int32,
                    "sportradar_id": pl.String,
                    "yahoo_id": pl.Int32,
                    "rotowire_id": pl.Int32,
                    "pff_id": pl.Int32,
                    "pfr_id": pl.String,
                    "fantasy_data_id": pl.Int32,
                    "sleeper_id": pl.Int32,
                    "esb_id": pl.String,
                    "smart_id": pl.String,
                    "years_exp": pl.UInt8,
                    "headshot_url": pl.String,
                    "headshot_image": pl.String,
                    "ngs_position": pl.String,
                    "week": pl.UInt8,
                    "game_type": pl.String,
                    "status_description_abbr": pl.String,
                    "entry_year": pl.UInt16,
                    "rookie_year": pl.UInt16,
                },
            )

        except sqlite3.OperationalError as e:
            logging.warning(
                "A SQLite3 Operational Error has been raised. " +
                f"Reason: {e}"
            )
            cur.executescript(SqliteSampleFiles.rosters_sql_file())
            con.commit()
            df = pl.read_database(
                query="SELECT * FROM fb_rosters",
                connection=cur,
                schema_overrides={
                    "season": pl.String,
                    "league_id": pl.String,
                    "team_id": pl.String,
                    "team_abv": pl.String,
                    "player_id": pl.Int64,
                    "position": pl.String,
                    "depth_chart_position": pl.String,
                    "jersey_number": pl.String,
                    "status": pl.String,
                    "player_full_name": pl.String,
                    "player_football_name": pl.String,
                    "player_first_name": pl.String,
                    "player_last_name": pl.String,
                    "player_bday": pl.Date,
                    "height": pl.UInt8,
                    "height_ft": pl.UInt8,
                    "height_in": pl.UInt8,
                    "weight": pl.UInt16,
                    "college": pl.String,
                    "gsis_id": pl.String,
                    "espn_id": pl.Int32,
                    "sportradar_id": pl.String,
                    "yahoo_id": pl.Int32,
                    "rotowire_id": pl.Int32,
                    "pff_id": pl.Int32,
                    "pfr_id": pl.String,
                    "fantasy_data_id": pl.Int32,
                    "sleeper_id": pl.Int32,
                    "esb_id": pl.String,
                    "smart_id": pl.String,
                    "years_exp": pl.UInt8,
                    "headshot_url": pl.String,
                    "headshot_image": pl.String,
                    "ngs_position": pl.String,
                    "week": pl.UInt8,
                    "game_type": pl.String,
                    "status_description_abbr": pl.String,
                    "entry_year": pl.UInt16,
                    "rookie_year": pl.UInt16,
                },
            )

        except Exception as e:
            logging.critical(f"An unhandled exception has occurred: {e}")
            raise e

        if len(df) < 1:
            logging.error(
                "[sqlite3].[dbo].[fb_rosters] has no data. "
                + "Recreating database table."
            )
        return df

    def load_fb_stadiums(
            con: sqlite3.Connection,
            cur: sqlite3.Cursor
    ) -> pl.DataFrame:
        """ """
        try:
            df = pl.read_database(
                query="SELECT * FROM fb_stadiums",
                connection=cur,
                schema_overrides={
                    "stadium_id": pl.UInt64,
                    "team_id": pl.String,
                    "pfr_stadium_id": pl.String,
                    "stadium_name": pl.String,
                    "stadium_capacity": pl.UInt32,
                    "stadium_city": pl.String,
                    "stadium_state": pl.String,
                    "stadium_nation": pl.String,
                    "is_dome": pl.Boolean,
                    "is_retractable_roof": pl.Boolean,
                    "stadium_plus_code": pl.String,
                    "stadium_elevation_ft": pl.Int32,
                    "stadium_elevation_m": pl.Int32,
                    "stadium_timezone": pl.String,
                    "stadium_location_x": pl.Float32,
                    "stadium_location_y": pl.Float32,
                },
            )
        except sqlite3.OperationalError as e:
            logging.warning(
                "A SQLite3 Operational Error has been raised. " +
                f"Reason: {e}"
            )
            cur.executescript(SqliteSampleFiles.stadiums_sql_file())
            con.commit()
            df = pl.read_database(
                query="SELECT * FROM fb_stadiums",
                connection=cur,
                schema_overrides={
                    "stadium_id": pl.UInt64,
                    "team_id": pl.String,
                    "pfr_stadium_id": pl.String,
                    "stadium_name": pl.String,
                    "stadium_capacity": pl.UInt32,
                    "stadium_city": pl.String,
                    "stadium_state": pl.String,
                    "stadium_nation": pl.String,
                    "is_dome": pl.Boolean,
                    "is_retractable_roof": pl.Boolean,
                    "stadium_plus_code": pl.String,
                    "stadium_elevation_ft": pl.Int32,
                    "stadium_elevation_m": pl.Int32,
                    "stadium_timezone": pl.String,
                    "stadium_location_x": pl.Float32,
                    "stadium_location_y": pl.Float32,
                },
            )
        except Exception as e:
            logging.critical(f"An unhandled exception has occurred: {e}")
            raise e

        # print(df)
        if len(df) < 1:
            logging.error(
                "[sqlite3].[dbo].[fb_stadiums] has no data. "
                + "Recreating database table."
            )
        return df

    def load_fb_weekly_rosters(
        con: sqlite3.Connection, cur: sqlite3.Cursor
    ) -> pl.DataFrame:
        """ """
        try:
            df = pl.read_database(
                query="SELECT * FROM fb_weekly_rosters",
                connection=cur,
                schema_overrides={
                    "season": pl.String,
                    "game_id": pl.Int64,
                    "league_id": pl.String,
                    "team_id": pl.String,
                    "team_abv": pl.String,
                    "player_id": pl.Int64,
                    "position": pl.String,
                    "depth_chart_position": pl.String,
                    "jersey_number": pl.String,
                    "status": pl.String,
                    "player_full_name": pl.String,
                    "player_football_name": pl.String,
                    "player_first_name": pl.String,
                    "player_last_name": pl.String,
                    "player_bday": pl.Date,
                    "height": pl.UInt8,
                    "height_ft": pl.UInt8,
                    "height_in": pl.UInt8,
                    "weight": pl.UInt16,
                    "college": pl.String,
                    "gsis_id": pl.String,
                    "espn_id": pl.Int32,
                    "sportradar_id": pl.String,
                    "yahoo_id": pl.Int32,
                    "rotowire_id": pl.Int32,
                    "pff_id": pl.Int32,
                    "pfr_id": pl.String,
                    "fantasy_data_id": pl.Int32,
                    "sleeper_id": pl.Int32,
                    "esb_id": pl.String,
                    "smart_id": pl.String,
                    "years_exp": pl.UInt8,
                    "headshot_url": pl.String,
                    "headshot_image": pl.String,
                    "ngs_position": pl.String,
                    "week": pl.UInt8,
                    "game_type": pl.String,
                    "status_description_abbr": pl.String,
                    "entry_year": pl.UInt16,
                    "rookie_year": pl.UInt16,
                },
            )
        except sqlite3.OperationalError as e:
            logging.warning(
                "A SQLite3 Operational Error has been raised. " +
                f"Reason: {e}"
            )
            cur.executescript(SqliteSampleFiles.weekly_rosters_sql_file())
            con.commit()
            df = pl.read_database(
                query="SELECT * FROM fb_weekly_rosters",
                connection=cur,
                schema_overrides={
                    "season": pl.String,
                    "game_id": pl.Int64,
                    "league_id": pl.String,
                    "team_id": pl.String,
                    "team_abv": pl.String,
                    "player_id": pl.Int64,
                    "position": pl.String,
                    "depth_chart_position": pl.String,
                    "jersey_number": pl.String,
                    "status": pl.String,
                    "player_full_name": pl.String,
                    "player_football_name": pl.String,
                    "player_first_name": pl.String,
                    "player_last_name": pl.String,
                    "player_bday": pl.Date,
                    "height": pl.UInt8,
                    "height_ft": pl.UInt8,
                    "height_in": pl.UInt8,
                    "weight": pl.UInt16,
                    "college": pl.String,
                    "gsis_id": pl.String,
                    "espn_id": pl.Int32,
                    "sportradar_id": pl.String,
                    "yahoo_id": pl.Int32,
                    "rotowire_id": pl.Int32,
                    "pff_id": pl.Int32,
                    "pfr_id": pl.String,
                    "fantasy_data_id": pl.Int32,
                    "sleeper_id": pl.Int32,
                    "esb_id": pl.String,
                    "smart_id": pl.String,
                    "years_exp": pl.UInt8,
                    "headshot_url": pl.String,
                    "headshot_image": pl.String,
                    "ngs_position": pl.String,
                    "week": pl.UInt8,
                    "game_type": pl.String,
                    "status_description_abbr": pl.String,
                    "entry_year": pl.UInt16,
                    "rookie_year": pl.UInt16,
                },
            )
        except Exception as e:
            logging.critical(f"An unhandled exception has occurred: {e}")
            raise e

        # print(df)
        if len(df) < 1:
            logging.error(
                "[sqlite3].[dbo].[fb_weekly_rosters] has no data. "
                + "Recreating database table."
            )
        return df

    def load_fb_depth_charts(
        con: sqlite3.Connection, cur: sqlite3.Cursor
    ) -> pl.DataFrame:
        """ """
        try:
            df = pl.read_database(
                query="SELECT * FROM fb_depth_charts",
                connection=cur,
                schema_overrides={
                    "season": pl.Int16,
                    "league_id": pl.String,
                    "team_abv": pl.String,
                    "week": pl.Int8,
                    "game_type": pl.String,
                    "game_id": pl.UInt64,
                    "depth_team": pl.UInt8,
                    "player_id": pl.UInt64,
                    "player_jersey_number": pl.String,
                    "player_last_name": pl.String,
                    "player_first_name": pl.String,
                    "player_football_name": pl.String,
                    "player_full_name": pl.String,
                    "formation": pl.String,
                    "player_position": pl.String,
                    "player_depth_position": pl.String,
                    "gsis_id": pl.String,
                    "espn_id": pl.UInt32,
                    "sportradar_id": pl.String,
                    "yahoo_id": pl.UInt32,
                    "rotowire_id": pl.UInt32,
                    "pff_id": pl.UInt32,
                    "pfr_id": pl.String,
                    "fantasy_data_id": pl.UInt32,
                    "sleeper_id": pl.UInt32,
                    "esb_id": pl.String,
                    "smart_id": pl.String,
                },
            )
        except sqlite3.OperationalError as e:
            logging.warning(
                "A SQLite3 Operational Error has been raised. " +
                f"Reason: {e}"
            )
            cur.executescript(SqliteSampleFiles.depth_chart_sql_file())
            con.commit()
            df = pl.read_database(
                query="SELECT * FROM fb_depth_charts",
                connection=cur,
                schema_overrides={
                    "season": pl.Int16,
                    "league_id": pl.String,
                    "team_abv": pl.String,
                    "week": pl.Int8,
                    "game_type": pl.String,
                    "game_id": pl.UInt64,
                    "depth_team": pl.UInt8,
                    "player_id": pl.UInt64,
                    "player_jersey_number": pl.String,
                    "player_last_name": pl.String,
                    "player_first_name": pl.String,
                    "player_football_name": pl.String,
                    "player_full_name": pl.String,
                    "formation": pl.String,
                    "player_position": pl.String,
                    "player_depth_position": pl.String,
                    "gsis_id": pl.String,
                    "espn_id": pl.UInt32,
                    "sportradar_id": pl.String,
                    "yahoo_id": pl.UInt32,
                    "rotowire_id": pl.UInt32,
                    "pff_id": pl.UInt32,
                    "pfr_id": pl.String,
                    "fantasy_data_id": pl.UInt32,
                    "sleeper_id": pl.UInt32,
                    "esb_id": pl.String,
                    "smart_id": pl.String,
                },
            )
        except Exception as e:
            logging.critical(f"An unhandled exception has occurred: {e}")
            raise e

        # print(df)
        if len(df) < 1:
            logging.error(
                "[sqlite3].[dbo].[fb_weekly_rosters] has no data. "
                + "Recreating database table."
            )
        return df

    def load_fb_schedule(
            con: sqlite3.Connection,
            cur: sqlite3.Cursor
    ) -> pl.DataFrame:
        """ """
        try:
            df = pl.read_database(
                query="SELECT * FROM fb_schedule",
                connection=cur,
                schema_overrides={
                    "game_is_in_progress": pl.Boolean,
                    "game_is_finished": pl.Boolean,
                    "season": pl.UInt16,
                    "game_id": pl.UInt64,
                    "league_id": pl.String,
                    "game_status": pl.String,
                    "nflverse_game_id": pl.String,
                    "game_type": pl.String,
                    "week": pl.UInt8,
                    "game_day": pl.String,
                    "game_time": pl.String,
                    "game_time_zone": pl.String,
                    "game_datetime_utc": pl.String,
                    "game_day_of_week": pl.String,
                    "away_team_abv": pl.String,
                    "away_team_score": pl.String,
                    "home_team_abv": pl.String,
                    "home_team_score": pl.String,
                    "nflverse_old_game_id": pl.String,
                    "gsis_id": pl.UInt64,
                    "nfl_detail_id": pl.String,
                    "pfr_game_id": pl.String,
                    "pff_game_id": pl.String,
                    "espn_game_id": pl.UInt64,
                    "ftn_game_id": pl.UInt64,
                    "away_days_rest": pl.UInt16,
                    "home_days_rest": pl.UInt16,
                    "is_neutral_site_game": pl.Boolean,
                    "is_overtime_game": pl.Boolean,
                    "is_divisional_game": pl.Boolean,
                    "game_roof": pl.String,
                    "surface": pl.String,
                    "temp_f": pl.Float32,
                    "temp_c": pl.Float32,
                    "wind": pl.UInt8,
                    "away_coach_name": pl.String,
                    "home_coach_name": pl.String,
                    "stadium_ID": pl.UInt64,
                    "stadium_name": pl.String,
                    "pfr_stadium_id": pl.String,
                },
            )
        except sqlite3.OperationalError as e:
            logging.warning(
                "A SQLite3 Operational Error has been raised. " +
                f"Reason: {e}"
            )
            cur.executescript(SqliteSampleFiles.schedule_sql_file())
            con.commit()
            df = pl.read_database(
                query="SELECT * FROM fb_schedule",
                connection=cur,
                schema_overrides={
                    "game_is_in_progress": pl.Boolean,
                    "game_is_finished": pl.Boolean,
                    "season": pl.UInt16,
                    "game_id": pl.UInt64,
                    "league_id": pl.String,
                    "game_status": pl.String,
                    "nflverse_game_id": pl.String,
                    "game_type": pl.String,
                    "week": pl.UInt8,
                    "game_day": pl.String,
                    "game_time": pl.String,
                    "game_time_zone": pl.String,
                    "game_datetime_utc": pl.String,
                    "game_day_of_week": pl.String,
                    "away_team_abv": pl.String,
                    "away_team_score": pl.String,
                    "home_team_abv": pl.String,
                    "home_team_score": pl.String,
                    "nflverse_old_game_id": pl.String,
                    "gsis_id": pl.UInt64,
                    "nfl_detail_id": pl.String,
                    "pfr_game_id": pl.String,
                    "pff_game_id": pl.String,
                    "espn_game_id": pl.UInt64,
                    "ftn_game_id": pl.UInt64,
                    "away_days_rest": pl.UInt16,
                    "home_days_rest": pl.UInt16,
                    "is_neutral_site_game": pl.Boolean,
                    "is_overtime_game": pl.Boolean,
                    "is_divisional_game": pl.Boolean,
                    "game_roof": pl.String,
                    "surface": pl.String,
                    "temp_f": pl.Float32,
                    "temp_c": pl.Float32,
                    "wind": pl.UInt8,
                    "away_coach_name": pl.String,
                    "home_coach_name": pl.String,
                    "stadium_ID": pl.UInt64,
                    "stadium_name": pl.String,
                    "pfr_stadium_id": pl.String,
                },
            )

        except Exception as e:
            logging.critical(f"An unhandled exception has occurred: {e}")
            raise e

        # print(df)
        if len(df) < 1:
            logging.error(
                "[sqlite3].[dbo].[fb_weekly_rosters] has no data. "
                + "Recreating database table."
            )
        return df

    def load_fb_game_refs(
            con: sqlite3.Connection,
            cur: sqlite3.Cursor
    ) -> pl.DataFrame:
        """ """
        try:
            df = pl.read_database(
                query="SELECT * FROM fb_game_refs",
                connection=cur,
                schema_overrides={
                    "game_id": pl.UInt64,
                    "ref_num": pl.UInt16,
                    "ref_position_abv": pl.String,
                    "ref_position_name": pl.String,
                    "ref_full_name": pl.String,
                    "ref_first_name": pl.String,
                    "ref_last_name": pl.String,
                },
            )
        except sqlite3.OperationalError as e:
            logging.warning(
                "A SQLite3 Operational Error has been raised. " +
                f"Reason: {e}"
            )
            cur.executescript(SqliteSampleFiles.game_refs_sql_file())
            con.commit()
            df = pl.read_database(
                query="SELECT * FROM fb_game_refs",
                connection=cur,
                schema_overrides={
                    "game_id": pl.UInt64,
                    "ref_num": pl.UInt16,
                    "ref_position_abv": pl.String,
                    "ref_position_name": pl.String,
                    "ref_full_name": pl.String,
                    "ref_first_name": pl.String,
                    "ref_last_name": pl.String,
                },
            )
        except Exception as e:
            logging.critical(f"An unhandled exception has occurred: {e}")
            raise e

        # print(df)
        if len(df) < 1:
            logging.error(
                "[sqlite3].[dbo].[fb_weekly_rosters] has no data. "
                + "Recreating database table."
            )
        return df

    def load_fb_pbp(
            con: sqlite3.Connection,
            cur: sqlite3.Cursor
    ) -> pl.DataFrame:
        """ """
        try:
            df = pl.read_database(
                query="SELECT * FROM fb_pbp",
                connection=cur,
                schema_overrides={
                    "game_id": pl.UInt64,
                    "game_json_str": pl.String
                },
            )
        except sqlite3.OperationalError as e:
            logging.warning(
                "A SQLite3 Operational Error has been raised. " +
                f"Reason: {e}"
            )
            cur.executescript(SqliteSampleFiles.game_pbp_sql_file())
            con.commit()
            df = pl.read_database(
                query="SELECT * FROM fb_pbp",
                connection=cur,
                schema_overrides={
                    "game_id": pl.UInt64,
                    "game_json_str": pl.String
                },
            )

        except Exception as e:
            logging.critical(f"An unhandled exception has occurred: {e}")
            raise e

        # print(df)
        if len(df) < 1:
            logging.error(
                "[sqlite3].[dbo].[fb_pbp] has no data. " +
                "Recreating database table."
            )
        return df


def test_sqlite3_load(custom_dir: str = None):
    home_dir = expanduser("~")
    sql_dir = ""
    if custom_dir is not None:
        sql_dir = custom_dir
    else:
        sql_dir = home_dir

    try:
        con = sqlite3.connect(f"{sql_dir}/.sdv_pbp_fb/sdv_pbp_py.sqlite")
        cur = con.cursor()
    except sqlite3.OperationalError as e:
        create_app_sqlite3_db(custom_dir)
        logging.warning(
            "A SQLite3 Operational Error has been raised. " + f"Reason: {e}"
        )
        con = sqlite3.connect(f"{sql_dir}/.sdv_pbp_fb/sdv_pbp_py.sqlite")
        cur = con.cursor()

    print(SqliteLoadData.load_iso_nations(con, cur))
    print(SqliteLoadData.load_iso_states(con, cur))
    print(SqliteLoadData.load_iso_timezones(con, cur))
    print(SqliteLoadData.load_leagues(con, cur))
    print(SqliteLoadData.load_seasons(con, cur))
    print(SqliteLoadData.load_fb_teams(con, cur))
    print(SqliteLoadData.load_fb_stadiums(con, cur))
    print(SqliteLoadData.load_fb_depth_charts(con, cur))
    print(SqliteLoadData.load_fb_schedule(con, cur))
    print(SqliteLoadData.load_fb_game_refs(con, cur))
    print(SqliteLoadData.load_fb_pbp(con, cur))


if __name__ == "__main__":
    test_sqlite3_load()
