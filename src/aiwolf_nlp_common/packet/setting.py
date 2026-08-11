"""スキーマから生成した定義の再エクスポート. 実体は _models.py にあります."""

from aiwolf_nlp_common.packet._models import (
    Setting,
    SettingAttackVote,
    SettingTalk,
    SettingTalkMaxCount,
    SettingTalkMaxLength,
    SettingTimeout,
    SettingVote,
)

Talk = SettingTalk
TalkMaxCount = SettingTalkMaxCount
TalkMaxLength = SettingTalkMaxLength
Whisper = SettingTalk
WhisperMaxCount = SettingTalkMaxCount
WhisperMaxLength = SettingTalkMaxLength
Vote = SettingVote
AttackVote = SettingAttackVote
Timeout = SettingTimeout

__all__ = [
    "AttackVote",
    "Setting",
    "Talk",
    "TalkMaxCount",
    "TalkMaxLength",
    "Timeout",
    "Vote",
    "Whisper",
    "WhisperMaxCount",
    "WhisperMaxLength",
]
