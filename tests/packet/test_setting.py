import json

from aiwolf_nlp_common.packet.role import Role
from aiwolf_nlp_common.packet.setting import Setting


def test_setting() -> None:
    value = json.loads(
        """{"agent_count":13,"max_day":5,"talk_on_first_day":true,"talk":{"max_count":{"per_agent":4,"per_day":28},"max_length":{"count_in_word":false,"mention_length":50,"base_length":50},"max_skip":0},"whisper":{"max_count":{"per_agent":4,"per_day":12},"max_length":{"count_in_word":false,"mention_length":50,"base_length":50},"max_skip":0},"vote":{"max_count":1,"allow_self_vote":true},"attack_vote":{"max_count":1,"allow_self_vote":true,"allow_no_target":false},"timeout":{"action":60000,"response":120000},"role_num_map":{"BODYGUARD":1,"MEDIUM":1,"POSSESSED":1,"SEER":1,"VILLAGER":6,"WEREWOLF":3}}""",
    )
    setting = Setting.from_dict(value)

    assert setting.agent_count == 13
    assert setting.role_num_map == {
        Role.BODYGUARD: 1,
        Role.MEDIUM: 1,
        Role.POSSESSED: 1,
        Role.SEER: 1,
        Role.VILLAGER: 6,
        Role.WEREWOLF: 3,
    }
    assert setting.vote_visibility is False
    assert setting.max_day == 5
    assert setting.talk.max_count.per_agent == 4
    assert setting.talk.max_count.per_day == 28
    assert setting.talk.max_length.count_in_word is False
    assert setting.talk.max_length.per_talk is None
    assert setting.talk.max_length.mention_length == 50
    assert setting.talk.max_length.per_agent is None
    assert setting.talk.max_length.base_length == 50
    assert setting.talk.max_skip == 0
    assert setting.whisper.max_count.per_agent == 4
    assert setting.whisper.max_count.per_day == 12
    assert setting.whisper.max_length.count_in_word is False
    assert setting.whisper.max_length.per_talk is None
    assert setting.whisper.max_length.mention_length == 50
    assert setting.whisper.max_length.per_agent is None
    assert setting.whisper.max_length.base_length == 50
    assert setting.whisper.max_skip == 0
    assert setting.vote.max_count == 1
    assert setting.vote.allow_self_vote is True
    assert setting.attack_vote.max_count == 1
    assert setting.attack_vote.allow_self_vote is True
    assert setting.attack_vote.allow_no_target is False
    assert setting.timeout.action == 60000
    assert setting.timeout.response == 120000
