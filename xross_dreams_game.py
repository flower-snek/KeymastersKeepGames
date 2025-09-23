from __future__ import annotations

import functools

from typing import List

from dataclasses import dataclass

from Options import OptionSet, Toggle

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class XrossDreamsArchipelagoOptions:
    pass


class XrossDreamsGame(Game):
    name = "Xross Dreams"

    platform = KeymastersKeepGamePlatforms.PC
    is_adult_only_or_unrated = False
    options_cls = XrossDreamsArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return list()

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                # first 3 chapters of any story
                label="Complete CHAPTER of CHARACTER's story",
                data={"CHAPTER": (self.early_chapters, 1), "CHARACTER": (self.characters, 1)},
                is_time_consuming=False,
                is_difficult=False,
                weight=10
            ),
            GameObjectiveTemplate(
                # chapter 4-5 of any story
                label="Complete CHAPTER of CHARACTER's story",
                data={"CHAPTER": (self.mid_chapters, 1), "CHARACTER": (self.characters, 1)},
                is_time_consuming=False,
                is_difficult=False,  # maaaaaybe worth a difficult tag bc of hive/dino (one of them idr off the top of my head) but most are fine
                weight=6
            ),
            GameObjectiveTemplate(
                # chapter 6 of any story
                label="Complete Chapter 6 of CHARACTER's story",
                data={"CHARACTER": (self.characters, 1)},
                is_time_consuming=False,
                is_difficult=True,  # some of these arent bad but some are messed up (staring at hive/dino)
                weight=2
            ),
            GameObjectiveTemplate(
                # finale
                label="Complete the finale using the following character on your team: CHARACTERS",
                data={"CHARACTER": (self.characters, 1)},
                is_time_consuming=False,
                is_difficult=True,  # honestly not that hard if you know how to solo as certain characters (*cough* robot) but i'll put it in difficult just to be careful
                weight=1
            ),
            GameObjectiveTemplate(
                # finale but you might have to do journey/dino (gl lol!!!!)
                label="Complete the finale using the following two characters: CHARACTERS",
                data={"CHARACTERS": (self.characters, 2)},
                is_time_consuming=False,
                is_difficult=True,  # now THIS is actually super hard if you get a bad roll
                weight=1
            ),
            GameObjectiveTemplate(
                label="Complete all of CHARACTER's story, from start to finish",
                data={"CHARACTER": (self.characters, 1)},
                is_time_consuming=True,
                is_difficult=True,  # really stage 6 (and 5 in the few where that's arguably harder) is the only one that matters
                weight=1
            ),
        ]


    @staticmethod
    def characters() -> List[str]:
        return [
            "Fighter",
            "Robot",
            "Goddess",
            "Journey",
            "Astronaut",
            "Skeleton",
            "Thinker",
            "Comet",
            "Hive",
            "Dinosaur",
        ]

    @staticmethod
    def early_chapters() -> List[str]:
        return [
            "Chapter 1",
            "Chapter 2",
            "Chapter 3",
        ]

    @staticmethod
    def mid_chapters() -> List[str]:
        return [
            "Chapter 4",
            "Chapter 5",
        ]

