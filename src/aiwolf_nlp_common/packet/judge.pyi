from aiwolf_nlp_common.packet.role import Species as Species
from dataclasses import dataclass
from typing import Any

@dataclass
class Judge:
    day: int
    agent: str
    target: str
    result: Species
    @staticmethod
    def from_dict(obj: Any) -> Judge: ...
