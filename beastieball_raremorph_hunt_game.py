from __future__ import annotations

from typing import List

from dataclasses import dataclass

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class BeastieballRaremorphArchipelagoOptions:
    pass


class BeastieballRaremorphGame(Game):
    name = "Beastieball Raremorph Hunt"
    platform = KeymastersKeepGamePlatforms.PC

    is_adult_only_or_unrated = False

    options_cls = BeastieballRaremorphArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return list()
    
    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Catch a raremorph beastie in REGION",
                data={"REGION": (self.regions, 1)},
                is_time_consuming=False,
                is_difficult=False,
                weight=8,
            ),
            GameObjectiveTemplate(
                label="Catch (and metamorph, if necessary) a raremorph BEASTIE",
                data={"BEASTIE": (self.beasties, 1)},
                is_time_consuming=True,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Catch (and metamorph, if necessary) a raremorph RAREBEASTIE",
                data={"RAREBEASTIE": (self.rare_beasties, 1)},
                is_time_consuming=True,
                is_difficult=True,
                weight=1,
            ),
        ]
    
    @staticmethod
    def regions() -> List[str]:
        return [
            "Amberstone",
            "Amberstone",
            "Amberstone",
            "the Chroma Sea",
            "the Chroma Sea",
            "the Chroma Sea",
            "Mythwood",
            "Mythwood",
            "Mythwood",
            "Geo City",
            "Geo City",
            "Geo City",
            "the Alto Alps",
            "the Alto Alps",
            "the Alto Alps",
            "the Jasper Mines",  # (cave between Amberstone and Mythwood)
            "the Tawny Wilds",  # (north of Gamboge)
            "the Eburnean Cavern",  # (cave between Chroma Sea and Geo City)
        ]
    
    @staticmethod
    def beasties() -> List[str]:
        return [
            "Collarva",
            "Wormask",
            "Plumask",
            "Shooga",
            "Supassum",
            "Supilero",
            "Sefren",
            "Zefyre",
            "Woollie",
            "Fetcham",
            "Rookee",
            "Garood",
            "Kaleidarn",
            "Platenna",
            "Platypulse",
            "Servitt",
            "Servace",
            "Daredillo",  # probably the only example of an evolved form being here when a pre-evolution is in rare, bc this spawns like 30% of the time in quartz canyon
            "Noizard",
            "Merrifly",
            "Cherrily",
            "Yueffowl",
            "Albrax",
            "Scrubbub",
            "Grubiron",
            "Beetlback",
            "Webbounce",
            "Goofsder",
            "Gastic",  # actually kinda rare but not rare enough to make the rare list
            "Wisper",
            "Mistic",
            "Wottle",  # ok i think this is actually the rarest im willing to go for the common list. 2 just-under-10% spawn rate slots and a bunch of 5%-ish slots w/o attract spray
            "Troglum",
            "Varkabond",
            "Armantis",
            "Grazada",  # ew
            "Seakit",
            "Vultoxin",
            "Turogue",
            "Turtaneer",
            "Tortanchor",
            "Waglash",
            "Riplash",
            "Gullit",
            "Skiffrig",
            "Petula",
            "Flowish",
            "Orgella",
            "Squimage",
            "Crabaret",
            "Leobro",
            "Broslidon",
            "Mudslee",
            "Musselbound",
            "Conjarr",
            "Skibble",
            "Skorock",
            "Boldlur",
            "Milimine",
            "Demolipede",
            "Trat",
            "Punkchirp",
            "Magpike",
            "Calcroach",
            "Debugly",
            "Beelb",
            "Jellibat",
            "Froofulks",
            "Bindiva",
            "Gremlur",
            "Blitzwift",
            "Druppa",
            "Scauldra",
            "Humflit",
            "Heliath",
            "Lunaptra",
            "Deluja",
        ]
    
    @staticmethod
    def rare_beasties() -> List[str]:
        return [
            "Sprecko",
            "Bongus",
            "Surgus",
            "Illugus",
            "Kitchik",
            "Ostrisigh",
            "Kasaleet",
            "Axolati",
            "Hopsong",
            "Hopra",
            "Bildit",
            "Handicoot",
            "Bandicraft",
            "Radillo",  # 3% spawn rate without attract spray??
            "Diggum",  # on the fence about this one. looks like a consistant one-at-a-time spawn which is probably better than some other stuff on this list but worse than basically all of the commons.
            "Crawlurk",
            "Xiphosaur",  # based on the wottle cut-off, barely makes the cut
            "Psylusc",
            "alternate-sprite Trat",  # large can; if you're looking here for a hint, i've heard they spawn more commonly from garbage bins?
            "Opposur",
            "Proteos",
            "Hydrolm",
            "Yamyth",
            "Pladion",
            "Duggout",
            "Mascurry",
            "Diabloceras",
            "Maraptor",
            "Shloom",
        ]


# Archipelago Options
# ...
