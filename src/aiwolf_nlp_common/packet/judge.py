from dataclasses import dataclass
from typing import Any

from aiwolf_nlp_common.packet.role import Species


@dataclass
class Judge:
    day: int
    agent: str
    target: str
    result: Species

    @staticmethod
    def from_dict(obj: Any) -> "Judge":  # noqa: ANN401
        _day = int(obj.get("day"))
        _agent = str(obj.get("agent"))
        _target = str(obj.get("target"))
        _result = Species(obj.get("result"))
        return Judge(_day, _agent, _target, _result)
