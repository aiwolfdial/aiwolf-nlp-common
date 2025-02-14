from dataclasses import dataclass
from typing import Any


@dataclass
class Vote:
    """投票の内容を示す情報の構造体.

    Attributes:
        day (int): 投票が行われた日数.
        agent (str): 投票を行ったエージェントのインデックス付き文字列.
        target (str): 投票の対象となったエージェントのインデックス付き文字列.
    """

    day: int
    agent: str
    target: str

    @staticmethod
    def from_dict(obj: Any) -> "Vote":  # noqa: ANN401
        _day = int(obj.get("day"))
        _agent = str(obj.get("agent"))
        _target = str(obj.get("target"))
        return Vote(_day, _agent, _target)
