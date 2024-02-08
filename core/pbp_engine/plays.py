# Creation Date: 01/14/2024 4:14 PM EDT
# Authors: Joseph Armstrong (armstrongjoseph08@gmail.com)
# file: `./core/pbp_engine/plays.py`
# Purpose: Code for generating plays, and their objects.
################################################################################


class plays:
    def pass_play():
        """
        Data structure for a passing play.
        """
        passing_play = {
            "play_desc": None,
            # Can be one of the following values:
            #   - "pass"
            #   - "rush"
            #   - "punt"
            #   - "field_goal"
            #   - "xp" (kicking an XP after a TD)
            #   - "conversion_attempt" (anything that isn't an XP after a TD)
            #   - "kickoff"
            #   - "safety_kickoff"
            #   - "fair_catch_kick"
            "play_type": "pass",
            # In seconds, the time left in this quarter.
            "quarter_time_left": None,
            # In seconds, the time left in this half.
            "half_time_left": None,
            # In seconds, the time left in this game.
            "game_time_left": None,
            # will be formatted as "Q1 15:00"
            "quarter_time_left_str": None,
            "home_score": None,
            "away_score": None,
            "home_score_post": None,
            "away_score_post": None,
            "posteam_score": None,
            "defteam_score": None,
            "posteam_post": None,
            "defteam_post": None,
            "pos_team": None,
            "def_team": None,
            "down": 0,
            "distance": 0,
            "is_goal_to_go": False,
            "drive_num": 0,
            # Can be one of the following values:
            #  - `1`: First Half
            #  - `2`: Second Half
            #  - `3`: OT
            "half_num": 0,
            "quarter_num": 0,
            "is_scoring_play": False,
            "is_first_down": False,
            "is_first_down_penalty": False,
            "is_third_down": False,
            "is_third_down_converted": False,
            "is_fourth_down": False,
            "is_fourth_down_converted": False,
            "is_touchback": False,
            "is_safety": False,
            "yardline_start": None,
            "yardline_end": None,
            # Can only be one of the following values:
            # -- "L": Left hash
            # -- "M": Middle hash
            # -- "R": Right hash
            "starting_hash": "M",
            # Can only be one of the following values:
            # -- "U": QB is under center for this play.
            # -- "S": QB is in shotgun for this play.
            # -- "P": QB is in pistol for this play.
            # -- "H": QB is the holder for a FG on this play.
            # -- "K": QB is a punter/kicker for this play.
            "qb_location": None,
            # Denotes the number of RBs in the backfield for this play.
            "n_offense_backfield": 0,
            "is_no_huddle": False,
            "is_motion": False,
            "is_no_play": False,
            "penalties": [
                # If a player commits a penalty,
                # this is how this section will look like:
                # {
                #     # Auto incriments by 1 during the game.
                #     "penalty_num":0,
                #     # ID for this specific penalty
                #     "penalty_id":None,
                #     "penalty_name":None,
                #     "is_offensive_penalty":False,
                #     "is_penalty_accepted":False,
                #     "is_personal_foul":False,
                #     "is_player_ejected":False,
                #     "is_team_penalty":False,
                #     "player":{
                #         "player_id": None,
                #         "team_id": None,
                #         "player_num": None,
                #         "player_full_name": None,
                #         "player_football_name": None,
                #     }
                # }
            ],
            "injured_players": [
                # if there is a player or players injured
                # on a play, this is how this section will look like:
                # {
                #     "player_id": None,
                #     "team_id": None,
                #     "player_num": None,
                #     "player_full_name": None,
                #     "player_football_name": None,
                #     # String, identiying the suspected injury
                #     "type_of_injury":None
                # }
            ],
            # The yardline where the QB attempts the pass.
            # (if the QB actually got a pass off)
            "pass_attempted_at_yardline": None,
            "pass_caught_at_yardline": None,
            # If the pass is caught,
            # this is the yardline where the reciver was first touched by a defender.
            "first_contact_yardline": None,
            "passer": {
                "player_id": None,
                "team_id": None,
                "player_num": None,
                "player_full_name": None,
                "player_football_name": None,
            },
            "is_completed_pass": False,
            "is_spiked_pass": False,
            "is_deflected_pass": False,
            "is_intercepted": False,
            "is_play_action": False,
            "is_screen_pass": False,
            "is_rpo": False,
            "is_trick_play": False,
            "is_qb_out_of_pocket": False,
            "is_interception_worthy": False,
            "is_throw_away": False,
            "is_catchable_ball": False,
            "is_contested_ball": False,
            # Reciver physically pulls away the ball on a catch,
            "is_created_reception": False,
            "is_drop": False,
            "is_touchdown": False,
            "is_turnover": False,  
            # Set to true if there is a play where there is a turnover by the offense,
            # but the offense then forces their own turnover and gets the ball back in that same play.
            # Examples: https://www.youtube.com/watch?v=6jOnMiJKJ5s
            "is_double_turnover": False,
            "is_bad_snap": False,
            "is_sack_play": False,
            "receiver": {
                ## If this pass play results in a completed pass,
                ## this is what will be populated in this section.
                # "player_id":None,
                # "team_id":None,
                # "player_num":None,
                # "player_full_name":None,
                # "player_football_name":None
            },
            "is_qb_fumble": False,
            "is_receiver_fumble": False,
            "is_assisted_tackle": False,
            "tacklers": [
                ## If this pass play results in a completed pass,
                ## this is what will be populated in this section.
                # {
                #     "player_id":None,
                #     "team_id":None,
                #     "player_num":None,
                #     "player_full_name":None,
                #     "player_football_name":None,
                #     "is_tfl":False,
                #     "is_sack":False,
                #     "is_sack_fumble":False,
                # }
            ],
            "forced_fumbles": [
                ## If this pass play results in a completed pass,
                ## this is what will be populated in this section.
                # {
                #     "forced_fumble_num":0,
                #     "player_id":None,
                #     "team_id":None,
                #     "player_num":None,
                #     "player_full_name":None,
                #     "player_football_name":None,
                #     "fumble_forced_at":None,
                # }
            ],
            "fumble_recoveries": [
                ## If this pass play results in a completed pass,
                ## this is what will be populated in this section.
                # {
                #     "fumble_recovery_num":0,
                #     "player_id":None,
                #     "team_id":None,
                #     "player_num":None,
                #     "player_full_name":None,
                #     "player_football_name":None,
                #     "is_defensive_fumble_recovery":False,
                #     "fumble_recovered_at":None,
                #     "retunred_to":None,
                #     "return_yards":0,
                #     "player_fumbled":False,
                #     "player_lost_fumble":False,
                #     "player_lateraled":False,
                #     "scored_touchdown":False,
                # }
            ],
        }

        return passing_play

    def rush_play():
        """
        Data structure for a rushing play.
        """
        rushing_play = {
            "play_desc": None,
            # Can be one of the following values:
            #   - "pass"
            #   - "rush"
            #   - "punt"
            #   - "field_goal"
            #   - "xp" (kicking an XP after a TD)
            #   - "conversion_attempt" (anything that isn't an XP after a TD)
            #   - "kickoff"
            #   - "safety_kickoff"
            #   - "fair_catch_kick"
            "play_type": "rush",
            # In seconds, the time left in this quarter.
            "quarter_time_left": None,
            # In seconds, the time left in this half.
            "half_time_left": None,
            # In seconds, the time left in this game.
            "game_time_left": None,
            "home_score": None,
            "away_score": None,
            "home_score_post": None,
            "away_score_post": None,
            "posteam_score": None,
            "defteam_score": None,
            "posteam_post": None,
            "defteam_post": None,
            "pos_team": None,
            "def_team": None,
            "down": 0,
            "distance": 0,
            "is_goal_to_go": False,
            "drive_num": 0,
            # Can be one of the following values:
            #  - `1`: First Half
            #  - `2`: Second Half
            #  - `3`: OT
            "half_num": 0,
            "quarter_num": 0,
            "is_scoring_play": False,
            "is_first_down": False,
            "is_first_down_penalty": False,
            "is_third_down": False,
            "is_third_down_converted": False,
            "is_fourth_down": False,
            "is_fourth_down_converted": False,
            "is_touchback": False,
            "is_safety": False,
            "yardline_start": None,
            "yardline_end": None,
            # Can only be one of the following values:
            # -- "L": Left hash
            # -- "M": Middle hash
            # -- "R": Right hash
            "starting_hash": "M",
            # Can only be one of the following values:
            # -- "U": QB is under center for this play.
            # -- "S": QB is in shotgun for this play.
            # -- "P": QB is in pistol for this play.
            # -- "H": QB is the holder for a FG on this play.
            # -- "K": QB is a punter/kicker for this play.
            "qb_location": None,
            # Denotes the number of RBs in the backfield for this play.
            "n_offense_backfield": 0,
            "is_no_huddle": False,
            "is_motion": False,
            "rusher": {
                "player_id": None,
                "team_id": None,
                "player_num": None,
                "player_full_name": None,
                "player_football_name": None,
            },
            "first_contact_yardline": 0,
            # Can be one of the following values:
            #   - "left"
            #   - "middle"
            #   - "right"
            "run_location": None,
            # Can be one of the following values,
            # but only if "run_location" != "middle"
            #   - "end"
            #   - "tackle"
            #   - "guard"
            "run_gap": None,
            "is_rpo": False,
            "is_read_option": False,
            "is_trick_play": False,
            "is_touchdown": False,
            "is_turnover": False,  # Set to true if there is a play where there is a turnover by the offense,
            # but the offense then forces their own turnover and gets the ball back in that same play.
            # Examples: https://www.youtube.com/watch?v=6jOnMiJKJ5s
            "is_double_turnover": False,
            "is_bad_snap": False,
            "is_fumble": False,
            "is_qb_kneel": False,
            "is_assisted_tackle": False,
            "tacklers": [
                ## If this pass play results in a completed pass,
                ## this is what will be populated in this section.
                # {
                #     "player_id":None,
                #     "team_id":None,
                #     "player_num":None,
                #     "player_full_name":None,
                #     "player_football_name":None,
                #     "is_tfl":False,
                #     "is_sack":False,
                #     "is_sack_fumble":False,
                # }
            ],
            "forced_fumbles": [
                ## If this pass play results in a completed pass,
                ## this is what will be populated in this section.
                # {
                #     "forced_fumble_num":0,
                #     "player_id":None,
                #     "team_id":None,
                #     "player_num":None,
                #     "player_full_name":None,
                #     "player_football_name":None,
                #     "fumble_forced_at":None,
                # }
            ],
            "fumble_recoveries": [
                ## If this pass play results in a completed pass,
                ## this is what will be populated in this section.
                # {
                #     "fumble_recovery_num":0,
                #     "player_id":None,
                #     "team_id":None,
                #     "player_num":None,
                #     "player_full_name":None,
                #     "player_football_name":None,
                #     "is_defensive_fumble_recovery":False,
                #     "fumble_recovered_at":None,
                #     "retunred_to":None,
                #     "return_yards":0,
                #     "player_fumbled":False,
                #     "player_lost_fumble":False,
                #     "player_lateraled":False,
                #     "scored_touchdown":False,
                # }
            ],
        }

        return rushing_play

    def punt_play():
        """
        Data structure for a punt play.
        """
        punt_play = {
            "play_desc": None,
            # Can be one of the following values:
            #   - "pass"
            #   - "rush"
            #   - "punt"
            #   - "field_goal"
            #   - "xp" (kicking an XP after a TD)
            #   - "conversion_attempt" (anything that isn't an XP after a TD)
            #   - "kickoff"
            #   - "safety_kickoff"
            #   - "fair_catch_kick"
            "play_type": "punt",
            # In seconds, the time left in this quarter.
            "quarter_time_left": None,
            # In seconds, the time left in this half.
            "half_time_left": None,
            # In seconds, the time left in this game.
            "game_time_left": None,
            "home_score": None,
            "away_score": None,
            "home_score_post": None,
            "away_score_post": None,
            "posteam_score": None,
            "defteam_score": None,
            "posteam_post": None,
            "defteam_post": None,
            "pos_team": None,
            "def_team": None,
            "down": 0,
            "distance": 0,
            "is_goal_to_go": False,
            "drive_num": 0,
            # Can be one of the following values:
            #  - `1`: First Half
            #  - `2`: Second Half
            #  - `3`: OT
            "half_num": 0,
            "quarter_num": 0,
            "is_scoring_play": False,
            "is_first_down": False,
            "is_first_down_penalty": False,
            "is_third_down": False,
            "is_third_down_converted": False,
            "is_fourth_down": False,
            "is_fourth_down_converted": False,
            "is_touchback": False,
            "is_safety": False,
            "yardline_start": None,
            "yardline_end": None,
            # Can only be one of the following values:
            # -- "L": Left hash
            # -- "M": Middle hash
            # -- "R": Right hash
            "starting_hash": "M",
            # Can only be one of the following values:
            # -- "U": QB is under center for this play.
            # -- "S": QB is in shotgun for this play.
            # -- "P": QB is in pistol for this play.
            # -- "H": QB is the holder for a FG on this play.
            # -- "K": QB is a punter/kicker for this play.
            "qb_location": "K",
            # Denotes the number of RBs in the backfield for this play.
            "n_offense_backfield": 0,
            "is_no_huddle": False,
            "is_motion": False,
            "is_no_play": False,
            "punter": {
                "player_id": None,
                "team_id": None,
                "player_num": None,
                "player_full_name": None,
                "player_football_name": None,
            },
            "is_returned": False,
            "is_blocked": False,
            "is_rouge": False,
            "returner": {
                # If "is_returned" = True, this will be seen in "returner"
                # "player_id":None,
                # "team_id":None,
                # "player_num":None,
                # "player_full_name":None,
                # "player_football_name":None,
                # "return_start_yarline":0,
                # "return_end_yarline":0,
                # "is_return_td":False,
                # "is_muffed_punt":False,
            },
            "is_trick_play": False,
            "is_touchdown": False,
            "is_turnover": False,  # Set to true if there is a play where there is a turnover by the offense,
            # but the offense then forces their own turnover and gets the ball back in that same play.
            # Examples: https://www.youtube.com/watch?v=6jOnMiJKJ5s
            "is_double_turnover": False,
            "is_bad_snap": False,
            "is_fumble": False,
            "is_assisted_tackle": False,
            "tacklers": [
                ## If this pass play results in a completed pass,
                ## this is what will be populated in this section.
                # {
                #     "player_id":None,
                #     "team_id":None,
                #     "player_num":None,
                #     "player_full_name":None,
                #     "player_football_name":None,
                #     "is_tfl":False,
                #     "is_sack":False,
                #     "is_sack_fumble":False,
                # }
            ],
            "blocker": {
                # If the kick is blocked, this indicates who blocked the kick.
                #     "player_id":None,
                #     "team_id":None,
                #     "player_num":None,
                #     "player_full_name":None,
                #     "player_football_name":None,
            },
            "forced_fumbles": [
                ## If this pass play results in a completed pass,
                ## this is what will be populated in this section.
                # {
                #     "forced_fumble_num":0,
                #     "player_id":None,
                #     "team_id":None,
                #     "player_num":None,
                #     "player_full_name":None,
                #     "player_football_name":None,
                #     "fumble_forced_at":None,
                # }
            ],
            "fumble_recoveries": [
                ## If this pass play results in a completed pass,
                ## this is what will be populated in this section.
                # {
                #     "fumble_recovery_num":0,
                #     "player_id":None,
                #     "team_id":None,
                #     "player_num":None,
                #     "player_full_name":None,
                #     "player_football_name":None,
                #     "is_defensive_fumble_recovery":False,
                #     "fumble_recovered_at":None,
                #     "retunred_to":None,
                #     "return_yards":0,
                #     "player_fumbled":False,
                #     "player_lost_fumble":False,
                #     "player_lateraled":False,
                #     "scored_touchdown":False,
                # }
            ],
        }

        return punt_play

    def field_goal_play():
        """
        Data structure for a FG play.
        """
        fg_play = {
            "play_desc": None,
            # Can be one of the following values:
            #   - "pass"
            #   - "rush"
            #   - "punt"
            #   - "field_goal"
            #   - "xp" (kicking an XP after a TD)
            #   - "conversion_attempt" (anything that isn't an XP after a TD)
            #   - "kickoff"
            #   - "safety_kickoff"
            #   - "fair_catch_kick"
            "play_type": "field_goal",
            # In seconds, the time left in this quarter.
            "quarter_time_left": None,
            # In seconds, the time left in this half.
            "half_time_left": None,
            # In seconds, the time left in this game.
            "game_time_left": None,
            "home_score": None,
            "away_score": None,
            "home_score_post": None,
            "away_score_post": None,
            "posteam_score": None,
            "defteam_score": None,
            "posteam_post": None,
            "defteam_post": None,
            "pos_team": None,
            "def_team": None,
            "down": 0,
            "distance": 0,
            "is_goal_to_go": False,
            "drive_num": 0,
            # Can be one of the following values:
            #  - `1`: First Half
            #  - `2`: Second Half
            #  - `3`: OT
            "half_num": 0,
            "quarter_num": 0,
            "is_scoring_play": False,
            "is_first_down": False,
            "is_first_down_penalty": False,
            "is_third_down": False,
            "is_third_down_converted": False,
            "is_fourth_down": False,
            "is_fourth_down_converted": False,
            "is_touchback": False,
            "is_safety": False,
            "yardline_start": None,
            "yardline_end": None,
            # Can only be one of the following values:
            # -- "L": Left hash
            # -- "M": Middle hash
            # -- "R": Right hash
            "starting_hash": "M",
            # Can only be one of the following values:
            # -- "U": QB is under center for this play.
            # -- "S": QB is in shotgun for this play.
            # -- "P": QB is in pistol for this play.
            # -- "H": QB is the holder for a FG on this play.
            # -- "K": QB is a punter/kicker for this play.
            "qb_location": "H",
            # Denotes the number of RBs in the backfield for this play.
            # In a normal universe, this is always 0.
            "n_offense_backfield": 0,
            "is_no_huddle": False,
            "is_motion": False,
            "is_no_play": False,
            "kicker": {
                "player_id": None,
                "team_id": None,
                "player_num": None,
                "player_full_name": None,
                "player_football_name": None,
            },
            "is_returned": False,
            "is_rouge": False,
            "fg_attempt_distance": 0,
            "is_fg_made": False,
            # can be one of the following values:
            # - "wide_left"
            # - "wide_right"
            # - "doink"
            # - "block"
            # - "short"
            "missed_fg_reason": None,
            "returner": {
                # If "is_returned" = True, this will be seen in "returner"
                # "player_id":None,
                # "team_id":None,
                # "player_num":None,
                # "player_full_name":None,
                # "player_football_name":None,
                # "return_start_yarline":0,
                # "return_end_yarline":0,
                # "is_return_td":False,
                # "is_muffed_punt":False,
            },
            "is_trick_play": False,
            "is_touchdown": False,
            "is_turnover": False,  # Set to true if there is a play where there is a turnover by the offense,
            # but the offense then forces their own turnover and gets the ball back in that same play.
            # Examples: https://www.youtube.com/watch?v=6jOnMiJKJ5s
            "is_double_turnover": False,
            "is_bad_snap": False,
            "is_fumble": False,
            "is_assisted_tackle": False,
            "blocker": {
                # If the kick is blocked, this indicates who blocked the kick.
                #     "player_id":None,
                #     "team_id":None,
                #     "player_num":None,
                #     "player_full_name":None,
                #     "player_football_name":None,
            },
            "tacklers": [
                ## If this pass play results in a completed pass,
                ## this is what will be populated in this section.
                # {
                #     "player_id":None,
                #     "team_id":None,
                #     "player_num":None,
                #     "player_full_name":None,
                #     "player_football_name":None,
                #     "is_tfl":False,
                #     "is_sack":False,
                #     "is_sack_fumble":False,
                # }
            ],
            "forced_fumbles": [
                ## If this pass play results in a completed pass,
                ## this is what will be populated in this section.
                # {
                #     "forced_fumble_num":0,
                #     "player_id":None,
                #     "team_id":None,
                #     "player_num":None,
                #     "player_full_name":None,
                #     "player_football_name":None,
                #     "fumble_forced_at":None,
                # }
            ],
            "fumble_recoveries": [
                ## If this pass play results in a completed pass,
                ## this is what will be populated in this section.
                # {
                #     "fumble_recovery_num":0,
                #     "player_id":None,
                #     "team_id":None,
                #     "player_num":None,
                #     "player_full_name":None,
                #     "player_football_name":None,
                #     "is_defensive_fumble_recovery":False,
                #     "fumble_recovered_at":None,
                #     "retunred_to":None,
                #     "return_yards":0,
                #     "player_fumbled":False,
                #     "player_lost_fumble":False,
                #     "player_lateraled":False,
                #     "scored_touchdown":False,
                # }
            ],
        }

        return fg_play

    def extra_point_play():
        """
        Data structure for a FG play.
        """
        xp_play = {
            "play_desc": None,
            # Can be one of the following values:
            #   - "pass"
            #   - "rush"
            #   - "punt"
            #   - "field_goal"
            #   - "xp" (kicking an XP after a TD)
            #   - "conversion_attempt" (anything that isn't an XP after a TD)
            #   - "kickoff"
            #   - "safety_kickoff"
            #   - "fair_catch_kick"
            "play_type": "xp",
            # In seconds, the time left in this quarter.
            "quarter_time_left": None,
            # In seconds, the time left in this half.
            "half_time_left": None,
            # In seconds, the time left in this game.
            "game_time_left": None,
            "home_score": None,
            "away_score": None,
            "home_score_post": None,
            "away_score_post": None,
            "posteam_score": None,
            "defteam_score": None,
            "posteam_post": None,
            "defteam_post": None,
            "pos_team": None,
            "def_team": None,
            "drive_num": 0,
            # Can be one of the following values:
            #  - `1`: First Half
            #  - `2`: Second Half
            #  - `3`: OT
            "half_num": 0,
            "quarter_num": 0,
            "is_scoring_play": False,
            "is_safety": False,
            "yardline_start": None,
            "yardline_end": None,
            # Can only be one of the following values:
            # -- "L": Left hash
            # -- "M": Middle hash
            # -- "R": Right hash
            "starting_hash": "M",
            # Can only be one of the following values:
            # -- "U": QB is under center for this play.
            # -- "S": QB is in shotgun for this play.
            # -- "P": QB is in pistol for this play.
            # -- "H": QB is the holder for a FG on this play.
            # -- "K": QB is a punter/kicker for this play.
            "qb_location": "H",
            # Denotes the number of RBs in the backfield for this play.
            # In a normal universe, this is always 0.
            "n_offense_backfield": 0,
            "is_no_huddle": False,
            "is_motion": False,
            "is_no_play": False,
            "kicker": {
                "player_id": None,
                "team_id": None,
                "player_num": None,
                "player_full_name": None,
                "player_football_name": None,
            },
            "is_returned": False,
            "is_rouge": False,
            "is_punt_in_20": False,
            "fg_attempt_distance": 0,
            "is_fg_made": False,
            # can be one of the following values:
            # - "wide_left"
            # - "wide_right"
            # - "doink"
            # - "block"
            # - "short"
            "missed_fg_reason": None,
            "returner": {
                # If "is_returned" = True, this will be seen in "returner"
                # "player_id":None,
                # "team_id":None,
                # "player_num":None,
                # "player_full_name":None,
                # "player_football_name":None,
                # "return_start_yarline":0,
                # "return_end_yarline":0,
                # "is_return_td":False,
                # "is_muffed_punt":False,
            },
            "is_trick_play": False,
            "is_touchdown": False,
            "is_turnover": False,
            # Set to true if there is a play where there is a turnover by the offense,
            # but the offense then forces their own turnover and gets the ball back in that same play.
            # Examples: https://www.youtube.com/watch?v=6jOnMiJKJ5s
            "is_double_turnover": False,
            "is_bad_snap": False,
            "is_fumble": False,
            "is_assisted_tackle": False,
            "blocker": {
                # If the kick is blocked, this indicates who blocked the kick.
                #     "player_id":None,
                #     "team_id":None,
                #     "player_num":None,
                #     "player_full_name":None,
                #     "player_football_name":None,
            },
            "tacklers": [
                ## If this pass play results in a completed pass,
                ## this is what will be populated in this section.
                # {
                #     "player_id":None,
                #     "team_id":None,
                #     "player_num":None,
                #     "player_full_name":None,
                #     "player_football_name":None,
                #     "is_tfl":False,
                #     "is_sack":False,
                #     "is_sack_fumble":False,
                # }
            ],
            "forced_fumbles": [
                ## If this pass play results in a completed pass,
                ## this is what will be populated in this section.
                # {
                #     "forced_fumble_num":0,
                #     "player_id":None,
                #     "team_id":None,
                #     "player_num":None,
                #     "player_full_name":None,
                #     "player_football_name":None,
                #     "fumble_forced_at":None,
                # }
            ],
            "fumble_recoveries": [
                ## If this pass play results in a completed pass,
                ## this is what will be populated in this section.
                # {
                #     "fumble_recovery_num":0,
                #     "player_id":None,
                #     "team_id":None,
                #     "player_num":None,
                #     "player_full_name":None,
                #     "player_football_name":None,
                #     "is_defensive_fumble_recovery":False,
                #     "fumble_recovered_at":None,
                #     "retunred_to":None,
                #     "return_yards":0,
                #     "player_fumbled":False,
                #     "player_lost_fumble":False,
                #     "player_lateraled":False,
                #     "scored_touchdown":False,
                # }
            ],
        }

        return xp_play

    def conversion_attempt_play():
        """
        Data structure for a conversion attempt play (like a 2 point attempt).
        """
        conversion_play = {
            "play_desc": None,
            # Can be one of the following values:
            #   - "pass"
            #   - "rush"
            #   - "punt"
            #   - "field_goal"
            #   - "xp" (kicking an XP after a TD)
            #   - "conversion_attempt" (anything that isn't an XP after a TD)
            #   - "kickoff"
            #   - "safety_kickoff"
            #   - "fair_catch_kick"
            "play_type": "conversion_attempt",
            # In seconds, the time left in this quarter.
            "quarter_time_left": None,
            # In seconds, the time left in this half.
            "half_time_left": None,
            # In seconds, the time left in this game.
            "game_time_left": None,
            # will be formatted as "Q1 15:00"
            "quarter_time_left_str": None,
            "home_score": None,
            "away_score": None,
            "home_score_post": None,
            "away_score_post": None,
            "posteam_score": None,
            "defteam_score": None,
            "posteam_post": None,
            "defteam_post": None,
            "pos_team": None,
            "def_team": None,
            "down": 0,
            "distance": 0,
            "is_goal_to_go": False,
            "drive_num": 0,
            # Can be one of the following values:
            #  - `1`: First Half
            #  - `2`: Second Half
            #  - `3`: OT
            "half_num": 0,
            "quarter_num": 0,
            "is_scoring_play": False,
            "is_1pt_conversion": False,
            "is_1pt_successful_conversion": False,
            "is_2pt_conversion": False,
            "is_2pt_successful_conversion": False,
            "is_3pt_conversion": False,
            "is_3pt_successful_conversion": False,
            "is_touchback": False,
            "is_safety": False,
            "yardline_start": None,
            "yardline_end": None,
            # Can only be one of the following values:
            # -- "L": Left hash
            # -- "M": Middle hash
            # -- "R": Right hash
            "starting_hash": "M",
            # Can only be one of the following values:
            # -- "U": QB is under center for this play.
            # -- "S": QB is in shotgun for this play.
            # -- "P": QB is in pistol for this play.
            # -- "H": QB is the holder for a FG on this play.
            # -- "K": QB is a punter/kicker for this play.
            "qb_location": None,
            # Denotes the number of RBs in the backfield for this play.
            "n_offense_backfield": 0,
            "is_no_huddle": False,
            "is_motion": False,
            "is_no_play": False,
            "penalties": [
                # If a player commits a penalty,
                # this is how this section will look like:
                # {
                #     # Auto incriments by 1 during the game.
                #     "penalty_num":0,
                #     # ID for this specific penalty
                #     "penalty_id":None,
                #     "penalty_name":None,
                #     "is_offensive_penalty":False,
                #     "is_penalty_accepted":False,
                #     "is_personal_foul":False,
                #     "is_player_ejected":False,
                #     "is_team_penalty":False,
                #     "player":{
                #         "player_id": None,
                #         "team_id": None,
                #         "player_num": None,
                #         "player_full_name": None,
                #         "player_football_name": None,
                #     }
                # }
            ],
            "injured_players": [
                # if there is a player or players injured
                # on a play, this is how this section will look like:
                # {
                #     "player_id": None,
                #     "team_id": None,
                #     "player_num": None,
                #     "player_full_name": None,
                #     "player_football_name": None,
                #     # String, identiying the suspected injury
                #     "type_of_injury":None
                # }
            ],
            # The type of play ran on this conversion attempt.
            # can either ber a "pass" or "run" play.
            "conversion_play_type":"pass", 
            # The yardline where the QB attempts the pass.
            # (if the QB actually got a pass off)
            "pass_attempted_at_yardline": None,
            "pass_caught_at_yardline": None,
            # If the pass is caught,
            # this is the yardline where the reciver was first touched by a defender.
            "first_contact_yardline": None,
            "passer": {
                "player_id": None,
                "team_id": None,
                "player_num": None,
                "player_full_name": None,
                "player_football_name": None,
            },
            "is_completed_pass": False,
            "is_spiked_pass": False,
            "is_deflected_pass": False,
            "is_intercepted": False,
            "is_play_action": False,
            "is_screen_pass": False,
            "is_rpo": False,
            "is_trick_play": False,
            "is_qb_out_of_pocket": False,
            "is_interception_worthy": False,
            "is_throw_away": False,
            "is_catchable_ball": False,
            "is_contested_ball": False,
            # Reciver physically pulls away the ball on a catch,
            "is_created_reception": False,
            "is_drop": False,
            "is_touchdown": False,
            "is_turnover": False,  # Set to true if there is a play where there is a turnover by the offense,
            # but the offense then forces their own turnover and gets the ball back in that same play.
            # Examples: https://www.youtube.com/watch?v=6jOnMiJKJ5s
            "is_double_turnover": False,
            "is_bad_snap": False,
            "is_sack_play": False,
            "receiver": {
                ## If this pass play results in a completed pass,
                ## this is what will be populated in this section.
                # "player_id":None,
                # "team_id":None,
                # "player_num":None,
                # "player_full_name":None,
                # "player_football_name":None
            },
            "is_qb_fumble": False,
            "rusher": {
                "player_id": None,
                "team_id": None,
                "player_num": None,
                "player_full_name": None,
                "player_football_name": None,
            },
            "is_receiver_fumble": False,
            "is_assisted_tackle": False,
            "tacklers": [
                ## If this pass play results in a completed pass,
                ## this is what will be populated in this section.
                # {
                #     "player_id":None,
                #     "team_id":None,
                #     "player_num":None,
                #     "player_full_name":None,
                #     "player_football_name":None,
                #     "is_tfl":False,
                #     "is_sack":False,
                #     "is_sack_fumble":False,
                # }
            ],
            "forced_fumbles": [
                ## If this pass play results in a completed pass,
                ## this is what will be populated in this section.
                # {
                #     "forced_fumble_num":0,
                #     "player_id":None,
                #     "team_id":None,
                #     "player_num":None,
                #     "player_full_name":None,
                #     "player_football_name":None,
                #     "fumble_forced_at":None,
                # }
            ],
            "fumble_recoveries": [
                ## If this pass play results in a completed pass,
                ## this is what will be populated in this section.
                # {
                #     "fumble_recovery_num":0,
                #     "player_id":None,
                #     "team_id":None,
                #     "player_num":None,
                #     "player_full_name":None,
                #     "player_football_name":None,
                #     "is_defensive_fumble_recovery":False,
                #     "fumble_recovered_at":None,
                #     "retunred_to":None,
                #     "return_yards":0,
                #     "player_fumbled":False,
                #     "player_lost_fumble":False,
                #     "player_lateraled":False,
                #     "scored_touchdown":False,
                # }
            ],
        }

        return conversion_play

    def kickoff_play(is_safety_kickoff:bool=False):
        """
        Data structure for a kickoff play.
        """
        kickoff_play = {
            "play_desc": None,
            # Can be one of the following values:
            #   - "pass"
            #   - "rush"
            #   - "punt"
            #   - "field_goal"
            #   - "xp" (kicking an XP after a TD)
            #   - "conversion_attempt" (anything that isn't an XP after a TD)
            #   - "kickoff"
            #   - "safety_kickoff"
            #   - "fair_catch_kick"
            "play_type": "kickoff",
            # In seconds, the time left in this quarter.
            "quarter_time_left": None,
            # In seconds, the time left in this half.
            "half_time_left": None,
            # In seconds, the time left in this game.
            "game_time_left": None,
            "home_score": None,
            "away_score": None,
            "home_score_post": None,
            "away_score_post": None,
            # In Kickoffs, "pos_team" is the returning team, "def_team" is the kicking team.
            "posteam_score": None,
            "defteam_score": None,
            "posteam_post": None,
            "defteam_post": None,
            "pos_team": None,
            "def_team": None,

            "drive_num": 0,
            # Can be one of the following values:
            #  - `1`: First Half
            #  - `2`: Second Half
            #  - `3`: OT
            "half_num": 0,
            "quarter_num": 0,
            "is_scoring_play": False,
            "is_safety_kickoff":is_safety_kickoff,
            "is_touchback": False,
            "is_safety": False,
            "yardline_start": None,
            "yardline_end": None,
            # Can only be one of the following values:
            # -- "L": Left hash
            # -- "M": Middle hash
            # -- "R": Right hash
            "starting_hash": "M",
            # Can only be one of the following values:
            # -- "U": QB is under center for this play.
            # -- "S": QB is in shotgun for this play.
            # -- "P": QB is in pistol for this play.
            # -- "H": QB is the holder for a FG on this play.
            # -- "K": QB is a punter/kicker for this play.
            "qb_location": "K",
            # Denotes the number of RBs in the backfield for this play.
            # In a normal universe, this is always 0.
            "n_offense_backfield": 0,
            "is_no_huddle": False,
            "is_motion": False,
            "is_no_play": False,
            "kicker": {
                "player_id": None,
                "team_id": None,
                "player_num": None,
                "player_full_name": None,
                "player_football_name": None,
            },
            "is_returned": False,
            "is_rouge": False,
            "kickoff_yardline": 0,
            "is_fg_made": False,
            # can be one of the following values:
            # - "wide_left"
            # - "wide_right"
            # - "doink"
            # - "block"
            # - "short"
            "missed_fg_reason": None,
            "returner": {
                # If "is_returned" = True, this will be seen in "returner"
                # "player_id":None,
                # "team_id":None,
                # "player_num":None,
                # "player_full_name":None,
                # "player_football_name":None,
                # "return_start_yarline":0,
                # "return_end_yarline":0,
                # "is_return_td":False,
                # "is_muffed_punt":False,
            },
            "is_trick_play": False,
            "is_touchdown": False,
            "is_turnover": False,  # Set to true if there is a play where there is a turnover by the offense,
            # but the offense then forces their own turnover and gets the ball back in that same play.
            # Examples: https://www.youtube.com/watch?v=6jOnMiJKJ5s
            "is_double_turnover": False,
            "is_bad_snap": False,
            "is_fumble": False,
            "is_assisted_tackle": False,
            "is_own_kickoff_recovery":False,
            "own_kickoff_recovery_player":{
                # {
                #     "player_id":None,
                #     "team_id":None,
                #     "player_num":None,
                #     "player_full_name":None,
                #     "player_football_name":None,
                #     "recovered_at":None
                # }
            },
            "tacklers": [
                ## If this pass play results in a completed pass,
                ## this is what will be populated in this section.
                # {
                #     "player_id":None,
                #     "team_id":None,
                #     "player_num":None,
                #     "player_full_name":None,
                #     "player_football_name":None,
                #     "is_tfl":False,
                #     "is_sack":False,
                #     "is_sack_fumble":False,
                # }
            ],
            "forced_fumbles": [
                ## If this pass play results in a completed pass,
                ## this is what will be populated in this section.
                # {
                #     "forced_fumble_num":0,
                #     "player_id":None,
                #     "team_id":None,
                #     "player_num":None,
                #     "player_full_name":None,
                #     "player_football_name":None,
                #     "fumble_forced_at":None,
                # }
            ],
            "fumble_recoveries": [
                ## If this pass play results in a completed pass,
                ## this is what will be populated in this section.
                # {
                #     "fumble_recovery_num":0,
                #     "player_id":None,
                #     "team_id":None,
                #     "player_num":None,
                #     "player_full_name":None,
                #     "player_football_name":None,
                #     "is_defensive_fumble_recovery":False,
                #     "fumble_recovered_at":None,
                #     "retunred_to":None,
                #     "return_yards":0,
                #     "player_fumbled":False,
                #     "player_lost_fumble":False,
                #     "player_lateraled":False,
                #     "scored_touchdown":False,
                # }
            ],
        }

        if is_safety_kickoff is True:
            kickoff_play["play_type"] = "safety_kickoff"

        return kickoff_play

    def fair_catch_kick_play():
        """
        Data structure for a fair catch kick play.
        """
        fair_catch_kick_play = {
            "play_desc": None,
            # Can be one of the following values:
            #   - "pass"
            #   - "rush"
            #   - "punt"
            #   - "field_goal"
            #   - "xp" (kicking an XP after a TD)
            #   - "conversion_attempt" (anything that isn't an XP after a TD)
            #   - "kickoff"
            #   - "safety_kickoff"
            #   - "fair_catch_kick"
            "play_type": "fair_catch_kick",
            # In seconds, the time left in this quarter.
            "quarter_time_left": None,
            # In seconds, the time left in this half.
            "half_time_left": None,
            # In seconds, the time left in this game.
            "game_time_left": None,
            "home_score": None,
            "away_score": None,
            "home_score_post": None,
            "away_score_post": None,
            "posteam_score": None,
            "defteam_score": None,
            "posteam_post": None,
            "defteam_post": None,
            "pos_team": None,
            "def_team": None,
            "down": 0,
            "distance": 0,
            "is_goal_to_go": False,
            "drive_num": 0,
            # Can be one of the following values:
            #  - `1`: First Half
            #  - `2`: Second Half
            #  - `3`: OT
            "half_num": 0,
            "quarter_num": 0,
            "is_scoring_play": False,
            "is_first_down": False,
            "is_first_down_penalty": False,
            "is_third_down": False,
            "is_third_down_converted": False,
            "is_fourth_down": False,
            "is_fourth_down_converted": False,
            "is_touchback": False,
            "is_safety": False,
            "yardline_start": None,
            "yardline_end": None,
            # Can only be one of the following values:
            # -- "L": Left hash
            # -- "M": Middle hash
            # -- "R": Right hash
            "starting_hash": "M",
            # Denotes the number of RBs in the backfield for this play.
            # In a normal universe, this is always 0.
            "n_offense_backfield": 0,
            "is_no_huddle": False,
            "is_motion": False,
            "is_no_play": False,
            "kicker": {
                "player_id": None,
                "team_id": None,
                "player_num": None,
                "player_full_name": None,
                "player_football_name": None,
            },
            "is_returned": False,
            "is_rouge": False,
            "fg_attempt_distance": 0,
            "is_fg_made": False,
            # can be one of the following values:
            # - "wide_left"
            # - "wide_right"
            # - "doink"
            # - "block"
            # - "short"
            "missed_xp_reason": None,
            # In some leagues,
            # a turnover on a 2 PT attempt can be returned,
            # and if a defender can return it into the
            # opposite end zone, that defensive team gets
            # 2 points
            "is_defensive_2pc": None,
            "returner": {
                # If "is_returned" = True, this will be seen in "returner"
                # "player_id":None,
                # "team_id":None,
                # "player_num":None,
                # "player_full_name":None,
                # "player_football_name":None,
                # "return_start_yarline":0,
                # "return_end_yarline":0,
                # "is_return_td":False,
                # "is_muffed_punt":False,
            },
            "is_trick_play": False,
            "is_touchdown": False,
            "is_turnover": False,  # Set to true if there is a play where there is a turnover by the offense,
            # but the offense then forces their own turnover and gets the ball back in that same play.
            # Examples: https://www.youtube.com/watch?v=6jOnMiJKJ5s
            "is_double_turnover": False,
            "is_bad_snap": False,
            "is_fumble": False,
            "is_assisted_tackle": False,
            "blocker": {
                # If the kick is blocked, this indicates who blocked the kick.
                #     "player_id":None,
                #     "team_id":None,
                #     "player_num":None,
                #     "player_full_name":None,
                #     "player_football_name":None,
            },
            "tacklers": [
                ## If this pass play results in a completed pass,
                ## this is what will be populated in this section.
                # {
                #     "player_id":None,
                #     "team_id":None,
                #     "player_num":None,
                #     "player_full_name":None,
                #     "player_football_name":None,
                #     "is_tfl":False,
                #     "is_sack":False,
                #     "is_sack_fumble":False,
                # }
            ],
            "forced_fumbles": [
                ## If this pass play results in a completed pass,
                ## this is what will be populated in this section.
                # {
                #     "forced_fumble_num":0,
                #     "player_id":None,
                #     "team_id":None,
                #     "player_num":None,
                #     "player_full_name":None,
                #     "player_football_name":None,
                #     "fumble_forced_at":None,
                # }
            ],
            "fumble_recoveries": [
                ## If this pass play results in a completed pass,
                ## this is what will be populated in this section.
                # {
                #     "fumble_recovery_num":0,
                #     "player_id":None,
                #     "team_id":None,
                #     "player_num":None,
                #     "player_full_name":None,
                #     "player_football_name":None,
                #     "is_defensive_fumble_recovery":False,
                #     "fumble_recovered_at":None,
                #     "retunred_to":None,
                #     "return_yards":0,
                #     "player_fumbled":False,
                #     "player_lost_fumble":False,
                #     "player_lateraled":False,
                #     "scored_touchdown":False,
                # }
            ],
        }

        return fair_catch_kick_play
