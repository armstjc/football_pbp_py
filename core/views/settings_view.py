"""
- Creation Date: 01/27/2024 12:01 PM EST
- Last Updated: 04/15/2024 10:25 AM EDT
- Authors: Joseph Armstrong (armstrongjoseph08@gmail.com)
- file: `./core/views/settings_view.py`
- Purpose: Settings window for this application.
"""

###############################################################################

import PySimpleGUI as sg

# from core.settings.settings_core import AppSettings, AppThemes
from core.settings.settings_core import AppSettings


class SettingsWindow:
    """ """

    settings_dict = {}
    alt_settings_dict = {}
    app_settings = AppSettings()
    changed_settings = False

    def __init__(self) -> None:
        """ """
        self.main()

    def check_settings_version(self) -> None:
        pass

    def changed_settings_check(self) -> str:
        check = sg.popup_yes_no(
            """
            You have unsaved settings.
            Do you want to save your changes?
            """.replace(
                "            ",
                ""
            ),
            title="Unsaved Settings"
        )
        return check

    def main(self):
        """ """
        # theme_names_list = AppThemes.theme_names()
        # theme_names_dict = AppThemes.theme_conversion_dictionary()
        self.settings_dict = self.app_settings.load_settings()
        self.alt_settings_dict = self.app_settings.load_settings()

        appearance_layout = [
            [
                sg.Text("App Theme"),
                sg.Push(),
                sg.Combo(
                    values=sg.theme_list(),
                    size=(40, 1),
                    default_value=self.settings_dict["app_theme"],
                    key="-APP_THEME_COMBO-",
                    enable_events=True,
                ),
                sg.Button(
                    button_text="Show Selected App Theme",
                    visible=True,
                    key="-SHOW_THEME_BUTTON-",
                )
            ]
        ]

        user_identity_layout = [
            [
                sg.Text(
                    """
    Allows you to identify yourself (if you want to),
    as the person who charted this game.
                    """.replace(
                        "    ", ""
                    )
                )
            ],
            [
                sg.Text(
                    text="User Identity:",
                    tooltip="The name you want to go by on the internet.",
                ),
                sg.Push(),
                sg.Input(
                    default_text=self.settings_dict["user_identity"][
                        "internet_identity"
                    ],
                    size=(70, 1),
                    enable_events=True,
                    key="-INTERNET_IDENTITY_INPUT-",
                ),
            ],
            [
                sg.Text(
                    "First Name:",
                    tooltip="Your first name "
                    + "(if you want to self-identify yourself).",
                ),
                sg.Push(),
                sg.Input(
                    default_text=self.settings_dict[
                        "user_identity"]["first_name"],
                    size=(70, 1),
                    enable_events=True,
                    key="-USER_F_NAME-",
                ),
            ],
            [
                sg.Text(
                    "Last Name:",
                    tooltip="Your last name "
                    + "(if you want to self-identify yourself).",
                ),
                sg.Push(),
                sg.Input(
                    default_text=self.settings_dict[
                        "user_identity"]["last_name"],
                    size=(70, 1),
                    enable_events=True,
                    key="-USER_L_NAME-",
                ),
            ],
            [
                sg.Text(
                    "Email:",
                    tooltip="Your email account "
                    + "(if you have one, and want it public).",
                ),
                sg.Push(),
                sg.Input(
                    default_text=self.settings_dict[
                        "user_identity"]["email"],
                    size=(70, 1),
                    enable_events=True,
                    key="-USER_EMAIL-",
                ),
            ],
            [
                sg.Text(
                    "GitHub:",
                    tooltip="The username to your GitHub account "
                    + "(if you have one, and want it public).",
                ),
                sg.Push(),
                sg.Input(
                    default_text=self.settings_dict[
                        "user_identity"]["github_username"],
                    size=(70, 1),
                    enable_events=True,
                    key="-GH_USERNAME-",
                ),
            ],
            [
                sg.Text(
                    "X/Twitter:",
                    tooltip="Your X (formerly Twitter) account handle "
                    + "(if you have one, and want it public).",
                ),
                sg.Push(),
                sg.Input(
                    default_text=self.settings_dict[
                        "user_identity"]["twitter_handle"],
                    size=(70, 1),
                    enable_events=True,
                    key="-TW_HANDLE-",
                ),
            ],
            [
                sg.Text(
                    "Reddit:",
                    tooltip="The username to your Reddit account "
                    + "(if you have one, and want it public).",
                ),
                sg.Push(),
                sg.Input(
                    default_text=self.settings_dict[
                        "user_identity"]["reddit_username"],
                    size=(70, 1),
                    enable_events=True,
                    key="-REDDIT_USERNAME-",
                ),
            ],
            [
                sg.Text(
                    "Contact:",
                    tooltip="""
                    If you want to add additional contact details
                    (for any reason), place them in the following
                    text box:
                    """,
                ),
                sg.Push(),
                sg.Multiline(
                    default_text=self.settings_dict[
                        "user_identity"]["contact"],
                    size=(68, 4),
                    enable_events=True,
                    # horizontal_scroll=True,
                    key="-CONTACT-",
                ),
            ],
        ]

        data_settings_layout = [
            [
                sg.Text(
                    """
    By default, all user data will exist within the user's home directory.
    If you need the data generated by this app to exist
    in a different directory or directories, you can change that here.
                    """.replace(
                        "    ", ""
                    ),
                    auto_size_text=True
                )
            ],
            [
                sg.Text(
                    text="Data Directory:",
                    tooltip="""
    The directory all user-generated data from this app is stored.
                    """,
                ),
                sg.Push(),
                sg.Input(
                    default_text=self.settings_dict["data"][
                        "data_directory"
                    ],
                    size=(70, 1),
                    enable_events=True,
                    key="-DATA_DIR-",
                ),
            ],
            [
                sg.Text(
                    text="Data Directory:",
                    tooltip="""
    The directory the SQL database for this app is stored in.
                    """,
                ),
                sg.Push(),
                sg.Input(
                    default_text=self.settings_dict["data"][
                        "sql_directory"
                    ],
                    size=(70, 1),
                    enable_events=True,
                    key="-SQL_DIR-",
                ),
            ],
            [
                sg.Text(
                    text="SQL Engine:",
                    tooltip="""
    The SQL engine used by this app.
                    """,
                ),
                sg.Push(),
                sg.Combo(
                    values=["sqlite"],
                    default_value=self.settings_dict["data"][
                        "sql_language"
                    ],
                    size=(70, 1),
                    disabled=True,
                    enable_events=True,
                    key="-SQL_DIR-",

                ),
            ],

        ]

        tab_layout = [
            [
                sg.Tab(
                    title="Appearance",
                    layout=appearance_layout,
                    expand_x=True,
                    expand_y=True
                )
            ],
            [
                sg.Tab(
                    title="User Identity",
                    layout=user_identity_layout,
                    expand_x=True,
                    expand_y=True
                )
            ],
            [
                sg.Tab(
                    title="Data",
                    layout=data_settings_layout,
                    expand_x=True,
                    expand_y=True
                )
            ],
        ]

        window_layout = [
            [
                sg.Text(
                    "Settings",
                    font="Arial 20",
                    expand_x=True,
                    justification="center"
                )
            ],
            [
                sg.TabGroup(
                    tab_layout,
                    expand_x=True,
                    expand_y=True
                )
            ],
            [
                sg.Push(),
                sg.Button(
                    "OK",
                    key="-OK_BUTTON-"
                ),
                sg.Button(
                    "Cancel",
                    key="-CANCEL_BUTTON-"
                ),
                sg.Button(
                    "Apply",
                    key="-APPLY_BUTTON-",
                    disabled=True
                ),
            ]
        ]
        window = sg.Window(
            title="Settings",
            layout=window_layout,
            size=(640, 480),
            finalize=True,
            grab_anywhere=True
        )
        window.set_min_size(size=(640, 600))

        while True:
            event, values = window.read(timeout=1000)
            print(event)
            print(values)
            if event == sg.WIN_CLOSED or event == "Quit":
                break
            elif event == "-APP_THEME_COMBO-":
                self.alt_settings_dict[
                    "app_theme"
                ] = values["-APP_THEME_COMBO-"]
                self.changed_settings = True
            elif event == "-INTERNET_IDENTITY_INPUT-":
                self.alt_settings_dict[
                    "user_identity"
                ]["internet_identity"] = values["-APP_THEME_COMBO-"]
                self.changed_settings = True
            elif event == "-USER_F_NAME-":
                self.alt_settings_dict[
                    "user_identity"
                ]["first_name"] = values["-USER_F_NAME-"]
                self.changed_settings = True
            elif event == "-USER_L_NAME-":
                self.alt_settings_dict[
                    "user_identity"
                ]["last_name"] = values["-USER_L_NAME-"]
                self.changed_settings = True
            elif event == "-USER_EMAIL-":
                self.alt_settings_dict[
                    "user_identity"
                ]["email"] = values["-USER_EMAIL-"]
                self.changed_settings = True
            elif event == "-GH_USERNAME-":
                self.alt_settings_dict[
                    "user_identity"
                ]["github_username"] = values["-GH_USERNAME-"]
                self.changed_settings = True
            elif event == "-TW_HANDLE-":
                self.alt_settings_dict[
                    "user_identity"
                ]["twitter_handle"] = values["-TW_HANDLE-"]
                self.changed_settings = True
            elif event == "-REDDIT_USERNAME-":
                self.alt_settings_dict[
                    "user_identity"
                ]["reddit_username"] = values["-REDDIT_USERNAME-"]
                self.changed_settings = True
            elif event == "-CONTACT-":
                self.alt_settings_dict[
                    "user_identity"
                ]["contact"] = values["-CONTACT-"]
                self.changed_settings = True
            elif event == "-DATA_DIR-":
                self.alt_settings_dict[
                    "data"
                ]["data_directory"] = values["-DATA_DIR-"]
                self.changed_settings = True

            if self.changed_settings is True:
                window["-APPLY_BUTTON-"].update(
                    disabled=False
                )

            if event == "-OK_BUTTON-" and self.changed_settings is True:
                check_flag = self.changed_settings_check()
                # print(check_flag)
                if check_flag == "Yes":
                    print("check")
                    self.app_settings.save_settings(
                        self.alt_settings_dict
                    )
                    break
                elif check_flag == "No":
                    pass
                del check_flag
            elif event == "-OK_BUTTON-" and self.changed_settings is False:
                break
            elif event == "-CANCEL_BUTTON-" and self.changed_settings is True:
                if check_flag == "Yes":
                    print("check")
                    self.app_settings.save_settings(
                        self.alt_settings_dict
                    )
                    break
                elif check_flag == "No":
                    pass
            elif event == "-CANCEL_BUTTON-" and self.changed_settings is False:
                break
            elif event == "-APPLY-" and self.changed_settings is True:
                self.app_settings.save_settings(
                    self.alt_settings_dict
                )
                self.changed_settings = False
                window["-APPLY_BUTTON-"].update(
                    disabled=True
                )

            print(self.changed_settings)
        window.close()


if __name__ == "__main__":
    SettingsWindow()
