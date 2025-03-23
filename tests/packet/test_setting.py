import json

from aiwolf_nlp_common.packet.role import Role
from aiwolf_nlp_common.packet.setting import Setting


def test_setting() -> None:
    value = json.loads(
        """{"agentCount":5,"voteVisibility":false,"talkOnFirstDay":true,"talk":{"maxCount":{"perAgent":5,"perDay":20},"maxLength":{"perTalk":-1,"perAgent":-1,"baseLength":0},"maxSkip":0},"whisper":{"maxCount":{"perAgent":5,"perDay":20},"maxLength":{"perTalk":-1,"perAgent":-1,"baseLength":0},"maxSkip":0},"vote":{"maxCount":1},"attackVote":{"maxCount":1,"allowNoTarget":false},"timeout":{"action":60000,"response":120000},"roleNumMap":{"BODYGUARD":0,"MEDIUM":0,"POSSESSED":1,"SEER":1,"VILLAGER":2,"WEREWOLF":1}}""",
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
    assert setting.talk.max_length.per_talk == -1
    assert setting.talk.max_length.per_agent == -1
    assert setting.talk.max_length.base_length == 0
    assert setting.talk.max_skip == 0
    assert setting.whisper.max_count.per_agent == 5
    assert setting.whisper.max_count.per_day == 20
    assert setting.whisper.max_length.per_talk == -1
    assert setting.whisper.max_length.per_agent == -1
    assert setting.whisper.max_length.base_length == 0
    assert setting.whisper.max_skip == 0
    assert setting.vote.max_count == 1
    assert setting.attack_vote.max_count == 1
    assert setting.attack_vote.allow_no_target is False
    assert setting.timeout.action == 60
    assert setting.timeout.response == 120
