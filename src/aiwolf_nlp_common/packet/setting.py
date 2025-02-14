from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from aiwolf_nlp_common.packet.role import Role


@dataclass
class Setting:
    player_num: int
    role_num_map: dict[Role, int]
    max_talk: int
    max_talk_turn: int
    max_whisper: int
    max_whisper_turn: int
    max_skip: int
    is_enabled_no_attack: bool
    is_vote_visible: bool
    is_talk_on_first_day: bool
    response_timeout: int
    action_timeout: int
    max_revote: int
    max_attack_revote: int

    @staticmethod
    def from_dict(obj: Any) -> Setting:  # noqa: ANN401
        _player_num = int(obj.get("playerNum"))
        _role_num_map = {Role(k): int(v) for k, v in obj.get("roleNumMap").items()}
        _max_talk = int(obj.get("maxTalk"))
        _max_talk_turn = int(obj.get("maxTalkTurn"))
        _max_whisper = int(obj.get("maxWhisper"))
        _max_whisper_turn = int(obj.get("maxWhisperTurn"))
        _max_skip = int(obj.get("maxSkip"))
        _is_enabled_no_attack = bool(obj.get("isEnableNoAttack"))
        _is_vote_visible = bool(obj.get("isVoteVisible"))
        _is_talk_on_first_day = bool(obj.get("isTalkOnFirstDay"))
        _response_timeout = int(obj.get("responseTimeout"))
        _action_timeout = int(obj.get("actionTimeout"))
        _max_revote = int(obj.get("maxRevote"))
        _max_attack_revote = int(obj.get("maxAttackRevote"))
        return Setting(
            _player_num,
            _role_num_map,
            _max_talk,
            _max_talk_turn,
            _max_whisper,
            _max_whisper_turn,
            _max_skip,
            _is_enabled_no_attack,
            _is_vote_visible,
            _is_talk_on_first_day,
            _response_timeout,
            _action_timeout,
            _max_revote,
            _max_attack_revote,
        )
