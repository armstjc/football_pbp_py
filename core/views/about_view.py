"""
- Creation Date: 03/10/2024 4:40 PM EST
- Last Updated: 05/29/2024 01:15 AM EDT
- Authors: Joseph Armstrong (armstrongjoseph08@gmail.com)
- file: `./core/settings/about_view.py`
- Purpose: About page for this application.
"""

import PySimpleGUI as sg

from core.other.embedded import EmbeddedElements


def about_view():
    """ """
    app_version = EmbeddedElements.app_version()
    about_text = f"""
    App Version: {app_version}

    Development Team:
    - Joseph Armstrong (GitHub: armstjc)


    This application uses FreeSimpleGUI version 5.1,
    a continuation of PySimpleGUI 4.

    MaxPreps is a registered trademark of CBS Broadcasting Inc.


    """.replace(
        "   ", ""
    )
    layout = [
        [
            sg.Text(
                "The Football PBP Application",
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
            sg.Multiline(
                default_text=about_text,
                disabled=True,
                expand_x=True,
                expand_y=True,
            )
        ],
    ]
    sg.theme("Dark")
    window = sg.Window(
        "About", layout=layout, size=(600, 480), resizable=False, finalize=True
    )
    keep_open = True
    while keep_open:
        event, values = window.read(timeout=1000)
        # print(values)
        print(event)

        if event == sg.WIN_CLOSED or event == "Quit":
            break
        elif event == "_OK_":
            break


if __name__ == "__main__":
    about_view()
