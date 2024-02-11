# Creation Date: 01/27/2024 12:00 PM EDT
# Last Updated: 02/11/2024 11:50 AM EST
# Authors: Joseph Armstrong (armstrongjoseph08@gmail.com)
# file: `./main_window.py`
# Purpose: Main startup window for this application.
################################################################################

from os.path import expanduser

import polars as pl
import PySimpleGUI as sg

from core.database.load_db_elements import sqlite3_load_data
from core.database.sqlite3_connectors import initialize_sqlite3_connectors
from core.settings.settings_core import app_settings
from resources.embeded import embeded_elements


class main_window:
    """ """

    # sqlite3 connectors
    sqlite3_con = None
    sqlite3_cur = None

    # defaults
    settings_dict = {}
    sql_engine_type = "sqlite3"
    app_theme = "DarkBlue"
    home_dir = expanduser("~")
    default_data_directory = f"{home_dir}/.sdv_pbp/"

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

    # Leagues
    leagues_list = [None]
    default_league = None

    # Seasons
    league_seasons = [None]
    defalt_season = None

    # Weeks
    league_weeks = [None]
    default_week = 1

    # Teams
    league_teams = [None]
    default_team = None

    def __init__(self):
        self.app_startup()


    
    def app_startup(self):
        # Load in settings file
        self.settings_dict = app_settings.load_settings()

        # Set app defaults
        self.set_settings()
        # Get SQLite3 connections
        self.sqlite3_con, self.sqlite3_cur = initialize_sqlite3_connectors()

        # Load dataframes
        self.iso_nations_df = sqlite3_load_data.load_iso_nations(
            self.sqlite3_con, self.sqlite3_cur
        )
        self.iso_states_df = sqlite3_load_data.load_iso_states(
            self.sqlite3_con, self.sqlite3_cur
        )
        self.iso_timezones_df = sqlite3_load_data.load_iso_timezones(
            self.sqlite3_con, self.sqlite3_cur
        )
        self.fb_leagues_df = sqlite3_load_data.load_leagues(
            self.sqlite3_con, self.sqlite3_cur
        )
        self.fb_seasons_df = sqlite3_load_data.load_seasons(
            self.sqlite3_con, self.sqlite3_cur
        )
        self.fb_stadiums_df = sqlite3_load_data.load_fb_stadiums(
            self.sqlite3_con, self.sqlite3_cur
        )
        self.fb_game_refs = sqlite3_load_data.load_fb_game_refs(
            self.sqlite3_con, self.sqlite3_cur
        )

        self.refresh_league_weeks()

        self.league_seasons = self.fb_seasons_df.filter(
            pl.col("league_id") == self.default_league
        )["season"].to_list()

        self.shown_schedule_df = self.fb_schedule_df.filter(
            (pl.col("league_id") == self.default_league)
            & (pl.col("season") == self.defalt_season)
        )
        self.clean_shown_schedule_df()
        self.refresh_league_teams(
            lg_abv=self.default_league,lg_season=self.defalt_season
        )
        self.main()
    
    ## Data Manipulation
    def set_settings(self) -> None:
        """ """
        self.default_league = self.settings_dict["defaults"]["default_league"]
        self.defalt_season = self.settings_dict["defaults"]["default_season"]
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

    def filter_shown_schedule_df(self, lg_abv: str, lg_season: int) -> None:
        """ """
        self.shown_schedule_df = self.fb_schedule_df.filter(
            (pl.col("league_id") == lg_abv) & (pl.col("season") == lg_season)
        )
        self.shown_schedule_df = self.shown_schedule_df.sort("nflverse_game_id")
        self.clean_shown_schedule_df()

    def refresh_league_weeks(self):
        self.fb_schedule_df = sqlite3_load_data.load_fb_schedule(
            self.sqlite3_con, self.sqlite3_cur
        )
        self.league_weeks = self.fb_schedule_df["week"].to_list()
        set(self.league_weeks)
        self.league_weeks.sort()

    def refresh_league_teams(self, lg_abv: str, lg_season: int):
        """ """
        self.fb_teams_df = sqlite3_load_data.load_fb_teams(
            self.sqlite3_con, self.sqlite3_cur
        )
        temp_league_teams = self.fb_teams_df.filter(
            (pl.col("season") == lg_season) & (pl.col("league_id") == lg_abv)
        )
        self.league_teams = temp_league_teams["team_id"].to_list()
        self.league_teams.append("-ALL-")
        set(self.league_teams)
        self.league_teams.sort()

    def main(self):
        """ """
        menu_bar = [
            [
                "File",
                [
                    "New Game",
                    "Load Game",
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
            ["New", ["New League", "New Season", "New Team", "New Game", "New Player"]],
            ["test", ["stets"]],
            [
                "Help",
                ["Documentation (Local)", "Docuemntation (Web)", "About"],
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
                sg.Button("League Settings", key="-LG_SETTINGS-", size=(15, 1)),
                # sg.Push(),
                # sg.Button("test")
            ],
            [
                sg.Text("Season:\t"),
                sg.Combo(
                    values=self.league_seasons,
                    default_value=self.defalt_season,
                    size=(10, 1),
                    enable_events=True,
                    key="-LEAGUE_SEASON_COMBO-",
                ),
                sg.Button("Season Settings", key="-SEA_SETTINGS-", size=(15, 1)),
            ],
            [
                sg.Text("Team:\t"),
                sg.Combo(
                    values=self.league_teams,
                    default_value=self.league_teams[0],
                    size=(10, 1),
                    expand_x=True,
                    enable_events=True,
                    key="-TEAM_SEASON_COMBO-",
                ),
                sg.Button("Team Settings", key="-TEAM_SETTINGS-", size=(15, 1)),
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
            ],
            [sg.Button("New Game", key="-NEW_GAME_BUTTON-", expand_x=True)],
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
                    "Edit Game", key="-EDIT_GAME_BUTTON-", expand_x=True, disabled=True
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
            [sg.Text("This is a test.")],
            [
                sg.Frame(
                    "test",
                    game_sidebar_layout,
                    expand_y=True,
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

        sg.theme(self.app_theme)
        window = sg.Window(
            icon=embeded_elements.desktop_icon(),
            title="The SDV Football PBP App",
            size=(1280, 720),
            layout=layout,
            resizable=True,
        )

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

            match event:
                # File Menu
                case "About":
                    print(embeded_elements.app_version())
                case "Exit":
                    keep_open = False
                ## File
                case "New Game":
                    print(event)
                case "Load Game":
                    print(event)
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
                ## New
                case "New League":
                    print(event)
                case "New Season":
                    print(event)
                case "New Team":
                    print(event)
                case "New Game":
                    print(event)
                case "New Player":
                    print(event)
                ## Help
                case "Documentation (Local)":
                    print(event)
                case "Docuemntation (Web)":
                    print(event)
                # Window Button events
                case "-LEAGUE_ABV_COMBO-":
                    print(event)
                case "-LEAGUE_SEASON_COMBO-":
                    self.filter_shown_schedule_df(
                        values["-LEAGUE_ABV_COMBO-"], values["-LEAGUE_SEASON_COMBO-"]
                    )
                    window["-SCHEDULE_TABLE-"].update(
                        values=self.shown_schedule_df.rows()
                    )
                case "-SEA_SETTINGS-":
                    self.filter_shown_schedule_df(
                        values["-LEAGUE_ABV_COMBO-"], values["-LEAGUE_SEASON_COMBO-"]
                    )
                    window["-SCHEDULE_TABLE-"].update(
                        values=self.shown_schedule_df.rows()
                    )
                case "-LG_SETTINGS-":
                    print(event)
                    # window["-WINDOW_MENU-"].update(visible=False)
                case _:
                    pass

        window.close()


if __name__ == "__main__":
    main_window()
    # print(sg.theme_list())
