# Creation Date: 01/14/2024 4:14 PM EDT
# Last Updated: 02/11/2024 11:50 AM EST
# Authors: Joseph Armstrong (armstrongjoseph08@gmail.com)
# file: `./core/pbp_engine/game.py`
# Purpose: Code for generating game data for the PBP JSON format.
###############################################################################


def get_initial_game_file():
    """ """

    return {
        "format_standard": {
            "format_name": "sdv_football_pbp",
            "version": "0.1",
            "notes": "WARNING: Indev version. Expect file format changes",
        },
        "statistician": {
            "internet_identity": "Unknown_Person",
            "first_name": None,
            "last_name": None,
            "contact": None,
            "github_username": None,
            "email": None,
        },
        "settings": {
            "field_length": 100,
            "downs": 4,
            "first_down_yards": 10,
            "end_zone_length": 10,
            "kickoff_yardline": 35,
            "safety_kick_yardline": 20,
            "kickoff_toucback_yardline": 75,
            "punt_touchback_yardline": 80,
            "normal_touchback_yardline": 80,
            # if a league/game uses a kansas-like OT,
            # this determines the starting yardline.
            "kansas_ot_yardline": 25,
            "pat_yardline": 3,
            "1PC_yardline": 3,
            "2PC_yardline": 3,
            "3PC_yardline": 10,  # Seen in alt-football leagues
            "quarters": 4,
            "quarter_seconds": 900,  # 15 * 60 = 900
            "timeouts_per_half": 3,
            # - If this is set to a variable greater than 0,
            #   OT is timed, but uses "quarter_seconds" for the time.
            # - If this is set to 0, OT is untimed, if enabled
            # - If you're charting an NFL game from 2017-present,
            #   set "ot_period_seconds" to 600
            "ot_period_seconds": 0,
            # If this is set to -1,
            # there is no limit to the number of OT periods that can happen.
            "ot_periods": 1,
            # If "ncaa_ot" is set to `True`,
            # this is the number of OT periods that must be played,
            # until the game becomes a two point conversion contest.
            # From 2019-2020, this value would be `4`,
            # and from 2021-Present,
            # this value would be `2` if it's an NCAA football game.
            "ot_periods_until_shootout": -1,
            # - "min_xfl_ot_periods":
            #   determines the minimum number of OT rounds
            #   that have to be played in an XFL OT before
            #   a winner is determined.
            #   For the 2020 version of the XFL, this should be set to `5`,
            #   and for the 2023 version, this should be set to `3`.
            # - "set_xfl_ot_periods":
            #   If after first 3/5 OT rounds there isn't a winner,
            #   this is the number of OT periods that have to be played to
            #   attempt to determine a victor.
            # If for any reason, an ot period isn't played
            # (because Team A scored on both rounds,
            # and Team B failed to score in both rounds),
            # the user running this app should just manually end the game.
            "min_xfl_ot_periods": -1,
            "set_xfl_ot_periods": -1,
            "touchdown_points": 6,
            "field_goal_points": 3,
            "safety_points": 2,
            "pat_points": 1,
            "pat_defense": 2,
            # AKA: the thing that allows the 6-1 scorigami
            #   that Jon Bios warned us about.
            "pat_safety": 1,
            # Refers to the maximum number of players that are allowed
            # on the field during the play.
            "players_on_field": 11,

            # OT rules

            # If set to `False`, and the game is tied after 4 quarters,
            # the game ends in a tie.
            # If set to `True`, "sudden_death_ot", "modified_sudden_death_ot",
            # "super_modified_sudden_death_ot", "kansas_ot", "ncaa_ot", or
            # "xfl_ot_rule" must be set to `True`,
            # and only one of the 6 listed above can be set to `True`
            "overtime_enabled": True,
            # If set to true, any score wins the game in OT instantly.
            "sudden_death_ot": False,
            # - Used in the NFL in the playoffs from 2010 to 2021,
            #   and in the regular season from 2012 to present.
            # - If set to `True`,
            #   the following rules are applied to a game that goes to OT:
            #   § If the team starting with the ball scores a touchdown,
            #       the game is over.
            #   § If a team scores a safety, the game ends.
            #   § If the team starting with the ball scores (Team A),
            #       but doesn't score a touchdown or a safety,
            #       the other team (Team B) has the chance to continue overtime
            #       by scoring the exact amount of points as Team A,
            #       or win the game by scoring more points than Team A
            #       did in their first possession.
            #       If Team A scores on their first posession,
            #       and they have more points than Team B did
            #       after their first possession in OT, Team A wins.
            #   § If Team A fails to score on their first possession,
            #       and neither team scores a safety on OT possession #1,
            #       the game reverts back to a true sudden death OT,
            #       and whoever scores first wins the game.
            "modified_sudden_death_ot": True,
            # Same as "modified_sudden_death_ot",
            # but the team with the first offensive possession
            # cannot win the game with a touchdown.
            # Used by the Arena Football League, UFL (2009-2012),
            # and by the NFL in its playoffs from 2022 to present.
            "super_modified_sudden_death_ot": False,
            # Overtime rules used by the NCAA from 1995-2020,
            # and by many high school football leagues.
            # - In each OT period, both teams get one possesion each.
            # - If one team at the end of the OT period
            #   has more points scored in that OT period,
            #   that team wins the game.
            # - If both teams score the same
            #   amount of points in that OT period,
            #   or both teams fail to score, start another OT period.
            # - If a team scores either a safety or a touchdown on defense,
            #   that team wins the game.
            "kansas_ot": False,
            # Starting in 2019, following a 7OT game between LSU and Texas A&M,
            # the NCAA instituted a change to the OT rules,
            # where starting in 5OT (later changed to 3OT in 2021),
            # the game became a 2 point conversion contest
            # until one team at the end of a OT period had more points.
            # If set to `True`, this will reference "ot_periods_until_shootout"
            # on when to switch from the Kansas OT system,
            # to the 2 point conversion contest.
            "ncaa_ot": False,
            # known as a "hockey shootout" in the XFL's API,
            # teams alternate 2 point conversions until one team either
            # A. has an advantage in the first 5 plays, or
            # B. both teams convert the same number of 2 point conversions,
            #   so whoever bilnks (scores a 2pc and stops the opponent) wins.
            "xfl_ot_rule": False,
            # Seen in the now defunct World Football League (WFL)
            "full_period_ot": False,

            # General rules

            # In the 2020 version of the XFL,
            # you could throw the ball twice forwards.
            "two_forward_passes": False,
            "spikes_are_team_stats": False,
            # in the CFB and simliar leauges,
            # a sack is always a  rush.
            "sacks_are_rushes": False,
            "kneeldowns_are_team_stats": False,
            # In Collge football starting in 2018, and in the NFL in 2023,
            # a kickoff that's fair caught outside of the endzone,
            # but is caught within the touchback line (25 yard line),
            # is automatically sent to the touchback line for kickoffs,
            # unless the fair catch is done
            # beyond the touchback line for kickoffs.
            "kickoff_fair_catch_always_goes_to_touchback": False,
            # Done in the Alliance of American Football (AAF),
            # this was a league that did away with kickoffs,
            # and there have been some coaches
            # advocating for the complete
            # removal of the kickoff from football.
            "kickoffs_enabled": True,
            # XFL and the European League of Football (ELF)
            # use a unique approach to kickoffs,
            # where both the kicking team and kick return team
            # are lined up within 5 yards.
            "use_xfl_kickoff": False,
            "drop_kick_enabled": True,
            # In some arena leagues, a drop kick gives you an extra point.
            "drop_kick_bonus_point": False,
            "field_goal_adds_end_zone_length": True,
            # Seen in some arena leauges,
            # where a 50+ yard FG is a 4 point score,
            # instead of a 3 point score.
            "long_fg_bonus_point": False,
            # Unless you're a weird league like the XFL,
            # you can kick the ball for a successfull extra point.
            "xp_is_a_fg": True,
            "rouges_enabled": False,  # Seen in Canadian football
            "punting_enabled": True,
            "onside_punts_enabled": False,  # Also seen in Canadian football
            "fair_catch_enabled": True,
        },
        "game_info": {
            "game_is_in_progress": False,
            "game_is_finished": False,
            "season": None,
            "league_id": None,
            "week": None,
            "game_id": None,
            "nflverse_game_id": None,
            "nflverse_old_game_id": None,
            "gsis_id": None,
            "nfl_detail_id": None,
            "pfr_game_id": None,
            "pff_game_id": None,
            "espn_game_id": None,
            "ftn_game_id": None,
            "game_type": None,
            "game_status": None,
            "game_day": None,
            "game_time": None,
            "game_time_zone": None,
            "game_time_offset": None,
            "game_datetime_utc": None,
            "game_day_of_week": None,
            "away_days_rest": None,
            "home_days_rest": None,
            "is_neutral_site_game": False,
            "is_overtime_game": False,
            "is_divisional_game": False,
            "game_roof": "otdoors",  # Can also be "dome", "closed", or "open"
            "surface": "grass",
            "temp_f": None,
            "temp_c": None,
            "wind": None,
            "away_coach_name": None,
            "home_coach_name": None,
            "stadium_ID": None,
            "stadium_name": None,
            "pfr_stadium_id": None,
        },
        "league": {
            "league_id": None,
            "league_long_name": None,
            "league_short_name": None,
            "league_sport_type": None,
            "league_default_sex": None,
            "league_default_gender": None,
            "league_notes": "",
        },
        "score": {
            "away_team_score": 0,
            "home_team_score": 0,
            "by_quarter": [
                # This is how this section will look like:
                # {"quarter": 1, "quarter_name":"Q1", "home": 0, "away": 0},
                # {"quarter": 2, "quarter_name":"Q2", "home": 0, "away": 0},
                # {"quarter": 3, "quarter_name":"Q3", "home": 0, "away": 0},
                # {"quarter": 4, "quarter_name":"Q4", "home": 0, "away": 0},
                # {"quarter": 5, "quarter_name":"OT", "home": 0, "away": 0},
                # {"quarter": 6, "quarter_name":"2 OT", "home": 0, "away": 0}
            ],
        },
        "stadium": {
            "stadium_id": None,
            "team_id": None,
            "pfr_stadium_id": None,
            "stadium_name": None,
            "stadium_capacity": None,
            "stadium_city": None,
            "stadium_state": None,
            "stadium_nation": None,
            "is_dome": None,
            "is_retractable_roof": None,
            "stadium_plus_code": None,  # Google's Plus code system
            "stadium_elevation_ft": None,
            "stadium_elevation_m": None,
            # Timezone of this stadium, formatted as a string,
            # like "America/Phoenix" or "America/New_York"
            "stadium_timezone": None,
            # Latitude and Longitude of a given stadium (if available).
            # For example, Paycor Stadium (formerly Paul Brown Stadium)
            # would have a latitude of 39.09554
            # and a Longitude of -84.51648
            "stadium_location_x": None,  # Latitude of the stadium
            "stadium_location_y": None,  # Longitude of the stadium
        },
        "referees": [
            # This is how this section will look like:
            # {
            #     "ref_num": 11,
            #     "ref_position_abv": "R",
            #     "ref_position_name": "Referee",
            #     "ref_full_name": "Cyril Apolinar",
            #     "ref_first_name": "Cyril",
            #     "ref_last_name": "Apolinar",
            # },
            # {
            #     "ref_num": 22,
            #     "ref_position_abv": "U",
            #     "ref_position_name": "Umpire",
            #     "ref_full_name": "Aya Stanimir",
            #     "ref_first_name": "Aya",
            #     "ref_last_name": "Stanimir",
            # },
        ],
        "betting_lines": [
            # This is how this section will look like:
            # {
            #     "betting_book": "dontbetongames.you.idiot",
            #     "over_under_open": 50,
            #     "over_under_close": 30.5,
            #     "home_spread_open": -8,
            #     "home_spread_close": -3,
            #     "away_spread_open": 8,
            #     "away_spread_close": 3,
            #     "home_moneyline_open": 150,
            #     "home_moneyline_close": 150,
            #     "away_moneyline_open": 1000,
            #     "away_moneyline_close": 1000,
            # }
        ],
        "home_team": {
            "team_id": None,
            "pfr_team_id": None,
            "pfr_fran_id": None,
            "sr_team_id": None,
            "ncaa_old_team_id": None,
            "ncaa_team_id": None,
            "stats_crew_team_id": None,
            "footballdb_team_id": None,
            "team_abv": None,
            "team_name": None,
            "team_location": None,
            "team_nickname": None,
            "team_city": None,
            "team_state": None,
            "team_confrence": None,
            "team_division": None,
            "team_head_coach": None,
            "team_oc": None,
            "team_dc": None,
            "team_primary_logo": None,
            "team_secondary_logo": None,
        },
        "away_team": {
            "team_id": None,
            "pfr_team_id": None,
            "pfr_fran_id": None,
            "sr_team_id": None,
            "ncaa_old_team_id": None,
            "ncaa_team_id": None,
            "stats_crew_team_id": None,
            "footballdb_team_id": None,
            "team_abv": None,
            "team_name": None,
            "team_location": None,
            "team_nickname": None,
            "team_city": None,
            "team_state": None,
            "team_confrence": None,
            "team_division": None,
            "team_head_coach": None,
            "team_oc": None,
            "team_dc": None,
            "team_primary_logo": None,
            "team_secondary_logo": None,
        },
        "rosters": {"home_team": [], "away_team": []},
        "starters": {"home_team": [], "away_team": []},
        "coin_flip": {
            "winning_team": "home",  # can also be "away"
            "decision": "defer",  # can also be "receive",
            # "kick", or "field_direction"
            "has_ot_coin_flip": False,
            "ot_coin_flip_winner": "home",  # can also be "away"
            "ot_decision": "defer",  # can also be "receive",
            # "kick", or "field_direction"
        },
        "drives": [],
        "plays": [],
        "stats": {
            "passing": [],
            "rushing": [],
            "receiving": [],
            "fumbles": [],
            "defense": [],
            "interceptions": [],
            "blocks": [],
            "field_goals": [],
            "punting": [],
            "missed_fg": [],
            "kick_return": [],
            "punt_return": [],
        },
    }


if __name__ == "__main__":
    print(get_initial_game_file())
