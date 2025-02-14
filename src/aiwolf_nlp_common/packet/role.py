from enum import Enum


class Team(str, Enum):
    VILLAGER = "VILLAGER"
    WEREWOLF = "WEREWOLF"
    NONE = "NONE"


class Species(str, Enum):
    HUMAN = "HUMAN"
    WEREWOLF = "WEREWOLF"


class Role(str, Enum):
    WEREWOLF = "WEREWOLF"
    POSSESSED = "POSSESSED"
    SEER = "SEER"
    BODYGUARD = "BODYGUARD"
    VILLAGER = "VILLAGER"
    MEDIUM = "MEDIUM"

    @property
    def team(self) -> Team:
        if self in [Role.WEREWOLF, Role.POSSESSED]:
            return Team.WEREWOLF
        return Team.VILLAGER

    @property
    def species(self) -> Species:
        if self == Role.WEREWOLF:
            return Species.WEREWOLF
        return Species.HUMAN
