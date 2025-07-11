"""
This type stub file was generated by pyright.
"""

from dataclasses import dataclass
from typing import Any
from aiwolf_nlp_common.packet.info import Info
from aiwolf_nlp_common.packet.request import Request
from aiwolf_nlp_common.packet.setting import Setting
from aiwolf_nlp_common.packet.talk import Talk

"""
This type stub file was generated by pyright.
"""
@dataclass
class Packet:
    """パケットの構造体.

    Attributes:
        request (Request): リクエストの種類.
        info (Info | None): ゲームの設定を示す情報.
        setting (Setting | None): ゲームの設定情報.
        talk_history (list[Talk] | None): トークの履歴を示す情報.
        whisper_history (list[Talk] | None): 囁きの履歴を示す情報.
    """
    request: Request
    info: Info | None
    setting: Setting | None
    talk_history: list[Talk] | None
    whisper_history: list[Talk] | None
    @staticmethod
    def from_dict(obj: Any) -> Packet:
        ...
    


