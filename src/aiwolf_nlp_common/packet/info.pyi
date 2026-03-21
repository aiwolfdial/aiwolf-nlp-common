from aiwolf_nlp_common.packet.judge import Judge as Judge
from aiwolf_nlp_common.packet.role import Role as Role
from aiwolf_nlp_common.packet.status import Status as Status
from aiwolf_nlp_common.packet.vote import Vote as Vote
from dataclasses import dataclass
from typing import Any

@dataclass
class Info:
    game_id: str
    day: int
    agent: str
    profile: str | None
    medium_result: Judge | None
    divine_result: Judge | None
    executed_agent: str | None
    attacked_agent: str | None
    vote_list: list[Vote] | None
    attack_vote_list: list[Vote] | None
    status_map: dict[str, Status]
    role_map: dict[str, Role]
    remain_count: int | None = ...
    remain_length: int | None = ...
    remain_skip: int | None = ...
    @staticmethod
    def from_dict(obj: Any) -> Info: ...
