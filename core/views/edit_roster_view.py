"""
- Creation Date: 03/10/2024 4:35 PM EDT
- Last Updated: 05/29/2024 01:15 AM EDT
- Authors: Joseph Armstrong (armstrongjoseph08@gmail.com)
- file: `./core/views/new_game_view.py`
- Purpose: Code behind for the window that adds a game to a schedule.
"""

import logging
import polars as pl
import FreeSimpleGUI as sg

from core.database.load_db_elements import SqliteLoadData
from core.database.sqlite3_connectors import initialize_sqlite3_connectors
from core.other.embedded import EmbeddedElements, LettersAndNumbers


class RosterView:
    """
    Handles logic with editing the rosters of teams.
    """

    letters_all = LettersAndNumbers.letters_all(include_space=True)
    letters_lower = LettersAndNumbers.letters_lower()
    letters_upper = LettersAndNumbers.letters_upper()
    numbers_all = LettersAndNumbers.numbers_all()
    numbers_with_dashes = LettersAndNumbers.numbers_all(
        include_dash_and_underscore=True
    )
    letters_and_numbers = LettersAndNumbers.letters_and_numbers(
        include_space=True,
        include_dash_and_underscore=True
    )
    upper_letters_and_numbers = LettersAndNumbers.upper_letters_and_numbers()

    player_jersey_numbers_arr = [x for x in range(0, 100)]
    player_positions = [
        "QB",
        "RB",
        "HB",
        "FB",
        "WR",
        # "SWR",
        "SE",
        "FL",
        "TE",
        "OL",
        "OT",
        # "LT",
        # "RT",
        "OG",
        # "LG",
        # "RG",
        "C",
        "DL",
        "DE",
        # "RDE",
        # "LDE",
        "DT",
        # "RDT",
        # "LDT",
        "NT",
        "NG",
        "LB",
        "OLB",
        # "RLB",
        # "LLB",
        # "ROLB",
        # "LOLB",
        "MLB",
        "ILB",
        # "LILB",
        # "RILB",
        # "MIKE",
        # "WILL",
        # "SAM",
        # "RAM",
        # "JACK",
        "DB",
        "CB",
        # "RCB",
        # "LCB",
        "SCB",
        "SAF",
        "SS",
        "FS",
        "K",
        "PK",
        "P",
        "LS",
        "RET",
        "PR",
        "KR",
        "ATH"
    ]
    roster_status = ["ACT", "INA", "PUP", "CUT", "RES"]

    # sqlite3 connectors
    sqlite3_con = None
    sqlite3_cur = None

    settings_dict = {}
    app_theme = ""

    team_df = pl.DataFrame()
    team_ids_arr = [None]

    roster_df = pl.DataFrame()
    show_roster_df = pl.DataFrame()

    show_height = ""
    show_height_arr = [
        "4' 0\"",
        "4' 1\"",
        "4' 2\"",
        "4' 3\"",
        "4' 4\"",
        "4' 6\"",
        "4' 7\"",
        "4' 8\"",
        "4' 9\"",
        "4' 10\"",
        "4' 11\"",
        "5' 0\"",
        "5' 1\"",
        "5' 2\"",
        "5' 3\"",
        "5' 4\"",
        "5' 5\"",
        "5' 6\"",
        "5' 7\"",
        "5' 8\"",
        "5' 9\"",
        "5' 10\"",
        "5' 11\"",
        "6' 0\"",
        "6' 1\"",
        "6' 2\"",
        "6' 3\"",
        "6' 4\"",
        "6' 5\"",
        "6' 6\"",
        "6' 7\"",
        "6' 8\"",
        "6' 9\"",
        "6' 10\"",
        "6' 11\"",
        "7' 0\"",
        "7' 1\"",
        "7' 2\"",
        "7' 3\"",
        "7' 4\"",
        "7' 5\"",
        "7' 6\"",
        "7' 7\"",
        "7' 8\"",
        "7' 9\"",
        "7' 10\"",
        "7' 11\"",
    ]
    # new_player_id = 0

    season = 0
    league_id = ""
    team_id = ""

    # Player info
    player_id = 0
    position = ""
    depth_chart_position = ""
    jersey_number = 0
    status = ""  # Can be `ACT`, `INA`, `PUP`, `CUT`, or `RES`
    player_full_name = ""
    player_football_name = ""
    player_first_name = ""
    player_last_name = ""
    player_bday = ""  # Handled with sg.CalendarButton()
    height = 0
    # `height_ft` and `height_in` will be handled by the app, not the user.
    height_ft = 0
    height_in = 0
    weight = 0
    college = ""

    fb_master_player_id = ""
    gsis_id = ""
    espn_id = 0
    sportradar_id = ""  # This is a UID
    yahoo_id = 0
    rotowire_id = 0
    pff_id = 0
    pfr_id = ""
    fantasy_data_id = 0
    sleeper_id = 0
    esb_id = ""
    status_description_abbr = ""
    entry_year = None
    rookie_year = None
    smart_id = ""
    sr_player_id = ""
    stats_crew_player_id = ""
    footballdb_player_id = ""
    ncaa_player_id = ""
    arenafan_player_id = ""
    years_exp = 0
    headshot_url = ""
    # ngs_position = ""

    def __init__(
        self,
        settings_json: dict,
        season: int,
        league_id: str
    ) -> None:
        """ """
        self.settings_dict = settings_json
        self.season = season
        self.league_id = league_id
        self.app_theme = self.settings_dict["app_theme"]
        self.sqlite3_con, self.sqlite3_cur = initialize_sqlite3_connectors()

        self.initial_data_load()

        self.rosters_view()

    def initial_data_load(self):
        """ """
        self.team_df = SqliteLoadData.load_fb_teams(
            con=self.sqlite3_con, cur=self.sqlite3_cur
        )
        self.team_df = self.team_df.filter(
            (pl.col("league_id") == self.league_id) &
            (pl.col("season") == self.season)
        )

        self.team_ids_arr = self.team_df["team_id"].to_list()
        self.team_id = self.team_ids_arr[0]

        if len(self.team_ids_arr) == 0:
            self.show_roster_df = self.team_df
        else:
            self.refresh_show_roster(team_id=self.team_ids_arr[0])

        # print(self.season_df)

    def refresh_show_roster(self, team_id: str) -> None:
        self.roster_df = SqliteLoadData.load_fb_rosters(
            con=self.sqlite3_con, cur=self.sqlite3_cur
        )
        self.show_roster_df = self.roster_df
        self.show_roster_df = self.show_roster_df.filter(
            (pl.col("team_id") == team_id)
        )
        self.show_roster_df = self.show_roster_df[
            [
                "team_id",
                "player_id",
                "jersey_number",
                "depth_chart_position",
                "player_full_name",
                "player_first_name",
                "player_last_name",
            ]
        ]
        self.show_roster_df = self.show_roster_df.sort(
            "team_id",
            "jersey_number",
        )

    def validate_player_input(self) -> bool:
        """ """
        if len(self.depth_chart_position) >= 1:
            pass
        else:
            sg.PopupError(
                "You must input a value for " +
                "\"Position\"."
            )
            return False

        self.position = self.depth_chart_position

        if len(str(self.jersey_number)) >= 1:
            pass
        else:
            sg.PopupError(
                "You must input a value for " +
                "\"Jersey Number\"."
            )
            return False

        if len(str(self.status)) >= 1:
            pass
        else:
            sg.PopupError(
                "You must input a value for " +
                "\"Roster Status\"."
            )
            return False

        if (len(str(self.weight)) >= 2) and (len(str(self.weight)) <= 3):
            pass
        else:
            sg.PopupError(
                "You must input a value for " +
                "\"Weight\"."
            )
            return False

        if (len(self.player_first_name) > 2):
            pass
        elif (len(self.player_first_name) > 0) \
                and (len(self.player_first_name) < 3):
            check = sg.popup_yes_no(
                "Are you sure the player's first name " +
                f"is \"{self.player_first_name}\"?",
                title="Player Validation Check."
            )
            if check == "Yes":
                pass
            elif check == "No":
                return False
            else:
                raise Exception("Something is weird here")

        else:
            sg.PopupError(
                "You must input a value for " +
                "\"Weight\"."
            )
            return False

        if (len(self.player_last_name) > 2):
            pass
        elif (len(self.player_last_name) > 0) \
                and (len(self.player_last_name) < 3):
            check = sg.popup_yes_no(
                "Are you sure the player's last name " +
                f"is \"{self.player_last_name}\"?",
                title="Player Validation Check."
            )
            if check == "Yes":
                pass
            elif check == "No":
                return False
            else:
                raise Exception("Something is weird here")
            del check

        if len(self.player_football_name) == 0:
            self.player_football_name = self.player_first_name
        elif self.player_football_name is None:
            self.player_football_name = self.player_first_name
        else:
            pass

        if len(self.player_full_name) == 0:
            self.player_full_name = \
                f"{self.player_football_name} {self.player_last_name}"
        elif self.player_full_name is None:
            self.player_full_name = \
                f"{self.player_football_name} {self.player_last_name}"
        elif len(self.player_full_name) < 10:
            check = sg.popup_yes_no(
                "Are you sure the player's last name " +
                f"is \"{self.player_last_name}\"?",
                title="Player Validation Check."
            )
            if check == "Yes":
                pass
            elif check == "No":
                return False
            else:
                raise Exception("Something is weird here")
            del check
        else:
            pass

        return True

    def delete_player(self, player_id: int) -> bool:
        """ """
        check = sg.popup_yes_no(
            f"ARE YOU SURE YOU WANT TO DELETE {self.player_full_name}?\n\n" +
            "THIS DECISION IS NOT REVERSIBLE!\n\n" +
            "If this player has been released from the team, " +
            "it's better to set his/her roster status to \"CUT\" " +
            "compared to deleting the player.\n" +
            "If this player has been suspended from the team, " +
            "it's better to set his/her roster status to \"RES\".\n",
            "Do you really want to delete this player permanently?",
            title="CAUTION: Player Deletion"
        )
        if check == "Yes":
            sql_script = """
            DELETE FROM fb_rosters
            WHERE player_id = ?
            """
            self.sqlite3_cur.execute(
                sql_script,
                (self.player_id,)
            )
            self.sqlite3_con.commit()
            return True
        elif check == "No":
            return False
        elif check is None:
            return False
        else:
            raise ValueError(
                "Something is very wrong with your computer, " +
                "or with this instance of the application. " +
                "Function: `core.views.edit_roster_view." +
                "RosterView().delete_player()`."
            )

    def save_player(self) -> None:
        """ """
        if self.player_id == 0:
            sql_script = """
            INSERT INTO "fb_rosters"
            (
                "season",
                "league_id",
                "team_id",
                "position",
                "depth_chart_position",
                "jersey_number",
                "status",
                "player_full_name",
                "player_football_name",
                "player_first_name",
                "player_last_name",
                "player_bday",
                "height",
                "height_ft",
                "height_in",
                "weight",
                "college",
                "fb_master_player_id",
                "gsis_id",
                "espn_id",
                "sportradar_id",
                "yahoo_id",
                "rotowire_id",
                "pff_id",
                "pfr_id",
                "sleeper_id",
                "sr_player_id",
                "ncaa_player_id",
                "stats_crew_player_id",
                "footballdb_player_id",
                "arenafan_player_id",
                "years_exp",
                "headshot_url",
                "entry_year",
                "rookie_year",
                "status_description_abbr"
            )
            VALUES
            (
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?
            )
            """
            self.sqlite3_cur.executemany(
                sql_script,
                [(
                    self.season,
                    self.league_id,
                    self.team_id,
                    self.position,
                    self.depth_chart_position,
                    int(self.jersey_number),
                    self.status,
                    self.player_full_name,
                    self.player_football_name,
                    self.player_first_name,
                    self.player_last_name,
                    self.player_bday,
                    self.height,
                    self.height_ft,
                    self.height_in,
                    self.weight,
                    self.college,
                    self.fb_master_player_id,
                    self.gsis_id,
                    self.espn_id,
                    self.sportradar_id,
                    self.yahoo_id,
                    self.rotowire_id,
                    self.pff_id,
                    self.pfr_id,
                    # self.fantasy_data_id,
                    self.sleeper_id,
                    self.esb_id,
                    self.smart_id,
                    self.sr_player_id,
                    self.ncaa_player_id,
                    self.stats_crew_player_id,
                    self.footballdb_player_id,
                    self.arenafan_player_id,
                    self.years_exp,
                    self.headshot_url,
                    self.entry_year,
                    self.rookie_year,
                    self.status_description_abbr,
                )]
            )
            self.sqlite3_con.commit()

        elif self.player_id > 0:
            sql_script = """
            UPDATE "fb_rosters"
            SET
                "position" = ?,
                "depth_chart_position" = ?,
                "jersey_number" = ?,
                "status" = ?,
                "player_full_name" = ?,
                "player_football_name" = ?,
                "player_first_name" = ?,
                "player_last_name" = ?,
                "player_bday" = ?,
                "height" = ?,
                "height_ft" = ?,
                "height_in" = ?,
                "weight" = ?,
                "college" = ?,
                "fb_master_player_id" = ?,
                "gsis_id" = ?,
                "espn_id" = ?,
                "sportradar_id" = ?,
                "yahoo_id" = ?,
                "rotowire_id" = ?,
                "pff_id" = ?,
                "pfr_id" = ?,
                "fantasy_data_id" = ?,
                "sleeper_id" = ?,
                "esb_id" = ?,
                "smart_id" = ?,
                "sr_player_id" = ?,
                "ncaa_player_id" = ?,
                "stats_crew_player_id" = ?,
                "footballdb_player_id" = ?,
                "arenafan_player_id" = ?,
                "years_exp" = ?,
                "headshot_url" = ?,
                "entry_year" = ?,
                "rookie_year" = ?
            WHERE
                "player_id" = ?
            """
            self.sqlite3_cur.executemany(
                sql_script,
                [(
                    self.position,
                    self.depth_chart_position,
                    self.jersey_number,
                    self.status,
                    self.player_full_name,
                    self.player_football_name,
                    self.player_first_name,
                    self.player_last_name,
                    self.player_bday,
                    self.height,
                    self.height_ft,
                    self.height_in,
                    self.weight,
                    self.college,
                    self.fb_master_player_id,
                    self.gsis_id,
                    self.espn_id,
                    self.sportradar_id,
                    self.yahoo_id,
                    self.rotowire_id,
                    self.pff_id,
                    self.pfr_id,
                    self.fantasy_data_id,
                    self.sleeper_id,
                    self.esb_id,
                    self.smart_id,
                    self.sr_player_id,
                    self.ncaa_player_id,
                    self.stats_crew_player_id,
                    self.footballdb_player_id,
                    self.arenafan_player_id,
                    self.years_exp,
                    self.headshot_url,
                    self.entry_year,
                    self.rookie_year,
                    self.player_id
                )]
            )
            self.sqlite3_con.commit()

    def show_height_from_inches(self, ht_in: int) -> str:
        inches = ht_in % 12
        feet = ht_in // 12

        return f"{feet}' {inches}\""

    def convert_show_height(self):
        temp = self.show_height.replace("\"", "")
        self.height_ft, self.height_in = temp.split("' ")

        self.height_ft = int(self.height_ft)
        self.height_in = int(self.height_in)

        self.height = (self.height_ft * 12) + self.height_in

    def rosters_view(self) -> None:
        """ """
        def select_player(table_loc: int):
            p_id = self.show_roster_df["player_id"][table_loc]

            temp_df = self.roster_df.filter(
                (pl.col("player_id") == p_id)
            )
            del p_id

            self.player_id = temp_df["player_id"][0]
            window["-PLAYER_ID-"].update(value=self.player_id)

            self.jersey_number = temp_df["jersey_number"][0]
            window["-JERSEY_NUMBER-"].update(
                value=self.jersey_number, disabled=False
            )

            self.depth_chart_position = temp_df["depth_chart_position"][0]
            window["-PLAYER_POSITION-"].update(
                value=self.depth_chart_position, disabled=False
            )

            self.show_height = self.show_height_from_inches(
                temp_df["height"][0]
            )
            window["-PLAYER_SHOW_HEIGHT-"].update(
                value=self.show_height, disabled=False
            )
            self.convert_show_height()

            self.weight = temp_df["weight"][0]
            window["-PLAYER_WEIGHT-"].update(
                value=self.weight, disabled=False
            )

            self.player_first_name = temp_df["player_first_name"][0]
            window["-PLAYER_FIRST_NAME-"].update(
                value=self.player_first_name, disabled=False
            )

            self.player_last_name = temp_df["player_last_name"][0]
            window["-PLAYER_LAST_NAME-"].update(
                value=self.player_last_name, disabled=False
            )

            self.player_full_name = temp_df["player_full_name"][0]
            window["-PLAYER_FULL_NAME-"].update(
                value=self.player_full_name, disabled=False
            )

            self.player_football_name = temp_df["player_football_name"][0]
            window["-PLAYER_FB_NAME-"].update(
                value=self.player_football_name, disabled=False
            )

            self.status = temp_df["status"][0]
            window["-ROSTER_STATUS-"].update(
                value=self.status, disabled=False
            )

            self.years_exp = temp_df["years_exp"][0]
            window["-YEARS_EXP-"].update(
                value=self.years_exp, disabled=False
            )

            self.player_bday = temp_df["player_bday"][0]
            window["-PLAYER_BDAY_TEXT-"].update(value=self.player_bday)
            window["-PLAYER_BDAY_BUTTON-"].update(disabled=False)

            self.college = temp_df["college"][0]
            window["-PLAYER_COLLEGE-"].update(
                value=self.college, disabled=False
            )

            self.headshot_url = temp_df["headshot_url"][0]
            window["-PLAYER_HEADSHOT-"].update(
                value=self.headshot_url, disabled=False
            )

            self.gsis_id = temp_df["gsis_id"][0]
            window["-GSIS_PLAYER_ID-"].update(
                value=self.gsis_id, disabled=False
            )

            self.sportradar_id = temp_df["sportradar_id"][0]
            window["-SPORTRADAR_PLAYER_ID-"].update(
                value=self.sportradar_id, disabled=False
            )

            self.sr_player_id = temp_df["sr_player_id"][0]
            window["-SR_PLAYER_ID-"].update(
                value=self.sr_player_id, disabled=False
            )

            self.footballdb_player_id = temp_df["footballdb_player_id"][0]
            window["-FOOTBALLDB_PLAYER_ID-"].update(
                value=self.footballdb_player_id, disabled=False
            )

            self.stats_crew_player_id = temp_df["stats_crew_player_id"][0]
            window["-STATS_CREW_PLAYER_ID-"].update(
                value=self.stats_crew_player_id, disabled=False
            )

            self.pfr_id = temp_df["pfr_id"][0]
            window["-PFR_PLAYER_ID-"].update(
                value=self.pfr_id, disabled=False
            )

            self.espn_id = temp_df["espn_id"][0]
            window["-ESPN_PLAYER_ID-"].update(
                value=self.espn_id, disabled=False
            )

            self.arenafan_player_id = temp_df["arenafan_player_id"][0]
            window["-ARENAFAN_PLAYER_ID-"].update(
                value=self.arenafan_player_id, disabled=False
            )

            self.ncaa_player_id = temp_df["ncaa_player_id"][0]
            window["-NCAA_PLAYER_ID-"].update(
                value=self.ncaa_player_id, disabled=False
            )

            self.yahoo_id = temp_df["yahoo_id"][0]
            window["-YAHOO_PLAYER_ID-"].update(
                value=self.yahoo_id, disabled=False
            )

            self.rotowire_id = temp_df["rotowire_id"][0]
            window["-ROTOWIRE_PLAYER_ID-"].update(
                value=self.rotowire_id, disabled=False
            )

            self.pff_id = temp_df["pff_id"][0]
            window["-PFF_PLAYER_ID-"].update(
                value=self.pff_id, disabled=False
            )

            self.sleeper_id = temp_df["pff_id"][0]
            window["-SLEEPER_PLAYER_ID-"].update(
                value=self.sleeper_id, disabled=False
            )

            self.entry_year = temp_df["entry_year"][0]
            window["-ENTRY_YEAR-"].update(
                value=self.entry_year, disabled=False
            )

            self.rookie_year = temp_df["rookie_year"][0]
            window["-ROOKIE_YEAR-"].update(
                value=self.rookie_year, disabled=False
            )

            window["-DELETE_PLAYER-"].update(
                disabled=False
            )
            window["-SAVE_PLAYER-"].update(
                disabled=False
            )

        def clear_player():
            """ """
            self.player_id = 0
            window["-PLAYER_ID-"].update(value=self.player_id)

            self.jersey_number = 0
            window["-JERSEY_NUMBER-"].update(
                value=self.jersey_number, disabled=True
            )

            self.depth_chart_position = "QB"
            window["-PLAYER_POSITION-"].update(
                value=self.depth_chart_position, disabled=True
            )

            self.show_height = "6' 0\""
            window["-PLAYER_SHOW_HEIGHT-"].update(
                value=self.show_height, disabled=True
            )

            self.weight = 200
            window["-PLAYER_WEIGHT-"].update(
                value=self.weight, disabled=True
            )

            self.player_first_name = ""
            window["-PLAYER_FIRST_NAME-"].update(
                value=self.player_first_name, disabled=True
            )

            self.player_last_name = ""
            window["-PLAYER_LAST_NAME-"].update(
                value=self.player_last_name, disabled=True
            )

            self.player_full_name = ""
            window["-PLAYER_FULL_NAME-"].update(
                value=self.player_full_name, disabled=True
            )

            self.player_football_name = ""
            window["-PLAYER_FB_NAME-"].update(
                value=self.player_football_name, disabled=True
            )

            self.status = "ACT"
            window["-ROSTER_STATUS-"].update(
                value=self.status, disabled=True
            )

            self.years_exp = 0
            window["-YEARS_EXP-"].update(
                value=self.years_exp, disabled=True
            )

            self.player_bday = ""
            window["-PLAYER_BDAY_TEXT-"].update(value=self.player_bday)
            window["-PLAYER_BDAY_BUTTON-"].update(disabled=True)

            self.college = ""
            window["-PLAYER_COLLEGE-"].update(
                value=self.college, disabled=True
            )

            self.headshot_url = ""
            window["-PLAYER_HEADSHOT-"].update(
                value=self.headshot_url, disabled=True
            )

            self.gsis_id = ""
            window["-GSIS_PLAYER_ID-"].update(
                value=self.gsis_id, disabled=True
            )

            self.sportradar_id = ""
            window["-SPORTRADAR_PLAYER_ID-"].update(
                value=self.sportradar_id, disabled=True
            )

            self.sr_player_id = ""
            window["-SR_PLAYER_ID-"].update(
                value=self.sr_player_id, disabled=True
            )

            self.footballdb_player_id = ""
            window["-FOOTBALLDB_PLAYER_ID-"].update(
                value=self.footballdb_player_id, disabled=True
            )

            self.stats_crew_player_id = ""
            window["-STATS_CREW_PLAYER_ID-"].update(
                value=self.stats_crew_player_id, disabled=True
            )

            self.pfr_id = ""
            window["-PFR_PLAYER_ID-"].update(
                value=self.pfr_id, disabled=True
            )

            self.espn_id = ""
            window["-ESPN_PLAYER_ID-"].update(
                value=self.espn_id, disabled=True
            )

            self.arenafan_player_id = ""
            window["-ARENAFAN_PLAYER_ID-"].update(
                value=self.arenafan_player_id, disabled=True
            )

            self.ncaa_player_id = ""
            window["-NCAA_PLAYER_ID-"].update(
                value=self.ncaa_player_id, disabled=True
            )

            self.yahoo_id = ""
            window["-YAHOO_PLAYER_ID-"].update(
                value=self.yahoo_id, disabled=True
            )

            self.rotowire_id = ""
            window["-ROTOWIRE_PLAYER_ID-"].update(
                value=self.rotowire_id, disabled=True
            )

            self.pff_id = ""
            window["-PFF_PLAYER_ID-"].update(
                value=self.pff_id, disabled=True
            )

            self.sleeper_id = ""
            window["-SLEEPER_PLAYER_ID-"].update(
                value=self.sleeper_id, disabled=True
            )

            self.entry_year = ""
            window["-ENTRY_YEAR-"].update(
                value=self.entry_year, disabled=True
            )

            self.rookie_year = ""
            window["-ROOKIE_YEAR-"].update(
                value=self.rookie_year, disabled=True
            )

        def new_player_refresh():
            """ """
            self.player_id = 0
            window["-PLAYER_ID-"].update(value=self.player_id)

            self.jersey_number = 0
            window["-JERSEY_NUMBER-"].update(
                value=self.jersey_number, disabled=False
            )

            self.depth_chart_position = "QB"
            window["-PLAYER_POSITION-"].update(
                value=self.depth_chart_position, disabled=False
            )

            self.show_height = "6' 0\""
            self.convert_show_height()
            window["-PLAYER_SHOW_HEIGHT-"].update(
                value=self.show_height, disabled=False
            )

            self.weight = 200
            window["-PLAYER_WEIGHT-"].update(
                value=self.weight, disabled=False
            )

            self.player_first_name = ""
            window["-PLAYER_FIRST_NAME-"].update(
                value=self.player_first_name, disabled=False
            )

            self.player_last_name = ""
            window["-PLAYER_LAST_NAME-"].update(
                value=self.player_last_name, disabled=False
            )

            self.player_full_name = ""
            window["-PLAYER_FULL_NAME-"].update(
                value=self.player_full_name, disabled=False
            )

            self.player_football_name = ""
            window["-PLAYER_FB_NAME-"].update(
                value=self.player_football_name, disabled=False
            )

            self.status = "ACT"
            window["-ROSTER_STATUS-"].update(
                value=self.status, disabled=False
            )

            self.years_exp = 0
            window["-YEARS_EXP-"].update(
                value=self.years_exp, disabled=False
            )

            self.player_bday = ""
            window["-PLAYER_BDAY_TEXT-"].update(value=self.player_bday)
            window["-PLAYER_BDAY_BUTTON-"].update(disabled=False)

            self.college = ""
            window["-PLAYER_COLLEGE-"].update(
                value=self.college, disabled=False
            )

            self.headshot_url = ""
            window["-PLAYER_HEADSHOT-"].update(
                value=self.headshot_url, disabled=False
            )

            self.gsis_id = ""
            window["-GSIS_PLAYER_ID-"].update(
                value=self.gsis_id, disabled=False
            )

            self.sportradar_id = ""
            window["-SPORTRADAR_PLAYER_ID-"].update(
                value=self.sportradar_id, disabled=False
            )

            self.sr_player_id = ""
            window["-SR_PLAYER_ID-"].update(
                value=self.sr_player_id, disabled=False
            )

            self.footballdb_player_id = ""
            window["-FOOTBALLDB_PLAYER_ID-"].update(
                value=self.footballdb_player_id, disabled=False
            )

            self.stats_crew_player_id = ""
            window["-STATS_CREW_PLAYER_ID-"].update(
                value=self.stats_crew_player_id, disabled=False
            )

            self.pfr_id = ""
            window["-PFR_PLAYER_ID-"].update(
                value=self.pfr_id, disabled=False
            )

            self.espn_id = ""
            window["-ESPN_PLAYER_ID-"].update(
                value=self.espn_id, disabled=False
            )

            self.arenafan_player_id = ""
            window["-ARENAFAN_PLAYER_ID-"].update(
                value=self.arenafan_player_id, disabled=False
            )

            self.ncaa_player_id = ""
            window["-NCAA_PLAYER_ID-"].update(
                value=self.ncaa_player_id, disabled=False
            )

            self.yahoo_id = ""
            window["-YAHOO_PLAYER_ID-"].update(
                value=self.yahoo_id, disabled=False
            )

            self.rotowire_id = ""
            window["-ROTOWIRE_PLAYER_ID-"].update(
                value=self.rotowire_id, disabled=False
            )

            self.pff_id = ""
            window["-PFF_PLAYER_ID-"].update(
                value=self.pff_id, disabled=False
            )

            self.sleeper_id = ""
            window["-SLEEPER_PLAYER_ID-"].update(
                value=self.sleeper_id, disabled=False
            )

            self.entry_year = self.season
            window["-ENTRY_YEAR-"].update(
                value=self.entry_year, disabled=False
            )

            self.rookie_year = self.season
            window["-ROOKIE_YEAR-"].update(
                value=self.rookie_year, disabled=False
            )

            window["-DELETE_PLAYER-"].update(disabled=True)
            window["-SAVE_PLAYER-"].update(disabled=False)

        sg.theme(self.app_theme)

        player_info = [
            [
                sg.Text("Player ID:\t"),
                sg.Text(
                    text=self.player_id,
                    background_color="black",
                    text_color="white",
                    # disabled=True,
                    enable_events=True,
                    size=(10, 1),
                    key="-PLAYER_ID-"
                )
            ],
            [
                sg.Text("Jersey Number:\t"),
                sg.Combo(
                    default_value=self.jersey_number,
                    values=self.player_jersey_numbers_arr,
                    disabled=True,
                    readonly=True,
                    size=(8, 1),
                    enable_events=True,
                    key="-JERSEY_NUMBER-"
                ),
                sg.Push(),
                sg.Text("Position:\t\t"),
                sg.Combo(
                    default_value=self.depth_chart_position,
                    values=self.player_positions,
                    enable_events=True,
                    disabled=True,
                    readonly=True,
                    size=(8, 1),
                    key="-PLAYER_POSITION-"
                )

            ],
            [
                sg.Text("Height:\t\t"),
                sg.Combo(
                    default_value=self.show_height,
                    values=self.show_height_arr,
                    enable_events=True,
                    disabled=True,
                    readonly=True,
                    size=(8, 1),
                    key="-PLAYER_SHOW_HEIGHT-"
                ),
                sg.Push(),
                sg.Text("Weight:\t\t"),
                sg.Input(
                    default_text=self.weight,
                    enable_events=True,
                    disabled=True,
                    size=(10, 1),
                    key="-PLAYER_WEIGHT-"
                )
            ],
            [
                sg.Text(
                    "First Name:\t"
                ),
                sg.Input(
                    default_text=self.player_first_name,
                    enable_events=True,
                    disabled=True,
                    size=(50, 1),
                    key="-PLAYER_FIRST_NAME-"
                )
            ],
            [
                sg.Text(
                    "Football Name:\t"
                ),
                sg.Input(
                    default_text=self.player_football_name,
                    enable_events=True,
                    disabled=True,
                    size=(50, 1),
                    key="-PLAYER_FB_NAME-"
                )
            ],
            [
                sg.Text(
                    "Last Name:\t"
                ),
                sg.Input(
                    default_text=self.player_last_name,
                    enable_events=True,
                    disabled=True,
                    size=(50, 1),
                    key="-PLAYER_LAST_NAME-"
                )
            ],
            [
                sg.Text("Full Name:\t"),
                sg.Input(
                    default_text=self.player_full_name,
                    enable_events=True,
                    disabled=True,
                    size=(50, 1),
                    key="-PLAYER_FULL_NAME-"
                )
            ],
            [
                sg.Text("Roster Status:\t"),
                sg.Combo(
                    default_value=self.status,
                    values=self.roster_status,
                    enable_events=True,
                    disabled=True,
                    readonly=True,
                    size=(8, 1),
                    key="-ROSTER_STATUS-"
                ),
                sg.Push(),
                sg.Text("Experience:\t"),
                sg.Input(
                    default_text=self.years_exp,
                    enable_events=True,
                    disabled=True,
                    size=(10, 1),
                    key="-YEARS_EXP-"
                )
            ],
            [
                sg.Text(
                    "Birthday:\t\t"
                ),
                # Yes, this is a hack.
                # No, I do not like this hack.
                sg.In(
                    key="-PLAYER_BDAY-",
                    enable_events=True,
                    visible=False
                ),
                # Seriously, why can't a successful press and use
                # of a calendar button not register an event?
                sg.CalendarButton(
                    "Select Date",
                    # close_when_date_chosen=True,
                    enable_events=True,
                    disabled=True,
                    no_titlebar=False,
                    default_date_m_d_y=(1, 1, 1999),
                    target="-PLAYER_BDAY-",
                    format="%Y-%m-%d",
                    key="-PLAYER_BDAY_BUTTON-"
                ),
                sg.Text(
                    text=self.player_bday,
                    size=(20, 1),
                    enable_events=True,
                    key="-PLAYER_BDAY_TEXT-"
                ),
            ],
            [
                sg.Text("College:\t\t"),
                sg.Input(
                    default_text=self.college,
                    enable_events=True,
                    disabled=True,
                    size=(50, 1),
                    key="-PLAYER_COLLEGE-"
                )
            ],
            [
                sg.Text("Player Photo URL:\t"),
                sg.Input(
                    default_text=self.headshot_url,
                    enable_events=True,
                    disabled=True,
                    size=(50, 1),
                    key="-PLAYER_HEADSHOT-"
                )
            ],
            [
                sg.Text("Rookie Year:\t"),
                sg.Input(
                    default_text=self.college,
                    enable_events=True,
                    disabled=True,
                    size=(10, 1),
                    key="-ROOKIE_YEAR-"
                ),
                sg.Push(),
                sg.Text("Entry Year:\t"),
                sg.Input(
                    default_text=self.college,
                    enable_events=True,
                    disabled=True,
                    size=(10, 1),
                    key="-ENTRY_YEAR-"
                ),
            ]
        ]

        player_ids = [
            [
                sg.Text(
                    "NFL GSIS Player ID:\t"
                ),
                sg.Input(
                    default_text=self.gsis_id,
                    size=(40, 1),
                    disabled=True,
                    enable_events=True,
                    key="-GSIS_PLAYER_ID-"
                )
            ],
            [
                sg.Text(
                    "Sportradar Player ID:\t"
                ),
                sg.Input(
                    default_text=self.sportradar_id,
                    size=(40, 1),
                    disabled=True,
                    enable_events=True,
                    key="-SPORTRADAR_PLAYER_ID-"
                )
            ],
            [
                sg.Text(
                    "Sports Reference Player ID:\t"
                ),
                sg.Input(
                    default_text=self.sr_player_id,
                    size=(40, 1),
                    disabled=True,
                    enable_events=True,
                    key="-SR_PLAYER_ID-"
                )
            ],
            [
                sg.Text(
                    "footballdb.com Player ID:\t"
                ),
                sg.Input(
                    default_text=self.footballdb_player_id,
                    size=(40, 1),
                    disabled=True,
                    enable_events=True,
                    key="-FOOTBALLDB_PLAYER_ID-"
                )
            ],
            [
                sg.Text(
                    "Stats Crew Player ID:\t"
                ),
                sg.Input(
                    default_text=self.stats_crew_player_id,
                    size=(40, 1),
                    disabled=True,
                    enable_events=True,
                    key="-STATS_CREW_PLAYER_ID-"
                )
            ],
            [
                sg.Text(
                    "ArenaFan Player ID:\t"
                ),
                sg.Input(
                    default_text=self.yahoo_id,
                    size=(40, 1),
                    disabled=True,
                    enable_events=True,
                    key="-ARENAFAN_PLAYER_ID-"
                )
            ],
            [
                sg.Text(
                    "Pro Football Reference ID:\t"
                ),
                sg.Input(
                    default_text=self.pfr_id,
                    size=(15, 1),
                    disabled=True,
                    enable_events=True,
                    key="-PFR_PLAYER_ID-"
                )
            ],
            [
                sg.Text(
                    "ESPN Player ID:\t\t"
                ),
                sg.Input(
                    default_text=self.espn_id,
                    size=(15, 1),
                    disabled=True,
                    enable_events=True,
                    key="-ESPN_PLAYER_ID-"
                )
            ],
            [
                sg.Text(
                    "Yahoo Player ID:\t\t"
                ),
                sg.Input(
                    default_text=self.yahoo_id,
                    size=(15, 1),
                    disabled=True,
                    enable_events=True,
                    key="-YAHOO_PLAYER_ID-"
                )
            ],
            [
                sg.Text(
                    "stats.ncaa.org Player ID:\t"
                ),
                sg.Input(
                    default_text=self.yahoo_id,
                    size=(15, 1),
                    disabled=True,
                    enable_events=True,
                    key="-NCAA_PLAYER_ID-"
                )
            ],
            [
                sg.Text(
                    "Rotowire Player ID:\t\t"
                ),
                sg.Input(
                    default_text=self.rotowire_id,
                    size=(15, 1),
                    disabled=True,
                    enable_events=True,
                    key="-ROTOWIRE_PLAYER_ID-"
                )
            ],
            [
                sg.Text(
                    "PFF Player ID:\t\t"
                ),
                sg.Input(
                    default_text=self.pff_id,
                    size=(15, 1),
                    disabled=True,
                    enable_events=True,
                    key="-PFF_PLAYER_ID-"
                )
            ],
            [
                sg.Text(
                    "sleeper.com Player ID:\t"
                ),
                sg.Input(
                    default_text=self.sleeper_id,
                    size=(15, 1),
                    disabled=True,
                    enable_events=True,
                    key="-SLEEPER_PLAYER_ID-"
                )
            ]
        ]

        player_layout = [
            [
                sg.Text("Team:\t"),
                sg.Combo(
                    default_value=self.team_ids_arr[0],
                    values=self.team_ids_arr,
                    enable_events=True,
                    # disabled=True,
                    key="-TEAM_ID-",
                    size=(10, 1),
                ),
            ],
            [
                sg.TabGroup(
                    [[
                        sg.Tab("Player", player_info),
                        sg.Tab("Player IDs", player_ids)
                    ]],
                    # expand_x=True,
                    expand_y=True
                )
            ],
            [
                # sg.Push(),
                sg.Button(
                    "New Player",
                    enable_events=True,
                    expand_x=True,
                    key="-NEW_PLAYER-"
                ),
                sg.Button(
                    "Delete Player",
                    enable_events=True,
                    expand_x=True,
                    disabled=True,
                    key="-DELETE_PLAYER-"
                ),
                sg.Button(
                    "Save Player",
                    enable_events=True,
                    expand_x=True,
                    disabled=True,
                    key="-SAVE_PLAYER-"
                )
            ]
        ]

        layout = [
            [
                sg.Text(
                    "Edit Rosters",
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
                sg.Frame(
                    title="Edit Player...",
                    layout=player_layout,
                    size=400,
                    # pad=0,
                    element_justification="top",
                    expand_x=True,
                    expand_y=True
                ),
                sg.Table(
                    values=self.show_roster_df.rows(),
                    headings=[
                        "Team",
                        "Player ID",
                        "Jersey",
                        "Position",
                        "Full Name",
                        "First Name",
                        "Last Name",
                    ],
                    expand_x=True,
                    expand_y=True,
                    enable_events=True,
                    justification="center",
                    key="-ROSTER_TABLE-",
                ),
            ],
        ]

        window = sg.Window(
            "Edit Rosters...",
            layout=layout,
            size=(1280, 800),
            resizable=True,
            finalize=True,
            keep_on_top=False,
        )

        keep_open = True
        while keep_open is True:
            event, values = window.read(timeout=1000)
            print(values)
            print(event)
            # print(self.player_bday)

            if event in (sg.WIN_CLOSED, "Exit"):
                keep_open = False

            # Player Weight
            if event == "-PLAYER_WEIGHT-" \
                    and len(values["-PLAYER_WEIGHT-"]) > 3:
                window["-PLAYER_WEIGHT-"].update(
                    values["-PLAYER_WEIGHT-"][:-1]
                )
            elif event == "-PLAYER_WEIGHT-" and (
                values["-PLAYER_WEIGHT-"] and
                values["-PLAYER_WEIGHT-"][-1] not in (
                    self.numbers_all
                )
            ):
                window["-PLAYER_WEIGHT-"].update(
                    values["-PLAYER_WEIGHT-"][:-1]
                )
                self.weight = values["-PLAYER_WEIGHT-"]
            elif event == "-PLAYER_WEIGHT-" and (
                values["-PLAYER_WEIGHT-"] and
                values["-PLAYER_WEIGHT-"][-1] in (
                    self.numbers_all
                )
            ):
                window["-PLAYER_WEIGHT-"].update(
                    values["-PLAYER_WEIGHT-"]
                )
                self.weight = values["-PLAYER_WEIGHT-"]

            # Player experience
            if event == "-YEARS_EXP-" and len(values["-YEARS_EXP-"]) > 2:
                window["-YEARS_EXP-"].update(
                    values["-YEARS_EXP-"][:-1]
                )
            elif event == "-YEARS_EXP-" and (
                values["-YEARS_EXP-"] and
                values["-YEARS_EXP-"][-1] not in (
                    self.numbers_all
                )
            ):
                window["-YEARS_EXP-"].update(
                    values["-YEARS_EXP-"][:-1]
                )
                self.years_exp = values["-YEARS_EXP-"]
            elif event == "-YEARS_EXP-" and (
                values["-YEARS_EXP-"] and
                values["-YEARS_EXP-"][-1] in (
                    self.numbers_all
                )
            ):
                window["-YEARS_EXP-"].update(
                    values["-YEARS_EXP-"]
                )
                self.years_exp = values["-YEARS_EXP-"]

            # NFL GSIS Player ID
            if event == "-GSIS_PLAYER_ID-" \
                    and len(values["-GSIS_PLAYER_ID-"]) > 10:
                window["-GSIS_PLAYER_ID-"].update(
                    values["-GSIS_PLAYER_ID-"][:-1]
                )
            elif event == "-GSIS_PLAYER_ID-" and (
                values["-GSIS_PLAYER_ID-"] and
                values["-GSIS_PLAYER_ID-"][-1] not in (
                    self.numbers_with_dashes
                )
            ):
                window["-GSIS_PLAYER_ID-"].update(
                    values["-GSIS_PLAYER_ID-"][:-1]
                )
                self.gsis_id = values["-GSIS_PLAYER_ID-"]
            elif event == "-GSIS_PLAYER_ID-" and (
                values["-GSIS_PLAYER_ID-"] and
                values["-GSIS_PLAYER_ID-"][-1] in (
                    self.numbers_with_dashes
                )
            ):
                window["-GSIS_PLAYER_ID-"].update(
                    values["-GSIS_PLAYER_ID-"]
                )
                self.gsis_id = values["-GSIS_PLAYER_ID-"]

            # Sportradar Player ID
            if event == "-SPORTRADAR_PLAYER_ID-" \
                    and len(values["-SPORTRADAR_PLAYER_ID-"]) > 36:
                window["-SPORTRADAR_PLAYER_ID-"].update(
                    values["-SPORTRADAR_PLAYER_ID-"][:-1]
                )
            elif event == "-SPORTRADAR_PLAYER_ID-" and (
                values["-SPORTRADAR_PLAYER_ID-"] and
                values["-SPORTRADAR_PLAYER_ID-"][-1] not in (
                    self.letters_and_numbers
                )
            ):
                window["-SPORTRADAR_PLAYER_ID-"].update(
                    values["-SPORTRADAR_PLAYER_ID-"][:-1]
                )
                self.sportradar_id = values["-SPORTRADAR_PLAYER_ID-"]
            elif event == "-SPORTRADAR_PLAYER_ID-" and (
                values["-SPORTRADAR_PLAYER_ID-"] and
                values["-SPORTRADAR_PLAYER_ID-"][-1] in (
                    self.letters_and_numbers
                )
            ):
                window["-SPORTRADAR_PLAYER_ID-"].update(
                    values["-SPORTRADAR_PLAYER_ID-"]
                )
                self.sportradar_id = values["-SPORTRADAR_PLAYER_ID-"]

            # Sports Reference Player ID
            if event == "-SR_PLAYER_ID-" \
                    and len(values["-SR_PLAYER_ID-"]) > 8:
                window["-SR_PLAYER_ID-"].update(
                    values["-SR_PLAYER_ID-"][:-1]
                )
            elif event == "-SR_PLAYER_ID-" and (
                values["-SR_PLAYER_ID-"] and
                values["-SR_PLAYER_ID-"][-1] not in (
                    self.letters_and_numbers
                )
            ):
                window["-SR_PLAYER_ID-"].update(
                    values["-SR_PLAYER_ID-"][:-1]
                )
                self.sr_player_id = values["-SR_PLAYER_ID-"]
            elif event == "-SR_PLAYER_ID-" and (
                values["-SR_PLAYER_ID-"] and
                values["-SR_PLAYER_ID-"][-1] in (
                    self.letters_and_numbers
                )
            ):
                window["-SR_PLAYER_ID-"].update(
                    values["-SR_PLAYER_ID-"]
                )
                self.sr_player_id = values["-SR_PLAYER_ID-"]

            # footballdb.com Player ID

            # This ID system is weird.
            # Let's handle this when someone saves a Player ID
            # for this ID system.
            # if event == "-FOOTBALLDB_PLAYER_ID-" \
            #         and len(values["-FOOTBALLDB_PLAYER_ID-"]) > 8:
            #     window["-FOOTBALLDB_PLAYER_ID-"].update(
            #         values["-FOOTBALLDB_PLAYER_ID-"][:-1]
            #     )
            # elif event == "-FOOTBALLDB_PLAYER_ID-" and (
            if event == "-FOOTBALLDB_PLAYER_ID-" and (
                values["-FOOTBALLDB_PLAYER_ID-"] and
                values["-FOOTBALLDB_PLAYER_ID-"][-1] not in (
                    self.letters_and_numbers
                )
            ):
                window["-FOOTBALLDB_PLAYER_ID-"].update(
                    values["-FOOTBALLDB_PLAYER_ID-"][:-1]
                )
                self.footballdb_player_id = values["-FOOTBALLDB_PLAYER_ID-"]
            elif event == "-FOOTBALLDB_PLAYER_ID-" and (
                values["-FOOTBALLDB_PLAYER_ID-"] and
                values["-FOOTBALLDB_PLAYER_ID-"][-1] in (
                    self.letters_and_numbers
                )
            ):
                window["-FOOTBALLDB_PLAYER_ID-"].update(
                    values["-FOOTBALLDB_PLAYER_ID-"]
                )
                self.footballdb_player_id = values["-FOOTBALLDB_PLAYER_ID-"]

            # Stats Crew Player ID
            if event == "-STATS_CREW_PLAYER_ID-" \
                    and len(values["-STATS_CREW_PLAYER_ID-"]) > 13:
                # NOTE: We can chop off the "p-" part of the Player ID
                # at the insert.

                # For now, make sure that a valid PID
                # is put in for this ID system.
                window["-STATS_CREW_PLAYER_ID-"].update(
                    values["-STATS_CREW_PLAYER_ID-"][:-1]
                )
            elif event == "-STATS_CREW_PLAYER_ID-" and (
                values["-STATS_CREW_PLAYER_ID-"] and
                values["-STATS_CREW_PLAYER_ID-"][-1] not in (
                    self.letters_and_numbers
                )
            ):
                window["-STATS_CREW_PLAYER_ID-"].update(
                    values["-STATS_CREW_PLAYER_ID-"][:-1]
                )
                self.stats_crew_player_id = values["-STATS_CREW_PLAYER_ID-"]
            elif event == "-STATS_CREW_PLAYER_ID-" and (
                values["-STATS_CREW_PLAYER_ID-"] and
                values["-STATS_CREW_PLAYER_ID-"][-1] in (
                    self.letters_and_numbers
                )
            ):
                window["-STATS_CREW_PLAYER_ID-"].update(
                    values["-STATS_CREW_PLAYER_ID-"]
                )
                self.stats_crew_player_id = values["-STATS_CREW_PLAYER_ID-"]

            # ArenaFan Player ID
            if event == "-ARENAFAN_PLAYER_ID-" and (
                values["-ARENAFAN_PLAYER_ID-"] and
                values["-ARENAFAN_PLAYER_ID-"][-1] not in (
                    self.letters_and_numbers
                )
            ):
                window["-ARENAFAN_PLAYER_ID-"].update(
                    values["-ARENAFAN_PLAYER_ID-"][:-1]
                )
                self.arenafan_player_id = values["-ARENAFAN_PLAYER_ID-"]
            elif event == "-ARENAFAN_PLAYER_ID-" and (
                values["-ARENAFAN_PLAYER_ID-"] and
                values["-ARENAFAN_PLAYER_ID-"][-1] in (
                    self.letters_and_numbers
                )
            ):
                window["-ARENAFAN_PLAYER_ID-"].update(
                    values["-ARENAFAN_PLAYER_ID-"]
                )
                self.arenafan_player_id = values["-ARENAFAN_PLAYER_ID-"]

            # Pro Football Reference Player ID
            if event == "-PFR_PLAYER_ID-" \
                    and len(values["-PFR_PLAYER_ID-"]) > 8:
                window["-PFR_PLAYER_ID-"].update(
                    values["-PFR_PLAYER_ID-"][:-1]
                )
            elif event == "-PFR_PLAYER_ID-" and (
                values["-PFR_PLAYER_ID-"] and
                values["-PFR_PLAYER_ID-"][-1] not in (
                    self.letters_and_numbers
                )
            ):
                window["-PFR_PLAYER_ID-"].update(
                    values["-PFR_PLAYER_ID-"][:-1]
                )
                self.pfr_id = values["-PFR_PLAYER_ID-"]
            elif event == "-PFR_PLAYER_ID-" and (
                values["-PFR_PLAYER_ID-"] and
                values["-PFR_PLAYER_ID-"][-1] in (
                    self.letters_and_numbers
                )
            ):
                window["-PFR_PLAYER_ID-"].update(
                    values["-PFR_PLAYER_ID-"]
                )
                self.pfr_id = values["-PFR_PLAYER_ID-"]

            # ESPN Player ID
            if event == "-ESPN_PLAYER_ID-" \
                    and len(values["-ESPN_PLAYER_ID-"]) > 7:
                window["-ESPN_PLAYER_ID-"].update(
                    values["-ESPN_PLAYER_ID-"][:-1]
                )
            elif event == "-ESPN_PLAYER_ID-" and (
                values["-ESPN_PLAYER_ID-"] and
                values["-ESPN_PLAYER_ID-"][-1] not in (
                    self.numbers_all
                )
            ):
                window["-ESPN_PLAYER_ID-"].update(
                    values["-ESPN_PLAYER_ID-"][:-1]
                )
                self.espn_id = values["-ESPN_PLAYER_ID-"]
            elif event == "-ESPN_PLAYER_ID-" and (
                values["-ESPN_PLAYER_ID-"] and
                values["-ESPN_PLAYER_ID-"][-1] in (
                    self.numbers_all
                )
            ):
                window["-ESPN_PLAYER_ID-"].update(
                    values["-ESPN_PLAYER_ID-"]
                )
                self.espn_id = values["-ESPN_PLAYER_ID-"]

            # stats.ncaa.org Player ID
            if event == "-NCAA_PLAYER_ID-" \
                    and len(values["-NCAA_PLAYER_ID-"]) > 7:
                window["-NCAA_PLAYER_ID-"].update(
                    values["-NCAA_PLAYER_ID-"][:-1]
                )
            elif event == "-NCAA_PLAYER_ID-" and (
                values["-NCAA_PLAYER_ID-"] and
                values["-NCAA_PLAYER_ID-"][-1] not in (
                    self.numbers_all
                )
            ):
                window["-NCAA_PLAYER_ID-"].update(
                    values["-NCAA_PLAYER_ID-"][:-1]
                )
                self.ncaa_player_id = values["-NCAA_PLAYER_ID-"]
            elif event == "-NCAA_PLAYER_ID-" and (
                values["-NCAA_PLAYER_ID-"] and
                values["-NCAA_PLAYER_ID-"][-1] in (
                    self.numbers_all
                )
            ):
                window["-NCAA_PLAYER_ID-"].update(
                    values["-NCAA_PLAYER_ID-"]
                )
                self.ncaa_player_id = values["-NCAA_PLAYER_ID-"]


            # Yahoo Player ID
            if event == "-YAHOO_PLAYER_ID-" \
                    and len(values["-YAHOO_PLAYER_ID-"]) > 5:
                window["-YAHOO_PLAYER_ID-"].update(
                    values["-YAHOO_PLAYER_ID-"][:-1]
                )
            elif event == "-YAHOO_PLAYER_ID-" and (
                values["-YAHOO_PLAYER_ID-"] and
                values["-YAHOO_PLAYER_ID-"][-1] not in (
                    self.numbers_all
                )
            ):
                window["-YAHOO_PLAYER_ID-"].update(
                    values["-YAHOO_PLAYER_ID-"][:-1]
                )
                self.yahoo_id = values["-YAHOO_PLAYER_ID-"]
            elif event == "-YAHOO_PLAYER_ID-" and (
                values["-YAHOO_PLAYER_ID-"] and
                values["-YAHOO_PLAYER_ID-"][-1] in (
                    self.numbers_all
                )
            ):
                window["-YAHOO_PLAYER_ID-"].update(
                    values["-YAHOO_PLAYER_ID-"]
                )
                self.yahoo_id = values["-YAHOO_PLAYER_ID-"]

            # Rotowire ID
            if event == "-ROTOWIRE_PLAYER_ID-" \
                    and len(values["-ROTOWIRE_PLAYER_ID-"]) > 5:
                window["-ROTOWIRE_PLAYER_ID-"].update(
                    values["-ROTOWIRE_PLAYER_ID-"][:-1]
                )
            elif event == "-ROTOWIRE_PLAYER_ID-" and (
                values["-ROTOWIRE_PLAYER_ID-"] and
                values["-ROTOWIRE_PLAYER_ID-"][-1] not in (
                    self.numbers_all
                )
            ):
                window["-ROTOWIRE_PLAYER_ID-"].update(
                    values["-ROTOWIRE_PLAYER_ID-"][:-1]
                )
                self.rotowire_id = values["-ROTOWIRE_PLAYER_ID-"]
            elif event == "-ROTOWIRE_PLAYER_ID-" and (
                values["-ROTOWIRE_PLAYER_ID-"] and
                values["-ROTOWIRE_PLAYER_ID-"][-1] in (
                    self.numbers_all
                )
            ):
                window["-ROTOWIRE_PLAYER_ID-"].update(
                    values["-ROTOWIRE_PLAYER_ID-"]
                )
                self.rotowire_id = values["-ROTOWIRE_PLAYER_ID-"]

            # PFF Player ID
            if event == "-PFF_PLAYER_ID-" \
                    and len(values["-PFF_PLAYER_ID-"]) > 6:
                window["-PFF_PLAYER_ID-"].update(
                    values["-PFF_PLAYER_ID-"][:-1]
                )
            elif event == "-PFF_PLAYER_ID-" and (
                values["-PFF_PLAYER_ID-"] and
                values["-PFF_PLAYER_ID-"][-1] not in (
                    self.numbers_all
                )
            ):
                window["-PFF_PLAYER_ID-"].update(
                    values["-PFF_PLAYER_ID-"][:-1]
                )
                self.pff_id = values["-PFF_PLAYER_ID-"]
            elif event == "-PFF_PLAYER_ID-" and (
                values["-PFF_PLAYER_ID-"] and
                values["-PFF_PLAYER_ID-"][-1] in (
                    self.numbers_all
                )
            ):
                window["-PFF_PLAYER_ID-"].update(
                    values["-PFF_PLAYER_ID-"]
                )
                self.pff_id = values["-PFF_PLAYER_ID-"]

            # sleeper.com Player ID
            if event == "-SLEEPER_PLAYER_ID-" \
                    and len(values["-SLEEPER_PLAYER_ID-"]) > 6:
                window["-SLEEPER_PLAYER_ID-"].update(
                    values["-SLEEPER_PLAYER_ID-"][:-1]
                )
            elif event == "-SLEEPER_PLAYER_ID-" and (
                values["-SLEEPER_PLAYER_ID-"] and
                values["-SLEEPER_PLAYER_ID-"][-1] not in (
                    self.numbers_all
                )
            ):
                window["-SLEEPER_PLAYER_ID-"].update(
                    values["-SLEEPER_PLAYER_ID-"][:-1]
                )
                self.sleeper_id = values["-SLEEPER_PLAYER_ID-"]
            elif event == "-SLEEPER_PLAYER_ID-" and (
                values["-SLEEPER_PLAYER_ID-"] and
                values["-SLEEPER_PLAYER_ID-"][-1] in (
                    self.numbers_all
                )
            ):
                window["-SLEEPER_PLAYER_ID-"].update(
                    values["-SLEEPER_PLAYER_ID-"]
                )
                self.sleeper_id = values["-SLEEPER_PLAYER_ID-"]

            match event:
                case "-TEAM_ID-":
                    # This will switch from one team's roster
                    # to another.
                    clear_player()
                    self.refresh_show_roster(values["-TEAM_ID-"])
                    window["-ROSTER_TABLE-"].update(
                        values=self.show_roster_df.rows()
                    )
                case "-NEW_PLAYER-":
                    new_player_refresh()
                case "-DELETE_PLAYER-":
                    check = self.delete_player(self.player_id)
                    if check is True:
                        clear_player()
                    del check
                    self.refresh_show_roster(self.team_id)
                    window["-ROSTER_TABLE-"].update(
                        values=self.show_roster_df.rows()
                    )
                case "-SAVE_PLAYER-":
                    check = self.validate_player_input()
                    if check is True:
                        self.save_player()
                    print()
                case "-ROSTER_TABLE-":
                    try:
                        select_player(values["-ROSTER_TABLE-"][0])
                    except IndexError as e:
                        """
                        # For some reason,
                        # when switching teams, while a player is selected,
                        # that triggers a "-ROSTER_TABLE-" event,
                        # exactly when the "-ROSTER_TABLE-" is empty.
                        # The above code fires off,
                        # and would crash when run in this situation
                        # (because there's nothing in "-ROSTER_TABLE-").
                        # This is of course,
                        # not a good thing with the above code,
                        # so we're catching an `IndexError` here,
                        # and largely ignoring it.

                        # Plus, it shouldn't be possible for the user
                        # to select something in a table with zero rows.
                        """
                        logging.info(
                            "Could not locate index location `0` " +
                            "in `-ROSTER_TABLE-`. " +
                            "Skipping over this section. " +
                            f"Full exception `{e}`."
                        )
                    except Exception as e:
                        raise e
                case "-JERSEY_NUMBER-":
                    self.jersey_number = values["-JERSEY_NUMBER-"]
                case "-PLAYER_POSITION-":
                    self.jersey_number = values["-PLAYER_POSITION-"]
                case "-PLAYER_SHOW_HEIGHT-":
                    self.show_height = values["-PLAYER_SHOW_HEIGHT-"]
                    self.convert_show_height()
                case "-PLAYER_FIRST_NAME-":
                    self.player_first_name = values["-PLAYER_FIRST_NAME-"]
                case "-PLAYER_LAST_NAME-":
                    self.player_last_name = values["-PLAYER_LAST_NAME-"]
                case "-PLAYER_FB_NAME-":
                    self.player_football_name = values["-PLAYER_FB_NAME-"]
                case "-PLAYER_FULL_NAME-":
                    self.player_football_name = values["-PLAYER_FULL_NAME-"]
                case "-ROSTER_STATUS-":
                    self.status = values["-ROSTER_STATUS-"]
                    print()
                case "-PLAYER_BDAY-":
                    self.player_bday = values["-PLAYER_BDAY-"]
                case "-PLAYER_COLLEGE-":
                    self.college = values["-PLAYER_COLLEGE-"]
                case "-PLAYER_HEADSHOT-":
                    self.headshot_url = values["-PLAYER_HEADSHOT-"]
                case _:
                    pass
