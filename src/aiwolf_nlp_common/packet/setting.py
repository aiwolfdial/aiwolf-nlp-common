from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from aiwolf_nlp_common.packet.role import Role


@dataclass
class Setting:
    """ゲームの設定を示す情報の構造体.

    Attributes:
        player_num (int): ゲームのプレイヤー数.
        role_num_map (dict[Role, int]): 各役職の人数を示すマップ.
        max_talk (int): 1日あたりの1エージェントの最大発言数 (トーク).
        max_talk_turn (int): 1日あたりの全体の発言回数 (トーク).
        max_whisper (int): 1日あたりの1エージェントの最大囁き数.
        max_whisper_turn (int): 1日あたりの全体の囁き回数.
        max_skip (int): 1日あたりの全体のスキップ回数 (トークと囁きのスキップ回数は区別してカウントされる).
        is_enabled_no_attack (bool): 襲撃なしの日を許可するか.
        is_vote_visible (bool): 投票の結果を公開するか.
        is_talk_on_first_day (bool): 1日目の発言を許可するか.
        response_timeout (int): エージェントのアクションのタイムアウト時間 (秒).
        action_timeout (int): エージェントの生存確認のタイムアウト時間 (秒).
        max_revote (int): 1位タイの場合の最大再投票回数.
        max_attack_revote (int): 1位タイの場合の最大襲撃再投票回数.
    """  # noqa: E501

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
        _response_timeout = int(obj.get("responseTimeout")) // 1000
        _action_timeout = int(obj.get("actionTimeout")) // 1000
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
