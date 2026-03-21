from dataclasses import dataclass
from typing import Any

@dataclass
class Vote:
    day: int
    agent: str
    target: str
    @staticmethod
    def from_dict(obj: Any) -> Vote: ...
