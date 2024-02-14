# Creation Date: 01/27/2024 12:01 PM EDT
# Last Updated: 02/11/2024 11:50 AM EST
# Authors: Joseph Armstrong (armstrongjoseph08@gmail.com)
# file: `./core/settings/main_window.py`
# Purpose: Settins window for this application.
###############################################################################

import PySimpleGUI as sg


class settings_window:

    def __init__(self) -> None:
        self.main()

    def main():
        layout = []
        sg.Window("Settings", layout)
