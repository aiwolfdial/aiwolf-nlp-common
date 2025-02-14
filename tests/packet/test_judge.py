import json

from aiwolf_nlp_common.packet.judge import Judge
from aiwolf_nlp_common.packet.role import Species


def test_judge() -> None:
    value = json.loads(
        """{"day":0,"agent":"Agent[02]","target":"Agent[01]","result":"WEREWOLF"}""",
    )
    judge = Judge.from_dict(value)

    assert judge.day == 0
    assert judge.agent == "Agent[02]"
    assert judge.target == "Agent[01]"
    assert judge.result == Species.WEREWOLF
