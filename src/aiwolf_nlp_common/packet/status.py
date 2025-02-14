from enum import Enum


class Status(str, Enum):
    """エージェントの生存状態を示す列挙型.

    Attributes:
        ALIVE (str): 生存している.
        DEAD (str): 死亡している.
    """

    ALIVE = "ALIVE"
    DEAD = "DEAD"
