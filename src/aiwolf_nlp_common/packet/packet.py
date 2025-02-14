from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from aiwolf_nlp_common.packet.info import Info
from aiwolf_nlp_common.packet.request import Request
from aiwolf_nlp_common.packet.setting import Setting
from aiwolf_nlp_common.packet.talk import Talk


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
    def from_dict(obj: Any) -> Packet:  # noqa: ANN401
        _request = Request(str(obj.get("request")))
        _info = Info.from_dict(obj.get("info")) if obj.get("info") is not None else None
        _setting = (
            Setting.from_dict(obj.get("setting"))
            if obj.get("setting") is not None
            else None
        )
        _talk_history = (
            [Talk.from_dict(y) for y in obj.get("talkHistory")]
            if obj.get("talkHistory") is not None
            else None
        )
        _whisper_history = (
            [Talk.from_dict(y) for y in obj.get("whisperHistory")]
            if obj.get("whisperHistory") is not None
            else None
        )
        return Packet(_request, _info, _setting, _talk_history, _whisper_history)
