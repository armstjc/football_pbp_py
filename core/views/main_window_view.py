"""
- Creation Date: 01/27/2024 12:00 PM EST
- Last Updated: 05/25/2024 09:45 PM EDT
- Authors: Joseph Armstrong (armstrongjoseph08@gmail.com)
- file: `./core/views/main_window_view.py`
- Purpose: Main startup window for this application.
"""

from os.path import expanduser

# from threading import Thread
import polars as pl
import PySimpleGUI as sg

from core.database.load_db_elements import SqliteLoadData
from core.database.sqlite3_connectors import initialize_sqlite3_connectors
from core.other.embedded import EmbeddedElements
from core.settings.settings_core import AppSettings
from core.views.about_view import about_view
from core.views.edit_league_view import LeagueView, new_league_view
from core.views.edit_season_view import SeasonView, new_season_view
from core.views.edit_team_view import NewTeamView, TeamView
from core.views.settings_view import SettingsWindow


class MainWindow:
    """ """

    # sqlite3 connectors
    sqlite3_con = None
    sqlite3_cur = None

    # defaults
    settings_dict = {}
    sql_engine_type = "sqlite3"
    app_theme = "DarkBlue"
    home_dir = expanduser("~")
    default_data_directory = f"{home_dir}/.sdv_pbp_fb/"

    # polars dataframes
    iso_nations_df = None
    iso_states_df = None
    iso_timezones_df = None
    fb_leagues_df = None
    fb_seasons_df = None
    fb_teams_df = None
    fb_stadiums_df = None
    fb_schedule_df = None
    fb_game_refs = None

    shown_schedule_df = None

    # Settings
    app_settings = AppSettings()

    # Leagues
    leagues_list = [None]
    default_league = None

    # Seasons
    league_seasons = [None]
    default_season = None

    # Weeks
    league_weeks = [None]
    default_week = 1

    # Teams
    league_teams = [None]
    default_team = None

    def __init__(self):
        self.app_startup()

    def app_startup(self):
        """
        """

        # Set app defaults
        self.load_settings()
        self.set_settings()
        # Get SQLite3 connections
        self.sqlite3_con, self.sqlite3_cur = initialize_sqlite3_connectors()

        # Load dataframes
        self.iso_nations_df = SqliteLoadData.load_iso_nations(
            con=self.sqlite3_con, cur=self.sqlite3_cur
        )
        self.iso_states_df = SqliteLoadData.load_iso_states(
            self.sqlite3_con, self.sqlite3_cur
        )
        self.iso_timezones_df = SqliteLoadData.load_iso_timezones(
            self.sqlite3_con, self.sqlite3_cur
        )
        self.fb_leagues_df = SqliteLoadData.load_leagues(
            self.sqlite3_con, self.sqlite3_cur
        )
        self.fb_seasons_df = SqliteLoadData.load_seasons(
            self.sqlite3_con, self.sqlite3_cur
        )
        self.fb_seasons_df = self.fb_seasons_df.sort(
            ["league_id", "season"],
        )
        self.fb_stadiums_df = SqliteLoadData.load_fb_stadiums(
            self.sqlite3_con, self.sqlite3_cur
        )
        self.fb_game_refs = SqliteLoadData.load_fb_game_refs(
            self.sqlite3_con, self.sqlite3_cur
        )

        self.refresh_leagues()
        self.refresh_league_weeks()
        self.refresh_league_seasons(league=self.default_league)

        self.shown_schedule_df = self.fb_schedule_df.filter(
            (pl.col("league_id") == self.default_league)
            & (pl.col("season") == self.default_season)
        )
        self.clean_shown_schedule_df()
        self.refresh_league_teams(
            lg_abv=self.default_league, lg_season=self.default_season
        )
        self.main()

    def load_settings(self) -> None:
        # Load in settings file
        self.settings_dict = self.app_settings.load_settings()
        self.set_settings()

    # Data Manipulation
    def set_settings(self) -> None:
        """ """

        self.default_league = self.settings_dict["defaults"]["default_league"]
        self.default_season = self.settings_dict["defaults"]["default_season"]
        self.default_team = self.settings_dict["defaults"]["default_team"]
        self.app_theme = self.settings_dict["app_theme"]

    def clean_shown_schedule_df(self) -> None:
        """ """
        self.shown_schedule_df = self.shown_schedule_df[
            [
                "nflverse_game_id",
                "game_type",
                "week",
                "game_day",
                "away_team_abv",
                "home_team_abv",
                "away_team_score",
                "home_team_score",
                "game_is_finished",
            ]
        ]

    def filter_shown_schedule_df(
        self,
        lg_abv: str,
        lg_season: int,
        team_abv: str = None
    ) -> None:
        """ """
        self.shown_schedule_df = self.fb_schedule_df.filter(
            (pl.col("league_id") == lg_abv) & (pl.col("season") == lg_season)
        )
        if team_abv == "-ALL-":
            pass
        elif (team_abv is not None):
            self.shown_schedule_df = self.shown_schedule_df.filter(
                (pl.col("away_team_abv") == team_abv) | (pl.col("home_team_abv") == team_abv)
            )
        self.shown_schedule_df = self.shown_schedule_df.sort(
            "nflverse_game_id"
        )
        self.clean_shown_schedule_df()

    def refresh_league_weeks(self):
        self.fb_schedule_df = SqliteLoadData.load_fb_schedule(
            self.sqlite3_con, self.sqlite3_cur
        )
        self.league_weeks = self.fb_schedule_df["week"].to_list()

        # In the case there's no games in this league,
        # add a "Week 1" to the weeks list.
        # If there is a week 1, this move gets negated by the
        # `set()` function.
        self.league_weeks.append(1)

        self.league_weeks = list(set(self.league_weeks))
        self.league_weeks.sort()

    def refresh_league_teams(self, lg_abv: str, lg_season: int):
        """ """
        self.fb_teams_df = SqliteLoadData.load_fb_teams(
            self.sqlite3_con, self.sqlite3_cur
        )
        temp_league_teams = self.fb_teams_df.filter(
            (pl.col("season") == lg_season) & (pl.col("league_id") == lg_abv)
        )
        self.league_teams = temp_league_teams["team_id"].to_list()
        self.league_teams.append("-ALL-")
        set(self.league_teams)
        self.league_teams.sort()

    def refresh_leagues(self):
        """
        """
        self.fb_leagues_df = SqliteLoadData.load_leagues(
            self.sqlite3_con, self.sqlite3_cur
        )
        self.leagues_list = self.fb_leagues_df["league_id"].to_list()

        set(self.leagues_list)
        self.leagues_list.sort()

    def refresh_league_seasons(self, league: str):
        self.fb_seasons_df = SqliteLoadData.load_seasons(
            self.sqlite3_con, self.sqlite3_cur
        )
        self.league_seasons = self.fb_seasons_df.filter(
            pl.col("league_id") == league
        )["season"].to_list()
        self.league_seasons.sort()

    def main(self):
        """ """

        sg.theme(self.app_theme)
        # sg.theme("DarkBlack")
        menu_bar = [
            [
                "File",
                [
                    "New Game",
                    # "Load Game",
                    "Import Game",
                    "---",
                    "Print Game",
                    "Print Season",
                    "---",
                    "Export Game",
                    "Export Season",
                    "Export Team",
                    "---",
                    "Exit",
                ],
            ],
            [
                "New",
                [
                    "New League",
                    "New Season",
                    "New Team",
                    "New Game",
                    "New Player"
                ]
            ],
            # [
            #     "test",
            #     [
            #         "stets"
            #     ]
            # ],
            [
                "Settings",
                [
                    "App Settings",
                    "---"
                ]
            ],
            [
                "Help",
                ["Documentation (Local)", "Documentation (Web)", "About"],
            ],
        ]

        game_sidebar_layout = [
            [
                sg.Text("League:\t"),
                sg.Combo(
                    values=self.leagues_list,
                    default_value=self.default_league,
                    size=(10, 1),
                    enable_events=True,
                    key="-LEAGUE_ABV_COMBO-",
                ),
                sg.Button(
                    "League Settings",
                    key="-LG_SETTINGS-",
                    tooltip="Settings/rules for the selected league.",
                    size=(15, 1)
                ),
                sg.Push(),
                # sg.Button("test")
            ],
            [
                sg.Text("Season:\t"),
                sg.Combo(
                    values=self.league_seasons,
                    default_value=self.default_season,
                    size=(10, 1),
                    enable_events=True,
                    key="-LEAGUE_SEASON_COMBO-",
                ),
                sg.Button(
                    "Season Settings",
                    key="-SEA_SETTINGS-",
                    size=(15, 1)
                ),
                sg.Push(),
            ],
            [
                sg.Text("Team:\t"),
                sg.Combo(
                    values=self.league_teams,
                    default_value=self.league_teams[0],
                    size=(10, 1),
                    # expand_x=True,
                    enable_events=True,
                    key="-TEAM_SEASON_COMBO-",
                ),
                sg.Button(
                    "Team Settings",
                    key="-TEAM_SETTINGS-",
                    disabled=True,
                    size=(15, 1)
                ),
                sg.Push(),
            ],
            [
                sg.Text("Week:\t"),
                sg.Combo(
                    values=self.league_weeks,
                    default_value=self.default_week,
                    size=(10, 1),
                    enable_events=True,
                    key="-WEEK_SEASON_COMBO-",
                ),
                sg.Push(),
            ],
            [
                sg.Button(
                    "New League", key="New League", expand_x=True
                )
            ],
            [
                sg.Button(
                    "New Season", key="New Season", expand_x=True
                )
            ],
            [
                sg.Button(
                    "New Team", key="New Team", expand_x=True
                )
            ],
            [
                sg.Button(
                    "New Game", key="New Game", expand_x=True
                )
            ],
            [
                sg.Button(
                    "Import Game",
                    key="-IMPORT_GAME_BUTTON-",
                    expand_x=True,
                    disabled=True,
                )
            ],
            [
                sg.Button(
                    "Edit Game",
                    key="-EDIT_GAME_BUTTON-",
                    expand_x=True,
                    disabled=True
                )
            ],
            [
                sg.Button(
                    "Start Game",
                    key="-START_GAME_BUTTON-",
                    expand_x=True,
                    disabled=True,
                )
            ],
        ]

        layout = [
            [sg.MenuBar(menu_bar, visible=True, key="-WINDOW_MENU-")],
            [],
            # [sg.Text("This is a test.")],
            [
                sg.Frame(
                    "Sidebar",
                    game_sidebar_layout,
                    expand_y=True,
                    expand_x=True,
                    size=300,
                    pad=0,
                    element_justification="top",
                ),
                sg.Table(
                    values=self.shown_schedule_df.rows(),
                    headings=[
                        "Game ID",
                        "Game Type",
                        "Week",
                        "Date",
                        "Away Team",
                        "Home Team",
                        "Away Score",
                        "Home Score",
                        "Finished?",
                    ],
                    expand_x=True,
                    expand_y=True,
                    key="-SCHEDULE_TABLE-",
                ),

            ],
        ]

        window = sg.Window(
            icon=EmbeddedElements.desktop_icon(),
            title="The SDV Football PBP App",
            size=(1280, 720),
            layout=layout,
            resizable=True,
            finalize=True
        )
        window.set_min_size(
            size=(1280, 720)
        )

        # window.TKroot.minsize(1024,600)
        keep_open = True
        while keep_open:
            event, values = window.read(timeout=1000)
            print(values)
            print(event)

            if event == sg.WIN_CLOSED or event == "Quit":
                break

            if values["-SCHEDULE_TABLE-"] != []:
                window["-START_GAME_BUTTON-"].update(disabled=False)
                window["-EDIT_GAME_BUTTON-"].update(disabled=False)
                # print(values["-SCHEDULE_TABLE-"][0])

            if values["-TEAM_SEASON_COMBO-"] == "-ALL-":
                window["-TEAM_SETTINGS-"].update(disabled=True)
            elif values["-TEAM_SEASON_COMBO-"] != "-ALL-":
                window["-TEAM_SETTINGS-"].update(disabled=False)

            match event:
                # File Menu
                case "About":
                    # print(EmbeddedElements.app_version())
                    about_view()
                case "Exit":
                    keep_open = False
                # File
                case "New Game":
                    print(event)
                # case "Load Game":
                #     print(event)
                case "Import Game":
                    print(event)
                case "Print Game":
                    print(event)
                case "Print Season":
                    print(event)
                case "Export Game":
                    print(event)
                case "Export Team":
                    print(event)
                case "Export Season":
                    print(event)
                case "Export League":
                    print(event)
                # New
                case "New League":
                    check = values["-LEAGUE_ABV_COMBO-"]
                    new_league_view(settings_json=self.settings_dict)
                    self.refresh_leagues()
                    window["-LEAGUE_ABV_COMBO-"].update(
                        values=self.leagues_list,
                        value=check
                    )
                    del check
                case "New Season":
                    check = values["-LEAGUE_SEASON_COMBO-"]
                    check2 = values["-LEAGUE_ABV_COMBO-"]
                    new_season_view(
                        settings_json=self.settings_dict,
                        league_id=values["-LEAGUE_ABV_COMBO-"]
                    )
                    self.refresh_league_seasons(league=check2)
                    window["-LEAGUE_SEASON_COMBO-"].update(
                        values=self.league_seasons,
                        value=check
                    )
                    del check, check2
                case "New Team":
                    # print(event)
                    check = values["-LEAGUE_ABV_COMBO-"]
                    check2 = values["-LEAGUE_SEASON_COMBO-"]
                    check3 = values["-TEAM_SEASON_COMBO-"]
                    NewTeamView(
                        settings_json=self.settings_dict,
                        league_id=values["-LEAGUE_ABV_COMBO-"],
                        season=check2
                    )
                    self.refresh_league_teams(
                        lg_abv=check,
                        lg_season=check2
                    )
                    window["-TEAM_SEASON_COMBO-"].update(
                        values=self.league_teams,
                        value=check3
                    )
                    del check, check2, check3
                case "New Game":
                    print(event)
                case "New Player":
                    print(event)
                # Settings
                case "App Settings":
                    SettingsWindow()
                # Help
                case "Documentation (Local)":
                    print(event)
                case "Documentation (Web)":
                    print(event)

                # Window Button events
                case "-LEAGUE_ABV_COMBO-":
                    self.refresh_league_seasons(
                        values["-LEAGUE_ABV_COMBO-"]
                    )
                    self.refresh_league_weeks()
                    self.refresh_league_teams(
                        lg_abv=values["-LEAGUE_ABV_COMBO-"],
                        lg_season=self.league_seasons[0]
                    )

                    window["-LEAGUE_SEASON_COMBO-"].update(
                        values=self.league_seasons,
                        value=self.league_seasons[0],
                    )
                    window["-WEEK_SEASON_COMBO-"].update(
                        values=self.league_weeks,
                        value=self.league_weeks[0],
                    )
                    window["-TEAM_SEASON_COMBO-"].update(
                        values=self.league_teams,
                        value=self.league_teams[0]
                    )
                    self.filter_shown_schedule_df(
                        lg_abv=values["-LEAGUE_ABV_COMBO-"],
                        lg_season=self.league_seasons[0]
                    )
                    window["-SCHEDULE_TABLE-"].update(
                        values=self.shown_schedule_df.rows()
                    )

                case "-LEAGUE_SEASON_COMBO-":
                    self.filter_shown_schedule_df(
                        values["-LEAGUE_ABV_COMBO-"],
                        values["-LEAGUE_SEASON_COMBO-"]
                    )
                    window["-SCHEDULE_TABLE-"].update(
                        values=self.shown_schedule_df.rows()
                    )
                case "-SEA_SETTINGS-":
                    SeasonView(
                        settings_json=self.settings_dict,
                        league_id=values["-LEAGUE_ABV_COMBO-"],
                        season=values["-LEAGUE_SEASON_COMBO-"]
                    )
                    self.filter_shown_schedule_df(
                        values["-LEAGUE_ABV_COMBO-"],
                        values["-LEAGUE_SEASON_COMBO-"]
                    )
                    window["-SCHEDULE_TABLE-"].update(
                        values=self.shown_schedule_df.rows()
                    )
                case "-LG_SETTINGS-":
                    # print(event)
                    check = values["-LEAGUE_ABV_COMBO-"]
                    LeagueView(
                        settings_json=self.settings_dict,
                        league_id=values["-LEAGUE_ABV_COMBO-"],

                    )

                    self.refresh_leagues()
                    # self.refresh_league_teams(values["-LEAGUE_ABV_COMBO-"])
                    window["-LEAGUE_ABV_COMBO-"].update(
                        values=self.leagues_list,
                        value=values["-LEAGUE_ABV_COMBO-"]
                    )
                    del check
                case "-TEAM_SETTINGS-":

                    check = values["-LEAGUE_ABV_COMBO-"]
                    check2 = values["-LEAGUE_SEASON_COMBO-"]
                    check3 = values["-TEAM_SEASON_COMBO-"]
                    TeamView(
                        settings_json=self.settings_dict,
                        league_id=values["-LEAGUE_ABV_COMBO-"],
                        season=check2,
                        team_id=check3
                    )
                    self.refresh_league_teams(
                        lg_abv=check,
                        lg_season=check2
                    )
                    window["-TEAM_SEASON_COMBO-"].update(
                        values=self.league_teams,
                        value=check3
                    )
                    del check, check2, check3
                case "-TEAM_SEASON_COMBO-":

                    self.filter_shown_schedule_df(
                        lg_abv=values["-LEAGUE_ABV_COMBO-"],
                        lg_season=values["-LEAGUE_SEASON_COMBO-"],
                        team_abv=values["-TEAM_SEASON_COMBO-"],
                    )
                    window["-SCHEDULE_TABLE-"].update(
                        values=self.shown_schedule_df.rows()
                    )
                case _:
                    pass

        window.close()


if __name__ == "__main__":
    MainWindow()
    # print(sg.theme_list())
