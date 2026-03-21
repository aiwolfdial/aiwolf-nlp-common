from aiwolf_nlp_common.packet.info import Info as Info
from aiwolf_nlp_common.packet.request import Request as Request
from aiwolf_nlp_common.packet.setting import Setting as Setting
from aiwolf_nlp_common.packet.talk import Talk as Talk
from dataclasses import dataclass
from typing import Any

@dataclass
class Packet:
    request: Request
    info: Info | None
    setting: Setting | None
    talk_history: list[Talk] | None
    whisper_history: list[Talk] | None
    new_talk: Talk | None = ...
    new_whisper: Talk | None = ...
    @staticmethod
    def from_dict(obj: Any) -> Packet: ...
