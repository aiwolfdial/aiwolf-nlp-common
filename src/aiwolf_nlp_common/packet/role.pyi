from enum import Enum

class Team(str, Enum):
    VILLAGER = 'VILLAGER'
    WEREWOLF = 'WEREWOLF'

class Species(str, Enum):
    HUMAN = 'HUMAN'
    WEREWOLF = 'WEREWOLF'

class Role(str, Enum):
    WEREWOLF = 'WEREWOLF'
    POSSESSED = 'POSSESSED'
    SEER = 'SEER'
    BODYGUARD = 'BODYGUARD'
    VILLAGER = 'VILLAGER'
    MEDIUM = 'MEDIUM'
    @property
    def team(self) -> Team: ...
    @property
    def species(self) -> Species: ...
