from __future__ import annotations

import functools

from typing import List

from dataclasses import dataclass

from Options import OptionSet, Toggle, Choice

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class LuminesRemasteredArchipelagoOptions:
    lumines_remastered_unlocked_skins: LuminesRemasteredUnlockedSkins
    lumines_remastered_unlocked_puzzles: LuminesRemasteredUnlockedPuzzles
    lumines_remastered_unlocked_missions: LuminesRemasteredUnlockedMissions


class LuminesRemasteredGame(Game):
    name = "LUMINES REMASTERED"

    platform = KeymastersKeepGamePlatforms.PC
    platforms_other = [
        KeymastersKeepGamePlatforms.SW,
        KeymastersKeepGamePlatforms.PS4,
        KeymastersKeepGamePlatforms.XONE,
    ]
    is_adult_only_or_unrated = False
    options_cls = LuminesRemasteredArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return list()

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        objectives = [
            GameObjectiveTemplate(
                label="Reach level LEVEL in Basic Challenge mode",
                data={"LEVEL": (self.basic_early, 1)},
                is_time_consuming=False,
                is_difficult=False,
                weight=4
            ),
            GameObjectiveTemplate(
                label="Reach level LEVEL in Basic Challenge mode",
                data={"LEVEL": (self.basic_later, 1)},
                is_time_consuming=True,
                is_difficult=False,
                weight=2
            ),
            GameObjectiveTemplate(
                label="Clear at least CONDITION Time Attack",
                data={"CONDITION": (self.time_attack_easy, 1)},
                is_time_consuming=False,
                is_difficult=False,
                weight=4
            ),
            GameObjectiveTemplate(
                label="Clear at least CONDITION Time Attack",
                data={"CONDITION": (self.time_attack_hard, 1)},
                is_time_consuming=False,
                is_difficult=True,
                weight=4
            ),
            GameObjectiveTemplate(
                label="Win STAGE of VS CPU",
                data={"STAGE": (self.cpu_first_group, 1)},
                is_time_consuming=False,
                is_difficult=False,
                weight=2
            ),
            GameObjectiveTemplate(
                label="Win STAGE of VS CPU",
                data={"STAGE": (self.cpu_second_group, 1)},
                is_time_consuming=False,
                is_difficult=True,
                weight=2
            ),
            GameObjectiveTemplate(
                label="Win STAGE of VS CPU",
                data={"STAGE": (self.cpu_third_group, 1)},
                is_time_consuming=True,  # honestly probably less time-consuming than level 30 basic but oh well
                is_difficult=True,
                weight=1
            ),
            GameObjectiveTemplate(
                label="Complete puzzle PEASY",
                data={"PEASY": (self.puzzles_easy, 1)},
                is_time_consuming=False,
                is_difficult=False,
                weight=2
            ),
            GameObjectiveTemplate(
                label="Complete mission MEASY",
                data={"MEASY": (self.missions_easy, 1)},
                is_time_consuming=False,
                is_difficult=False,
                weight=2
            ),
        ]
        for i in range(2, 5+1):
            objectives.append(GameObjectiveTemplate(
                label="Complete a lap of a Skin Edit playlist consisting of the following skins: SKINS",
                data={"SKINS": (self.skins, i)},
                is_time_consuming=False,
                is_difficult=False,
                weight=1
            ))

        for i in range(7, 10+1):
            objectives.append(GameObjectiveTemplate(
                label="Complete a lap of a Skin Edit playlist consisting of the following skins: SKINS",
                data={"SKINS": (self.skins, i)},
                is_time_consuming=True,  # also probably less time-consuming than level 30 basic
                is_difficult=False,
                weight=1
            ))

        if self.puzzle_mode_max >= 1:
            objectives.append(GameObjectiveTemplate(
                label="Complete puzzle PHARD",
                data={"PHARD": (self.puzzles_hard, 1)},
                is_time_consuming=False,
                is_difficult=False,
                weight=2
            ))
        if self.puzzle_mode_max >= 2:
            objectives.append(GameObjectiveTemplate(
                label="Complete puzzle PSHARD",
                data={"PSHARD": (self.puzzles_superhard, 1)},
                is_time_consuming=False,
                is_difficult=True,
                weight=2
            ))

        if self.mission_mode_max >= 1:
            objectives.append(GameObjectiveTemplate(
                label="Complete mission MHARD",
                data={"MHARD": (self.missions_hard, 1)},
                is_time_consuming=False,
                is_difficult=False,
                weight=2
            ))
        if self.mission_mode_max >= 2:
            objectives.append(GameObjectiveTemplate(
                label="Complete mission MSHARD",
                data={"MSHARD": (self.missions_superhard, 1)},
                is_time_consuming=False,
                is_difficult=True,  # not true. but for the sake of consistency.
                weight=2
            ))

        return objectives


    @staticmethod
    def basic_early() -> List[str]:
        return [
            "10", "20", "30"
        ]


    @staticmethod
    def basic_later() -> List[str]:  # was named basic_late but 50 is only half way so can i really call it late?
        return [
            "40", "45", "50"
        ]

    @staticmethod
    def time_attack_easy() -> List[str]:
        return [
            "50 squares in 60sec",
            "150 squares in 180sec",
            "250 squares in 300sec",
        ]

    @staticmethod
    def time_attack_hard() -> List[str]:
        return [
            "70 squares in 60sec",
            "210 squares in 180sec",
            "350 squares in 300sec",
        ]

    @staticmethod
    def cpu_first_group() -> List[str]:
        return [
            "Stage 2", "Stage 3", "Stage 4", "Stage 5"
        ]

    @staticmethod
    def cpu_second_group() -> List[str]:
        return [
            "Stage 6", "Stage 7", "Stage 8"
        ]

    @staticmethod
    def cpu_third_group() -> List[str]:
        return [
            "Stage 10", "Stage 9"
        ]

    @staticmethod
    def puzzles_easy() -> List[str]:
        return [
            "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
            "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
            "21", "22", "23", "24", "25", "26", "27", "28", "29", "30",
            "31", "32", "33", "34", "35", "36", "37", "38", "39", "40",
        ]

    @staticmethod
    def puzzles_hard() -> List[str]:
        return [
            "41", "42", "43", "44", "45", "46", "47", "48", "49", "50",
            "51", "52", "53", "54", "55", "56", "57", "58", "59", "60",
            "61", "62", "63", "64", "65", "66", "67", "68", "69", "70",
        ]

    @staticmethod
    def puzzles_superhard() -> List[str]:
        return [
            "71", "72", "73", "74", "75", "76", "77", "78", "79", "80",
            "81", "82", "83", "84", "85", "86", "87", "88", "89", "90",
            "91", "92", "93", "94", "95", "96", "97", "98", "99", "100",
        ]

    @staticmethod
    def missions_easy() -> List[str]:
        return [
            "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
            "11", "12", "13", "14", "15",
        ]

    @staticmethod
    def missions_hard() -> List[str]:
        return [
            "16", "17", "18", "19", "20",
            "21", "22", "23", "24", "25", "26", "27", "28", "29", "30",
        ]

    @staticmethod
    def missions_superhard() -> List[str]:
        return [
            "31", "32", "33", "34", "35", "36", "37", "38", "39", "40",
            "41", "42", "43", "44", "45", "46", "47", "48", "49", "50",
        ]

    def skins(self) -> List[str]:
        return sorted(self.archipelago_options.lumines_remastered_unlocked_skins.value)

    @property
    def puzzle_mode_max(self) -> int:
        return self.archipelago_options.lumines_remastered_unlocked_puzzles.value

    @property
    def mission_mode_max(self) -> int:
        return self.archipelago_options.lumines_remastered_unlocked_missions.value


class LuminesRemasteredUnlockedSkins(OptionSet):
    """Indicates which skins the player has unlocked for use in Skin Edit mode.
    You should have at least 10 of these unlocked with time-consuming mode on, or 5 without, otherwise generation will likely fail.
    I put these in the code in order to make it easier to sort through but it seems that the order that they show up in the yaml gets randomized when the yaml is made :<"""
    display_name = "Lumines Remastered Unlocked Skins"
    valid_keys = {
        "SHININ\'",
        "URBANIZATION",
        "ROUNDABOUT",
        "SLIPPING",
        "Shake Ya Body",
        "SQUARE DANCE",
        "TALK 2 YOU",
        "JUST...",

        "I hear the music in my soul",
        "Dark Side Beside The River",
        "ABACK",
        "WORKING IN THE HOLE",
        "SISTER WALK",
        "Da-Di-Do",
        "STRANGERS",
        "HOLIDAY IN SUMMER",

        "TAKE A DOG OUT A WALK",  # i didnt even know it was missing the word "ON"
        "Big Elpaso",
        "My Generation",
        "MEGURO",
        "SPIRITS",
        "Get up and Go",
        "FLY INTO THE SKY",
        "Lights",

        "Japanese form",
        "Automobile Industry",
        "Please return my CD",
        "The bird singing in the night",
        "MEKONG",
        "Whoop-De-Do",
        "The SPY loves me",  # me when i play tf2 and i keep getting backstabbed
        "Brash",

        "Chinese restaurant",
        "MOON BEAM",
        "MORNING BEATS",
        "TIN TOY",
        "WATER,FLOWER & LIGHTS",
        "45DEGREES",
        "RODENT",
        "prime factor",
    }

    default = valid_keys


class LuminesRemasteredUnlockedPuzzles(Choice):
    """The maximum difficulty of puzzle that you have unlocked."""
    display_name = "Lumines Remastered Unlocked Puzzles"
    option_easy = 0
    option_hard = 1
    option_super_hard = 2
    default = 2


class LuminesRemasteredUnlockedMissions(Choice):
    """The maximum difficulty of mission that you have unlocked."""
    display_name = "Lumines Remastered Unlocked Missions"
    option_easy = 0
    option_hard = 1
    option_super_hard = 2
    default = 2
