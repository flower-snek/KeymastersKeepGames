from __future__ import annotations

from typing import List

from dataclasses import dataclass

from Options import Toggle

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class RiichiMahjongArchipelagoOptions:
    riichi_mahjong_include_yakuman: RiichiMahjongIncludeYakuman


class RiichiMahjongGame(Game):
    name = "Riichi Mahjong"
    platform = KeymastersKeepGamePlatforms.BOARD
    platforms_other = [
        KeymastersKeepGamePlatforms.PC,
    ]

    is_adult_only_or_unrated = False

    options_cls = RiichiMahjongArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return list()
    
    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        objectives = [
            GameObjectiveTemplate(
                label="Win a hand using the yaku YAKU",
                data={"YAKU": (self.common_yaku, 1)},
                is_time_consuming=False,
                is_difficult=False,
                weight=30,
            ),
            GameObjectiveTemplate(
                label="Win a hand using the yaku YAKU",
                data={"YAKU": (self.medium_yaku, 1)},
                is_time_consuming=False,
                is_difficult=True,
                weight=21,
            ),
            GameObjectiveTemplate(
                label="Win a hand using the yaku YAKU",
                data={"YAKU": (self.rare_yaku, 1)},
                is_time_consuming=True,
                is_difficult=True,
                weight=8,
            ),
            GameObjectiveTemplate(
                label="Win a hand with exactly DORA dora tiles (including dora, ura dora, red fives, and kita)",
                data={"DORA": (self.dora_easy, 1)},
                is_time_consuming=False,
                is_difficult=False,
                weight=12,
            ),
            GameObjectiveTemplate(
                label="Win a hand with exactly DORA dora tiles (including dora, ura dora, red fives, and kita)",
                data={"DORA": (self.dora_hard, 1)},
                is_time_consuming=False,
                is_difficult=True,
                weight=6,
            ),
            GameObjectiveTemplate(
                label="Get either first or second place in a MODE game",
                data={"MODE": (self.player_mode, 1)},
                is_time_consuming=False,
                is_difficult=False,
                weight=10,
            ),
            GameObjectiveTemplate(
                label="Get first place a MODE game",
                data={"MODE": (self.player_mode, 1)},
                is_time_consuming=False,
                is_difficult=True,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Win a mangan (or greater) hand in a 4 player game",
                data={},
                is_time_consuming=False,
                is_difficult=False,
                weight=6,
            ),
            GameObjectiveTemplate(
                label="Win a haneman (or greater) hand in a 3 player game",
                data={},
                is_time_consuming=False,
                is_difficult=False,
                weight=6,
            ),
            GameObjectiveTemplate(
                label="Win a haneman (or greater) hand in a 4 player game",
                data={},
                is_time_consuming=False,
                is_difficult=True,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Win a baiman (or greater) hand in a 3 player game",
                data={},
                is_time_consuming=False,
                is_difficult=True,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Win a hand after making 4 calls, leaving a single tile in your hand",
                data={},
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="Win a hand after declaring kan twice",
                data={},
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="Win a hand by declaring riichi after another player has already declared riichi",
                data={},
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="Win a hand with a 3-or-more-sided wait",
                data={},
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="Win a hand with a 4-or-more-sided wait",
                data={},
                is_time_consuming=False,
                is_difficult=True,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Win a hand with at least 4 unique yaku",
                data={},
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="Win a hand with at least 6 unique yaku",
                data={},
                is_time_consuming=False,
                is_difficult=True,
                weight=2,
            ),
        ]
        if self.yakuman_enabled():
            objectives.append(GameObjectiveTemplate(
                label="Win a yakuman hand",
                data={},
                is_time_consuming=True,
                is_difficult=True,
                weight=1,
            ))

        return objectives
    
    @staticmethod
    def common_yaku() -> List[str]:
        return ["Any Yakuhai (Any value wind / dragon triplet)",
                "Tanyao (All Simples)",
                "Riichi",
                "Menzen Tsumo (Fully Concealed Hand)",
                "Pinfu",
                "Ippatsu"]
    
    @staticmethod
    def medium_yaku() -> List[str]:
        return ["Honitsu (Half Flush)",
                "Toitoi (All Triplets)",
                "Chiitoitsu (Seven Pairs)",
                "Ittsuu (Pure Straight)",
                "Iipeikou (Pure Double Sequence)",
                "Chanta (Half Outside Hand)",
                "Sanshoku Doujun (Mixed Triple Sequence)"]
    
    @staticmethod
    def rare_yaku() -> List[str]:
        return ["Chinitsu (Full Flush)",
                "San ankou (Three Concealed Triplets)",
                "Junchan (Fully Outside Hand)",
                "Shousangen (Little Three Dragons)",
                "Double Riichi",
                "Rinshan (After a Kan)",
                "Haitei Raoyue (Under the Sea)",
                "Houtei Raoyui (Under the River)"]

    @staticmethod
    def player_mode() -> List[str]:
        return [
            "3 player",
            "4 player"
        ]

    @staticmethod
    def dora_easy() -> List[str]:
        return [
            "1", "2", "3"
        ]

    @staticmethod
    def dora_hard() -> List[str]:
        return [
            "4", "5", "6"
        ]

    @property
    def yakuman_enabled(self):
        return self.archipelago_options.riichi_mahjong_include_yakuman

class RiichiMahjongIncludeYakuman(Toggle):
    """Whether there should be a very rare objective that requires getting a yakuman. This isn't *completely* unreasonable in 3 player, but it can still be frustrating."""
    display_name = "Riichi Mahjong Include Yakuman"
