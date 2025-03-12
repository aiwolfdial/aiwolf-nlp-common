from dataclasses import dataclass
from typing import Any


@dataclass
class Talk:
    """会話の内容を示す情報の構造体.

    Attributes:
        idx (int): 会話のインデックス.
        day (int): 会話が行われた日数.
        turn (int): 会話が行われたターン数.
        agent (str): 会話を行ったエージェントのインデックス付き文字列.
        text (str): 会話の内容.
        skip (bool): 会話がスキップであるかどうか.
        over (bool): 会話がオーバーであるかどうか.
    """

    idx: int
    day: int
    turn: int
    agent: str
    text: str
    skip: bool = False
    over: bool = False

    @staticmethod
    def from_dict(obj: Any) -> "Talk":  # noqa: ANN401
        _idx = int(obj.get("idx"))
        _day = int(obj.get("day"))
        _turn = int(obj.get("turn"))
        _agent = str(obj.get("agent"))
        _text = str(obj.get("text"))
        _skip = bool(obj.get("skip"))
        _over = bool(obj.get("over"))
        return Talk(_idx, _day, _turn, _agent, _text, _skip, _over)
