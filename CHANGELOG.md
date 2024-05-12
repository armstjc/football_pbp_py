# Changelog - The Football PBP Application

## 0.0.4a: The "quick fix security" Update
- Fixed a potential security issue in `core.views.edit_league_view.new_league_view()` caused by unwanted characters being passed in.
- Fixed a potential security issue in `core.views.edit_league_view.new_league_view()` caused by too many characters being passed in.
- Updated the app version to `0.0.4a`

## 0.0.4: The "Leagues of Leagues" Update
- Added a prompt that allows one to create a new football league.
- Added a prompt that allows one to edit an existing football league.
- Added an "About" window for the application.
- Fixed a number of unforeseen bugs that were encountered when changing between differient football leagues and/or seasons.
- Simplified the `"fb_leagues"` and `"fb_seasons"` tables.
- Updated the app version to `0.0.4`

## 0.0.3: The "The Structure" Update
- Fixed spelling errors found in the code.
- Re-organized the structure of the application so that windows/views are in their own dedicated folder within `core`.
- Re-implemented PySimpleGUI version 4.60.5, a version of PySimpleGUI that conforms to the LGPL, as a standalone script.
- Added a settings window to the application.

## 0.0.2: The "Flake8 Refactor" Update
- Refactored base code to comply with Flake8 linting standards.

## 0.0.1: The "First Version" Update
- Implemented the core functionality of the application, and it's data structure.