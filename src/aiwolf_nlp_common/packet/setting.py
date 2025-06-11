from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from aiwolf_nlp_common.packet.role import Role


@dataclass
class TalkMaxCount:
    per_agent: int
    per_day: int


@dataclass
class TalkMaxLength:
    count_in_word: bool | None
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
    """ゲームの設定を示す情報の構造体.

    Attributes:
        agent_count (int): ゲームのプレイヤー数.
        max_day (int | None): ゲーム内の最大日数. 制限がない場合は None.
        role_num_map (dict[Role, int]): 各役職の人数を示すマップ.
        vote_visibility (bool): 投票の結果を公開するか.
        talk.max_count.per_agent (int): 1日あたりの1エージェントの最大発言回数.
        talk.max_count.per_day (int): 1日あたりの全体の発言回数.
        talk.max_length.count_in_word (bool | None): 単語数でカウントするか. 設定されない場合は None.
        talk.max_length.per_talk (int | None): 1回のトークあたりの最大文字数. 制限がない場合は None.
        talk.max_length.mention_length (int | None): 1回のトークあたりのメンションを含む場合の追加文字数. per_talk の制限がない場合は None.
        talk.max_length.per_agent (int | None): 1日あたりの1エージェントの最大文字数. 制限がない場合は None.
        talk.max_length.base_length (int | None): 1日あたりの1エージェントの最大文字数に含まない最低文字数. 制限がない場合は None.
        talk.max_skip (int): 1日あたりの1エージェントの最大スキップ回数.
        whisper.max_count.per_agent (int): 1日あたりの1エージェントの最大囁き回数.
        whisper.max_count.per_day (int): 1日あたりの全体の囁き回数.
        whisper.max_length.count_in_word (bool | None): 単語数でカウントするか. 設定されない場合は None.
        whisper.max_length.per_talk (int | None): 1回のトークあたりの最大文字数. 制限がない場合は None.
        whisper.max_length.mention_length (int | None): 1回のトークあたりのメンションを含む場合の追加文字数. per_talk の制限がない場合は None.
        whisper.max_length.per_agent (int | None): 1日あたりの1エージェントの最大文字数. 制限がない場合は None.
        whisper.max_length.base_length (int | None): 1日あたりの1エージェントの最大文字数に含まない最低文字数. 制限がない場合は None.
        whisper.max_skip (int): 1日あたりの1エージェントの最大スキップ回数.
        vote.max_count (int): 1位タイの場合の最大再投票回数.
        vote.allow_self_vote (bool): 自己投票を許可するか.
        attack_vote.max_count (int): 1位タイの場合の最大襲撃再投票回数.
        attack_vote.allow_self_vote (bool): 自己投票を許可するか.
        attack_vote.allow_no_target (bool): 襲撃なしの日を許可するか.
        timeout.action (int): エージェントのアクションのタイムアウト時間 (ミリ秒).
        timeout.response (int): エージェントの生存確認のタイムアウト時間 (ミリ秒).
    """  # noqa: E501

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
    def from_dict(obj: Any) -> Setting:  # noqa: ANN401
        def parse_optional_bool(obj: dict, key: str) -> bool | None:
            value = obj.get(key)
            return bool(value) if value is not None else None

        def parse_optional_int(obj: dict, key: str) -> int | None:
            value = obj.get(key)
            return int(value) if value is not None else None

        _agent_count = int(obj.get("agent_count"))
        _max_day = parse_optional_int(obj, "max_day")
        _role_num_map = {Role(k): int(v) for k, v in obj.get("role_num_map").items()}
        _vote_visibility = bool(obj.get("vote_visibility"))

        talk_obj = obj.get("talk", {})
        talk_max_count_obj = talk_obj.get("max_count", {})
        talk_max_length_obj = talk_obj.get("max_length", {})
        _talk_max_count = TalkMaxCount(
            per_agent=int(talk_max_count_obj.get("per_agent", 0)),
            per_day=int(talk_max_count_obj.get("per_day", 0)),
        )
        _talk_max_length = TalkMaxLength(
            count_in_word=parse_optional_bool(talk_max_length_obj, "count_in_word"),
            per_talk=parse_optional_int(talk_max_length_obj, "per_talk"),
            mention_length=parse_optional_int(talk_max_length_obj, "mention_length"),
            per_agent=parse_optional_int(talk_max_length_obj, "per_agent"),
            base_length=parse_optional_int(talk_max_length_obj, "base_length"),
        )
        _talk = Talk(
            max_count=_talk_max_count,
            max_length=_talk_max_length,
            max_skip=int(talk_obj.get("max_skip", 0)),
        )

        whisper_obj = obj.get("whisper", {})
        whisper_max_count_obj = whisper_obj.get("max_count", {})
        whisper_max_length_obj = whisper_obj.get("max_length", {})
        _whisper_max_count = WhisperMaxCount(
            per_agent=int(whisper_max_count_obj.get("per_agent", 0)),
            per_day=int(whisper_max_count_obj.get("per_day", 0)),
        )
        _whisper_max_length = WhisperMaxLength(
            count_in_word=parse_optional_bool(whisper_max_length_obj, "count_in_word"),
            per_talk=parse_optional_int(whisper_max_length_obj, "per_talk"),
            mention_length=parse_optional_int(whisper_max_length_obj, "mention_length"),
            per_agent=parse_optional_int(whisper_max_length_obj, "per_agent"),
            base_length=parse_optional_int(whisper_max_length_obj, "base_length"),
        )
        _whisper = Whisper(
            max_count=_whisper_max_count,
            max_length=_whisper_max_length,
            max_skip=int(whisper_obj.get("max_skip", 0)),
        )

        vote_obj = obj.get("vote", {})
        _vote = Vote(
            max_count=int(vote_obj.get("max_count", 0)),
            allow_self_vote=bool(vote_obj.get("allow_self_vote", False)),
        )

        attack_vote_obj = obj.get("attack_vote", {})
        _attack_vote = AttackVote(
            max_count=int(attack_vote_obj.get("max_count", 0)),
            allow_self_vote=bool(attack_vote_obj.get("allow_self_vote", False)),
            allow_no_target=bool(attack_vote_obj.get("allow_no_target", False)),
        )

        timeout_obj = obj.get("timeout", {})
        _timeout = Timeout(
            action=int(timeout_obj.get("action", 0)),
            response=int(timeout_obj.get("response", 0)),
        )
        return Setting(
            _agent_count,
            _max_day,
            _role_num_map,
            _vote_visibility,
            _talk,
            _whisper,
            _vote,
            _attack_vote,
            _timeout,
        )
