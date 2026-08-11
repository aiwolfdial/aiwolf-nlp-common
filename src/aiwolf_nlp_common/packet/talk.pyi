from dataclasses import dataclass
from typing import Any

@dataclass
class Talk:
    idx: int
    day: int
    turn: int
    agent: str
    text: str
    skip: bool = ...
    over: bool = ...
    time: int = ...
    @staticmethod
    def from_dict(obj: Any) -> Talk: ...
