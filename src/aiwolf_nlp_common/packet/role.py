from enum import Enum


class Team(str, Enum):
    VILLAGER = "VILLAGER"
    WEREWOLF = "WEREWOLF"
    NONE = "NONE"


class Species(str, Enum):
    HUMAN = "HUMAN"
    WEREWOLF = "WEREWOLF"


class Role(str, Enum):
    WEREWOLF = ("WEREWOLF", Team.WEREWOLF, Species.WEREWOLF)
    POSSESSED = ("POSSESSED", Team.WEREWOLF, Species.HUMAN)
    SEER = ("SEER", Team.VILLAGER, Species.HUMAN)
    BODYGUARD = ("BODYGUARD", Team.VILLAGER, Species.HUMAN)
    VILLAGER = ("VILLAGER", Team.VILLAGER, Species.HUMAN)
    MEDIUM = ("MEDIUM", Team.VILLAGER, Species.HUMAN)

    def __init__(self, value: str, team: Team, species: Species) -> None:
        self._value_ = value
        self.team = team
        self.species = species
