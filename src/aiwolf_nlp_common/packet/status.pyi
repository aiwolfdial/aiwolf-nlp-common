"""
This type stub file was generated by pyright.
"""

from enum import Enum

"""
This type stub file was generated by pyright.
"""
class Status(str, Enum):
    """エージェントの生存状態を示す列挙型.

    Attributes:
        ALIVE (str): 生存している.
        DEAD (str): 死亡している.
    """
    ALIVE = ...
    DEAD = ...


