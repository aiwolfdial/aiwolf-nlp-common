from dataclasses import dataclass
from typing import Any


@dataclass
class Talk:
    idx: int
    day: int
    turn: int
    agent: str
    text: str

    @staticmethod
    def from_dict(obj: Any) -> "Talk":  # noqa: ANN401
        _idx = int(obj.get("idx"))
        _day = int(obj.get("day"))
        _turn = int(obj.get("turn"))
        _agent = str(obj.get("agent"))
        _text = str(obj.get("text"))
        return Talk(_idx, _day, _turn, _agent, _text)
