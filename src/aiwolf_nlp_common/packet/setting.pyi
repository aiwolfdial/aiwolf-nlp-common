from aiwolf_nlp_common.packet.role import Role as Role
from dataclasses import dataclass
from typing import Any

@dataclass
class TalkMaxCount:
    per_agent: int
    per_day: int

@dataclass
class TalkMaxLength:
    count_in_word: bool | None
    count_spaces: bool | None
    per_talk: int | None
    mention_length: int | None
    per_agent: int | None
    base_length: int | None

@dataclass
class Talk:
    max_count: TalkMaxCount
    max_length: TalkMaxLength
    max_skip: int

@dataclass
class WhisperMaxCount:
    per_agent: int
    per_day: int

@dataclass
class WhisperMaxLength:
    count_in_word: bool | None
    count_spaces: bool | None
    per_talk: int | None
    mention_length: int | None
    per_agent: int | None
    base_length: int | None

@dataclass
class Whisper:
    max_count: WhisperMaxCount
    max_length: WhisperMaxLength
    max_skip: int

@dataclass
class Vote:
    max_count: int
    allow_self_vote: bool

@dataclass
class AttackVote:
    max_count: int
    allow_self_vote: bool
    allow_no_target: bool

@dataclass
class Timeout:
    action: int
    response: int

@dataclass
class Setting:
    agent_count: int
    max_day: int | None
    role_num_map: dict[Role, int]
    vote_visibility: bool
    talk: Talk
    whisper: Whisper
    vote: Vote
    attack_vote: AttackVote
    timeout: Timeout
    @staticmethod
    def from_dict(obj: Any) -> Setting: ...
