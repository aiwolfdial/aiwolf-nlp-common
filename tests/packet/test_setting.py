import json

from aiwolf_nlp_common.packet.role import Role
from aiwolf_nlp_common.packet.setting import Setting


def test_setting() -> None:
    value = json.loads(
        """{"agent_count":5,"vote_visibility":false,"talk_on_first_day":true,"talk":{"max_count":{"per_agent":5,"per_day":20},"max_length":{},"max_skip":0},"whisper":{"max_count":{"per_agent":5,"per_day":20},"max_length":{},"max_skip":0},"vote":{"max_count":1},"attack_vote":{"max_count":1,"allow_no_target":false},"timeout":{"action":60000,"response":120000},"role_num_map":{"BODYGUARD":0,"MEDIUM":0,"POSSESSED":1,"SEER":1,"VILLAGER":2,"WEREWOLF":1}}""",
    )
    setting = Setting.from_dict(value)

    assert setting.agent_count == 5
    assert setting.role_num_map == {
        Role.BODYGUARD: 0,
        Role.MEDIUM: 0,
        Role.POSSESSED: 1,
        Role.SEER: 1,
        Role.VILLAGER: 2,
        Role.WEREWOLF: 1,
    }
    assert setting.vote_visibility is False
    assert setting.talk_on_first_day is True
    assert setting.talk.max_count.per_agent == 5
    assert setting.talk.max_count.per_day == 20
    assert setting.talk.max_length.per_talk is None
    assert setting.talk.max_length.per_agent is None
    assert setting.talk.max_length.base_length is None
    assert setting.talk.max_skip == 0
    assert setting.whisper.max_count.per_agent == 5
    assert setting.whisper.max_count.per_day == 20
    assert setting.whisper.max_length.per_talk is None
    assert setting.whisper.max_length.per_agent is None
    assert setting.whisper.max_length.base_length is None
    assert setting.whisper.max_skip == 0
    assert setting.vote.max_count == 1
    assert setting.attack_vote.max_count == 1
    assert setting.attack_vote.allow_no_target is False
    assert setting.timeout.action == 60000
    assert setting.timeout.response == 120000
