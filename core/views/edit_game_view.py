"""
# Creation Date: 03/10/2024 4:35 PM EDT
# Last Updated: 06/04/2024 12:25 PM EDT
# Authors: Joseph Armstrong (armstrongjoseph08@gmail.com)
# file: `./core/views/new_game_view.py`
# Purpose: Code behind for the window that
    allows a user to edit a game.
"""
import FreeSimpleGUI as sg
import polars as pl

from core.database.load_db_elements import SqliteLoadData
from core.database.sqlite3_connectors import initialize_sqlite3_connectors
from core.other.embedded import EmbeddedElements, LettersAndNumbers
from core.time import convert_datetime_into_utc_time


class EditGameView:
    """
    Allows one to edit a game within a season.
    """

    letters_all = LettersAndNumbers.letters_all()
    letters_and_numbers = LettersAndNumbers.letters_and_numbers()
    numbers_all = LettersAndNumbers.numbers_all()
    letters_and_numbers_spec = LettersAndNumbers.letters_and_numbers(
        include_dash_and_underscore=True
    )

    # sqlite3 connectors
    sqlite3_con, sqlite3_cur = initialize_sqlite3_connectors()

    settings_dict = {}

    app_theme = ""
    teams_arr = []
    team_df = pl.DataFrame()
    schedule_df = pl.DataFrame()
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

    game_types_arr = ["PRE", "REG", "POST", "WC", "DIV", "CON", "SB", "CHAMP"]
    weeks_arr = [x for x in range(1, 31)]

    hours_12_arr = [f"{x:02d}" for x in range(1, 13)]
    hours_24_arr = [f"{x:02d}" for x in range(0, 24)]
    minutes_arr = [f"{x:02d}" for x in range(0, 60)]
    hour_12_num = "01"
    hour_24_num = "13"
    minute_num = "00"

    game_roof_arr = ["outdoors", "dome", "open", "closed"]
    surface_arr = [
        "A-Turf",
        "Astro Play Turf",
        "AstroTurf",
        "Desso Grass",
        "Field Turf",
        "Natural Grass",
        "Matrix Turf",
        "Sport Turf"
    ]
    surface_dict = {
        "A-Turf": "a_turf",
        "Astro Play Turf": "astro_play",
        "AstroTurf": "astroturf",
        "Desso Grass": "desso_grass",
        "Field Turf": "field_turf",
        "Natural Grass": "grass",
        "Matrix Turf": "matrix_turf",
        "Sport Turf": "sport_turf",
    }
    temp_c_arr = [x for x in range(-90, 90)]
    temp_f_arr = [x for x in range(-140, 180)]

    season = 0
    league_id = ""
    team_id = ""

    # NOTE: we don't need to worry about this in this part of the app.
    # SQLite automatically does this when we create a new game.

    # game_is_in_progress = 0
    # game_is_finished = 0
    # game_status = "not_started"
    # away_team_score = 0
    # home_team_score = 0

    nflverse_game_id = ""
    game_type = "REG"
    week = 1
    is_24_hour_time = False
    hours_12 = 0

    game_day = ""
    game_time = "13:00"
    game_timezone = "America/New_York"
    game_datetime = ""
    game_datetime_utc = ""
    game_day_of_week = ""
    game_nation = "US"
    game_state = "US-OH"

    away_team_abv = ""
    home_team_abv = ""

    nflverse_old_game_id = 0
    gsis_id = ""
    # nfl_detail_id = ""  # UID
    pfr_game_id = ""
    pff_game_id = 0
    espn_game_id = 0
    ftn_game_id = 0
    ncaa_game_id = 0
    # Stats Crew don't have game IDs... yet
    # stats_crew_team_id = ""
    yahoo_game_id = ""
    arenafan_game_id = ""
    football_db_game_id = ""

    away_days_rest = 0
    home_days_rest = 0
    is_neutral_site_game = False
    # is_overtime_game = False # We don't need that here.
    is_divisional_game = False
    game_roof = "outdoors"
    surface = "grass"
    temp_f = 64
    temp_c = 18
    wind = 0
    away_coach_name = ""
    home_coach_name = ""
    stadium_id = 0

    def __init__(
        self,
        settings_json: dict,
        game_id: str
    ) -> None:
        self.settings_dict = settings_json
        self.app_theme = self.settings_dict["app_theme"]

        self.nflverse_game_id = game_id

        self.initial_data_load()
        self.new_game_view()

    def initial_data_load(self):
        """ """
        self.schedule_df = SqliteLoadData.load_fb_schedule(
            con=self.sqlite3_con, cur=self.sqlite3_cur
        )

        temp_df = self.schedule_df.filter(
            (pl.col("nflverse_game_id") == self.nflverse_game_id)
        )
        self.season = temp_df["season"][0]
        self.league_id = temp_df["league_id"][0]

        self.team_df = SqliteLoadData.load_fb_teams(
            con=self.sqlite3_con, cur=self.sqlite3_cur
        )
        self.team_df = self.team_df.filter(
            (pl.col("league_id") == self.league_id) &
            (pl.col("season") == self.season)
        )
        self.teams_arr = self.team_df["team_id"].to_list()
        self.teams_arr.append("-TBD-")

        self.game_type = temp_df["game_type"][0]
        self.week = temp_df["week"][0]
        self.is_24_hour_time = False  # TODO: Make a setting for this.
        self.hours_12 = 0
        self.is_pm_time = False

        self.game_day = temp_df["game_day"][0]
        self.game_time = temp_df["game_time"][0]
        self.game_timezone = temp_df["game_time_zone"][0]
        self.game_datetime = temp_df["game_datetime"][0]
        self.game_datetime_utc = temp_df["game_datetime_utc"][0]
        self.game_day_of_week = temp_df["game_day_of_week"][0]
        self.game_nation = temp_df["game_nation"][0]
        self.game_state = temp_df["game_state"][0]

        self.away_team_abv = temp_df["away_team_abv"][0]
        self.home_team_abv = temp_df["home_team_abv"][0]

        self.nflverse_old_game_id = temp_df["nflverse_old_game_id"][0]
        self.gsis_id = temp_df["gsis_id"][0]
        self.pfr_game_id = temp_df["pfr_game_id"][0]
        self.pff_game_id = temp_df["pff_game_id"][0]
        self.espn_game_id = temp_df["espn_game_id"][0]
        self.ftn_game_id = temp_df["ftn_game_id"][0]
        self.ncaa_game_id = temp_df["ncaa_game_id"][0]
        self.yahoo_game_id = temp_df["yahoo_game_id"][0]
        self.arenafan_game_id = temp_df["arenafan_game_id"][0]
        self.football_db_game_id = temp_df["football_db_game_id"][0]

        self.away_days_rest = temp_df["away_days_rest"][0]
        self.home_days_rest = temp_df["home_days_rest"][0]
        self.is_neutral_site_game = temp_df["is_neutral_site_game"][0]

        self.is_divisional_game = temp_df["is_divisional_game"][0]
        self.game_roof = temp_df["game_roof"][0]
        self.surface = temp_df["surface"][0]

        # TODO: We need a setting to switch from F to C, and vice versa.
        self.temp_f = temp_df["temp_f"][0]
        self.temp_c = temp_df["temp_c"][0]

        if self.temp_f is None and self.temp_c is None:
            # If for some reason this is true,
            # set a default temperature.
            self.temp_f = 68
            self.temp_c = 20
        if self.temp_f is None:
            self.temp_f = (self.temp_c * (9/5)) + 32
        if self.temp_c is None:
            self.temp_c = (self.temp_f - 32) / (9/5)

        self.wind = temp_df["wind"][0]
        # self.away_coach_name = temp_df["away_coach_name"][0]
        # self.home_coach_name = temp_df["home_coach_name"][0]
        self.stadium_id = temp_df["stadium_id"][0]

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
            iso_2_nation="US",
            is_first_data_refresh=True
        )

        # Time zones
        self.refresh_iso_timezones(
            # iso_2_nation="US",
            is_first_data_refresh=True
        )

    def refresh_iso_nations(self) -> None:
        """ """
        self.iso_2_arr = self.iso_nations_df["nation_iso_alpha_2"].to_list()
        temp_nation_names_arr = self.iso_nations_df["nation_name"].to_list()

        for i in range(0, len(temp_nation_names_arr)):
            temp_nation_name = temp_nation_names_arr[i]
            temp_iso_2 = self.iso_2_arr[i]
            self.show_nations_arr.append(f"({temp_iso_2}) {temp_nation_name}")
            del temp_nation_name
            del temp_iso_2

        temp_pointer = self.iso_2_arr.index(self.game_nation)
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
            temp_pointer = self.iso_states_arr.index(self.game_state)

            del temp_state_names_arr

            self.show_state = self.show_states_arr[temp_pointer]
            del temp_pointer
        else:
            self.game_state = self.iso_states_arr[0]
            self.show_state = self.show_states_arr[0]

    def refresh_iso_timezones(
        self,
        # iso_2_nation: str,
        is_first_data_refresh: bool = False
    ):
        """ """
        # Timezones
        self.iso_timezones_df = SqliteLoadData.load_iso_timezones(
            con=self.sqlite3_con, cur=self.sqlite3_cur
        )
        temp_df = self.iso_timezones_df
        # temp_df = temp_df.filter(
        #     (pl.col("nation_iso_alpha_2") == iso_2_nation)
        # )
        self.show_timezones_arr = temp_df["timezone_name"].to_list()

        if is_first_data_refresh is False:
            self.game_timezone = self.show_timezones_arr[0]

    def search_iso_nation(self) -> None:
        """ """
        temp_pointer = self.show_nations_arr.index(self.show_nation)
        self.game_nation = self.iso_2_arr[temp_pointer]
        del temp_pointer

    def search_iso_state(self) -> None:
        """ """
        temp_pointer = self.show_states_arr.index(self.show_state)
        self.game_state = self.iso_states_arr[temp_pointer]
        del temp_pointer

    def game_validation_check(self) -> bool:
        """ """

        if self.week >= 1:
            # This should never be the case,
            # but let's be safe than sorry.
            pass
        else:
            sg.PopupError(
                "You must input a value for " +
                "\"Week\"."
            )
            return False

        if len(self.away_team_abv) > 0:
            pass
        else:
            sg.PopupError(
                "You must indicate who the away team is, " +
                "or set \"Away Team\" to \"-TBD-\"."
            )
            return False

        if len(self.home_team_abv) > 0:
            pass
        else:
            sg.PopupError(
                "You must indicate who the home team is, " +
                "or set \"Home Team\" to \"-TBD-\"."
            )
            return False

        if len(self.game_type) > 0:
            # This should never be the case,
            # but let's be safe than sorry.
            pass
        else:
            sg.PopupError(
                "You must indicate what type of game this is.\n" +
                "Please set an actual value for \"Game Type\"."
            )
            return False

        if len(self.surface) > 0:
            # This should never be the case,
            # but let's be safe than sorry.
            pass
        else:
            sg.PopupError(
                "You must indicate what the playing surface is " +
                "for this game.\n" +
                "Please set a valid value for \"Playing Surface\" " +
                "and try again."
            )
            return False

        if len(self.game_roof) > 0:
            # This should never be the case,
            # but let's be safe than sorry.
            pass
        else:
            sg.PopupError(
                "You must indicate if there is a roof over this game, " +
                "and if this roof is open or closed."
            )
            return False

        if len(self.game_state) > 0:
            # This should never be the case,
            # but let's be safe than sorry.
            pass
        else:
            sg.PopupError(
                "You must indicate which state this game transpired in."
            )
            return False

        if len(self.game_nation) > 0:
            # This should never be the case,
            # but let's be safe than sorry.
            pass
        else:
            sg.PopupError(
                "You must indicate which nation this game transpired in."
            )
            return False

        if len(self.game_timezone) > 0:
            # This should never be the case,
            # but let's be safe than sorry.
            pass
        else:
            sg.PopupError(
                "Please indicate which timezone this game's time is in."
            )
            return False

        if len(self.game_day) > 0 and len(self.game_time) > 0:
            self.game_datetime, \
                self.game_datetime_utc, \
                self.game_day_of_week = convert_datetime_into_utc_time(
                    date_str=self.game_day,
                    time_str=self.game_time,
                    timezone=self.game_timezone
                )
            # self.game_day = self.game_datetime.strftime("%A")
        else:
            sg.PopupError(
                "You must have valid inputs for \"Game Date\" " +
                "and \"Game Time\"."
            )
            return False

        self.nflverse_game_id = f"{self.season}_{self.league_id}_"
        self.nflverse_game_id += f"{self.week:02d}_"
        self.nflverse_game_id += f"{self.away_team_abv}_{self.home_team_abv}"
        # If we get to this point,
        # this means that the input is good,
        # so return `True` so the app knows this
        # is good, and it has permission to insert
        # this data.
        return True

    def update_game(self):
        """ """
        sql_script = """
        UPDATE "fb_schedule"
        SET
            "game_type" = ?,
            "week" = ?,
            "game_day" = ?,
            "game_time" = ?,
            "game_datetime" = ?,
            "game_time_zone" = ?,
            "game_datetime_utc" = ?,
            "game_day_of_week" = ?,
            "game_nation" = ?,
            "game_state" = ?,
            "away_team_abv" = ?,
            "home_team_abv" = ?,
            "nflverse_old_game_id" = ?,
            "gsis_id" = ?,
            "pfr_game_id" = ?,
            "pff_game_id" = ?,
            "espn_game_id" = ?,
            "ftn_game_id" = ?,
            "ncaa_game_id" = ?,
            "football_db_game_id" = ?,
            "arenafan_game_id" = ?,
            "yahoo_game_id" = ?,
            "is_neutral_site_game" = ?,
            "is_divisional_game" = ?,
            "game_roof" = ?,
            "surface" = ?,
            "temp_f" = ?,
            "temp_c" = ?,
            "wind" = ?,
            "stadium_id" = ?
        WHERE "nflverse_game_id" = ?;
        """
        self.sqlite3_cur.executemany(
            sql_script,
            [(
                self.game_type,
                self.week,
                self.game_day,
                self.game_time,
                self.game_datetime,
                self.game_timezone,
                self.game_datetime_utc,
                self.game_day_of_week,
                self.game_nation,
                self.game_state,
                self.away_team_abv,
                self.home_team_abv,
                self.nflverse_old_game_id,
                self.gsis_id,
                self.pfr_game_id,
                self.pff_game_id,
                self.espn_game_id,
                self.ftn_game_id,
                self.ncaa_game_id,
                self.football_db_game_id,
                self.arenafan_game_id,
                self.yahoo_game_id,
                self.is_neutral_site_game,
                self.is_divisional_game,
                self.game_roof,
                self.surface,
                self.temp_f,
                self.temp_c,
                self.wind,
                self.stadium_id,

                self.nflverse_game_id,

            )]
        )
        self.sqlite3_con.commit()

    def new_game_view(self):
        """ """
        sg.theme(self.app_theme)

        game_info_layout = [
            [
                sg.Text("Week:\t\t"),
                sg.Combo(
                    default_value=self.week,
                    values=self.weeks_arr,
                    size=(8, 1),
                    readonly=True,
                    enable_events=True,
                    key="-GAME_WEEK-",
                ),
                sg.Push(),
                sg.Text("Game Type:\t"),
                sg.Combo(
                    default_value=self.game_type,
                    values=self.game_types_arr,
                    size=(8, 1),
                    readonly=True,
                    enable_events=True,
                    key="-GAME_TYPE-",
                ),

            ],
            [
                sg.Text("Away Team:\t"),
                sg.Combo(
                    values=self.teams_arr,
                    default_value=self.away_team_abv,
                    size=(8, 1),
                    readonly=True,
                    enable_events=True,
                    key="-AWAY_TEAM-",
                ),
                sg.Push(),
                sg.Text("Home Team:\t"),
                sg.Combo(
                    values=self.teams_arr,
                    default_value=self.home_team_abv,
                    size=(8, 1),
                    readonly=True,
                    enable_events=True,
                    key="-HOME_TEAM-",
                ),
            ],
            [
                sg.Text("Game Date:\t"),
                # Yes, this is a hack.
                # No, I do not like this hack.
                sg.In(key="-GAME_DATE-", enable_events=True, visible=False),
                # Seriously, why can't a successful press and use
                # of a calendar button not register an event?
                sg.CalendarButton(
                    "Select Date",
                    # close_when_date_chosen=True,
                    enable_events=True,
                    # disabled=True,
                    no_titlebar=False,
                    default_date_m_d_y=(7, 1, self.season),
                    target="-GAME_DATE-",
                    format="%Y-%m-%d",
                    key="-GAME_DATE_BUTTON-",
                ),
                sg.Text(
                    text=self.game_day,
                    size=(20, 1),
                    enable_events=True,
                    key="-GAME_DATE_TEXT-",
                ),
            ],
            [
                sg.Text("Game Time:\t"),
                sg.Checkbox(
                    text="24 Hour Time?",
                    key="-IS_24_HOUR_TIME-",
                    enable_events=True
                ),
                sg.Combo(
                    self.hours_12_arr,
                    disabled=False,
                    default_value=self.hour_12_num,
                    # warp=True,
                    # background_color="white",
                    visible=True,
                    readonly=True,
                    enable_events=True,
                    size=(5, 1),
                    key="-GAME_TIME_HOURS_12-",
                ),
                sg.Combo(
                    self.hours_24_arr,
                    default_value=self.hour_24_num,
                    # background_color="gray",
                    enable_events=True,
                    readonly=True,
                    # warp=True,
                    visible=False,
                    size=(5, 1),
                    key="-GAME_TIME_HOURS_24-",
                ),
                sg.Combo(
                    self.minutes_arr,
                    default_value=self.minute_num,
                    readonly=True,
                    enable_events=True,
                    # warp=True,
                    size=(5, 1),
                    key="-GAME_MINUTES-",
                ),
                sg.Combo(
                    values=["AM", "PM"],
                    default_value="PM",
                    readonly=True,
                    enable_events=True,
                    size=(5, 1),
                    key="-AM_PM-",
                ),
            ],
            [
                sg.Text("Playing Surface:\t"),
                sg.Combo(
                    values=self.surface_arr,
                    default_value="Natural Grass",
                    readonly=True,
                    enable_events=True,
                    size=(15, 1),
                    key="-GAME_SURFACE-",
                ),
                sg.Push(),
                sg.Text("Game Roof:\t"),
                sg.Combo(
                    values=self.game_roof_arr,
                    default_value=self.game_roof_arr[0],
                    size=(8, 1),
                    key="-GAME_ROOF-",
                ),
            ],
            [
                sg.Text("Temperature (F°):\t", visible=True),
                sg.Text("Temperature (C°):\t", visible=False),
                sg.Combo(
                    values=self.temp_f_arr,
                    default_value=int(self.temp_f),
                    readonly=True,
                    visible=True,
                    enable_events=True,
                    size=(5, 1),
                    key="-TEMP_F-",
                ),
                sg.Combo(
                    values=self.temp_c_arr,
                    default_value=int(self.temp_c),
                    readonly=True,
                    visible=False,
                    enable_events=True,
                    size=(5, 1),
                    key="-TEMP_F-",
                ),
            ],
            [
                sg.Text("Game State:\t"),
                sg.Combo(
                    values=self.show_states_arr,
                    default_value=self.show_state,
                    readonly=True,
                    enable_events=True,
                    size=(38, 1),
                    key="-GAME_STATE-",
                )
            ],
            [
                sg.Text("Game Nation:\t"),
                sg.Combo(
                    values=self.show_nations_arr,
                    default_value=self.show_nation,
                    readonly=True,
                    enable_events=True,
                    size=(38, 1),
                    key="-GAME_NATION-",
                )
            ],
            [
                sg.Text("Time Zone:\t"),
                sg.Combo(
                    values=self.show_timezones_arr,
                    default_value=self.game_timezone,
                    readonly=True,
                    enable_events=True,
                    size=(38, 1),
                    key="-TIMEZONE-",
                )
            ],
            [
                sg.Text("Is this a neutral site game?\t"),
                sg.Checkbox(
                    text=" ",
                    key="-IS_NEUTRAL_GAME-",
                    enable_events=True,
                ),
            ],
            [
                sg.Text("Is this a divisional game?\t"),
                sg.Checkbox(
                    text="",
                    key="-IS_DIVISIONAL_GAME-",
                    enable_events=True,
                ),
            ],
        ]

        game_ids_layout = [
            [
                sg.Text("NFL Old Game ID:\t\t\t"),
                sg.Input(
                    default_text=self.nflverse_old_game_id,
                    size=(25, 1),
                    enable_events=True,
                    key="-NFLVERSE_OLD_GAME_ID-"
                )
            ],
            [
                sg.Text("GSIS Game ID:\t\t\t"),
                sg.Input(
                    default_text=self.gsis_id,
                    size=(25, 1),
                    enable_events=True,
                    key="-GSIS_GAME_ID-"
                ),
            ],
            [
                sg.Text("Pro Football Reference Game ID:\t"),
                sg.Input(
                    default_text=self.pfr_game_id,
                    size=(25, 1),
                    enable_events=True,
                    key="-PFR_GAME_ID-"
                ),
            ],
            [
                sg.Text("PFF Game ID:\t\t\t"),
                sg.Input(
                    default_text=self.pff_game_id,
                    size=(25, 1),
                    enable_events=True,
                    key="-PFF_GAME_ID-"
                ),
            ],
            [
                sg.Text("ESPN Game ID:\t\t\t"),
                sg.Input(
                    default_text=self.espn_game_id,
                    size=(25, 1),
                    enable_events=True,
                    key="-ESPN_GAME_ID-"
                ),
            ],
            [
                sg.Text("FTN Game ID:\t\t\t"),
                sg.Input(
                    default_text=self.ftn_game_id,
                    size=(25, 1),
                    enable_events=True,
                    key="-FTN_GAME_ID-"
                ),
            ],
            [
                sg.Text("stats.ncaa.com Game ID:\t\t"),
                sg.Input(
                    default_text=self.ncaa_game_id,
                    size=(25, 1),
                    enable_events=True,
                    key="-NCAA_GAME_ID-"
                ),
            ],
            [
                sg.Text("ArenaFan Game ID:\t\t"),
                sg.Input(
                    default_text=self.arenafan_game_id,
                    size=(25, 1),
                    enable_events=True,
                    key="-ARENAFAN_GAME_ID-"
                ),
            ],
            [
                sg.Text("footballdb.com Game ID:\t\t"),
                sg.Input(
                    default_text=self.football_db_game_id,
                    size=(25, 1),
                    enable_events=True,
                    key="-FOOTBALL_DB_GAME_ID-"
                ),
            ],
            [
                sg.Text("Yahoo Game ID:\t\t\t"),
                sg.Input(
                    default_text=self.yahoo_game_id,
                    size=(25, 1),
                    enable_events=True,
                    key="-YAHOO_DB_GAME_ID-"
                ),
            ],
        ]

        layout = [
            [
                sg.Text(
                    "Edit Game",
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
                    [
                        [
                            sg.Tab("Game Info", game_info_layout),
                            sg.Tab("Game IDs", game_ids_layout),
                        ]
                    ]
                )
            ],
            [
                sg.Button(
                    "Save Game",
                    expand_x=True,
                    key="-SAVE_GAME_BUTTON-"
                )
            ],
        ]

        window = sg.Window(
            "Edit Game..",
            layout=layout,
            # size=(500, 600),
            resizable=False,
            finalize=True,
            keep_on_top=False,
        )
        window["-IS_DIVISIONAL_GAME-"].update(
            value=self.is_divisional_game
        )
        window["-IS_NEUTRAL_GAME-"].update(
            value=self.is_neutral_site_game
        )

        keep_open = True
        while keep_open is True:
            event, values = window.read(timeout=1000)
            print(values)
            print(event)
            print(self.surface)
            # print(self.game_day, self.game_time)
            # print(self.game_nation, self.show_nation)
            # print(self.game_state, self.show_state)
            # print(self.is_24_hour_time)
            print(self.is_divisional_game, self.is_neutral_site_game)
            if event in (sg.WIN_CLOSED, "Exit"):
                keep_open = False

            match event:
                case "__TIMEOUT__":
                    # "__TIMEOUT__" = Nothing happened
                    # If we're doing nothing,
                    # pass and move on
                    pass
                case "-SAVE_GAME_BUTTON-":
                    check_flag = self.game_validation_check()
                    # print(check_flag)
                    if check_flag is True:
                        self.update_game()
                        keep_open = False
                    elif check_flag is False:
                        pass
                    del check_flag
                case "-GAME_WEEK-":
                    self.week = values["-GAME_WEEK-"]
                case "-AWAY_TEAM-":
                    self.away_team_abv = values["-AWAY_TEAM-"]
                case "-HOME_TEAM-":
                    self.home_team_abv = values["-HOME_TEAM-"]
                case "-GAME_TYPE-":
                    self.game_type = values["-GAME_TYPE-"]
                case "-GAME_DATE-":
                    self.game_day = values["-GAME_DATE-"]
                    window["-GAME_DATE_TEXT-"].update(
                        self.game_day
                    )
                case "-GAME_TIME_HOURS_12-":
                    self.hour_12_num = int(values["-GAME_TIME_HOURS_12-"])
                    if values["-AM_PM-"] == "PM":
                        self.hour_24_num = self.hour_12_num + 12
                    elif values["-AM_PM-"] == "AM" and self.hour_12_num == 12:
                        self.hour_24_num = 0
                    else:
                        self.hour_24_num = self.hour_12_num
                    self.game_time = f"{self.hour_24_num}:{self.minute_num}"
                case "-GAME_TIME_HOURS_24-":
                    self.hour_24_num = int(values["-GAME_TIME_HOURS_24-"])
                    if self.hour_24_num == 0:
                        self.hour_12_num = 12
                        window["-AM_PM-"].update(
                            value="AM"
                        )
                    elif self.hour_24_num > 12:
                        self.hour_12_num = self.hour_24_num - 12
                        window["-AM_PM-"].update(
                            value="PM"
                        )
                    else:
                        self.hour_12_num = self.hour_24_num
                        window["-AM_PM-"].update(
                            value="AM"
                        )
                    self.game_time = f"{self.hour_24_num}:{self.minute_num}"
                case "-GAME_MINUTES-":
                    self.minute_num = values["-GAME_MINUTES-"]
                case "-IS_24_HOUR_TIME-":
                    self.is_24_hour_time = values["-IS_24_HOUR_TIME-"]
                    if self.is_24_hour_time is True:
                        window["-GAME_MINUTES-"].update(
                            visible=False
                        )
                        window["-GAME_TIME_HOURS_12-"].update(
                            value=self.hour_12_num,
                            visible=False
                        )
                        window["-GAME_TIME_HOURS_24-"].update(
                            value=self.hour_24_num,
                            visible=True
                        )
                        window["-GAME_MINUTES-"].update(
                            visible=True
                        )
                        window["-AM_PM-"].update(
                            visible=False
                        )
                    elif self.is_24_hour_time is False:

                        window["-GAME_MINUTES-"].update(
                            visible=False
                        )
                        window["-GAME_TIME_HOURS_24-"].update(
                            value=self.hour_24_num,
                            visible=False
                        )
                        window["-GAME_TIME_HOURS_12-"].update(
                            value=self.hour_12_num,
                            visible=True
                        )
                        window["-GAME_MINUTES-"].update(
                            visible=True
                        )
                        window["-AM_PM-"].update(
                            visible=True
                        )
                case "-IS_NEUTRAL_GAME-":
                    self.is_neutral_site_game = values["-IS_NEUTRAL_GAME-"]
                case "-IS_DIVISIONAL_GAME-":
                    self.is_divisional_game = values["-IS_DIVISIONAL_GAME-"]
                case "-GAME_SURFACE-":
                    check = values["-GAME_SURFACE-"]
                    self.surface = self.surface_dict[check]
                case "-GAME_ROOF-":
                    self.game_roof = values["-GAME_ROOF-"]
                case "-TEMP_F-":
                    self.temp_f = int(values["-TEMP_F-"])
                    self.temp_c = int(
                        (self.temp_f - 32) / (9/5)
                    )
                case "-TEMP_C-":
                    self.temp_c = int(values["-TEMP_C-"])
                    self.temp_f = int(
                        (self.temp_f * (9/5)) + 32
                    )
                case "-GAME_STATE-":
                    self.show_state = values["-GAME_STATE-"]
                    self.search_iso_state()
                case "-GAME_NATION-":
                    self.show_nation = values["-GAME_NATION-"]
                    self.search_iso_nation()
                    self.refresh_iso_states(
                        iso_2_nation=self.game_nation
                    )
                    window["-GAME_STATE-"].update(
                        values=self.show_states_arr,
                        value=self.show_states_arr[0]
                    )
                case "-TIMEZONE-":
                    self.game_timezone = values["-TIMEZONE-"]
                case "-NFLVERSE_OLD_GAME_ID-":
                    # nflverse old game ID check
                    if event == "-NFLVERSE_OLD_GAME_ID-" \
                            and len(
                                str(values["-NFLVERSE_OLD_GAME_ID-"])
                            ) > 10:
                        window["-NFLVERSE_OLD_GAME_ID-"].update(
                            str(values["-NFLVERSE_OLD_GAME_ID-"])[:-1]
                        )
                    elif event == "-NFLVERSE_OLD_GAME_ID-" and (
                        str(values["-NFLVERSE_OLD_GAME_ID-"]) and
                        str(values["-NFLVERSE_OLD_GAME_ID-"])[-1] not in (
                            self.numbers_all
                        )
                    ):
                        window["-NFLVERSE_OLD_GAME_ID-"].update(
                            str(values["-NFLVERSE_OLD_GAME_ID-"])[:-1]
                        )
                        self.nflverse_old_game_id = values[
                            "-NFLVERSE_OLD_GAME_ID-"
                        ]
                    elif event == "-NFLVERSE_OLD_GAME_ID-" and (
                        values["-NFLVERSE_OLD_GAME_ID-"] and
                        str(values["-NFLVERSE_OLD_GAME_ID-"])[-1] in (
                            self.numbers_all
                        )
                    ):
                        window["-NFLVERSE_OLD_GAME_ID-"].update(
                            values["-NFLVERSE_OLD_GAME_ID-"]
                        )
                        self.nflverse_old_game_id = values[
                            "-NFLVERSE_OLD_GAME_ID-"
                        ]
                case "-GSIS_GAME_ID-":
                    # GSIS game ID check
                    if event == "-GSIS_GAME_ID-" \
                            and len(values["-GSIS_GAME_ID-"]) > 5:
                        window["-GSIS_GAME_ID-"].update(
                            values["-GSIS_GAME_ID-"][:-1]
                        )
                    elif event == "-GSIS_GAME_ID-" and (
                        values["-GSIS_GAME_ID-"] and
                        values["-GSIS_GAME_ID-"][-1] not in (
                            self.numbers_all
                        )
                    ):
                        window["-GSIS_GAME_ID-"].update(
                            values["-GSIS_GAME_ID-"][:-1]
                        )
                        self.gsis_id = values["-GSIS_GAME_ID-"]
                    elif event == "-GSIS_GAME_ID-" and (
                        values["-GSIS_GAME_ID-"] and
                        values["-GSIS_GAME_ID-"][-1] in (
                            self.numbers_all
                        )
                    ):
                        window["-GSIS_GAME_ID-"].update(
                            values["-GSIS_GAME_ID-"].upper()
                        )
                        self.gsis_id = values["-GSIS_GAME_ID-"]
                case "-PFR_GAME_ID-":
                    # Pro Football Reference game ID check
                    if event == "-PFR_GAME_ID-" \
                            and len(values["-PFR_GAME_ID-"]) > 12:
                        window["-PFR_GAME_ID-"].update(
                            values["-PFR_GAME_ID-"][:-1]
                        )
                    elif event == "-PFR_GAME_ID-" and (
                        values["-PFR_GAME_ID-"] and
                        values["-PFR_GAME_ID-"][-1] not in (
                            self.letters_and_numbers
                        )
                    ):
                        window["-PFR_GAME_ID-"].update(
                            values["-PFR_GAME_ID-"][:-1]
                        )
                        self.pfr_game_id = values["-PFR_GAME_ID-"]
                    elif event == "-PFR_GAME_ID-" and (
                        values["-PFR_GAME_ID-"] and
                        values["-PFR_GAME_ID-"][-1] in (
                            self.letters_and_numbers
                        )
                    ):
                        window["-PFR_GAME_ID-"].update(
                            values["-PFR_GAME_ID-"]
                        )
                        self.pfr_game_id = values["-PFR_GAME_ID-"]
                case "-PFF_GAME_ID-":
                    # Pro Football Reference game ID check
                    if event == "-PFF_GAME_ID-" \
                            and len(values["-PFF_GAME_ID-"]) > 5:
                        window["-PFF_GAME_ID-"].update(
                            values["-PFF_GAME_ID-"][:-1]
                        )
                    elif event == "-PFF_GAME_ID-" and (
                        values["-PFF_GAME_ID-"] and
                        values["-PFF_GAME_ID-"][-1] not in (
                            self.numbers_all
                        )
                    ):
                        window["-PFF_GAME_ID-"].update(
                            values["-PFF_GAME_ID-"][:-1]
                        )
                        self.pff_game_id = values["-PFF_GAME_ID-"]
                    elif event == "-PFF_GAME_ID-" and (
                        values["-PFF_GAME_ID-"] and
                        values["-PFF_GAME_ID-"][-1] in (
                            self.numbers_all
                        )
                    ):
                        window["-PFF_GAME_ID-"].update(
                            values["-PFF_GAME_ID-"].upper()
                        )
                        self.pff_game_id = values["-PFF_GAME_ID-"]
                case "-ESPN_GAME_ID-":
                    # Pro Football Reference game ID check
                    if event == "-ESPN_GAME_ID-" \
                            and len(values["-ESPN_GAME_ID-"]) > 9:
                        window["-ESPN_GAME_ID-"].update(
                            values["-ESPN_GAME_ID-"][:-1]
                        )
                    elif event == "-ESPN_GAME_ID-" and (
                        values["-ESPN_GAME_ID-"] and
                        values["-ESPN_GAME_ID-"][-1] not in (
                            self.numbers_all
                        )
                    ):
                        window["-ESPN_GAME_ID-"].update(
                            values["-ESPN_GAME_ID-"][:-1]
                        )
                        self.espn_game_id = values["-ESPN_GAME_ID-"]
                    elif event == "-ESPN_GAME_ID-" and (
                        values["-ESPN_GAME_ID-"] and
                        values["-ESPN_GAME_ID-"][-1] in (
                            self.numbers_all
                        )
                    ):
                        window["-ESPN_GAME_ID-"].update(
                            values["-ESPN_GAME_ID-"].upper()
                        )
                        self.espn_game_id = values["-ESPN_GAME_ID-"]
                case "-FTN_GAME_ID-":
                    # FTN game ID check
                    if event == "-FTN_GAME_ID-" \
                            and len(values["-FTN_GAME_ID-"]) > 4:
                        window["-FTN_GAME_ID-"].update(
                            values["-FTN_GAME_ID-"][:-1]
                        )
                    elif event == "-FTN_GAME_ID-" and (
                        values["-FTN_GAME_ID-"] and
                        values["-FTN_GAME_ID-"][-1] not in (
                            self.numbers_all
                        )
                    ):
                        window["-FTN_GAME_ID-"].update(
                            values["-FTN_GAME_ID-"][:-1]
                        )
                        self.ftn_game_id = values["-FTN_GAME_ID-"]
                    elif event == "-FTN_GAME_ID-" and (
                        values["-FTN_GAME_ID-"] and
                        values["-FTN_GAME_ID-"][-1] in (
                            self.numbers_all
                        )
                    ):
                        window["-FTN_GAME_ID-"].update(
                            values["-FTN_GAME_ID-"].upper()
                        )
                        self.ftn_game_id = values["-FTN_GAME_ID-"]
                case "-NCAA_GAME_ID-":
                    # NCAA game ID check
                    if event == "-NCAA_GAME_ID-" \
                            and len(values["-NCAA_GAME_ID-"]) > 7:
                        window["-NCAA_GAME_ID-"].update(
                            values["-NCAA_GAME_ID-"][:-1]
                        )
                    elif event == "-NCAA_GAME_ID-" and (
                        values["-NCAA_GAME_ID-"] and
                        values["-NCAA_GAME_ID-"][-1] not in (
                            self.numbers_all
                        )
                    ):
                        window["-NCAA_GAME_ID-"].update(
                            values["-NCAA_GAME_ID-"][:-1]
                        )
                        self.ncaa_game_id = values["-NCAA_GAME_ID-"]
                    elif event == "-NCAA_GAME_ID-" and (
                        values["-NCAA_GAME_ID-"] and
                        values["-NCAA_GAME_ID-"][-1] in (
                            self.numbers_all
                        )
                    ):
                        window["-NCAA_GAME_ID-"].update(
                            values["-NCAA_GAME_ID-"].upper()
                        )
                        self.ncaa_game_id = values["-NCAA_GAME_ID-"]
                case "-ARENAFAN_GAME_ID-":
                    # ArenaFan game ID check
                    if event == "-ARENAFAN_GAME_ID-" \
                            and len(values["-ARENAFAN_GAME_ID-"]) > 5:
                        window["-ARENAFAN_GAME_ID-"].update(
                            values["-ARENAFAN_GAME_ID-"][:-1]
                        )
                    elif event == "-ARENAFAN_GAME_ID-" and (
                        values["-ARENAFAN_GAME_ID-"] and
                        values["-ARENAFAN_GAME_ID-"][-1] not in (
                            self.numbers_all
                        )
                    ):
                        window["-ARENAFAN_GAME_ID-"].update(
                            values["-ARENAFAN_GAME_ID-"][:-1]
                        )
                        self.arenafan_game_id = values["-ARENAFAN_GAME_ID-"]
                    elif event == "-ARENAFAN_GAME_ID-" and (
                        values["-ARENAFAN_GAME_ID-"] and
                        values["-ARENAFAN_GAME_ID-"][-1] in (
                            self.numbers_all
                        )
                    ):
                        window["-ARENAFAN_GAME_ID-"].update(
                            values["-ARENAFAN_GAME_ID-"].upper()
                        )
                        self.arenafan_game_id = values["-ARENAFAN_GAME_ID-"]
                case "-FOOTBALL_DB_GAME_ID-":
                    # footballdb.com game ID check
                    if event == "-FOOTBALL_DB_GAME_ID-" and (
                        values["-FOOTBALL_DB_GAME_ID-"] and
                        values["-FOOTBALL_DB_GAME_ID-"][-1] not in (
                            self.letters_and_numbers_spec
                        )
                    ):
                        window["-FOOTBALL_DB_GAME_ID-"].update(
                            values["-FOOTBALL_DB_GAME_ID-"][:-1]
                        )
                        self.football_db_game_id = values[
                            "-FOOTBALL_DB_GAME_ID-"
                        ]
                    elif event == "-FOOTBALL_DB_GAME_ID-" and (
                        values["-FOOTBALL_DB_GAME_ID-"] and
                        values["-FOOTBALL_DB_GAME_ID-"][-1] in (
                            self.letters_and_numbers_spec
                        )
                    ):
                        window["-FOOTBALL_DB_GAME_ID-"].update(
                            values["-FOOTBALL_DB_GAME_ID-"]
                        )
                        self.football_db_game_id = values[
                            "-FOOTBALL_DB_GAME_ID-"
                        ]
                case "-YAHOO_DB_GAME_ID-":
                    # yahoo.com game ID check
                    # if event == "-YAHOO_DB_GAME_ID-" \
                    #         and len(values["-YAHOO_DB_GAME_ID-"]) > 5:
                    #     window["-YAHOO_DB_GAME_ID-"].update(
                    #         values["-YAHOO_DB_GAME_ID-"][:-1]
                    #     )
                    # elif event == "-YAHOO_DB_GAME_ID-" and (
                    if event == "-YAHOO_DB_GAME_ID-" and (
                        values["-YAHOO_DB_GAME_ID-"] and
                        values["-YAHOO_DB_GAME_ID-"][-1] not in (
                            self.letters_and_numbers_spec
                        )
                    ):
                        window["-YAHOO_DB_GAME_ID-"].update(
                            values["-YAHOO_DB_GAME_ID-"][:-1]
                        )
                        self.yahoo_game_id = values[
                            "-YAHOO_DB_GAME_ID-"
                        ]
                    elif event == "-YAHOO_DB_GAME_ID-" and (
                        values["-YAHOO_DB_GAME_ID-"] and
                        values["-YAHOO_DB_GAME_ID-"][-1] in (
                            self.letters_and_numbers_spec
                        )
                    ):
                        window["-YAHOO_DB_GAME_ID-"].update(
                            values["-YAHOO_DB_GAME_ID-"]
                        )
                        self.yahoo_game_id = values[
                            "-YAHOO_DB_GAME_ID-"
                        ]
                case _:
                    pass

        window.close()
