from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from aiwolf_nlp_common.packet.judge import Judge
from aiwolf_nlp_common.packet.role import Role
from aiwolf_nlp_common.packet.status import Status
from aiwolf_nlp_common.packet.vote import Vote


@dataclass
class Info:
    day: int
    agent: str | None
    medium_result: Judge | None
    divine_result: Judge | None
    executed_agent: str | None
    attacked_agent: str | None
    vote_list: list[Vote] | None
    attack_vote_list: list[Vote] | None
    status_map: dict[str, Status] | None
    role_map: dict[str, Role] | None

    @staticmethod
    def from_dict(obj: Any) -> Info:  # noqa: ANN401
        _day = int(obj.get("day"))
        _agent = str(obj.get("agent")) if obj.get("agent") is not None else None
        _medium_result = (
            Judge.from_dict(obj.get("mediumResult"))
            if obj.get("mediumResult") is not None
            else None
        )
        _divine_result = (
            Judge.from_dict(obj.get("divineResult"))
            if obj.get("divineResult") is not None
            else None
        )
        _executed_agent = (
            str(obj.get("executedAgent"))
            if obj.get("executedAgent") is not None
            else None
        )
        _attacked_agent = (
            str(obj.get("attackedAgent"))
            if obj.get("attackedAgent") is not None
            else None
        )
        _vote_list = (
            [Vote.from_dict(y) for y in obj.get("voteList")]
            if obj.get("voteList") is not None
            else None
        )
        _attack_vote_list = (
            [Vote.from_dict(y) for y in obj.get("attackVoteList")]
            if obj.get("attackVoteList") is not None
            else None
        )
        _status_map = (
            {k: Status(v) for k, v in obj.get("statusMap").items()}
            if obj.get("statusMap") is not None
            else None
        )
        _role_map = (
            {k: Role(v) for k, v in obj.get("roleMap").items()}
            if obj.get("roleMap") is not None
            else None
        )
        return Info(
            _day,
            _agent,
            _medium_result,
            _divine_result,
            _executed_agent,
            _attacked_agent,
            _vote_list,
            _attack_vote_list,
            _status_map,
            _role_map,
        )
