# Changelog - The Football PBP Application

## 0.0.6: The "Teamwork Makes the Dreams Work" Update:

- Added a prompt that allows one to create a new team within a season.
- Added a prompt that allows one to edit a team within an existing season.
- Added a `include_dash_and_underscore` option to `core.other.embedded.LettersAndNumbers().letters_and_numbers()`.
- Altered the game ID structure from `{season}_{week}_{away team}_{home team}` to `{season}_{league ID}_{week}_{away team}_{home team}`.
- Added `[espn_team_id]`, `[arenafan_team_id]`, `[team_nation]`, `[]`, and `[stadium_id]` to the `[fb_teams]` table.
- Consolidated `[ncaa_old_team_id]` and `[ncaa_team_id]` in the `[fb_teams]` table to just `[ncaa_team_id]`.
- Updated the app version to `0.0.6`

## 0.0.5: The "Seasons" Update
- Added a prompt that allows one to create a new season within a football league.
- Added a prompt that allows one to edit a season within an existing football league.
- Implemented `core.embedded.LettersAndNumbers()`, a class with sets of letters, numbers, and/or characters to make it easier to filter out unwanted characters for prompts/inputs in this app.
- Re-implemented all internal SQL scripts to no longer use f-strings.
- Fixed the title within `core.views.edit_league_view.LeagueView` to display `"Edit League..."` instead of `"About"`.
- Fixed the title within `core.views.edit_league_view.new_league_view` to display `"New League..."` instead of `"About"`.
- Fixed the title within `core.views.edit_season_view.SeasonView` to display `"Edit Season..."` instead of `"About"`.
- Fixed an issue within `core.views.edit_league_view.LeagueView` that would allow a user to name a football league with more than the intended 256 characters.
- Renamed `core.views.main_window_view.main_window()` to `core.views.main_window_view.MainWindow()` to better fit this application's naming scheme with classes and functions.
- Fixed a bug within `core.views.main_window_view.MainWindow().refresh_league_seasons()` that would result in the `fb_seasons_df` table to not refresh in every situation `core.views.main_window_view.MainWindow().refresh_league_seasons()` was called.
- Fixed a minor edge case issue in `core.views.main_window_view.MainWindow().refresh_league_seasons()` that would occasionally result in the list of seasons being noticeably out of order.
- Added `"New League"` and `"New League"` buttons to the main window in `core.views.main_window_view.MainWindow()`.
- Fixed a minor edge case in `core.views.main_window_view.MainWindow()` where the window would occasionally forget which league you had previously selected when accessing that league's settings.
- Updated the app version to `0.0.5`

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