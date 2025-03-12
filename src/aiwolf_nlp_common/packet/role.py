from enum import Enum


class Team(str, Enum):
    """陣営を示す列挙型.

    Attributes:
        VILLAGER (str): 市民陣営.
        WEREWOLF (str): 人狼陣営.
    """

    VILLAGER = "VILLAGER"
    WEREWOLF = "WEREWOLF"


class Species(str, Enum):
    """種族を示す列挙型.

    Attributes:
        HUMAN (str): 人間.
        WEREWOLF (str): 人狼.
    """

    HUMAN = "HUMAN"
    WEREWOLF = "WEREWOLF"


class Role(str, Enum):
    """役職を示す列挙型.

    Attributes:
        WEREWOLF (str): 人狼.
        POSSESSED (str): 狂人.
        SEER (str): 占い師.
        BODYGUARD (str): 騎士.
        VILLAGER (str): 村人.
        MEDIUM (str): 霊媒師.
    """

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
