from dataclasses import dataclass
from enum import StrEnum
from typing import Any, TypeAlias

@dataclass
class Vote:
    day: int
    agent: str
    target: str
    @classmethod
    def from_dict(cls, obj: Any) -> Vote: ...

@dataclass
class Talk:
    idx: int
    day: int
    turn: int
    agent: str
    text: str
    skip: bool
    over: bool
    time: int
    @classmethod
    def from_dict(cls, obj: Any) -> Talk: ...

@dataclass
class SettingTalkMaxCount:
    per_agent: int
    per_day: int
    @classmethod
    def from_dict(cls, obj: Any) -> SettingTalkMaxCount: ...

@dataclass
class SettingTalkMaxLength:
    count_in_word: bool | None = ...
    count_spaces: bool | None = ...
    per_talk: int | None = ...
    mention_length: int | None = ...
    per_agent: int | None = ...
    base_length: int | None = ...
    @classmethod
    def from_dict(cls, obj: Any) -> SettingTalkMaxLength: ...

@dataclass
class SettingVote:
    max_count: int
    allow_self_vote: bool
    @classmethod
    def from_dict(cls, obj: Any) -> SettingVote: ...

@dataclass
class SettingAttackVote:
    max_count: int
    allow_self_vote: bool
    allow_no_target: bool
    @classmethod
    def from_dict(cls, obj: Any) -> SettingAttackVote: ...

@dataclass
class SettingTimeout:
    action: int
    response: int
    @classmethod
    def from_dict(cls, obj: Any) -> SettingTimeout: ...

class Request(StrEnum):
    NAME = 'NAME'
    TALK = 'TALK'
    WHISPER = 'WHISPER'
    VOTE = 'VOTE'
    DIVINE = 'DIVINE'
    GUARD = 'GUARD'
    ATTACK = 'ATTACK'
    INITIALIZE = 'INITIALIZE'
    DAILY_INITIALIZE = 'DAILY_INITIALIZE'
    DAILY_FINISH = 'DAILY_FINISH'
    FINISH = 'FINISH'
    TALK_PHASE_START = 'TALK_PHASE_START'
    TALK_PHASE_END = 'TALK_PHASE_END'
    TALK_BROADCAST = 'TALK_BROADCAST'
    WHISPER_PHASE_START = 'WHISPER_PHASE_START'
    WHISPER_PHASE_END = 'WHISPER_PHASE_END'
    WHISPER_BROADCAST = 'WHISPER_BROADCAST'
    @property
    def require_response(self) -> bool: ...

class Role(StrEnum):
    WEREWOLF = 'WEREWOLF'
    POSSESSED = 'POSSESSED'
    SEER = 'SEER'
    BODYGUARD = 'BODYGUARD'
    VILLAGER = 'VILLAGER'
    MEDIUM = 'MEDIUM'
    @property
    def team(self) -> Team: ...
    @property
    def species(self) -> Species: ...

class Species(StrEnum):
    HUMAN = 'HUMAN'
    WEREWOLF = 'WEREWOLF'

class Team(StrEnum):
    VILLAGER = 'VILLAGER'
    WEREWOLF = 'WEREWOLF'

class Status(StrEnum):
    ALIVE = 'ALIVE'
    DEAD = 'DEAD'

@dataclass
class Judge:
    day: int
    agent: str
    target: str
    result: Species
    @classmethod
    def from_dict(cls, obj: Any) -> Judge: ...

@dataclass
class SettingTalk:
    max_count: SettingTalkMaxCount
    max_length: SettingTalkMaxLength
    max_skip: int
    duration: int | None = ...
    @classmethod
    def from_dict(cls, obj: Any) -> SettingTalk: ...

@dataclass
class Info:
    game_id: str
    day: int
    agent: str
    status_map: dict[str, Status]
    role_map: dict[str, Role]
    profile: str | None = ...
    medium_result: Judge | None = ...
    divine_result: Judge | None = ...
    executed_agent: str | None = ...
    attacked_agent: str | None = ...
    vote_list: list[Vote] | None = ...
    attack_vote_list: list[Vote] | None = ...
    remain_count: int | None = ...
    remain_length: int | None = ...
    remain_skip: int | None = ...
    @classmethod
    def from_dict(cls, obj: Any) -> Info: ...

@dataclass
class Setting:
    agent_count: int
    role_num_map: dict[str, int]
    vote_visibility: bool
    talk: SettingTalk
    whisper: SettingTalk
    vote: SettingVote
    attack_vote: SettingAttackVote
    timeout: SettingTimeout
    max_day: int | None = ...
    @classmethod
    def from_dict(cls, obj: Any) -> Setting: ...

@dataclass
class Packet:
    request: Request
    info: Info | None = ...
    setting: Setting | None = ...
    talk_history: list[Talk] | None = ...
    whisper_history: list[Talk] | None = ...
    new_talk: Talk | None = ...
    new_whisper: Talk | None = ...
    @classmethod
    def from_dict(cls, obj: Any) -> Packet: ...
AiwolfNlpProtocol: TypeAlias = Packet
