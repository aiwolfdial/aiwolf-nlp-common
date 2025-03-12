import json

from aiwolf_nlp_common.packet.role import Role
from aiwolf_nlp_common.packet.setting import Setting


def test_setting() -> None:
    value = json.loads(
        """{"playerNum":5,"maxTalk":5,"maxTalkTurn":20,"maxWhisper":5,"maxWhisperTurn":20,"maxSkip":0,"isEnableNoAttack":false,"isVoteVisible":false,"isTalkOnFirstDay":true,"responseTimeout":120000,"actionTimeout":60000,"maxRevote":1,"maxAttackRevote":1,"roleNumMap":{"BODYGUARD":0,"MEDIUM":0,"POSSESSED":1,"SEER":1,"VILLAGER":2,"WEREWOLF":1}}""",
    )
    setting = Setting.from_dict(value)

    assert setting.player_num == 5
    assert setting.role_num_map == {
        Role.BODYGUARD: 0,
        Role.MEDIUM: 0,
        Role.POSSESSED: 1,
        Role.SEER: 1,
        Role.VILLAGER: 2,
        Role.WEREWOLF: 1,
    }
    assert setting.max_talk == 5
    assert setting.max_talk_turn == 20
    assert setting.max_whisper == 5
    assert setting.max_whisper_turn == 20
    assert setting.max_skip == 0
    assert setting.is_enabled_no_attack is False
    assert setting.is_vote_visible is False
    assert setting.is_talk_on_first_day is True
    assert setting.response_timeout == 120
    assert setting.action_timeout == 60
    assert setting.max_revote == 1
    assert setting.max_attack_revote == 1
