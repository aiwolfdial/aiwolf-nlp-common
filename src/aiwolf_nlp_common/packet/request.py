from __future__ import annotations

from enum import Enum


class Request(str, Enum):
    """リクエストの種類を示す列挙型.

    Attributes:
        NAME (str): 名前リクエスト.
        TALK (str): トークリクエスト.
        WHISPER (str): 囁きリクエスト.
        VOTE (str): 投票リクエスト.
        DIVINE (str): 占いリクエスト.
        GUARD (str): 護衛リクエスト.
        ATTACK (str): 襲撃リクエスト.
        INITIALIZE (str): ゲーム開始リクエスト.
        DAILY_INITIALIZE (str): 昼開始リクエスト.
        DAILY_FINISH (str): 昼終了リクエスト.
        FINISH (str): ゲーム終了リクエスト.
    """

    NAME = "NAME"
    TALK = "TALK"
    WHISPER = "WHISPER"
    VOTE = "VOTE"
    DIVINE = "DIVINE"
    GUARD = "GUARD"
    ATTACK = "ATTACK"
    INITIALIZE = "INITIALIZE"
    DAILY_INITIALIZE = "DAILY_INITIALIZE"
    DAILY_FINISH = "DAILY_FINISH"
    FINISH = "FINISH"
