from __future__ import annotations

from enum import Enum


class Request(str, Enum):
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
