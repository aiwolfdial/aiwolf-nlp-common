import json

from aiwolf_nlp_common.packet import Info
from aiwolf_nlp_common.packet.role import Role
from aiwolf_nlp_common.packet.status import Status


def test_info() -> None:
    value = json.loads(
        """{"gameID":"ExampleGameId","day":0,"agent":"Agent[01]","statusMap":{"Agent[01]":"ALIVE","Agent[02]":"ALIVE","Agent[03]":"ALIVE","Agent[04]":"ALIVE","Agent[05]":"ALIVE"},"roleMap":{"Agent[01]":"WEREWOLF"}}""",
    )
    info = Info.from_dict(value)

    assert info.game_id == "ExampleGameId"
    assert info.day == 0
    assert info.agent == "Agent[01]"
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
    assert info.role_map == {"Agent[01]": Role.WEREWOLF}
