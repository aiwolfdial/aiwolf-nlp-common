from aiwolf_nlp_common.packet._models import Setting as Setting, SettingAttackVote, SettingTalk, SettingTalkMaxCount, SettingTalkMaxLength, SettingTimeout, SettingVote

__all__ = ['AttackVote', 'Setting', 'Talk', 'TalkMaxCount', 'TalkMaxLength', 'Timeout', 'Vote', 'Whisper', 'WhisperMaxCount', 'WhisperMaxLength']

Talk = SettingTalk
TalkMaxCount = SettingTalkMaxCount
TalkMaxLength = SettingTalkMaxLength
Whisper = SettingTalk
WhisperMaxCount = SettingTalkMaxCount
WhisperMaxLength = SettingTalkMaxLength
Vote = SettingVote
AttackVote = SettingAttackVote
Timeout = SettingTimeout
