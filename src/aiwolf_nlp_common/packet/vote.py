from dataclasses import dataclass
from typing import Any


@dataclass
class Vote:
    day: int
    agent: str
    target: str

    @staticmethod
    def from_dict(obj: Any) -> "Vote":  # noqa: ANN401
        _day = int(obj.get("day"))
        _agent = str(obj.get("agent"))
        _target = str(obj.get("target"))
        return Vote(_day, _agent, _target)
