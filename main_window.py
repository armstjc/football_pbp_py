# Creation Date: 01/27/2024 12:00 PM EDT
# Authors: Joseph Armstrong (armstrongjoseph08@gmail.com)
# file: `./main_window.py`
# Purpose: Main startup window for this application.
################################################################################

from os.path import expanduser

import PySimpleGUI as sg

from core.database.load_db_elements import sqlite3_load_data
from resources.embeded import embeded_elements


class main_window():
    """ """

    sql_engine_type = "sqlite3"
    app_theme = "DarkBlue"

    home_dir = expanduser("~")
    default_data_directory = f"{home_dir}/.sdv_pbp/"

    # Leagues
    leagues_list = ["DEFL"]
    default_league = "DEFL"

    # Seasons
    league_seasons = [2019]
    defalt_season = 2019

    def __init__(self):
        self.app_startup()

    def app_startup(self):

        self.main()

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
            ["New",[
                "New League",
                "New Season",
                "New Team",
                "New Game",
                "New Player"
            ]],
            ["test",["stets"]],
            [
                "Help",
                [
                    "Documentation (Local)",
                    "Docuemntation (Web)",
                    "About"
                ],
            ],
        ]

        layout = [
            [sg.MenuBar(menu_bar, visible=True, key="-WINDOW_MENU-")],
            [],
            [sg.Text("This is a test.")],
            [
                sg.Text("League:\t"),
                sg.Combo(
                    values=self.leagues_list,
                    default_value=self.default_league,
                    size=(5, 1),
                    key="-LEAGUE_ABV-",
                ),
                sg.Button("League Settings", key="-LG_SETTINGS-", size=(15, 1)),
            ],
            [
                sg.Text("Season:\t"),
                sg.Combo(
                    values=self.league_seasons,
                    default_value=self.defalt_season,
                    size=(5, 1),
                    key="-LEAGUE_SEASON-",
                ),
                sg.Button("Season Settings", key="-SEA_SETTINGS-", size=(15, 1)),
            ],
            [
                sg.Table(
                    values=["heck", "None"],
                    headings=["hecker", "jeff"],
                    expand_x=True,
                    expand_y=True,
                    key="-SCHEDULE_TABLE-",
                )
            ],
        ]

        sg.theme(self.app_theme)
        window = sg.Window(
            icon=embeded_elements.desktop_icon(),
            title="The SDV Football PBP App",
            size=(1280, 720),
            layout=layout,
            resizable=True
        )

        keep_open = True
        while keep_open:
            event, values = window.read(timeout=1000)
            print(values)
            # print(event)

            if event == sg.WIN_CLOSED or event == "Quit":
                break

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
                case "-SEA_SETTINGS-":
                    print(event)
                case "-LG_SETTINGS-":
                    print(event)
                    # window["-WINDOW_MENU-"].update(visible=False)
                case _:
                    pass

        window.close()


if __name__ == "__main__":
    main_window()
    # print(sg.theme_list())
