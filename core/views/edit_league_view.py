"""
- Creation Date: 03/10/2024 04:35 PM EDT
- Last Updated: 05/25/2024 09:45 PM EDT
- Authors: Joseph Armstrong (armstrongjoseph08@gmail.com)
- file: `./core/views/edit_league_view.py`
- Purpose: Code behind for the window
    that allows a user to view and edit leagues.
"""

import logging
import operator
import sqlite3
from datetime import datetime

import polars as pl
import PySimpleGUI as sg

from core.database.load_db_elements import SqliteLoadData
from core.database.sqlite3_connectors import initialize_sqlite3_connectors
from core.other.embedded import EmbeddedElements, LettersAndNumbers


class LeagueView:
    """
    Class for handling logic with editing league settings.
    """

    letters_all = LettersAndNumbers.letters_all(include_space=True)
    letters_lower = LettersAndNumbers.letters_lower()
    letters_upper = LettersAndNumbers.letters_upper()
    numbers_all = LettersAndNumbers.numbers_all()
    letters_and_numbers = LettersAndNumbers.letters_and_numbers(
        include_space=True
    )
    upper_letters_and_numbers = LettersAndNumbers.upper_letters_and_numbers()

    # sqlite3 connectors
    sqlite3_con = None
    sqlite3_cur = None

    settings_dict = {}
    ot_types_arr = [
        "Sudden Death OT",
        "Modified Sudden Death OT",
        "Super Modified Sudden Death OT",
        "Kansas OT",
        "NCAA OT",
        "XFL OT",
        "Full Period OT",
    ]
    lg_df = pl.DataFrame()

    # League variables
    league_id_original = ""
    league_id = ""
    league_long_name = ""
    league_short_name = ""
    # league_default_sex = ""
    league_notes = ""
    changed_settings = False

    field_length = 0
    downs = 0
    first_down_yards = 0
    end_zone_length = 0
    kickoff_yardline = 0
    safety_kick_yardline = 0
    kickoff_touchback_yardline = 0
    punt_touchback_yardline = 0
    normal_touchback_yardline = 0
    kansas_ot_yardline = 0
    pat_yardline = 0
    one_PC_Yardline = 0  # seen in the XFL/UFL
    two_PC_Yardline = 0
    three_PC_Yardline = 0
    quarters = 0
    timeouts_per_half = 0
    ot_period_seconds = 0
    game_seconds = 0
    half_seconds = 0
    quarter_seconds = 0
    ot_periods = 0
    ot_periods_until_shootout = 0
    min_xfl_ot_periods = 0
    set_xfl_ot_periods = 0
    touchdown_points = 0
    field_goal_points = 0
    safety_points = 0
    pat_points = 0
    pat_defense = 0
    pat_safety = 0
    players_on_field = 0

    xfl_pat_enabled = False

    preseason_ot_enabled = False
    reg_season_ot_enabled = False
    postseason_ot_enabled = False

    preseason_ot_type = ""
    reg_season_ot_type = ""
    postseason_ot_type = ""

    two_forward_passes = False
    spikes_are_team_stats = False
    sacks_are_rushes = False
    kneeldowns_are_team_stats = False
    kickoff_fc_always_goes_to_touchback = False
    kickoffs_enabled = False
    use_xfl_kickoff = False
    drop_kick_enabled = False
    drop_kick_bonus_point = False
    fg_adds_ez_length = False
    long_fg_bonus_point = False
    xp_is_a_fg = False
    rouges_enabled = False
    punting_enabled = False
    onside_punts_enabled = False
    fair_catch_enabled = False
    special_onside_play_enabled = False

    def __init__(
        self,
        settings_json: dict,
        league_id: str
    ):
        self.league_id = league_id
        self.league_id_original = league_id

        # Get SQLite3 connections
        self.sqlite3_con, self.sqlite3_cur = initialize_sqlite3_connectors()

        self.settings_dict = settings_json
        self.app_theme = self.settings_dict["app_theme"]
        self.initial_data_load()
        self.league_edit_view()

    def changed_settings_check(self) -> str:
        check = sg.popup_yes_no(
            """
            You have unsaved changes.
            Do you want to save your changes?
            """.replace(
                "            ",
                ""
            ),
            title="Unsaved Settings"
        )
        return check

    def update_league_settings(self):
        """
        """
        # Done to avoid a formatting error being raised
        # by a line being more than 80 characters long.
        kickoff_fc = self.kickoff_fc_always_goes_to_touchback

        sql_script = """
        UPDATE fb_leagues
        SET
            "league_id" = ?,
            "league_long_name" = ?,
            "league_short_name" = ?,
            "league_notes" = ?,
            "field_length" = ?,

            "downs" = ?,
            "first_down_yards" = ?,
            "kickoff_yardline" = ?,
            "safety_kick_yardline" = ?,
            "kickoff_touchback_yardline" = ?,
            "punt_touchback_yardline" = ?,
            "normal_touchback_yardline" = ?,
            "kansas_ot_yardline" = ?,
            "pat_yardline" = ?,
            "1PC_yardline" = ?,
            "2PC_yardline" = ?,
            "3PC_yardline" = ?,
            "quarters" = ?,
            "timeouts_per_half" = ?,
            "ot_period_seconds" = ?,
            "game_seconds" = ?,
            "half_seconds" = ?,
            "quarter_seconds" = ?,
            "ot_periods" = ?,
            "ot_periods_until_shootout" = ?,
            "min_xfl_ot_periods" = ?,
            "set_xfl_ot_periods" = ?,
            "touchdown_points" = ?,
            "field_goal_points" = ?,
            "safety_points" = ?,
            "pat_points" = ?,
            "pat_defense" = ?,
            "pat_safety" = ?,
            "players_on_field" = ?,
            "xfl_pat" = ?,

            "preseason_ot_enabled" = ?,
            "reg_season_ot_enabled" = ?,
            "postseason_ot_enabled" = ?,

            "preseason_ot_type" = ?,
            "reg_season_ot_type" = ?,
            "postseason_ot_type" = ?,

            "two_forward_passes" = ?,
            "spikes_are_team_stats" = ?,
            "sacks_are_rushes" = ?,
            "kneeldowns_are_team_stats" = ?,
            "kickoff_fc_always_goes_to_touchback" = ?,
            "kickoffs_enabled" = ?,
            "use_xfl_kickoff" = ?,
            "drop_kick_enabled" = ?,
            "drop_kick_bonus_point" = ?,
            "fg_adds_ez_length" = ?,
            "long_fg_bonus_point" = ?,
            "xp_is_a_fg" = ?,
            "rouges_enabled" = ?,
            "punting_enabled" = ?,
            "onside_punts_enabled" = ?,
            "special_onside_play_enabled" = ?,
            "fair_catch_enabled" = ?

        WHERE
            "league_id" = ?
        """
        # print(sql_script)

        self.sqlite3_cur.executemany(
            sql_script,
            [(
                self.league_id,
                self.league_long_name,
                self.league_short_name,
                self.league_notes,
                self.field_length,
                self.downs,
                self.first_down_yards,
                self.kickoff_yardline,
                self.safety_kick_yardline,
                self.kickoff_touchback_yardline,
                self.punt_touchback_yardline,
                self.normal_touchback_yardline,
                self.kansas_ot_yardline,
                self.pat_yardline,
                self.one_PC_Yardline,
                self.two_PC_Yardline,
                self.three_PC_Yardline,
                self.quarters,
                self.timeouts_per_half,
                self.ot_period_seconds,
                self.game_seconds,
                self.half_seconds,
                self.quarter_seconds,
                self.ot_periods,
                self.ot_periods_until_shootout,
                self.min_xfl_ot_periods,
                self.set_xfl_ot_periods,
                self.touchdown_points,
                self.field_goal_points,
                self.safety_points,
                self.pat_points,
                self.pat_defense,
                self.pat_safety,
                self.players_on_field,
                self.xfl_pat_enabled,
                self.preseason_ot_enabled,
                self.reg_season_ot_enabled,
                self.postseason_ot_enabled,
                self.preseason_ot_type,
                self.reg_season_ot_type,
                self.postseason_ot_type,
                self.two_forward_passes,
                self.spikes_are_team_stats,
                self.sacks_are_rushes,
                self.kneeldowns_are_team_stats,
                kickoff_fc,
                self.kickoffs_enabled,
                self.use_xfl_kickoff,
                self.drop_kick_enabled,
                self.drop_kick_bonus_point,
                self.fg_adds_ez_length,
                self.long_fg_bonus_point,
                self.xp_is_a_fg,
                self.rouges_enabled,
                self.punting_enabled,
                self.onside_punts_enabled,
                self.special_onside_play_enabled,
                self.fair_catch_enabled,
                self.league_id

            )]
        )
        self.sqlite3_con.commit()

    def initial_data_load(self):
        """

        """
        self.lg_df = SqliteLoadData.load_leagues(
            con=self.sqlite3_con, cur=self.sqlite3_cur
        )
        # print(self.lg_df)
        self.lg_df = self.lg_df.filter(pl.col("league_id") == self.league_id)

        # The following line is not run because we already know
        # what the `league_id` is.
        # self.league_id = self.lg_df["league_id"][0]
        self.league_long_name = self.lg_df["league_long_name"][0]
        self.league_short_name = self.lg_df["league_short_name"][0]
        # self.league_default_sex = self.lg_df["league_default_sex"][0]
        self.league_notes = self.lg_df["league_notes"][0]

        self.field_length = self.lg_df["field_length"][0]
        self.downs = self.lg_df["downs"][0]
        self.first_down_yards = self.lg_df["first_down_yards"][0]
        self.end_zone_length = self.lg_df["end_zone_length"][0]
        self.kickoff_yardline = self.lg_df["kickoff_yardline"][0]
        self.safety_kick_yardline = self.lg_df["safety_kick_yardline"][0]
        self.kickoff_touchback_yardline = self.lg_df[
            "kickoff_touchback_yardline"
        ][0]
        self.punt_touchback_yardline = self.lg_df["punt_touchback_yardline"][0]
        self.normal_touchback_yardline = self.lg_df[
            "normal_touchback_yardline"
        ][0]
        self.kansas_ot_yardline = self.lg_df["kansas_ot_yardline"][0]
        self.pat_yardline = self.lg_df["pat_yardline"][0]
        self.one_PC_Yardline = self.lg_df["1PC_yardline"][0]
        self.two_PC_Yardline = self.lg_df["2PC_yardline"][0]
        self.three_PC_Yardline = self.lg_df["3PC_yardline"][0]
        self.quarters = self.lg_df["quarters"][0]
        self.timeouts_per_half = self.lg_df["timeouts_per_half"][0]
        self.ot_period_seconds = self.lg_df["ot_period_seconds"][0]
        self.game_seconds = self.lg_df["game_seconds"][0]
        self.half_seconds = self.lg_df["half_seconds"][0]
        self.quarter_seconds = self.lg_df["quarter_seconds"][0]
        self.ot_periods = self.lg_df["ot_periods"][0]
        self.ot_periods_until_shootout = self.lg_df[
            "ot_periods_until_shootout"
        ][0]
        self.min_xfl_ot_periods = self.lg_df["min_xfl_ot_periods"][0]
        self.set_xfl_ot_periods = self.lg_df["set_xfl_ot_periods"][0]
        self.touchdown_points = self.lg_df["touchdown_points"][0]
        self.field_goal_points = self.lg_df["field_goal_points"][0]
        self.safety_points = self.lg_df["safety_points"][0]
        self.pat_points = self.lg_df["pat_points"][0]
        self.pat_defense = self.lg_df["pat_defense"][0]
        self.pat_safety = self.lg_df["pat_safety"][0]
        self.players_on_field = self.lg_df["players_on_field"][0]

        self.preseason_ot_enabled = self.lg_df["preseason_ot_enabled"][0]
        self.reg_season_ot_enabled = self.lg_df["reg_season_ot_enabled"][0]
        self.postseason_ot_enabled = self.lg_df["postseason_ot_enabled"][0]

        self.xfl_pat_enabled = self.lg_df["xfl_pat"][0]

        self.preseason_ot_type = self.lg_df["preseason_ot_type"][0]
        self.reg_season_ot_type = self.lg_df["reg_season_ot_type"][0]
        self.postseason_ot_type = self.lg_df["postseason_ot_type"][0]

        self.two_forward_passes = self.lg_df["two_forward_passes"][0]
        self.spikes_are_team_stats = self.lg_df["spikes_are_team_stats"][0]
        self.sacks_are_rushes = self.lg_df["sacks_are_rushes"][0]
        self.kneeldowns_are_team_stats = self.lg_df[
            "kneeldowns_are_team_stats"
        ][0]
        self.kickoff_fc_always_goes_to_touchback = self.lg_df[
            "kickoff_fc_always_goes_to_touchback"
        ][0]
        self.kickoffs_enabled = self.lg_df["kickoffs_enabled"][0]
        self.use_xfl_kickoff = self.lg_df["use_xfl_kickoff"][0]
        self.drop_kick_enabled = self.lg_df["drop_kick_enabled"][0]
        self.drop_kick_bonus_point = self.lg_df["drop_kick_bonus_point"][0]
        self.fg_adds_ez_length = self.lg_df["fg_adds_ez_length"][0]
        self.long_fg_bonus_point = self.lg_df["long_fg_bonus_point"][0]
        self.xp_is_a_fg = self.lg_df["xp_is_a_fg"][0]
        self.rouges_enabled = self.lg_df["rouges_enabled"][0]
        self.punting_enabled = self.lg_df["punting_enabled"][0]
        self.onside_punts_enabled = self.lg_df["onside_punts_enabled"][0]
        self.fair_catch_enabled = self.lg_df["fair_catch_enabled"][0]
        self.special_onside_play_enabled = self.lg_df[
            "special_onside_play_enabled"
        ][0]

    def league_edit_view(self):
        sg.theme(self.app_theme)
        lg_basics = [
            [
                sg.Text(
                    "League Full Name:\t\t"
                ),
                sg.Input(
                    default_text=self.league_long_name,
                    key="-LG_LONG_NAME-",
                    enable_events=True,
                    size=(40, 1)
                ),
                sg.Push(),
            ],
            [
                sg.Text("League Abbreviation:\t"),
                sg.Input(
                    default_text=self.league_short_name,
                    key="-LG_SHORT_NAME-",
                    enable_events=True,
                    size=(7, 1)
                ),
                sg.Push(),
            ],
            [
                sg.Text("League Notes:\t\t"),
                sg.Multiline(
                    default_text=self.league_notes,
                    key="-LG_NOTES-",
                    enable_events=True,
                    expand_x=True,
                    size=(40, 5)
                ),
                sg.Push(),
            ],
            [
                sg.Text("Field Length:\t\t"),
                sg.Combo(
                    values=[x * 5 for x in range(10, 23)],
                    default_value=self.field_length,
                    key="-FIELD_LENGTH-",
                    enable_events=True,
                    size=(10, 5)
                ),
                sg.Push(),
            ],
            [

                sg.Text("Players on field:\t\t"),
                sg.Combo(
                    values=[x for x in range(5, 20)],
                    default_value=self.players_on_field,
                    key="-PLAYER_COUNT-",
                    enable_events=True,
                    size=(10, 5),
                ),
                sg.Push(),
            ],
            [
                sg.Text("Downs:\t\t\t"),
                sg.Combo(
                    values=[3, 4],
                    default_value=self.downs,
                    key="-DOWNS-",
                    enable_events=True,
                    size=(10, 5)
                ),
                sg.Push(),
            ],
            [
                sg.Text("Yards for a First Down:\t"),
                sg.Combo(
                    values=[x for x in range(1, 20)],
                    default_value=self.first_down_yards,
                    key="-FIRST_DOWN_YARDS-",
                    enable_events=True,
                    size=(10, 5)
                ),
                sg.Push(),
            ],
            [
                sg.Text("End Zone Length:\t\t"),
                sg.Combo(
                    values=[x for x in range(1, 25)],
                    default_value=self.end_zone_length,
                    key="-EZ_LENGTH-",
                    enable_events=True,
                    size=(10, 5)
                ),
                sg.Push(),
            ],
            [
                sg.Text("Kickoff yardline:\t\t"),
                sg.Combo(
                    values=[x for x in range(5, self.field_length, 5)],
                    default_value=self.kickoff_yardline,
                    key="-KICKOFF_YARDLINE-",
                    enable_events=True,
                    size=(10, 5)
                ),
                sg.Push(),
            ],
            [
                sg.Text("Safety Kickoff Yardline:\t"),
                sg.Combo(
                    values=[x for x in range(5, self.field_length, 5)],
                    default_value=self.safety_kick_yardline,
                    key="-SAF_KICKOFF_YARDLINE-",
                    enable_events=True,
                    size=(10, 5)
                ),
                sg.Push(),
            ],
            [
                sg.Text("Kickoff Touchback Yardline:\t"),
                sg.Combo(
                    values=[x for x in range(5, self.field_length, 5)],
                    default_value=self.kickoff_touchback_yardline,
                    key="-KICKOFF_TB_YARDLINE-",
                    enable_events=True,
                    size=(10, 5)
                ),
                sg.Push(),
            ],
            [
                sg.Text("Punt Touchback Yardline:\t"),
                sg.Combo(
                    values=[x for x in range(5, self.field_length, 5)],
                    default_value=self.punt_touchback_yardline,
                    key="-PUNT_TB_YARDLINE-",
                    enable_events=True,
                    size=(10, 5)
                ),
                sg.Push(),
            ],
            [
                sg.Text("Normal Touchback Yardline:\t"),
                sg.Combo(
                    values=[x for x in range(5, self.field_length, 5)],
                    default_value=self.normal_touchback_yardline,
                    key="-NORMAL_TB_YARDLINE-",
                    enable_events=True,
                    size=(10, 5)
                ),
                sg.Push(),
            ],
        ]

        points_layout = [
            [
                sg.Text("Points for a touchdown:\t"),
                sg.Combo(
                    values=[x for x in range(1, 10)],
                    default_value=self.touchdown_points,
                    key="-TD_POINTS-",
                    enable_events=True,
                    size=(10, 5),
                ),
                sg.Push(),
            ],
            [
                sg.Text("Points for a field goal:\t"),
                sg.Combo(
                    values=[x for x in range(1, 10)],
                    default_value=self.field_goal_points,
                    key="-FG_POINTS-",
                    enable_events=True,
                    size=(10, 5),
                ),
                sg.Push(),
            ],
            [
                sg.Text("Points for a safety:\t\t"),
                sg.Combo(
                    values=[x for x in range(1, 10)],
                    default_value=self.safety_points,
                    key="-SAF_POINTS-",
                    enable_events=True,
                    size=(10, 5),
                ),
                sg.Push(),
            ],
            [
                sg.Text("Points for XP:\t\t"),
                sg.Combo(
                    values=[x for x in range(1, 10)],
                    default_value=self.pat_points,
                    key="-PAT_POINTS-",
                    enable_events=True,
                    size=(10, 5),
                ),
                sg.Push(),
            ],
            [
                sg.Text("Points for Def. conversion:\t"),
                sg.Combo(
                    values=[x for x in range(1, 10)],
                    default_value=self.pat_defense,
                    key="-PAT_DEFENSE-",
                    enable_events=True,
                    size=(10, 5),
                ),
                sg.Push(),
            ],
            [
                sg.Text("Points for a PAT Safety:\t"),
                sg.Combo(
                    values=[x for x in range(1, 10)],
                    default_value=self.pat_safety,
                    key="-PAT_SAF-",
                    enable_events=True,
                    size=(10, 5),
                ),
                sg.Push(),
            ],
            [
                sg.Text("PAT Yardline:\t\t"),
                sg.Combo(
                    values=[x for x in range(5, self.field_length, 1)],
                    default_value=self.pat_yardline,
                    key="-PAT_YARDLINE-",
                    enable_events=True,
                    size=(10, 5)
                ),
                sg.Push(),
            ],
            [
                sg.Checkbox(
                    "Long FG results in bonus point?",
                    key="-LONG_FG_BONUS_POINT-",
                    enable_events=True
                ),
            ],
            [
                sg.Checkbox(
                    "An XP is always a kick attempt?",
                    key="-XP_IS_FG-",
                    enable_events=True
                ),
            ],
            [
                sg.Checkbox(
                    "Rouges enabled?",
                    key="-ROUGES_ENABLED-",
                    enable_events=True
                ),
            ],
            [
                sg.Text("1-Point Conversion Yardline:\t"),
                sg.Combo(
                    values=[x for x in range(5, self.field_length, 1)],
                    default_value=self.one_PC_Yardline,
                    key="-1PC_YARDLINE-",
                    enable_events=True,
                    size=(10, 5)
                ),
                sg.Push(),
            ],
            [
                sg.Text("2-Point Conversion Yardline:\t"),
                sg.Combo(
                    values=[x for x in range(5, self.field_length, 1)],
                    default_value=self.two_PC_Yardline,
                    key="-2PC_YARDLINE-",
                    enable_events=True,
                    size=(10, 5)
                ),
                sg.Push(),
            ],
            [
                sg.Text("3-Point Conversion Yardline:\t"),
                sg.Combo(
                    values=[x for x in range(5, self.field_length, 1)],
                    default_value=self.three_PC_Yardline,
                    key="-3PC_YARDLINE-",
                    enable_events=True,
                    size=(10, 5)
                ),
                sg.Push(),
            ],
            [
                sg.Text("Timeouts per Half:\t\t"),
                sg.Combo(
                    values=[x for x in range(1, 5)],
                    default_value=self.timeouts_per_half,
                    key="-TIMEOUTS-",
                    enable_events=True,
                    size=(10, 5)
                ),
                sg.Push(),
            ],
            [
                sg.Text("Minutes per Quarter:\t"),
                sg.Combo(
                    values=[x for x in range(1, 20)],
                    default_value=int(self.quarter_seconds/60),
                    key="-QUARTER_MINUTES-",
                    enable_events=True,
                    size=(10, 5)
                ),
                sg.Push(),
            ],
            [
                sg.Text("Minutes per Quarter (OT):\t"),
                sg.Combo(
                    values=[x for x in range(1, 20)],
                    default_value=int(self.ot_period_seconds/60),
                    key="-OT_QUARTER_MINUTES-",
                    enable_events=True,
                    size=(10, 5)
                ),
                sg.Push(),
            ],
        ]

        ot_layout = [
            [
                sg.Checkbox(
                    "Pre-season OT?",
                    key="-IS_PRESEASON_OT-",
                    enable_events=True
                ),
            ],
            [
                sg.Text("Pre-season OT Type:\t"),
                sg.Combo(
                    values=self.ot_types_arr,
                    default_value=self.preseason_ot_type,
                    key="-PRE_SEASON_OT_TYPE-",
                    enable_events=True,
                    disabled=operator.not_(self.preseason_ot_enabled),
                    size=(30, 5),
                ),
                sg.Push(),
            ],
            [
                sg.Checkbox(
                    "Reg. Season OT?",
                    key="-IS_REG_SEASON_OT-",
                    enable_events=True
                ),

            ],
            [
                sg.Text("Reg. Season OT Type:\t"),
                sg.Combo(
                    values=self.ot_types_arr,
                    default_value=self.reg_season_ot_type,
                    key="-REG_SEASON_OT_TYPE-",
                    enable_events=True,
                    disabled=operator.not_(self.reg_season_ot_enabled),
                    size=(30, 5),
                ),
                sg.Push(),
            ],
            [
                sg.Checkbox(
                    "Post Season OT?",
                    key="-IS_POST_SEASON_OT-",
                    enable_events=True
                ),
            ],
            [
                sg.Text("Post Season OT Type:\t"),
                sg.Combo(
                    values=self.ot_types_arr,
                    default_value=self.postseason_ot_type,
                    key="-POST_SEASON_OT_TYPE-",
                    enable_events=True,
                    disabled=operator.not_(self.postseason_ot_enabled),
                    size=(30, 5),
                ),
                sg.Push(),
            ],
            [
                sg.Text("Overtime Quarters:\t\t"),
                sg.Combo(
                    values=[x for x in range(1, 20)],
                    default_value=self.ot_periods,
                    key="-OT_QUARTER_MINUTES-",
                    enable_events=True,
                    size=(10, 5)
                ),
                sg.Push(),
            ],
            [
                sg.Text("NCAA OT's before Shootout:\t"),
                sg.Combo(
                    values=[x for x in range(1, 20)],
                    default_value=self.ot_periods_until_shootout,
                    key="-OT_PERIODS_UNTIL_SHOOTOUT-",
                    enable_events=True,
                    size=(10, 5)
                ),
                sg.Push(),
            ],
            [
                sg.Text("Min. XFL OT Periods:\t"),
                sg.Combo(
                    values=[x for x in range(1, 10)],
                    default_value=self.min_xfl_ot_periods,
                    key="-MIN_XFL_OT_PERIODS-",
                    enable_events=True,
                    size=(10, 5)
                ),
                sg.Push(),
            ],
            [
                sg.Text("Set XFL OT Periods:\t"),
                sg.Combo(
                    values=[x for x in range(1, 10)],
                    default_value=self.set_xfl_ot_periods,
                    key="-SET_XFL_OT_PERIODS-",
                    enable_events=True,
                    size=(10, 5)
                ),
                sg.Push(),
            ],
            [
                sg.Text("Kansas OT Yardline:\t"),
                sg.Combo(
                    values=[x for x in range(5, self.field_length, 1)],
                    default_value=self.kansas_ot_yardline,
                    key="-KANSAS_OT_YARDLINE-",
                    enable_events=True,
                    size=(10, 5)
                ),
                sg.Push(),
            ],
        ]

        misc_layout = [
            [
                sg.Checkbox(
                    "Two Forward Passes?",
                    key="-TWO_FORWARD_PASSES-",
                    enable_events=True
                ),
            ],
            [
                sg.Checkbox(
                    "Spikes are team stats?",
                    key="-SPIKES_ARE_TEAM_STATS-",
                    enable_events=True
                ),
            ],
            [
                sg.Checkbox(
                    "Sacks are rushes?",
                    key="-SACKS_ARE_RUSHES-",
                    enable_events=True
                ),
            ],
            [
                sg.Checkbox(
                    "Sacks are rushes?",
                    key="-KNEELDOWNS_ARE_TEAM_STATS-",
                    enable_events=True
                ),
            ],
            [
                sg.Checkbox(
                    "Enable kickoffs?",
                    key="-ENABLE_KICKOFFS-",
                    enable_events=True
                ),
            ],
            [
                sg.Checkbox(
                    "Fair catches on kickoffs always go to touchback line?",
                    key="-KICKOFF_FC_TOUCHBACK_RULE-",
                    enable_events=True
                ),
            ],
            [
                sg.Checkbox(
                    "Use XFL kickoff rules?",
                    key="-USE_XFL_KICKOFF-",
                    enable_events=True
                ),
            ],
            [
                sg.Checkbox(
                    "Drop kicks enabled?",
                    key="-DROP_KICK_ENABLED-",
                    enable_events=True
                ),
            ],
            [
                sg.Checkbox(
                    "Successful drop kick results in bonus point?",
                    key="-DROP_KICK_BONUS_POINT-",
                    enable_events=True
                ),
            ],
            [
                sg.Checkbox(
                    "End Zone length is added to Field Goal length?",
                    key="-FG_ADDS_EZ_LENGTH-",
                    enable_events=True
                ),
            ],
            [
                sg.Checkbox(
                    "Punting enabled?",
                    key="-PUNTING_ENABLED-",
                    enable_events=True
                ),
            ],
            [
                sg.Checkbox(
                    "Onside Punting enabled?",
                    key="-ONSIDE_PUNTING_ENABLED-",
                    enable_events=True
                ),
            ],
            [
                sg.Checkbox(
                    "Fair Catch enabled?",
                    key="-FAIR_CATCH_ENABLED-",
                    enable_events=True
                ),
            ],
            [
                sg.Checkbox(
                    "Special onside play enabled?",
                    key="-SPECIAL_ONSIDE_PLAY_ENABLED-",
                    enable_events=True
                ),
            ],

        ]

        layout = [
            [
                sg.Text(
                    f"Edit League - {self.league_id}",
                    font="Arial 24",
                    justification="center",
                    expand_x=True,
                ),
                sg.Image(
                    EmbeddedElements.desktop_icon(),
                    size=(100, 100),
                    # expand_x=True,
                    # expand_y=True
                ),
            ],
            [
                sg.TabGroup(
                    [[
                        sg.Tab(
                            "Basics",
                            lg_basics
                        ),
                        sg.Tab(
                            "Overtime",
                            ot_layout
                        ),
                        sg.Tab(
                            "Points",
                            points_layout
                        ),
                        sg.Tab(
                            "Misc.",
                            misc_layout
                        )

                    ]],
                    expand_x=True

                )
            ],
            [
                sg.Push(),
                sg.Button(
                    "OK",
                    key="-OK_BUTTON-",
                    size=(10, 1)
                ),
                sg.Button(
                    "Apply",
                    key="-APPLY_BUTTON-",
                    size=(10, 1),
                    disabled=True
                ),
                sg.Button(
                    "Cancel",
                    key="-CANCEL_BUTTON-",
                    size=(10, 1)
                ),
            ],
        ]

        window = sg.Window(
            "Edit League...",
            layout=layout,
            # size=(500, 600),
            resizable=False,
            finalize=True,
            keep_on_top=False
        )

        window["-IS_PRESEASON_OT-"].update(self.preseason_ot_enabled)
        window["-IS_REG_SEASON_OT-"].update(self.reg_season_ot_enabled)
        window["-IS_POST_SEASON_OT-"].update(self.postseason_ot_enabled)

        window["-TWO_FORWARD_PASSES-"].update(self.two_forward_passes)
        window["-SPIKES_ARE_TEAM_STATS-"].update(self.spikes_are_team_stats)
        window["-SACKS_ARE_RUSHES-"].update(self.sacks_are_rushes)
        window["-KNEELDOWNS_ARE_TEAM_STATS-"].update(
            self.kneeldowns_are_team_stats
        )
        window["-KICKOFF_FC_TOUCHBACK_RULE-"].update(
            self.kickoff_fc_always_goes_to_touchback
        )
        window["-ENABLE_KICKOFFS-"].update(self.kickoffs_enabled)
        window["-SPIKES_ARE_TEAM_STATS-"].update(self.spikes_are_team_stats)
        window["-USE_XFL_KICKOFF-"].update(self.use_xfl_kickoff)
        window["-DROP_KICK_ENABLED-"].update(self.drop_kick_enabled)
        window["-DROP_KICK_BONUS_POINT-"].update(self.drop_kick_bonus_point)
        window["-FG_ADDS_EZ_LENGTH-"].update(self.fg_adds_ez_length)
        window["-LONG_FG_BONUS_POINT-"].update(self.long_fg_bonus_point)
        window["-XP_IS_FG-"].update(self.xp_is_a_fg)
        window["-ROUGES_ENABLED-"].update(self.rouges_enabled)
        window["-PUNTING_ENABLED-"].update(self.punting_enabled)
        window["-ONSIDE_PUNTING_ENABLED-"].update(self.onside_punts_enabled)
        window["-FAIR_CATCH_ENABLED-"].update(self.fair_catch_enabled)
        window["-SPECIAL_ONSIDE_PLAY_ENABLED-"].update(
            self.special_onside_play_enabled
        )

        keep_open = True
        change_count = 0
        while keep_open is True:
            event, values = window.read(timeout=1000)
            print(values)
            print(event)

            if event in (sg.WIN_CLOSED, 'Exit'):
                keep_open = False
            elif event == "-OK_BUTTON-" and (change_count != 0):
                check_flag = self.changed_settings_check()
                # print(check_flag)
                if check_flag == "Yes":
                    check = safety_check_league_ids(
                        self.league_id,
                        self.league_id_original,
                        self.sqlite3_cur
                    )
                    if check == "NOT_CLEAR":
                        pass
                    elif check == "ALL_CLEAR":
                        self.update_league_settings()
                    else:
                        raise ValueError(
                            f"Unhandled error code {check}"
                        )
                    del check
                    keep_open = False

                elif check_flag == "No":
                    pass
                del check_flag
            elif event == "-OK_BUTTON-" and (change_count == 0):
                keep_open = False
            elif event == "-CANCEL_BUTTON-":
                keep_open = False
            elif event == "-APPLY-" and (change_count != 0):
                check_flag = self.changed_settings_check()
                # print(check_flag)
                if check_flag == "Yes":
                    check = safety_check_league_ids(
                        self.league_id,
                        self.league_id_original,
                        self.sqlite3_cur
                    )
                    if check == "NOT_CLEAR":
                        pass
                    elif check == "ALL_CLEAR":
                        self.update_league_settings()
                    else:
                        raise ValueError(
                            f"Unhandled error code {check}"
                        )
                    del check
                elif check_flag == "No":
                    pass
                del check_flag
                window["-APPLY_BUTTON-"].update(
                    disabled=True
                )

            if change_count == 1:
                window["-APPLY_BUTTON-"].update(disabled=False)
            elif change_count == 0:
                window["-APPLY_BUTTON-"].update(disabled=True)
            # if event == "-LG_ID-" and len(values["-LG_ID-"]) > 5:
            #     window["-LG_ID-"].update(values["-LG_ID-"][:-1])
            # elif event == "-LG_ID-" and (
            #     values["-LG_ID-"] and
            #     values["-LG_ID-"][-1] not in (self.letters_all)
            # ):
            #     window["-LG_ID-"].update(values["-LG_ID-"][:-1])
            #     self.league_id = values["-LG_ID-"]
            # elif event == "-LG_ID-" and (
            #     values["-LG_ID-"] and
            #     values["-LG_ID-"][-1] in (self.letters_all)
            # ):
            #     window["-LG_ID-"].update(values["-LG_ID-"].upper())
            #     self.league_id = values["-LG_ID-"].upper()

            if event == "-LG_SHORT_NAME-" and len(
                values["-LG_SHORT_NAME-"]
            ) > 5:
                window["-LG_SHORT_NAME-"].update(
                    values["-LG_SHORT_NAME-"][:-1]
                )
                change_count += 1
            elif event == "-LG_SHORT_NAME-" and (
                values["-LG_SHORT_NAME-"] and
                values["-LG_SHORT_NAME-"][-1] not in (
                    self.letters_and_numbers
                )
            ):
                window["-LG_SHORT_NAME-"].update(
                    values["-LG_SHORT_NAME-"][:-1]
                )
                self.league_id = values["-LG_SHORT_NAME-"]
                change_count += 1
            elif event == "-LG_SHORT_NAME-" and (
                values["-LG_SHORT_NAME-"] and
                values["-LG_SHORT_NAME-"][-1] in (
                    self.letters_and_numbers
                )
            ):
                window["-LG_SHORT_NAME-"].update(
                    values["-LG_SHORT_NAME-"].upper()
                )
                self.league_id = values["-LG_SHORT_NAME-"].upper()
                change_count += 1

            if event == "-LG_LONG_NAME-" and (
                len(values["-LG_LONG_NAME-"]) > 256
            ):
                window["-LG_LONG_NAME-"].update(
                    values["-LG_LONG_NAME-"][:-1]
                )
            elif event == "-LG_LONG_NAME-" and (
                values["-LG_LONG_NAME-"] and
                values["-LG_LONG_NAME-"][-1] not in (
                    self.letters_and_numbers
                )
            ):
                window["-LG_LONG_NAME-"].update(
                    values["-LG_LONG_NAME-"][:-1]
                )
                self.league_long_name = values["-LG_LONG_NAME-"]
            elif event == "-LG_LONG_NAME-" and (
                values["-LG_LONG_NAME-"] and
                values["-LG_LONG_NAME-"][-1] in (
                    self.letters_and_numbers
                )
            ):
                window["-LG_LONG_NAME-"].update(
                    values["-LG_LONG_NAME-"]
                )
                self.league_long_name = values["-LG_LONG_NAME-"]

            if event == "-LG_LONG_NAME-":
                self.league_long_name = values["-LG_LONG_NAME-"]
                change_count += 1
            elif event == "-LG_SHORT_NAME-":
                self.league_short_name = values["-LG_SHORT_NAME-"]
                change_count += 1
            elif event == "-LG_NOTES-":
                self.league_notes = values["-LG_NOTES-"]
                change_count += 1
            elif event == "-FIELD_LENGTH-":
                self.field_length = values["-FIELD_LENGTH-"]
                change_count += 1
            elif event == "-DOWNS-":
                self.downs = values["-DOWNS-"]
                change_count += 1
            elif event == "-FIRST_DOWN_YARDS-":
                self.first_down_yards = values["-FIRST_DOWN_YARDS-"]
                change_count += 1
            elif event == "-EZ_LENGTH-":
                self.end_zone_length = values["-EZ_LENGTH-"]
                change_count += 1
            elif event == "-KICKOFF_YARDLINE-":
                self.kickoff_yardline = values["-KICKOFF_YARDLINE-"]
                change_count += 1
            elif event == "-SAF_KICKOFF_YARDLINE-":
                self.safety_kick_yardline = values["-SAF_KICKOFF_YARDLINE-"]
                change_count += 1
            elif event == "-KICKOFF_TB_YARDLINE-":
                self.kickoff_touchback_yardline = values[
                    "-KICKOFF_TB_YARDLINE-"
                ]
                change_count += 1
            elif event == "-PUNT_TB_YARDLINE-":
                self.punt_touchback_yardline = values["-PUNT_TB_YARDLINE-"]
                change_count += 1
            elif event == "-NORMAL_TB_YARDLINE-":
                self.normal_touchback_yardline = values["-NORMAL_TB_YARDLINE-"]
                change_count += 1
            elif event == "-KANSAS_OT_YARDLINE-":
                self.kansas_ot_yardline = values["-KANSAS_OT_YARDLINE-"]
                change_count += 1
            elif event == "-PAT_YARDLINE-":
                self.pat_yardline = values["-PAT_YARDLINE-"]
                change_count += 1
            elif event == "-KANSAS_OT_YARDLINE-":
                self.kansas_ot_yardline = values["-KANSAS_OT_YARDLINE-"]
                change_count += 1
            elif event == "-1PC_YARDLINE-":
                self.one_PC_Yardline = values["-1PC_YARDLINE-"]
                change_count += 1
            elif event == "-2PC_YARDLINE-":
                self.two_PC_Yardline = values["-2PC_YARDLINE-"]
                change_count += 1
            elif event == "-3PC_YARDLINE-":
                self.three_PC_Yardline = values["-3PC_YARDLINE-"]
                change_count += 1
            elif event == "-QUARTERS-":
                self.quarters = values["-QUARTERS-"]
                change_count += 1
            elif event == "-TIMEOUTS-":
                self.timeouts_per_half = values["-TIMEOUTS-"]
                change_count += 1
            elif event == "-QUARTER_MINUTES-":
                self.quarter_seconds = values["-QUARTER_MINUTES-"] * 60
                self.half_seconds = (values["-QUARTER_MINUTES-"] * 60) * 2
                self.game_seconds = (
                    (values["-QUARTER_MINUTES-"] * 60) * self.quarters
                )
                change_count += 1
            elif event == "-OT_QUARTER_MINUTES-":
                self.ot_period_seconds = values["-OT_QUARTER_MINUTES-"] * 60
                change_count += 1
            elif event == "-OT_PERIODS_UNTIL_SHOOTOUT-":
                self.ot_periods_until_shootout = values[
                    "-OT_PERIODS_UNTIL_SHOOTOUT-"
                ]
                change_count += 1
            elif event == "-MIN_XFL_OT_PERIODS-":
                self.min_xfl_ot_periods = values["-MIN_XFL_OT_PERIODS-"]
                change_count += 1
            elif event == "-SET_XFL_OT_PERIODS-":
                self.set_xfl_ot_periods = values["-SET_XFL_OT_PERIODS-"]
                change_count += 1
            elif event == "-TD_POINTS-":
                self.touchdown_points = values["-TD_POINTS-"]
                change_count += 1
            elif event == "-FG_POINTS-":
                self.field_goal_points = values["-FG_POINTS-"]
                change_count += 1
            elif event == "-SAF_POINTS-":
                self.safety_points = values["-SAF_POINTS-"]
                change_count += 1
            elif event == "-PAT_POINTS-":
                self.pat_points = values["-PAT_POINTS-"]
                change_count += 1
            elif event == "-PAT_DEFENSE-":
                self.pat_defense = values["-PAT_DEFENSE-"]
                change_count += 1
            elif event == "-PAT_SAF-":
                self.pat_safety = values["-PAT_SAF-"]
                change_count += 1
            elif event == "-PLAYER_COUNT-":
                self.players_on_field = values["-PLAYER_COUNT-"]
            # Pre-season OT
            elif event == "-IS_PRESEASON_OT-":
                window["-PRE_SEASON_OT_TYPE-"].update(disabled=False)
                self.preseason_ot_enabled = values["-IS_PRESEASON_OT-"]
                change_count += 1
            # Regular season OT
            elif event == "-IS_REG_SEASON_OT-":
                window["-REG_SEASON_OT_TYPE-"].update(disabled=True)
                self.reg_season_ot_enabled = values["-IS_REG_SEASON_OT-"]
                change_count += 1
            # Postseason OT
            elif event == "-IS_POST_SEASON_OT-":
                window["-POST_SEASON_OT_TYPE-"].update(disabled=False)
                self.postseason_ot_enabled = values["-IS_POST_SEASON_OT-"]
                change_count += 1
            # Miscellaneous items
            elif event == "-TWO_FORWARD_PASSES-":
                self.two_forward_passes = values["-TWO_FORWARD_PASSES-"]
                change_count += 1
            elif event == "-SPIKES_ARE_TEAM_STATS-":
                self.spikes_are_team_stats = values["-SPIKES_ARE_TEAM_STATS-"]
                change_count += 1
            elif event == "-SACKS_ARE_RUSHES-":
                self.sacks_are_rushes = values["-SACKS_ARE_RUSHES-"]
                change_count += 1
            elif event == "-KNEELDOWNS_ARE_TEAM_STATS-":
                self.kneeldowns_are_team_stats = values[
                    "-KNEELDOWNS_ARE_TEAM_STATS-"
                ]
                change_count += 1
            elif event == "-KICKOFF_FC_TOUCHBACK_RULE-":
                self.kickoff_fc_always_goes_to_touchback = values[
                    "-KICKOFF_FC_TOUCHBACK_RULE-"
                ]
                change_count += 1
            elif event == "-ENABLE_KICKOFFS-":
                self.kickoffs_enabled = values["-ENABLE_KICKOFFS-"]
                change_count += 1
            elif event == "-USE_XFL_KICKOFF-":
                self.use_xfl_kickoff = values["-USE_XFL_KICKOFF-"]
                change_count += 1
            elif event == "-DROP_KICK_ENABLED-":
                self.drop_kick_enabled = values["-DROP_KICK_ENABLED-"]
                change_count += 1
            elif event == "-DROP_KICK_BONUS_POINT-":
                self.drop_kick_bonus_point = values["-DROP_KICK_BONUS_POINT-"]
                change_count += 1
            elif event == "-FG_ADDS_EZ_LENGTH-":
                self.fg_adds_ez_length = values["-FG_ADDS_EZ_LENGTH-"]
                change_count += 1
            elif event == "-LONG_FG_BONUS_POINT-":
                self.long_fg_bonus_point = values["-LONG_FG_BONUS_POINT-"]
                change_count += 1
            elif event == "-XP_IS_FG-":
                self.xp_is_a_fg = values["-XP_IS_FG-"]
                change_count += 1
            elif event == "-ROUGES_ENABLED-":
                self.rouges_enabled = values["-ROUGES_ENABLED-"]
                change_count += 1
            elif event == "-PUNTING_ENABLED-":
                self.punting_enabled = values["-PUNTING_ENABLED-"]
                change_count += 1
            elif event == "-ONSIDE_PUNTING_ENABLED-":
                self.onside_punts_enabled = values["-ONSIDE_PUNTING_ENABLED-"]
                change_count += 1
            elif event == "-FAIR_CATCH_ENABLED-":
                self.fair_catch_enabled = values["-FAIR_CATCH_ENABLED-"]
                change_count += 1
            elif event == "-SPECIAL_ONSIDE_PLAY_ENABLED-":
                self.special_onside_play_enabled = values[
                    "-SPECIAL_ONSIDE_PLAY_ENABLED-"
                ]
                change_count += 1

        window.close()


def safety_check_league_ids(
    league_id: str, league_id_original: str, cur: sqlite3.Cursor
) -> str:
    """
    Validates that if you're changing the league ID,
    you're not infringing on a league ID that already exists.
    """
    sql_script = """
    SELECT DISTINCT
        league_id
    FROM fb_leagues
    WHERE league_id != ?
    """
    data = cur.execute(sql_script, [(league_id_original)])
    data.fetchall()
    lg_id_df = pl.DataFrame(
        data=data,
        schema_overrides={"league_id": pl.String},
    )
    if len(lg_id_df) > 0:
        lg_id_arr = lg_id_df["league_id"].to_list()
        if league_id in lg_id_arr:
            sg.popup_error(
                f"\"{league_id}\" is a league that already exists."
            )
            return "NOT_CLEAR"
        else:
            return "ALL_CLEAR"
    else:
        return "ALL_CLEAR"


def new_league_view(settings_json: dict):
    """
    """
    # Get SQLite3 connections
    sqlite3_con, sqlite3_cur = initialize_sqlite3_connectors()

    sg.theme(settings_json["app_theme"])
    league_id = ""
    league_long_name = ""
    letters_and_numbers = LettersAndNumbers.letters_and_numbers(
        include_space=True
    )

    base_ruleset_arr = [
        "AAF",
        # "Arena",
        "CFL",
        "High School",
        # "NCAA pre-1995",
        # "NCAA 1996-2018",
        # "NCAA 2019-2021",
        # "NCAA 2021-Present",
        "NCAA",
        # "NFL pre-1974",
        # "NFL 1974-1993",
        # "NFL 1994-2009",
        # "NFL 2010-2011",
        # "NFL 2012-2014",
        # "NFL 2015-2016",
        # "NFL 2017-2021",
        # "NFL 2022-2023",
        # "NFL 2024-Present",
        "NFL",
        # "USFL (1982)",
        # "USFL (2022)",
        "XFL",
        # "UFL (2009)",
        "UFL (2024)"
    ]
    current_year = datetime.now().year
    latest_season = current_year

    layout = [
        [
            sg.Text(
                "New League",
                font="Arial 24",
                justification="center",
                expand_x=True,
            )
        ],
        [
            sg.Text(
                "League ID:\t"
            ),
            sg.Input(
                key="-LG_SHORT_NAME-",
                enable_events=True,
                size=(7, 1)
            ),
        ],
        [
            sg.Text(
                "League name:\t"
            ),
            sg.Input(
                key="-LG_LONG_NAME-",
                enable_events=True,
                size=(40, 1)
            )
        ],
        [
            sg.Text(
                "Base ruleset:\t"
            ),
            sg.Combo(
                values=base_ruleset_arr,
                default_value="NFL",
                size=(15, 1),
                key="-BASE_RULESET-",
                readonly=True
            )
        ],
        [
            sg.Text(
                "Latest season:\t"
            ),
            sg.Combo(
                values=[x for x in range(1900, current_year+5)],
                default_value=current_year,
                size=(15, 1),
                enable_events=True,
                key="-LATEST_SEASON-",
                readonly=True
            )
        ],
        [
            sg.Push(),
            sg.Button(
                "Create New League",
                key="-CREATE_NEW_LEAGUE_BUTTON-",
                enable_events=True
            ),
            sg.Button(
                "Cancel",
                key="-CANCEL_BUTTON-",
                enable_events=True
            )
        ]
    ]

    window = sg.Window(
        "New League...",
        layout=layout,
        # size=(500, 600),
        resizable=False,
        finalize=True,
        keep_on_top=False
    )

    keep_open = True
    while keep_open is True:
        event, values = window.read(timeout=1000)
        print(values)
        print(event)
        print(league_id)

        # cur.executescript(SqliteSampleFiles.schedule_sql_file())
        # con.commit()

        if event in (sg.WIN_CLOSED, 'Exit', "-CANCEL_BUTTON-"):
            keep_open = False
        elif event == "-CREATE_NEW_LEAGUE_BUTTON-" and (
            values["-BASE_RULESET-"] == "NFL"
        ):
            sql_script = """
            INSERT INTO "fb_leagues"
            (
                "league_id",
                "league_short_name",
                "league_long_name",
                "field_length",
                "downs",
                "first_down_yards",
                "end_zone_length",
                "kickoff_yardline",
                "safety_kick_yardline",
                "kickoff_touchback_yardline",
                "punt_touchback_yardline",
                "normal_touchback_yardline",
                "kansas_ot_yardline",
                "pat_yardline",
                "1PC_yardline",
                "2PC_yardline",
                "3PC_yardline",
                "ot_period_seconds",
                "reg_season_ot_type",
                "postseason_ot_type",
                "kickoff_fc_always_goes_to_touchback"
            )
            VALUES
            (
                ?,
                ?,
                ?,
                100,
                4,
                10,
                10,
                35,
                20,
                75,
                80,
                80,
                25,
                15,
                3,
                5,
                10,
                600,
                "Modified Sudden Death OT",
                "Super Modified Sudden Death OT",
                1
            );
            """
            sql_script_2 = """
            INSERT INTO "fb_seasons"
            (
                "season",
                "league_id",
                "field_length",
                "downs",
                "first_down_yards",
                "end_zone_length",
                "kickoff_yardline",
                "safety_kick_yardline",
                "kickoff_touchback_yardline",
                "punt_touchback_yardline",
                "normal_touchback_yardline",
                "kansas_ot_yardline",
                "pat_yardline",
                "1PC_yardline",
                "2PC_yardline",
                "3PC_yardline",
                "ot_period_seconds",
                "reg_season_ot_type",
                "postseason_ot_type",
                "kickoff_fc_always_goes_to_touchback"
            )
            VALUES
            (
                ?,
                ?,
                100,
                4,
                10,
                10,
                35,
                20,
                75,
                80,
                80,
                25,
                15,
                3,
                5,
                10,
                600,
                "Modified Sudden Death OT",
                "Super Modified Sudden Death OT",
                1
            );
            """.replace("            ", "")
            try:
                sqlite3_cur.executemany(
                    sql_script,
                    [(
                        league_id,
                        league_id,
                        league_long_name
                    )]
                )
                sqlite3_con.commit()

                sqlite3_cur.executemany(
                    sql_script_2,
                    [(
                        latest_season,
                        league_id
                    )]
                )
                sqlite3_con.commit()
                keep_open = False
            except sqlite3.IntegrityError:
                sg.popup_error(
                    "You have already created a league " +
                    f"with a league ID of `{league_id}`.\n" +
                    "Please specify a differient league ID."
                )
            except Exception as e:
                logging.warning(
                    f"Unhandled exception `{e}`"
                )
                raise e
        elif event == "-CREATE_NEW_LEAGUE_BUTTON-" and (
            values["-BASE_RULESET-"] == "NCAA"
        ):
            sql_script = """
            INSERT INTO "fb_leagues"
            (
                "league_id",
                "league_short_name",
                "league_long_name",
                "field_length",
                "downs",
                "first_down_yards",
                "end_zone_length",
                "kickoff_yardline",
                "safety_kick_yardline",
                "kickoff_touchback_yardline",
                "punt_touchback_yardline",
                "normal_touchback_yardline",
                "kansas_ot_yardline",
                "pat_yardline",
                "1PC_yardline",
                "2PC_yardline",
                "3PC_yardline",
                "ot_period_seconds",
                "preseason_ot_type",
                "reg_season_ot_type",
                "postseason_ot_type",
                "spikes_are_team_stats",
                "sacks_are_rushes",
                "kneeldowns_are_team_stats",
                "kickoff_fc_always_goes_to_touchback"
            )
            VALUES
            (
                ?,
                ?,
                ?,
                100,
                4,
                10,
                10,
                35,
                20,
                75,
                80,
                80,
                25,
                3,
                3,
                5,
                10,
                0,
                "NCAA OT",
                "NCAA OT",
                "NCAA OT",
                1,
                1,
                1,
                1
            );
            """
            sql_script_2 = """
            INSERT INTO "fb_seasons"
            (
                "season",
                "league_id",
                "field_length",
                "downs",
                "first_down_yards",
                "end_zone_length",
                "kickoff_yardline",
                "safety_kick_yardline",
                "kickoff_touchback_yardline",
                "punt_touchback_yardline",
                "normal_touchback_yardline",
                "kansas_ot_yardline",
                "pat_yardline",
                "1PC_yardline",
                "2PC_yardline",
                "3PC_yardline",
                "ot_period_seconds",
                "preseason_ot_type",
                "reg_season_ot_type",
                "postseason_ot_type",
                "spikes_are_team_stats",
                "sacks_are_rushes",
                "kneeldowns_are_team_stats",
                "kickoff_fc_always_goes_to_touchback"
            )
            VALUES
            (
                ?,
                ?,
                100,
                4,
                10,
                10,
                35,
                20,
                75,
                80,
                80,
                25,
                3,
                3,
                5,
                10,
                0,
                "NCAA OT",
                "NCAA OT",
                "NCAA OT",
                1,
                1,
                1,
                1
            );

            """
            try:
                sqlite3_cur.executemany(
                    sql_script,
                    [(
                        league_id,
                        league_id,
                        league_long_name,
                    )]
                )
                sqlite3_con.commit()

                sqlite3_cur.executemany(
                    sql_script_2,
                    [(
                        latest_season,
                        league_id
                    )]
                )
                sqlite3_con.commit()
                keep_open = False
            except sqlite3.IntegrityError:
                sg.popup_error(
                    "You have already created a league " +
                    f"with a league ID of `{league_id}`.\n" +
                    "Please specify a differient league ID."
                )
            except Exception as e:
                logging.warning(
                    f"Unhandled exception `{e}`"
                )
                raise e
        elif event == "-CREATE_NEW_LEAGUE_BUTTON-" and (
            values["-BASE_RULESET-"] == "CFL"
        ):
            sql_script = """
            INSERT INTO "fb_leagues"
            (
                "league_id",
                "league_short_name",
                "league_long_name",
                "field_length",
                "downs",
                "first_down_yards",
                "end_zone_length",
                "kickoff_yardline",
                "safety_kick_yardline",
                "kickoff_touchback_yardline",
                "punt_touchback_yardline",
                "normal_touchback_yardline",
                "kansas_ot_yardline",
                "pat_yardline",
                "1PC_yardline",
                "2PC_yardline",
                "3PC_yardline",
                "timeouts_per_half",
                "ot_period_seconds",
                "fg_adds_ez_length",
                "rouges_enabled",
                "onside_punts_enabled",
                "fair_catch_enabled",
                "players_on_field"
            )
            VALUES
            (
                ?,
                ?,
                ?,
                110,
                3,
                10,
                20,
                30,
                20,
                85,
                85,
                85,
                35,
                25,
                3,
                3,
                10,
                2,
                0,
                0,
                1,
                1,
                0,
                1
            );
            """
            sql_script_2 = """
            INSERT INTO "fb_seasons"
            (
                "season",
                "league_id",
                "field_length",
                "downs",
                "first_down_yards",
                "end_zone_length",
                "kickoff_yardline",
                "safety_kick_yardline",
                "kickoff_touchback_yardline",
                "punt_touchback_yardline",
                "normal_touchback_yardline",
                "kansas_ot_yardline",
                "pat_yardline",
                "1PC_yardline",
                "2PC_yardline",
                "3PC_yardline",
                "timeouts_per_half",
                "ot_period_seconds",
                "fg_adds_ez_length",
                "rouges_enabled",
                "onside_punts_enabled",
                "fair_catch_enabled",
                "players_on_field"
            )
            VALUES
            (
                ?,
                ?,
                110,
                3,
                10,
                20,
                30,
                20,
                85,
                85,
                85,
                35,
                25,
                3,
                3,
                10,
                2,
                0,
                0,
                1,
                1,
                0,
                1
            );
            """
            try:
                sqlite3_cur.executemany(
                    sql_script,
                    [(
                        league_id,
                        league_id,
                        league_long_name,
                    )]
                )
                sqlite3_con.commit()

                sqlite3_cur.executemany(
                    sql_script_2,
                    [(
                        latest_season,
                        league_id
                    )]
                )
                sqlite3_con.commit()
                keep_open = False
            except sqlite3.IntegrityError:
                sg.popup_error(
                    "You have already created a league " +
                    f"with a league ID of `{league_id}`.\n" +
                    "Please specify a differient league ID."
                )
            except Exception as e:
                logging.warning(
                    f"Unhandled exception `{e}`"
                )
                raise e
        elif event == "-CREATE_NEW_LEAGUE_BUTTON-" and (
            values["-BASE_RULESET-"] == "UFL (2024)"
        ):
            sql_script = """
            INSERT INTO "fb_leagues"
            (
                "league_id",
                "league_short_name",
                "league_long_name",
                "kickoff_yardline",
                "safety_kick_yardline",
                "kickoff_touchback_yardline",
                "punt_touchback_yardline",
                "normal_touchback_yardline",
                "1PC_yardline",
                "2PC_yardline",
                "3PC_yardline",
                "ot_period_seconds",
                "min_xfl_ot_periods",
                "set_xfl_ot_periods",
                "xfl_pat",
                "preseason_ot_type",
                "reg_season_ot_type",
                "postseason_ot_type",
                "xp_is_a_fg",
                "special_onside_play_enabled",
                "use_xfl_kickoff"
            )
            VALUES
            (
                ?,
                ?,
                ?,
                20,
                20,
                75,
                80,
                80,
                3,
                5,
                10,
                0,
                3,
                1,
                1,
                "XFL OT",
                "XFL OT",
                "XFL OT",
                0,
                1,
                1
            );
            """
            sql_script_2 = """
            INSERT INTO "fb_seasons"
            (
                "season",
                "league_id",
                "kickoff_yardline",
                "safety_kick_yardline",
                "kickoff_touchback_yardline",
                "punt_touchback_yardline",
                "normal_touchback_yardline",
                "1PC_yardline",
                "2PC_yardline",
                "3PC_yardline",
                "ot_period_seconds",
                "min_xfl_ot_periods",
                "set_xfl_ot_periods",
                "xfl_pat",
                "preseason_ot_type",
                "reg_season_ot_type",
                "postseason_ot_type",
                "xp_is_a_fg",
                "special_onside_play_enabled",
                "use_xfl_kickoff"
            )
            VALUES
            (
                ?,
                ?,
                20,
                20,
                75,
                80,
                80,
                3,
                5,
                10,
                0,
                3,
                1,
                1,
                "XFL OT",
                "XFL OT",
                "XFL OT",
                0,
                1,
                1
            );
            """
            try:
                sqlite3_cur.executemany(
                    sql_script,
                    [(
                        league_id,
                        league_id,
                        league_long_name,
                    )]
                )
                sqlite3_con.commit()

                sqlite3_cur.executemany(
                    sql_script_2,
                    [(
                        latest_season,
                        league_id
                    )]
                )
                sqlite3_con.commit()
                keep_open = False
            except sqlite3.IntegrityError:
                sg.popup_error(
                    "You have already created a league " +
                    f"with a league ID of `{league_id}`.\n" +
                    "Please specify a differient league ID."
                )
            except Exception as e:
                logging.warning(
                    f"Unhandled exception `{e}`"
                )
                raise e
        elif event == "-CREATE_NEW_LEAGUE_BUTTON-" and (
            values["-BASE_RULESET-"] == "XFL"
        ):
            sql_script = """
            INSERT INTO "fb_leagues"
            (
                "league_id",
                "league_short_name",
                "league_long_name",
                "kickoff_yardline",
                "kickoff_touchback_yardline",
                "punt_touchback_yardline",
                "normal_touchback_yardline",
                "1PC_yardline",
                "2PC_yardline",
                "3PC_yardline",
                "min_xfl_ot_periods",
                "set_xfl_ot_periods",
                "preseason_ot_type",
                "reg_season_ot_type",
                "postseason_ot_type",
                "two_forward_passes",
                "use_xfl_kickoff",
                "special_onside_play_enabled"
            )
            VALUES
            (
                ?,
                ?,
                ?,
                30,
                65,
                65,
                80,
                3,
                5,
                10,
                3,
                1,
                "XFL OT",
                "XFL OT",
                "XFL OT",
                1,
                1,
                1
            );
            """
            sql_script_2 = """
            INSERT INTO "fb_seasons"
            (
                "season",
                "league_id",
                "kickoff_yardline",
                "kickoff_touchback_yardline",
                "punt_touchback_yardline",
                "normal_touchback_yardline",
                "1PC_yardline",
                "2PC_yardline",
                "3PC_yardline",
                "min_xfl_ot_periods",
                "set_xfl_ot_periods",
                "preseason_ot_type",
                "reg_season_ot_type",
                "postseason_ot_type",
                "two_forward_passes",
                "use_xfl_kickoff",
                "special_onside_play_enabled"
            )
            VALUES
            (
                ?,
                ?,
                30,
                65,
                65,
                80,
                3,
                5,
                10,
                3,
                1,
                "XFL OT",
                "XFL OT",
                "XFL OT",
                1,
                1,
                1
            );

            """
            try:
                sqlite3_cur.executemany(
                    sql_script,
                    [(
                        league_id,
                        league_id,
                        league_long_name,
                    )]
                )
                sqlite3_con.commit()

                sqlite3_cur.executemany(
                    sql_script_2,
                    [(
                        latest_season,
                        league_id
                    )]
                )
                sqlite3_con.commit()
                keep_open = False
            except sqlite3.IntegrityError:
                sg.popup_error(
                    "You have already created a league " +
                    f"with a league ID of `{league_id}`.\n" +
                    "Please specify a differient league ID."
                )
            except Exception as e:
                logging.warning(
                    f"Unhandled exception `{e}`"
                )
                raise e
        elif event == "-CREATE_NEW_LEAGUE_BUTTON-" and (
            values["-BASE_RULESET-"] == "AAF"
        ):
            sql_script = """
            INSERT INTO "fb_leagues"
            (
                "league_id",
                "league_short_name",
                "league_long_name",
                "kansas_ot_yardline",
                "ot_period_seconds",
                "kickoffs_enabled",
                "xp_is_a_fg",
                "special_onside_play_enabled"
            )
            VALUES
            (
                ?,
                ?,
                ?,
                10,
                0,
                0,
                0,
                1
            );
            """
            sql_script_2 = """
            INSERT INTO "fb_seasons"
            (
                "season",
                "league_id",
                "kansas_ot_yardline",
                "ot_period_seconds",
                "kickoffs_enabled",
                "xp_is_a_fg",
                "special_onside_play_enabled"
            )
            VALUES
            (
                ?,
                ?,
                10,
                0,
                0,
                0,
                1
            );

            """
            try:
                sqlite3_cur.executemany(
                    sql_script,
                    [(
                        league_id,
                        league_id,
                        league_long_name
                    )]
                )
                sqlite3_con.commit()

                sqlite3_cur.executemany(
                    sql_script_2,
                    [(
                        latest_season,
                        league_id
                    )]
                )
                sqlite3_con.commit()
                keep_open = False
            except sqlite3.IntegrityError:
                sg.popup_error(
                    "You have already created a league " +
                    f"with a league ID of `{league_id}`.\n" +
                    "Please specify a differient league ID."
                )
            except Exception as e:
                logging.warning(
                    f"Unhandled exception `{e}`"
                )
                raise e
        elif event == "-CREATE_NEW_LEAGUE_BUTTON-" and (
            values["-BASE_RULESET-"] == "High School"
        ):
            sql_script = """
            INSERT INTO "fb_leagues"
            (
                "league_id",
                "league_short_name",
                "league_long_name",
                "game_seconds",
                "half_seconds",
                "quarter_seconds",
                "sacks_are_rushes",
                "kneeldowns_are_team_stats"
            )
            VALUES
            (
                ?,
                ?,
                ?,
                -- Not all HS leagues are built the same
                -- and I am not building out a ruleset for literally
                -- every HS league.
                2880,
                1440,
                720,
                1,
                1
            );
            """
            sql_script_2 = """
            INSERT INTO "fb_seasons"
            (
                "season",
                "league_id",
                "game_seconds",
                "half_seconds",
                "quarter_seconds",
                "sacks_are_rushes",
                "kneeldowns_are_team_stats"
            )
            VALUES
            (
                ?,
                ?,
                2880,
                1440,
                720,
                1,
                1
            );
            """
            try:
                sqlite3_cur.executemany(
                    sql_script,
                    [(
                        league_id,
                        league_id,
                        league_long_name
                    )]
                )
                sqlite3_con.commit()

                sqlite3_cur.executemany(
                    sql_script_2,
                    [(
                        latest_season,
                        league_id
                    )]
                )
                sqlite3_con.commit()

                keep_open = False
            except sqlite3.IntegrityError:
                sg.popup_error(
                    "You have already created a league " +
                    f"with a league ID of `{league_id}`.\n" +
                    "Please specify a differient league ID."
                )
            except Exception as e:
                logging.warning(
                    f"Unhandled exception `{e}`"
                )
                raise e

        if event == "-LG_SHORT_NAME-" and (
            len(values["-LG_SHORT_NAME-"]) > 5
        ):
            window["-LG_SHORT_NAME-"].update(
                values["-LG_SHORT_NAME-"][:-1]
            )
        elif event == "-LG_SHORT_NAME-" and (
            values["-LG_SHORT_NAME-"] and
            values["-LG_SHORT_NAME-"][-1] not in (
                letters_and_numbers
            )
        ):
            window["-LG_SHORT_NAME-"].update(
                values["-LG_SHORT_NAME-"][:-1]
            )
            league_id = values["-LG_SHORT_NAME-"]
        elif event == "-LG_SHORT_NAME-" and (
            values["-LG_SHORT_NAME-"] and
            values["-LG_SHORT_NAME-"][-1] in (
                letters_and_numbers
            )
        ):
            window["-LG_SHORT_NAME-"].update(
                values["-LG_SHORT_NAME-"].upper()
            )
            league_id = values["-LG_SHORT_NAME-"].upper()
        if event == "-LG_LONG_NAME-" and (
            len(values["-LG_LONG_NAME-"]) > 256
        ):
            window["-LG_LONG_NAME-"].update(
                values["-LG_LONG_NAME-"][:-1]
            )
        elif event == "-LG_LONG_NAME-" and (
            values["-LG_LONG_NAME-"] and
            values["-LG_LONG_NAME-"][-1] not in (
                letters_and_numbers
            )
        ):
            window["-LG_LONG_NAME-"].update(
                values["-LG_LONG_NAME-"][:-1]
            )
            league_long_name = values["-LG_LONG_NAME-"]
        elif event == "-LG_LONG_NAME-" and (
            values["-LG_LONG_NAME-"] and
            values["-LG_LONG_NAME-"][-1] in (
                letters_and_numbers
            )
        ):
            window["-LG_LONG_NAME-"].update(
                values["-LG_LONG_NAME-"]
            )
            league_long_name = values["-LG_LONG_NAME-"]
        elif event == "-LATEST_SEASON-":
            latest_season = values["-LATEST_SEASON-"]

    window.close()
