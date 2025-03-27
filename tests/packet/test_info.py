import json

from aiwolf_nlp_common.packet import Info
from aiwolf_nlp_common.packet.role import Role
from aiwolf_nlp_common.packet.status import Status


def test_info() -> None:
    value = json.loads(
        """{"game_id":"01JQB6KPWSN10HGNBCWXE5AN04","day":0,"agent":"Agent[01]","status_map":{"Agent[01]":"ALIVE","Agent[02]":"ALIVE","Agent[03]":"ALIVE","Agent[04]":"ALIVE","Agent[05]":"ALIVE"},"role_map":{"Agent[01]":"POSSESSED"}}""",
    )
    info = Info.from_dict(value)

    assert info.game_id == "01JQB6KPWSN10HGNBCWXE5AN04"
    assert info.day == 0
    assert info.agent == "Agent[01]"
    assert info.profile is None
    assert info.medium_result is None
    assert info.divine_result is None
    assert info.executed_agent is None
    assert info.attacked_agent is None
    assert info.vote_list is None
    assert info.attack_vote_list is None
    assert info.status_map == {
        "Agent[01]": Status.ALIVE,
        "Agent[02]": Status.ALIVE,
        "Agent[03]": Status.ALIVE,
        "Agent[04]": Status.ALIVE,
        "Agent[05]": Status.ALIVE,
    }
    assert info.role_map == {"Agent[01]": Role.POSSESSED}
    assert info.remain_count is None
    assert info.remain_length is None
    assert info.remain_skip is None
