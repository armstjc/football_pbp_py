"""
- Creation Date: 03/10/2024 4:35 PM EDT
- Last Updated: 05/31/2024 01:15 PM EDT
- Authors: Joseph Armstrong (armstrongjoseph08@gmail.com)
- file: `./core/views/new_game_view.py`
- Purpose: Code behind for the window that allows a user
    to view and edit a teams.
"""

import FreeSimpleGUI as sg
import polars as pl

from core.database.load_db_elements import SqliteLoadData
from core.database.sqlite3_connectors import initialize_sqlite3_connectors
from core.other.embedded import EmbeddedElements, LettersAndNumbers


class TeamView():
    """
    Class for handling logic with editing team information.
    """
    # new_team_creation = False

    letters_all = LettersAndNumbers.letters_all()
    letters_and_numbers = LettersAndNumbers.letters_and_numbers()
    numbers_all = LettersAndNumbers.numbers_all()
    letters_and_numbers_spec = LettersAndNumbers.letters_and_numbers(
        include_dash_and_underscore=True
    )
    # sqlite3 connectors
    sqlite3_con, sqlite3_cur = initialize_sqlite3_connectors()

    settings_dict = {}

    team_df = pl.DataFrame()

    iso_nations_df = pl.DataFrame()
    iso_states_df = pl.DataFrame()
    filtered_iso_states_df = pl.DataFrame()
    iso_timezones_df = pl.DataFrame()

    iso_2_arr = []
    iso_states_arr = []

    # The text shown to a user to represent a specific state/nation.
    show_nations_arr = []
    show_states_arr = []
    show_timezones_arr = []
    show_nation = ""
    show_state = ""

    season = 0
    league_id = ""
    team_id = ""

    # External Team ID systems
    pfr_team_id = ""
    pfr_fran_id = ""
    sr_team_id = ""
    # ncaa_old_team_id = ""
    ncaa_team_id = ""
    stats_crew_team_id = ""
    footballdb_team_id = ""
    espn_team_id = ""
    arenafan_team_id = ""

    # Team Info
    team_abv = ""
    team_name = ""
    team_location = ""
    team_nickname = ""
    team_city = ""
    team_state = ""
    team_nation = ""
    team_conference = ""
    team_division = ""
    team_head_coach = ""
    team_oc = ""
    team_dc = ""
    team_timezone = ""
    team_notes = ""
    stadium_id = 0

    def __init__(
        self,
        settings_json: dict,
        league_id: str,
        season: int,
        team_id: str
    ) -> None:
        """ """

        self.settings_dict = settings_json
        self.app_theme = self.settings_dict["app_theme"]

        self.league_id = league_id
        self.season = season
        self.team_id = team_id

        self.initial_data_load()
        self.team_edit_view()

    def update_team_settings(self) -> None:
        """ """
        sql_script = """
        UPDATE fb_teams
        SET
            "team_abv" = ?,
            "team_name" = ?,
            "team_location" = ?,
            "team_nickname" = ?,
            "team_city" = ?,
            "team_state" = ?,
            "team_nation" = ?,
            "team_conference" = ?,
            "team_division" = ?,
            "team_head_coach" = ?,
            "team_oc" = ?,
            "team_dc" = ?,
            "timezone_name" = ?,
            "team_notes" = ?,
            "pfr_team_id" = ?,
            "pfr_fran_id" = ?,
            "sr_team_id" = ?,
            "ncaa_team_id" = ?,
            "stats_crew_team_id" = ?,
            "footballdb_team_id" = ?,
            "espn_team_id" = ?,
            "arenafan_team_id" = ?

        WHERE
            "league_id" = ? AND
            "team_id" = ? AND
            "season" = ?

        """

        self.sqlite3_cur.executemany(
            sql_script,
            [(
                self.team_abv,
                self.team_name,
                self.team_location,
                self.team_nickname,
                self.team_city,
                self.team_state,
                self.team_nation,
                self.team_conference,
                self.team_division,
                self.team_head_coach,
                self.team_oc,
                self.team_dc,
                self.team_timezone,
                self.team_notes,
                self.pfr_team_id,
                self.pfr_fran_id,
                self.sr_team_id,
                self.ncaa_team_id,
                self.stats_crew_team_id,
                self.footballdb_team_id,
                self.espn_team_id,
                self.arenafan_team_id,
                self.league_id,
                self.team_id,
                self.season

            )]
        )
        self.sqlite3_con.commit()

    def initial_data_load(self) -> None:
        """ """

        self.team_df = SqliteLoadData.load_fb_teams(
            con=self.sqlite3_con, cur=self.sqlite3_cur
        )
        self.team_df = self.team_df.filter(
            (pl.col("league_id") == self.league_id) &
            (pl.col("season") == self.season) &
            (pl.col("team_id") == self.team_id)
        )

        self.pfr_team_id = self.team_df["pfr_team_id"][0]
        self.sr_team_id = self.team_df["sr_team_id"][0]
        # self.ncaa_old_team_id = self.team_df["ncaa_old_team_id"][0]
        self.ncaa_team_id = self.team_df["ncaa_team_id"][0]
        self.stats_crew_team_id = self.team_df["stats_crew_team_id"][0]
        self.footballdb_team_id = self.team_df["footballdb_team_id"][0]
        self.espn_team_id = self.team_df["espn_team_id"][0]
        self.arenafan_team_id = self.team_df["arenafan_team_id"][0]

        self.team_abv = self.team_df["team_abv"][0]
        self.team_name = self.team_df["team_name"][0]
        self.team_location = self.team_df["team_location"][0]
        self.team_nickname = self.team_df["team_nickname"][0]
        self.team_city = self.team_df["team_city"][0]
        self.team_state = self.team_df["team_state"][0]
        self.team_nation = self.team_df["team_nation"][0]
        self.team_conference = self.team_df["team_conference"][0]
        self.team_division = self.team_df["team_division"][0]
        self.team_head_coach = self.team_df["team_head_coach"][0]
        self.team_oc = self.team_df["team_oc"][0]
        self.team_dc = self.team_df["team_dc"][0]
        self.team_timezone = self.team_df["timezone_name"][0]
        self.team_notes = self.team_df["team_notes"][0]
        self.stadium_id = self.team_df["stadium_id"][0]

        # Nations
        self.iso_nations_df = SqliteLoadData.load_iso_nations(
            con=self.sqlite3_con, cur=self.sqlite3_cur
        )
        self.refresh_iso_nations()

        # States
        self.iso_states_df = SqliteLoadData.load_iso_states(
            con=self.sqlite3_con, cur=self.sqlite3_cur
        )
        self.refresh_iso_states(
            iso_2_nation=self.team_nation,
            is_first_data_refresh=True
        )

        # Time zones
        self.refresh_iso_timezones(
            iso_2_nation=self.team_nation,
            is_first_data_refresh=True
        )

    def refresh_iso_nations(self) -> None:
        """ """
        self.iso_2_arr = self.iso_nations_df["nation_iso_alpha_2"].to_list()
        temp_nation_names_arr = self.iso_nations_df["nation_name"].to_list()

        for i in range(0, len(temp_nation_names_arr)):
            temp_nation_name = temp_nation_names_arr[i]
            temp_iso_2 = self.iso_2_arr[i]
            self.show_nations_arr.append(
                f"({temp_iso_2}) {temp_nation_name}"
            )
            del temp_nation_name
            del temp_iso_2

        temp_pointer = self.iso_2_arr.index(
            self.team_nation
        )
        self.show_nation = self.show_nations_arr[temp_pointer]
        del temp_nation_names_arr
        del temp_pointer

    def refresh_iso_states(
        self,
        iso_2_nation: str,
        is_first_data_refresh: bool = False
    ):
        """ """

        self.filtered_iso_states_df = self.iso_states_df

        self.filtered_iso_states_df = self.filtered_iso_states_df.filter(
            (pl.col("nation_iso_alpha_2") == iso_2_nation)
        )
        self.iso_states_arr = self.filtered_iso_states_df[
            "subdivision_iso_3166_2_code"
        ].to_list()
        temp_state_names_arr = self.filtered_iso_states_df[
            "subdivision_name"
        ].to_list()
        self.show_states_arr = []

        for i in range(0, len(temp_state_names_arr)):
            temp_state_name = temp_state_names_arr[i]
            temp_iso = self.iso_states_arr[i]
            self.show_states_arr.append(f"({temp_iso}) {temp_state_name}")
            del temp_state_name
            del temp_iso

        if is_first_data_refresh is True:
            temp_pointer = self.iso_states_arr.index(
                self.team_state
            )

            del temp_state_names_arr

            self.show_state = self.show_states_arr[temp_pointer]
            del temp_pointer
        else:
            self.team_state = self.iso_states_arr[0]
            self.show_state = self.show_states_arr[0]

    def refresh_iso_timezones(
        self,
        iso_2_nation: str,
        is_first_data_refresh: bool = False
    ):
        """ """
        # Timezones
        self.iso_timezones_df = SqliteLoadData.load_iso_timezones(
            con=self.sqlite3_con, cur=self.sqlite3_cur
        )
        temp_df = self.iso_timezones_df
        temp_df = temp_df.filter(
            (pl.col("nation_iso_alpha_2") == iso_2_nation)
        )
        self.show_timezones_arr = temp_df["timezone_name"].to_list()

        if is_first_data_refresh is False:
            self.team_timezone = self.show_timezones_arr[0]

    def search_iso_nation(self, show_nation: str) -> None:
        """ """
        temp_pointer = self.show_nations_arr.index(
            show_nation
        )
        self.team_nation = self.iso_2_arr[temp_pointer]
        del temp_pointer

    def search_iso_state(self, show_state: str) -> None:
        """ """
        temp_pointer = self.show_states_arr.index(
            show_state
        )
        self.team_state = self.iso_states_arr[temp_pointer]
        del temp_pointer

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

    def team_edit_view(self) -> None:
        """ """
        sg.theme(self.app_theme)
        team_info_layout = [
            [
                sg.Text("Team Abbreviation:\t\t"),
                sg.Input(
                    default_text=self.team_abv,
                    size=(7, 1),
                    enable_events=True,
                    key="-TEAM_ABV-"
                )
            ],
            [
                sg.Text("Team Name:\t\t"),
                sg.Input(
                    default_text=self.team_name,
                    size=(40, 1),
                    enable_events=True,
                    key="-TEAM_NAME-"
                )
            ],
            [
                sg.Text("Team Location:\t\t"),
                sg.Input(
                    default_text=self.team_location,
                    size=(40, 1),
                    enable_events=True,
                    key="-TEAM_LOCATION-"
                )
            ],
            [
                sg.Text("Team Nickname:\t\t"),
                sg.Input(
                    default_text=self.team_nickname,
                    size=(40, 1),
                    enable_events=True,
                    key="-TEAM_NICKNAME-"
                )
            ],
            [
                sg.Text("Nation:\t\t\t"),
                sg.Combo(
                    values=self.show_nations_arr,
                    default_value=self.show_nation,
                    size=(38, 1),
                    enable_events=True,
                    key="-TEAM_NATION-"
                )
            ],
            [
                sg.Text("City:\t\t\t"),
                sg.Input(
                    default_text=self.team_city,
                    size=(40, 1),
                    enable_events=True,
                    key="-TEAM_CITY-"
                )
            ],
            [
                sg.Text("State/Province/Territory:\t"),
                sg.Combo(
                    values=self.show_states_arr,
                    default_value=self.show_state,
                    size=(38, 1),
                    enable_events=True,
                    key="-TEAM_STATE-"
                )
            ],
            [
                sg.Text("Time Zone:\t\t"),
                sg.Combo(
                    values=self.show_timezones_arr,
                    default_value=self.team_timezone,
                    size=(38, 1),
                    enable_events=True,
                    key="-TEAM_TIME_ZONE-"
                )
            ],
            [
                sg.Text("Conference:\t\t"),
                sg.Input(
                    default_text=self.team_conference,
                    size=(40, 1),
                    enable_events=True,
                    key="-TEAM_CONFERENCE-"
                )
            ],
            [
                sg.Text("Division:\t\t\t"),
                sg.Input(
                    default_text=self.team_division,
                    size=(40, 1),
                    enable_events=True,
                    key="-TEAM_DIVISION-"
                )
            ],
            [
                sg.Text("Team Head Coach:\t\t"),
                sg.Input(
                    default_text=self.team_head_coach,
                    size=(40, 1),
                    enable_events=True,
                    key="-TEAM_HC-"
                )
            ],
            [
                sg.Text("Team Offensive Coordinator:\t"),
                sg.Input(
                    default_text=self.team_oc,
                    size=(40, 1),
                    enable_events=True,
                    key="-TEAM_OC-"
                )
            ],
            [
                sg.Text("Team Defensive Coordinator:\t"),
                sg.Input(
                    default_text=self.team_dc,
                    size=(40, 1),
                    enable_events=True,
                    key="-TEAM_DC-"
                )
            ],
            [
                sg.Text("Team Notes:\t\t"),
                sg.Multiline(
                    default_text=self.team_notes,
                    size=(38, 4),
                    enable_events=True,
                    key="-TEAM_NOTES-"
                )
            ],

        ]

        team_ids_layout = [
            [
                sg.Text("Pro Football Reference Team ID:\t"),
                sg.Input(
                    default_text=self.pfr_team_id,
                    size=(7, 1),
                    enable_events=True,
                    key="-PFR_TEAM_ID-"
                )
            ],
            [
                sg.Text("Pro Football Reference Franchise ID:\t"),
                sg.Input(
                    default_text=self.pfr_fran_id,
                    size=(7, 1),
                    enable_events=True,
                    key="-PFR_FRAN_ID-"
                )
            ],
            [
                sg.Text("NCAA Team ID:\t\t\t"),
                sg.Input(
                    default_text=self.ncaa_team_id,
                    size=(7, 1),
                    enable_events=True,
                    key="-NCAA_TEAM_ID-"
                )
            ],
            [
                sg.Text("ESPN Team ID:\t\t\t"),
                sg.Input(
                    default_text=self.espn_team_id,
                    size=(7, 1),
                    enable_events=True,
                    key="-ESPN_TEAM_ID-"
                )
            ],
            [
                sg.Text("ArenaFan Team ID:\t\t"),
                sg.Input(
                    default_text=self.arenafan_team_id,
                    size=(7, 1),
                    enable_events=True,
                    key="-ARENAFAN_TEAM_ID-"
                )
            ],
            [
                sg.Text("Stats Crew Team ID:\t\t"),
                sg.Input(
                    default_text=self.stats_crew_team_id,
                    size=(10, 1),
                    enable_events=True,
                    key="-STATS_CREW_TEAM_ID-"
                )
            ],
            [
                sg.Text("sports-reference.com Team ID:\t"),
                sg.Input(
                    default_text=self.sr_team_id,
                    size=(25, 1),
                    enable_events=True,
                    key="-SR_ID-"
                )
            ],
            [
                sg.Text("Football DB Team ID:\t\t"),
                sg.Input(
                    default_text=self.footballdb_team_id,
                    size=(25, 1),
                    enable_events=True,
                    key="-FOOTBALLDB_TEAM_ID-"
                )
            ],
        ]

        layout = [
            [
                sg.Text(
                    f"Edit Team:\n{self.season} " +
                    f"{self.team_name}",
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
                        sg.Tab("Team Info", team_info_layout),
                        sg.Tab("External Team IDs", team_ids_layout),
                    ]],
                    expand_x=True,
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
            "Edit Team...",
            layout=layout,
            # size=(500, 600),
            resizable=False,
            finalize=True,
            keep_on_top=False,
        )

        keep_open = True
        change_count = 0
        while keep_open is True:
            event, values = window.read(timeout=1000)
            print(values)
            print(event)
            # print(self.team_timezone)
            # print(self.team_nation, self.team_state)

            if event in (sg.WIN_CLOSED, "Exit"):
                keep_open = False
            elif event == "-OK_BUTTON-" and (change_count != 0):
                check_flag = self.changed_settings_check()
                # print(check_flag)
                if check_flag == "Yes":
                    self.update_team_settings()
                    keep_open = False
                elif check_flag == "No":
                    pass
                del check_flag
            elif event == "-OK_BUTTON-" and (change_count == 0):
                keep_open = False
            elif event == "-CANCEL_BUTTON-":
                keep_open = False
            elif event == "-APPLY_BUTTON-" and (change_count != 0):
                check_flag = self.changed_settings_check()
                # print(check_flag)
                if check_flag == "Yes":
                    self.update_team_settings()
                    change_count = 0
                elif check_flag == "No":
                    pass
                del check_flag
                window["-APPLY_BUTTON-"].update(disabled=True)

            if change_count == 1 and event not in (sg.WIN_CLOSED, "Exit"):
                window["-APPLY_BUTTON-"].update(disabled=False)
            elif change_count == 0 and event not in (sg.WIN_CLOSED, "Exit"):
                window["-APPLY_BUTTON-"].update(disabled=True)

            # Team abbreviation check
            if event == "-TEAM_ABV-" and len(values["-TEAM_ABV-"]) > 5:
                window["-TEAM_ABV-"].update(
                    values["-TEAM_ABV-"][:-1]
                )
                change_count += 1
            elif event == "-TEAM_ABV-" and (
                values["-TEAM_ABV-"] and
                values["-TEAM_ABV-"][-1] not in (
                    self.letters_and_numbers
                )
            ):
                window["-TEAM_ABV-"].update(
                    values["-TEAM_ABV-"][:-1]
                )
                self.team_abv = values["-TEAM_ABV-"]
                change_count += 1
            elif event == "-TEAM_ABV-" and (
                values["-TEAM_ABV-"] and
                values["-TEAM_ABV-"][-1] in (
                    self.letters_and_numbers
                )
            ):
                window["-TEAM_ABV-"].update(
                    values["-TEAM_ABV-"].upper()
                )
                self.team_abv = values["-TEAM_ABV-"].upper()
                change_count += 1

            # Pro Football Reference Team ID check
            if event == "-PFR_TEAM_ID-" and len(values["-PFR_TEAM_ID-"]) > 3:
                window["-PFR_TEAM_ID-"].update(
                    values["-PFR_TEAM_ID-"][:-1]
                )
                change_count += 1
            elif event == "-PFR_TEAM_ID-" and (
                values["-PFR_TEAM_ID-"] and
                values["-PFR_TEAM_ID-"][-1] not in (
                    self.letters_all
                )
            ):
                window["-PFR_TEAM_ID-"].update(
                    values["-PFR_TEAM_ID-"][:-1]
                )
                self.pfr_team_id = values["-PFR_TEAM_ID-"]
                change_count += 1
            elif event == "-PFR_TEAM_ID-" and (
                values["-PFR_TEAM_ID-"] and
                values["-PFR_TEAM_ID-"][-1] in (
                    self.letters_all
                )
            ):
                window["-PFR_TEAM_ID-"].update(
                    values["-PFR_TEAM_ID-"].upper()
                )
                self.pfr_team_id = values["-PFR_TEAM_ID-"].upper()
                change_count += 1

            #  Team ID check
            if event == "-PFR_TEAM_ID-" and len(values["-PFR_TEAM_ID-"]) > 3:
                window["-PFR_TEAM_ID-"].update(
                    values["-PFR_TEAM_ID-"][:-1]
                )
                change_count += 1
            elif event == "-PFR_TEAM_ID-" and (
                values["-PFR_TEAM_ID-"] and
                values["-PFR_TEAM_ID-"][-1] not in (
                    self.letters_all
                )
            ):
                window["-PFR_TEAM_ID-"].update(
                    values["-PFR_TEAM_ID-"][:-1]
                )
                self.pfr_team_id = values["-PFR_TEAM_ID-"]
                change_count += 1
            elif event == "-PFR_TEAM_ID-" and (
                values["-PFR_TEAM_ID-"] and
                values["-PFR_TEAM_ID-"][-1] in (
                    self.letters_all
                )
            ):
                window["-PFR_TEAM_ID-"].update(
                    values["-PFR_TEAM_ID-"].upper()
                )
                self.pfr_team_id = values["-PFR_TEAM_ID-"].upper()
                change_count += 1

            # Pro Football Reference Franchise ID check
            if event == "-PFR_FRAN_ID-" and len(values["-PFR_FRAN_ID-"]) > 3:
                window["-PFR_FRAN_ID-"].update(
                    values["-PFR_FRAN_ID-"][:-1]
                )
                change_count += 1
            elif event == "-PFR_FRAN_ID-" and (
                values["-PFR_FRAN_ID-"] and
                values["-PFR_FRAN_ID-"][-1] not in (
                    self.letters_all
                )
            ):
                window["-PFR_FRAN_ID-"].update(
                    values["-PFR_FRAN_ID-"][:-1]
                )
                self.pfr_fran_id = values["-PFR_FRAN_ID-"]
                change_count += 1
            elif event == "-PFR_FRAN_ID-" and (
                values["-PFR_FRAN_ID-"] and
                values["-PFR_FRAN_ID-"][-1] in (
                    self.letters_all
                )
            ):
                window["-PFR_FRAN_ID-"].update(
                    values["-PFR_FRAN_ID-"].upper()
                )
                self.pfr_fran_id = values["-PFR_FRAN_ID-"].upper()
                change_count += 1

            # Stats Crew Team ID check
            if event == "-STATS_CREW_TEAM_ID-" \
                    and len(values["-STATS_CREW_TEAM_ID-"]) > 7:
                window["-STATS_CREW_TEAM_ID-"].update(
                    values["-STATS_CREW_TEAM_ID-"][:-1]
                )
                change_count += 1
            elif event == "-STATS_CREW_TEAM_ID-" and (
                values["-STATS_CREW_TEAM_ID-"] and
                values["-STATS_CREW_TEAM_ID-"][-1] not in (
                    self.letters_and_numbers
                )
            ):
                window["-STATS_CREW_TEAM_ID-"].update(
                    values["-STATS_CREW_TEAM_ID-"][:-1]
                )
                self.stats_crew_team_id = values["-STATS_CREW_TEAM_ID-"]
                change_count += 1
            elif event == "-STATS_CREW_TEAM_ID-" and (
                values["-STATS_CREW_TEAM_ID-"] and
                values["-STATS_CREW_TEAM_ID-"][-1] in (
                    self.letters_and_numbers
                )
            ):
                window["-STATS_CREW_TEAM_ID-"].update(
                    values["-STATS_CREW_TEAM_ID-"].upper()
                )
                self.stats_crew_team_id = values[
                    "-STATS_CREW_TEAM_ID-"
                ].upper()
                change_count += 1

            # footballdb.com Team ID Check
            if event == "-FOOTBALLDB_TEAM_ID-" and (
                values["-FOOTBALLDB_TEAM_ID-"] and
                values["-FOOTBALLDB_TEAM_ID-"][-1] not in (
                    self.letters_and_numbers_spec
                )
            ):
                window["-FOOTBALLDB_TEAM_ID-"].update(
                    values["-FOOTBALLDB_TEAM_ID-"][:-1]
                )
                self.footballdb_team_id = values["-FOOTBALLDB_TEAM_ID-"]
                change_count += 1
            elif event == "-FOOTBALLDB_TEAM_ID-" and (
                values["-FOOTBALLDB_TEAM_ID-"] and
                values["-FOOTBALLDB_TEAM_ID-"][-1] in (
                    self.letters_and_numbers_spec
                )
            ):
                window["-FOOTBALLDB_TEAM_ID-"].update(
                    values["-FOOTBALLDB_TEAM_ID-"]
                )
                self.footballdb_team_id = values[
                    "-FOOTBALLDB_TEAM_ID-"
                ]
                change_count += 1

            # sports-reference.com Team ID Check
            if event == "-SR_ID-" and (
                values["-SR_ID-"] and
                values["-SR_ID-"][-1] not in (
                    self.letters_and_numbers_spec
                )
            ):
                window["-SR_ID-"].update(
                    values["-SR_ID-"][:-1]
                )
                self.sr_team_id = values["-SR_ID-"]
                change_count += 1
            elif event == "-SR_ID-" and (
                values["-SR_ID-"] and
                values["-SR_ID-"][-1] in (
                    self.letters_and_numbers_spec
                )
            ):
                window["-SR_ID-"].update(
                    values["-SR_ID-"]
                )
                self.sr_team_id = values[
                    "-SR_ID-"
                ]
                change_count += 1

            # stats.ncaa.org Team ID check
            if event == "-NCAA_TEAM_ID-" and (
                values["-NCAA_TEAM_ID-"] and
                values["-NCAA_TEAM_ID-"][-1] not in (
                    self.numbers_all
                )
            ):
                window["-NCAA_TEAM_ID-"].update(
                    values["-NCAA_TEAM_ID-"][:-1]
                )
                self.stats_crew_team_id = values["-NCAA_TEAM_ID-"]
                change_count += 1
            elif event == "-NCAA_TEAM_ID-" and (
                values["-NCAA_TEAM_ID-"] and
                values["-NCAA_TEAM_ID-"][-1] in (
                    self.numbers_all
                )
            ):
                window["-NCAA_TEAM_ID-"].update(
                    values["-NCAA_TEAM_ID-"].upper()
                )
                self.stats_crew_team_id = values["-NCAA_TEAM_ID-"].upper()
                change_count += 1

            # ESPN Team ID check
            if event == "-ESPN_TEAM_ID-" and (
                values["-ESPN_TEAM_ID-"] and
                str(values["-ESPN_TEAM_ID-"])[-1] not in (
                    self.numbers_all
                )
            ):
                window["-ESPN_TEAM_ID-"].update(
                    values["-ESPN_TEAM_ID-"][:-1]
                )
                self.espn_team_id = values["-ESPN_TEAM_ID-"]
                change_count += 1
            elif event == "-ESPN_TEAM_ID-" and (
                values["-ESPN_TEAM_ID-"] and
                values["-ESPN_TEAM_ID-"][-1] in (
                    self.numbers_all
                )
            ):
                window["-ESPN_TEAM_ID-"].update(
                    values["-ESPN_TEAM_ID-"].upper()
                )
                self.espn_team_id = values["-ESPN_TEAM_ID-"].upper()
                change_count += 1

            # ArenaFan Team ID check
            if event == "-ARENAFAN_TEAM_ID-" and (
                values["-ARENAFAN_TEAM_ID-"] and
                str(values["-ARENAFAN_TEAM_ID-"])[-1] not in (
                    self.numbers_all
                )
            ):
                window["-ARENAFAN_TEAM_ID-"].update(
                    values["-ARENAFAN_TEAM_ID-"][:-1]
                )
                self.arenafan_team_id = values["-ARENAFAN_TEAM_ID-"]
                change_count += 1
            elif event == "-ARENAFAN_TEAM_ID-" and (
                values["-ARENAFAN_TEAM_ID-"] and
                values["-ARENAFAN_TEAM_ID-"][-1] in (
                    self.numbers_all
                )
            ):
                window["-ARENAFAN_TEAM_ID-"].update(
                    values["-ARENAFAN_TEAM_ID-"].upper()
                )
                self.arenafan_team_id = values["-ARENAFAN_TEAM_ID-"].upper()
                change_count += 1

            if event == "-TEAM_NATION-":
                self.search_iso_nation(show_nation=values["-TEAM_NATION-"])
                self.refresh_iso_states(iso_2_nation=self.team_nation)
                window["-TEAM_STATE-"].update(
                    values=self.show_states_arr,
                    value=self.show_states_arr[0]
                )
                self.refresh_iso_timezones(iso_2_nation=self.team_nation)
                window["-TEAM_TIME_ZONE-"].update(
                    values=self.show_timezones_arr,
                    value=self.team_timezone
                )
                change_count += 1
            elif event == "-TEAM_STATE-":
                self.search_iso_state(show_state=values["-TEAM_STATE-"])
                change_count += 1
            elif event == "-TEAM_LOCATION-":
                self.team_location = values["-TEAM_LOCATION-"]
                change_count += 1
            elif event == "-TEAM_NAME-":
                self.team_name = values["-TEAM_NAME-"]
                change_count += 1
            elif event == "-TEAM_NICKNAME-":
                self.team_nickname = values["-TEAM_NICKNAME-"]
                change_count += 1
            elif event == "-TEAM_CITY-":
                self.team_city = values["-TEAM_CITY-"]
                change_count += 1
            elif event == "-TEAM_TIME_ZONE-":
                self.team_timezone = values["-TEAM_TIME_ZONE-"]
                change_count += 1
            elif event == "-TEAM_CONFERENCE-":
                self.team_conference = values["-TEAM_CONFERENCE-"]
                change_count += 1
            elif event == "-TEAM_DIVISION-":
                self.team_division = values["-TEAM_DIVISION-"]
                change_count += 1
            elif event == "-TEAM_HC-":
                self.team_head_coach = values["-TEAM_HC-"]
                change_count += 1
            elif event == "-TEAM_OC-":
                self.team_oc = values["-TEAM_OC-"]
                change_count += 1
            elif event == "-TEAM_DC-":
                self.team_dc = values["-TEAM_DC-"]
                change_count += 1
            elif event == "-TEAM_NOTES-":
                self.team_notes = values["-TEAM_NOTES-"]
                change_count += 1

        window.close()


class NewTeamView():
    """ """
    letters_all = LettersAndNumbers.letters_all()
    letters_and_numbers = LettersAndNumbers.letters_and_numbers()
    numbers_all = LettersAndNumbers.numbers_all()
    letters_and_numbers_spec = LettersAndNumbers.letters_and_numbers(
        include_dash_and_underscore=True
    )
    # sqlite3 connectors
    sqlite3_con, sqlite3_cur = initialize_sqlite3_connectors()

    settings_dict = {}

    team_df = pl.DataFrame()

    iso_nations_df = pl.DataFrame()
    iso_states_df = pl.DataFrame()
    filtered_iso_states_df = pl.DataFrame()
    iso_timezones_df = pl.DataFrame()

    iso_2_arr = []
    iso_states_arr = []

    # The text shown to a user to represent a specific state/nation.
    show_nations_arr = []
    show_states_arr = []
    show_timezones_arr = []
    show_nation = ""
    show_state = ""

    season = 0
    league_id = ""
    # team_id = ""

    # External Team ID systems
    pfr_team_id = None
    pfr_fran_id = None
    sr_team_id = None
    # ncaa_old_team_id = ""
    ncaa_team_id = 0
    stats_crew_team_id = None
    footballdb_team_id = None
    espn_team_id = 0
    arenafan_team_id = 0

    # Team Info
    team_abv = ""
    team_name = ""
    team_location = ""
    team_nickname = ""
    team_city = ""
    team_state = "US-OH"
    team_nation = "US"
    team_conference = None
    team_division = None
    team_head_coach = None
    team_oc = None
    team_dc = None
    team_timezone = "America/Detroit"
    team_notes = ""
    stadium_id = 0

    def __init__(
        self,
        settings_json: dict,
        league_id: str,
        season: int
    ) -> None:
        """ """
        self.settings_dict = settings_json
        self.app_theme = self.settings_dict["app_theme"]
        self.league_id = league_id
        self.season = season

        self.initial_data_load()
        self.refresh_iso_nations()
        self.refresh_iso_states(
            self.team_nation, is_first_data_refresh=True
        )
        self.refresh_iso_timezones(
            self.team_nation, is_first_data_refresh=True
        )
        self.new_team_view()

    def initial_data_load(self) -> None:
        """ """
        # Existing teams (so we can validate if a team already exists
        # before doing an insert statement).
        self.team_df = SqliteLoadData.load_fb_teams(
            con=self.sqlite3_con, cur=self.sqlite3_cur
        )
        # Nations
        self.iso_nations_df = SqliteLoadData.load_iso_nations(
            con=self.sqlite3_con, cur=self.sqlite3_cur
        )
        self.refresh_iso_nations()

        # States
        self.iso_states_df = SqliteLoadData.load_iso_states(
            con=self.sqlite3_con, cur=self.sqlite3_cur
        )
        self.refresh_iso_states(
            iso_2_nation=self.team_nation,
            is_first_data_refresh=True
        )

        # Time zones
        self.refresh_iso_timezones(
            iso_2_nation=self.team_nation,
            is_first_data_refresh=True
        )

    def refresh_iso_nations(self) -> None:
        """ """
        self.iso_2_arr = self.iso_nations_df["nation_iso_alpha_2"].to_list()
        temp_nation_names_arr = self.iso_nations_df["nation_name"].to_list()

        for i in range(0, len(temp_nation_names_arr)):
            temp_nation_name = temp_nation_names_arr[i]
            temp_iso_2 = self.iso_2_arr[i]
            self.show_nations_arr.append(
                f"({temp_iso_2}) {temp_nation_name}"
            )
            del temp_nation_name
            del temp_iso_2

        temp_pointer = self.iso_2_arr.index(
            self.team_nation
        )
        self.show_nation = self.show_nations_arr[temp_pointer]
        del temp_nation_names_arr
        del temp_pointer

    def refresh_iso_states(
        self,
        iso_2_nation: str,
        is_first_data_refresh: bool = False
    ):
        """ """

        self.filtered_iso_states_df = self.iso_states_df

        self.filtered_iso_states_df = self.filtered_iso_states_df.filter(
            (pl.col("nation_iso_alpha_2") == iso_2_nation)
        )
        self.iso_states_arr = self.filtered_iso_states_df[
            "subdivision_iso_3166_2_code"
        ].to_list()
        temp_state_names_arr = self.filtered_iso_states_df[
            "subdivision_name"
        ].to_list()
        self.show_states_arr = []

        for i in range(0, len(temp_state_names_arr)):
            temp_state_name = temp_state_names_arr[i]
            temp_iso = self.iso_states_arr[i]
            self.show_states_arr.append(
                f"{temp_state_name} ({temp_iso})"
            )
            del temp_state_name
            del temp_iso

        if is_first_data_refresh is True:
            temp_pointer = self.iso_states_arr.index(
                self.team_state
            )

            del temp_state_names_arr

            self.show_state = self.show_states_arr[temp_pointer]
            del temp_pointer
        else:
            self.team_state = self.iso_states_arr[0]
            self.show_state = self.show_states_arr[0]

    def refresh_iso_timezones(
        self,
        iso_2_nation: str,
        is_first_data_refresh: bool = False
    ):
        """ """
        # Timezones
        self.iso_timezones_df = SqliteLoadData.load_iso_timezones(
            con=self.sqlite3_con, cur=self.sqlite3_cur
        )
        temp_df = self.iso_timezones_df
        temp_df = temp_df.filter(
            (pl.col("nation_iso_alpha_2") == iso_2_nation)
        )
        self.show_timezones_arr = temp_df["timezone_name"].to_list()

        if is_first_data_refresh is False:
            self.team_timezone = self.show_timezones_arr[0]

    def search_iso_nation(self, show_nation: str) -> None:
        """ """
        temp_pointer = self.show_nations_arr.index(
            show_nation
        )
        self.team_nation = self.iso_2_arr[temp_pointer]
        del temp_pointer

    def search_iso_state(self, show_state: str) -> None:
        """ """
        temp_pointer = self.show_states_arr.index(
            show_state
        )
        self.team_state = self.iso_states_arr[temp_pointer]
        del temp_pointer

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

    def validate_input(self) -> bool:
        """
        This function exists so that we can double check
        that the user is actually inputting data,
        and not blindly hitting "OK" without much thought.

        Because the SQL Database for this app requires these
        parameters to be not null for a valid insert.
        """
        temp_df = self.team_df.filter(
            (pl.col("league_id") == self.league_id) &
            (pl.col("season") == self.season) &
            (pl.col("team_id") == self.team_abv)
        )
        if len(temp_df) > 0:
            sg.PopupError(
                f"A team with an team ID of {self.team_abv} " +
                f"already exists in the {self.season} {self.league_id} " +
                "season."
            )
            return False

        if len(self.team_abv) > 1:
            pass
        else:
            sg.PopupError(
                "You must input a value for " +
                "\"Team Abbreviation\"."
            )
            return False

        if len(self.team_name) > 1:
            pass
        else:
            sg.PopupError(
                "You must input a value for " +
                "\"Team Name\"."
            )
            return False

        if len(self.team_location) > 1:
            pass
        else:
            sg.PopupError(
                "You must input a value for " +
                "\"Team Location\"."
            )
            return False

        if len(self.team_nickname) > 1:
            pass
        else:
            sg.PopupError(
                "You must input a value for " +
                "\"Team Location\"."
            )
            return False

        if len(self.team_city) > 1:
            pass
        else:
            sg.PopupError(
                "You must input a value for " +
                "\"City\".\n" +
                "Even if this is a traveling team, " +
                "please input the city this team is supposed to represent."
            )
            return False

        if int(self.arenafan_team_id) < 10000:
            pass
        else:
            sg.PopupError(
                "Your input for \"ArenaFan Team ID\" is inconsistent " +
                "with known team IDs from that website.\n" +
                "Double check that you are inputting the correct data."
            )
            return False

        if int(self.ncaa_team_id) < 1000000:
            pass
        else:
            sg.PopupError(
                "Your input for \"NCAA Team ID\" is inconsistent " +
                "with known team IDs from stats.ncaa.org.\n" +
                "Double check that you are inputting the correct data."
            )
            return False

        if int(self.espn_team_id) < 1000000:
            pass
        else:
            sg.PopupError(
                "Your input for \"ESPN Team ID\" is inconsistent " +
                "with known team IDs from that website.\n" +
                "Double check that you are inputting the correct data."
            )
            return False
        # If we're at this point, this means that the user at minimum
        # inputted something resembling a real actual football team.

        # Return `True` to tell the main loop that this team is perfectly
        # valid to insert into the SQL database.
        return True

    def update_team_settings(self) -> None:
        sql_script = """
        INSERT INTO "fb_teams"
        (
            "season",
            "league_id",
            "team_id",
            "pfr_team_id",
            "pfr_fran_id",
            "sr_team_id",
            "ncaa_team_id",
            "stats_crew_team_id",
            "footballdb_team_id",
            "espn_team_id",
            "arenafan_team_id",
            "team_abv",
            "team_name",
            "team_location",
            "team_nickname",
            "team_city",
            "team_state",
            "team_nation",
            "team_conference",
            "team_division",
            "team_head_coach",
            "team_oc",
            "team_dc",
            "timezone_name",
            "team_notes",
            "stadium_id"
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
            ?
        );
        """
        self.sqlite3_cur.execute(
            sql_script,
            (
                self.season,
                self.league_id,
                self.team_abv,
                self.pfr_team_id,
                self.pfr_fran_id,
                self.sr_team_id,
                self.ncaa_team_id,
                self.stats_crew_team_id,
                self.footballdb_team_id,
                self.espn_team_id,
                self.arenafan_team_id,
                self.team_abv,
                self.team_name,
                self.team_location,
                self.team_nickname,
                self.team_city,
                self.team_state,
                self.team_nation,
                self.team_conference,
                self.team_division,
                self.team_head_coach,
                self.team_oc,
                self.team_dc,
                self.team_timezone,
                self.team_notes,
                self.stadium_id
            ),
        )
        self.sqlite3_con.commit()

    def new_team_view(self) -> None:
        """ """
        sg.theme(self.app_theme)

        team_info_layout = [
            [
                sg.Text("Team Abbreviation:\t\t"),
                sg.Input(
                    default_text=self.team_abv,
                    size=(7, 1),
                    enable_events=True,
                    key="-TEAM_ABV-"
                )
            ],
            [
                sg.Text("Team Name:\t\t"),
                sg.Input(
                    default_text=self.team_name,
                    size=(40, 1),
                    enable_events=True,
                    key="-TEAM_NAME-"
                )
            ],
            [
                sg.Text("Team Location:\t\t"),
                sg.Input(
                    default_text=self.team_location,
                    size=(40, 1),
                    enable_events=True,
                    key="-TEAM_LOCATION-"
                )
            ],
            [
                sg.Text("Team Nickname:\t\t"),
                sg.Input(
                    default_text=self.team_nickname,
                    size=(40, 1),
                    enable_events=True,
                    key="-TEAM_NICKNAME-"
                )
            ],
            [
                sg.Text("Nation:\t\t\t"),
                sg.Combo(
                    values=self.show_nations_arr,
                    default_value=self.show_nation,
                    size=(38, 1),
                    enable_events=True,
                    key="-TEAM_NATION-"
                )
            ],
            [
                sg.Text("City:\t\t\t"),
                sg.Input(
                    default_text=self.team_city,
                    size=(40, 1),
                    enable_events=True,
                    key="-TEAM_CITY-"
                )
            ],
            [
                sg.Text("State/Province/Territory:\t"),
                sg.Combo(
                    values=self.show_states_arr,
                    default_value=self.show_state,
                    size=(38, 1),
                    enable_events=True,
                    key="-TEAM_STATE-"
                )
            ],
            [
                sg.Text("Time Zone:\t\t"),
                sg.Combo(
                    values=self.show_timezones_arr,
                    default_value=self.team_timezone,
                    size=(38, 1),
                    enable_events=True,
                    key="-TEAM_TIME_ZONE-"
                )
            ],
            [
                sg.Text("Conference:\t\t"),
                sg.Input(
                    default_text=self.team_conference,
                    size=(40, 1),
                    enable_events=True,
                    key="-TEAM_CONFERENCE-"
                )
            ],
            [
                sg.Text("Division:\t\t\t"),
                sg.Input(
                    default_text=self.team_division,
                    size=(40, 1),
                    enable_events=True,
                    key="-TEAM_DIVISION-"
                )
            ],
            [
                sg.Text("Team Head Coach:\t\t"),
                sg.Input(
                    default_text=self.team_head_coach,
                    size=(40, 1),
                    enable_events=True,
                    key="-TEAM_HC-"
                )
            ],
            [
                sg.Text("Team Offensive Coordinator:\t"),
                sg.Input(
                    default_text=self.team_oc,
                    size=(40, 1),
                    enable_events=True,
                    key="-TEAM_OC-"
                )
            ],
            [
                sg.Text("Team Defensive Coordinator:\t"),
                sg.Input(
                    default_text=self.team_dc,
                    size=(40, 1),
                    enable_events=True,
                    key="-TEAM_DC-"
                )
            ],
            [
                sg.Text("Team Notes:\t\t"),
                sg.Multiline(
                    default_text=self.team_notes,
                    size=(38, 4),
                    enable_events=True,
                    key="-TEAM_NOTES-"
                )
            ],

        ]

        team_ids_layout = [
            [
                sg.Text("Pro Football Reference Team ID:\t"),
                sg.Input(
                    default_text=self.pfr_team_id,
                    size=(7, 1),
                    enable_events=True,
                    key="-PFR_TEAM_ID-"
                )
            ],
            [
                sg.Text("Pro Football Reference Franchise ID:\t"),
                sg.Input(
                    default_text=self.pfr_fran_id,
                    size=(7, 1),
                    enable_events=True,
                    key="-PFR_FRAN_ID-"
                )
            ],
            [
                sg.Text("NCAA Team ID:\t\t\t"),
                sg.Input(
                    default_text=self.ncaa_team_id,
                    size=(7, 1),
                    enable_events=True,
                    key="-NCAA_TEAM_ID-"
                )
            ],
            [
                sg.Text("ESPN Team ID:\t\t\t"),
                sg.Input(
                    default_text=self.espn_team_id,
                    size=(7, 1),
                    enable_events=True,
                    key="-ESPN_TEAM_ID-"
                )
            ],
            [
                sg.Text("ArenaFan Team ID:\t\t"),
                sg.Input(
                    default_text=self.arenafan_team_id,
                    size=(7, 1),
                    enable_events=True,
                    key="-ARENAFAN_TEAM_ID-"
                )
            ],
            [
                sg.Text("Stats Crew Team ID:\t\t"),
                sg.Input(
                    default_text=self.stats_crew_team_id,
                    size=(10, 1),
                    enable_events=True,
                    key="-STATS_CREW_TEAM_ID-"
                )
            ],
            [
                sg.Text("sports-reference.com Team ID:\t"),
                sg.Input(
                    default_text=self.sr_team_id,
                    size=(25, 1),
                    enable_events=True,
                    key="-SR_ID-"
                )
            ],
            [
                sg.Text("Football DB Team ID:\t\t"),
                sg.Input(
                    default_text=self.footballdb_team_id,
                    size=(25, 1),
                    enable_events=True,
                    key="-FOOTBALLDB_TEAM_ID-"
                )
            ],
        ]

        layout = [
            [
                sg.Text(
                    f"Edit Team:\n{self.season} " +
                    f"{self.team_name}",
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
                        sg.Tab("Team Info", team_info_layout),
                        sg.Tab("External Team IDs", team_ids_layout),
                    ]],
                    expand_x=True,
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
            "Edit Team...",
            layout=layout,
            # size=(500, 600),
            resizable=False,
            finalize=True,
            keep_on_top=False,
        )

        keep_open = True
        while keep_open is True:
            event, values = window.read(timeout=1000)
            print(values)
            print(event)
            # print(self.team_timezone)
            # print(self.team_nation, self.team_state)

            if event in (sg.WIN_CLOSED, "Exit"):
                keep_open = False
            elif event == "-OK_BUTTON-":
                check_flag = self.changed_settings_check()
                # print(check_flag)
                if check_flag == "Yes":
                    check = self.validate_input()
                    if check is True:
                        self.update_team_settings()
                        keep_open = False
                elif check_flag == "No":
                    pass
                del check_flag
            elif event == "-CANCEL_BUTTON-":
                keep_open = False

            # Team abbreviation check
            if event == "-TEAM_ABV-" and len(values["-TEAM_ABV-"]) > 5:
                window["-TEAM_ABV-"].update(
                    values["-TEAM_ABV-"][:-1]
                )
            elif event == "-TEAM_ABV-" and (
                values["-TEAM_ABV-"] and
                values["-TEAM_ABV-"][-1] not in (
                    self.letters_and_numbers
                )
            ):
                window["-TEAM_ABV-"].update(
                    values["-TEAM_ABV-"][:-1]
                )
                self.team_abv = values["-TEAM_ABV-"]
            elif event == "-TEAM_ABV-" and (
                values["-TEAM_ABV-"] and
                values["-TEAM_ABV-"][-1] in (
                    self.letters_and_numbers
                )
            ):
                window["-TEAM_ABV-"].update(
                    values["-TEAM_ABV-"].upper()
                )
                self.team_abv = values["-TEAM_ABV-"].upper()

            # Pro Football Reference Team ID check
            if event == "-PFR_TEAM_ID-" and len(values["-PFR_TEAM_ID-"]) > 3:
                window["-PFR_TEAM_ID-"].update(
                    values["-PFR_TEAM_ID-"][:-1]
                )
            elif event == "-PFR_TEAM_ID-" and (
                values["-PFR_TEAM_ID-"] and
                values["-PFR_TEAM_ID-"][-1] not in (
                    self.letters_all
                )
            ):
                window["-PFR_TEAM_ID-"].update(
                    values["-PFR_TEAM_ID-"][:-1]
                )
                self.pfr_team_id = values["-PFR_TEAM_ID-"]
            elif event == "-PFR_TEAM_ID-" and (
                values["-PFR_TEAM_ID-"] and
                values["-PFR_TEAM_ID-"][-1] in (
                    self.letters_all
                )
            ):
                window["-PFR_TEAM_ID-"].update(
                    values["-PFR_TEAM_ID-"].upper()
                )
                self.pfr_team_id = values["-PFR_TEAM_ID-"].upper()

            # Pro Football Reference Franchise ID check
            if event == "-PFR_FRAN_ID-" and len(values["-PFR_FRAN_ID-"]) > 3:
                window["-PFR_FRAN_ID-"].update(
                    values["-PFR_FRAN_ID-"][:-1]
                )
            elif event == "-PFR_FRAN_ID-" and (
                values["-PFR_FRAN_ID-"] and
                values["-PFR_FRAN_ID-"][-1] not in (
                    self.letters_all
                )
            ):
                window["-PFR_FRAN_ID-"].update(
                    values["-PFR_FRAN_ID-"][:-1]
                )
                self.pfr_fran_id = values["-PFR_FRAN_ID-"]
            elif event == "-PFR_FRAN_ID-" and (
                values["-PFR_FRAN_ID-"] and
                values["-PFR_FRAN_ID-"][-1] in (
                    self.letters_all
                )
            ):
                window["-PFR_FRAN_ID-"].update(
                    values["-PFR_FRAN_ID-"].upper()
                )
                self.pfr_fran_id = values["-PFR_FRAN_ID-"].upper()

            # Stats Crew Team ID check
            if event == "-STATS_CREW_TEAM_ID-" \
                    and len(values["-STATS_CREW_TEAM_ID-"]) > 7:
                window["-STATS_CREW_TEAM_ID-"].update(
                    values["-STATS_CREW_TEAM_ID-"][:-1]
                )
            elif event == "-STATS_CREW_TEAM_ID-" and (
                values["-STATS_CREW_TEAM_ID-"] and
                values["-STATS_CREW_TEAM_ID-"][-1] not in (
                    self.letters_and_numbers
                )
            ):
                window["-STATS_CREW_TEAM_ID-"].update(
                    values["-STATS_CREW_TEAM_ID-"][:-1]
                )
                self.stats_crew_team_id = values["-STATS_CREW_TEAM_ID-"]
            elif event == "-STATS_CREW_TEAM_ID-" and (
                values["-STATS_CREW_TEAM_ID-"] and
                values["-STATS_CREW_TEAM_ID-"][-1] in (
                    self.letters_and_numbers
                )
            ):
                window["-STATS_CREW_TEAM_ID-"].update(
                    values["-STATS_CREW_TEAM_ID-"].upper()
                )
                self.stats_crew_team_id = values[
                    "-STATS_CREW_TEAM_ID-"
                ].upper()

            # footballdb.com Team ID Check
            if event == "-FOOTBALLDB_TEAM_ID-" and (
                values["-FOOTBALLDB_TEAM_ID-"] and
                values["-FOOTBALLDB_TEAM_ID-"][-1] not in (
                    self.letters_and_numbers_spec
                )
            ):
                window["-FOOTBALLDB_TEAM_ID-"].update(
                    values["-FOOTBALLDB_TEAM_ID-"][:-1]
                )
                self.footballdb_team_id = values["-FOOTBALLDB_TEAM_ID-"]
            elif event == "-FOOTBALLDB_TEAM_ID-" and (
                values["-FOOTBALLDB_TEAM_ID-"] and
                values["-FOOTBALLDB_TEAM_ID-"][-1] in (
                    self.letters_and_numbers_spec
                )
            ):
                window["-FOOTBALLDB_TEAM_ID-"].update(
                    values["-FOOTBALLDB_TEAM_ID-"]
                )
                self.footballdb_team_id = values[
                    "-FOOTBALLDB_TEAM_ID-"
                ]

            # sports-reference.com Team ID Check
            if event == "-SR_ID-" and (
                values["-SR_ID-"] and
                values["-SR_ID-"][-1] not in (
                    self.letters_and_numbers_spec
                )
            ):
                window["-SR_ID-"].update(
                    values["-SR_ID-"][:-1]
                )
                self.sr_team_id = values["-SR_ID-"]
            elif event == "-SR_ID-" and (
                values["-SR_ID-"] and
                values["-SR_ID-"][-1] in (
                    self.letters_and_numbers_spec
                )
            ):
                window["-SR_ID-"].update(
                    values["-SR_ID-"]
                )
                self.sr_team_id = values[
                    "-SR_ID-"
                ]

            # stats.ncaa.org Team ID check
            if event == "-NCAA_TEAM_ID-" and (
                values["-NCAA_TEAM_ID-"] and
                values["-NCAA_TEAM_ID-"][-1] not in (
                    self.numbers_all
                )
            ):
                window["-NCAA_TEAM_ID-"].update(
                    values["-NCAA_TEAM_ID-"][:-1]
                )
                self.ncaa_team_id = values["-NCAA_TEAM_ID-"]
            elif event == "-NCAA_TEAM_ID-" and (
                values["-NCAA_TEAM_ID-"] and
                values["-NCAA_TEAM_ID-"][-1] in (
                    self.numbers_all
                )
            ):
                window["-NCAA_TEAM_ID-"].update(
                    values["-NCAA_TEAM_ID-"].upper()
                )
                self.ncaa_team_id = values["-NCAA_TEAM_ID-"].upper()

            # ESPN Team ID check
            if event == "-ESPN_TEAM_ID-" and (
                values["-ESPN_TEAM_ID-"] and
                values["-ESPN_TEAM_ID-"][-1] not in (
                    self.numbers_all
                )
            ):
                window["-ESPN_TEAM_ID-"].update(
                    values["-ESPN_TEAM_ID-"][:-1]
                )
                self.espn_team_id = values["-ESPN_TEAM_ID-"]
            elif event == "-ESPN_TEAM_ID-" and (
                values["-ESPN_TEAM_ID-"] and
                values["-ESPN_TEAM_ID-"][-1] in (
                    self.numbers_all
                )
            ):
                window["-ESPN_TEAM_ID-"].update(
                    values["-ESPN_TEAM_ID-"]
                )
                self.espn_team_id = values["-ESPN_TEAM_ID-"].upper()

            # ArenaFan Team ID check
            if event == "-ARENAFAN_TEAM_ID-" and (
                values["-ARENAFAN_TEAM_ID-"] and
                values["-ARENAFAN_TEAM_ID-"][-1] not in (
                    self.numbers_all
                )
            ):
                window["-ARENAFAN_TEAM_ID-"].update(
                    values["-ARENAFAN_TEAM_ID-"][:-1]
                )
                self.arenafan_team_id = values["-ARENAFAN_TEAM_ID-"]
            elif event == "-ARENAFAN_TEAM_ID-" and (
                values["-ARENAFAN_TEAM_ID-"] and
                values["-ARENAFAN_TEAM_ID-"][-1] in (
                    self.numbers_all
                )
            ):
                window["-ARENAFAN_TEAM_ID-"].update(
                    values["-ARENAFAN_TEAM_ID-"].upper()
                )
                self.arenafan_team_id = values["-ARENAFAN_TEAM_ID-"].upper()

            if event == "-TEAM_NATION-":
                self.search_iso_nation(show_nation=values["-TEAM_NATION-"])
                self.refresh_iso_states(iso_2_nation=self.team_nation)
                window["-TEAM_STATE-"].update(
                    values=self.show_states_arr,
                    value=self.show_states_arr[0]
                )
                self.refresh_iso_timezones(iso_2_nation=self.team_nation)
                window["-TEAM_TIME_ZONE-"].update(
                    values=self.show_timezones_arr,
                    value=self.team_timezone
                )
            elif event == "-TEAM_STATE-":
                self.search_iso_state(show_state=values["-TEAM_STATE-"])
            elif event == "-TEAM_LOCATION-":
                self.team_location = values["-TEAM_LOCATION-"]
            elif event == "-TEAM_NAME-":
                self.team_name = values["-TEAM_NAME-"]
            elif event == "-TEAM_NICKNAME-":
                self.team_nickname = values["-TEAM_NICKNAME-"]
            elif event == "-TEAM_CITY-":
                self.team_city = values["-TEAM_CITY-"]
            elif event == "-TEAM_TIME_ZONE-":
                self.team_timezone = values["-TEAM_TIME_ZONE-"]
            elif event == "-TEAM_CONFERENCE-":
                self.team_conference = values["-TEAM_CONFERENCE-"]
            elif event == "-TEAM_DIVISION-":
                self.team_division = values["-TEAM_DIVISION-"]
            elif event == "-TEAM_HC-":
                self.team_head_coach = values["-TEAM_HC-"]
            elif event == "-TEAM_OC-":
                self.team_oc = values["-TEAM_OC-"]
            elif event == "-TEAM_DC-":
                self.team_dc = values["-TEAM_DC-"]
            elif event == "-TEAM_NOTES-":
                self.team_notes = values["-TEAM_NOTES-"]

        window.close()
