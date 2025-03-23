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
    per_talk: int
    per_agent: int
    base_length: int


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
    per_talk: int
    per_agent: int
    base_length: int


@dataclass
class Whisper:
    max_count: WhisperMaxCount
    max_length: WhisperMaxLength
    max_skip: int


@dataclass
class Vote:
    max_count: int


@dataclass
class AttackVote:
    max_count: int
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
        role_num_map (dict[Role, int]): 各役職の人数を示すマップ.
        vote_visibility (bool): 投票の結果を公開するか.
        talk_on_first_day (bool): 1日目の発言を許可するか.
        talk.max_count.per_agent (int): 1日あたりの1エージェントの最大発言回数.
        talk.max_count.per_day (int): 1日あたりの全体の発言回数.
        talk.max_length.per_talk (int): 1回のトークあたりの最大文字数.
        talk.max_length.per_agent (int): 1日あたりの1エージェントの最大文字数.
        talk.max_length.base_length (int): 1日あたりの1エージェントの最大文字数に含まない最低文字数.
        talk.max_skip (int): 1日あたりの1エージェントの最大スキップ回数.
        whisper.max_count.per_agent (int): 1日あたりの1エージェントの最大囁き回数.
        whisper.max_count.per_day (int): 1日あたりの全体の囁き回数.
        whisper.max_length.per_talk (int): 1回のトークあたりの最大文字数.
        whisper.max_length.per_agent (int): 1日あたりの1エージェントの最大文字数.
        whisper.max_length.base_length (int): 1日あたりの1エージェントの最大文字数に含まない最低文字数.
        whisper.max_skip (int): 1日あたりの1エージェントの最大スキップ回数.
        vote.max_count (int): 1位タイの場合の最大再投票回数.
        attack_vote.max_count (int): 1位タイの場合の最大襲撃再投票回数.
        attack_vote.allow_no_target (bool): 襲撃なしの日を許可するか.
        timeout.action (int): エージェントのアクションのタイムアウト時間 (秒).
        timeout.response (int): エージェントの生存確認のタイムアウト時間 (秒).
    """  # noqa: E501

    agent_count: int
    role_num_map: dict[Role, int]
    vote_visibility: bool
    talk_on_first_day: bool
    talk: Talk
    whisper: Whisper
    vote: Vote
    attack_vote: AttackVote
    timeout: Timeout

    @staticmethod
    def from_dict(obj: Any) -> Setting:  # noqa: ANN401
        _agent_count = int(obj.get("agentCount"))
        _role_num_map = {Role(k): int(v) for k, v in obj.get("roleNumMap").items()}
        _vote_visibility = bool(obj.get("voteVisibility"))
        _talk_on_first_day = bool(obj.get("talkOnFirstDay"))

        talk_obj = obj.get("talk", {})
        talk_max_count_obj = talk_obj.get("maxCount", {})
        talk_max_length_obj = talk_obj.get("maxLength", {})
        _talk_max_count = TalkMaxCount(
            per_agent=int(talk_max_count_obj.get("perAgent", 0)),
            per_day=int(talk_max_count_obj.get("perDay", 0)),
        )
        _talk_max_length = TalkMaxLength(
            per_talk=int(talk_max_length_obj.get("perTalk", 0)),
            per_agent=int(talk_max_length_obj.get("perAgent", 0)),
            base_length=int(talk_max_length_obj.get("baseLength", 0)),
        )
        _talk = Talk(
            max_count=_talk_max_count,
            max_length=_talk_max_length,
            max_skip=int(talk_obj.get("maxSkip", 0)),
        )

        whisper_obj = obj.get("whisper", {})
        whisper_max_count_obj = whisper_obj.get("maxCount", {})
        whisper_max_length_obj = whisper_obj.get("maxLength", {})
        _whisper_max_count = WhisperMaxCount(
            per_agent=int(whisper_max_count_obj.get("perAgent", 0)),
            per_day=int(whisper_max_count_obj.get("perDay", 0)),
        )
        _whisper_max_length = WhisperMaxLength(
            per_talk=int(whisper_max_length_obj.get("perTalk", 0)),
            per_agent=int(whisper_max_length_obj.get("perAgent", 0)),
            base_length=int(whisper_max_length_obj.get("baseLength", 0)),
        )
        _whisper = Whisper(
            max_count=_whisper_max_count,
            max_length=_whisper_max_length,
            max_skip=int(whisper_obj.get("maxSkip", 0)),
        )

        vote_obj = obj.get("vote", {})
        _vote = Vote(
            max_count=int(vote_obj.get("maxCount", 0)),
        )

        attack_vote_obj = obj.get("attackVote", {})
        _attack_vote = AttackVote(
            max_count=int(attack_vote_obj.get("maxCount", 0)),
            allow_no_target=bool(attack_vote_obj.get("allowNoTarget", False)),
        )

        timeout_obj = obj.get("timeout", {})
        _timeout = Timeout(
            action=int(timeout_obj.get("action", 0)) // 1000,
            response=int(timeout_obj.get("response", 0)) // 1000,
        )
        return Setting(
            _agent_count,
            _role_num_map,
            _vote_visibility,
            _talk_on_first_day,
            _talk,
            _whisper,
            _vote,
            _attack_vote,
            _timeout,
        )
