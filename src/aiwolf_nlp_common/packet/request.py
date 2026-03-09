from __future__ import annotations

from enum import Enum


class Request(str, Enum):
    """リクエストの種類を示す列挙型.

    Attributes:
        NAME (str): 名前リクエスト.
        TALK (str): トークリクエスト（ターン制モード用）.
        WHISPER (str): 囁きリクエスト（ターン制モード用）.
        VOTE (str): 投票リクエスト.
        DIVINE (str): 占いリクエスト.
        GUARD (str): 護衛リクエスト.
        ATTACK (str): 襲撃リクエスト.
        INITIALIZE (str): ゲーム開始リクエスト.
        DAILY_INITIALIZE (str): 昼開始リクエスト.
        DAILY_FINISH (str): 昼終了リクエスト.
        FINISH (str): ゲーム終了リクエスト.
        TALK_PHASE_START (str): トークフェーズ開始通知（グループチャット方式用）.
        TALK_PHASE_END (str): トークフェーズ終了通知（グループチャット方式用）.
        TALK_BROADCAST (str): トーク配信通知（グループチャット方式用）.
        WHISPER_PHASE_START (str): 囁きフェーズ開始通知（グループチャット方式用）.
        WHISPER_PHASE_END (str): 囁きフェーズ終了通知（グループチャット方式用）.
        WHISPER_BROADCAST (str): 囁き配信通知（グループチャット方式用）.
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
    TALK_PHASE_START = "TALK_PHASE_START"
    TALK_PHASE_END = "TALK_PHASE_END"
    TALK_BROADCAST = "TALK_BROADCAST"
    WHISPER_PHASE_START = "WHISPER_PHASE_START"
    WHISPER_PHASE_END = "WHISPER_PHASE_END"
    WHISPER_BROADCAST = "WHISPER_BROADCAST"
