import json

from aiwolf_nlp_common.packet.judge import Judge
from aiwolf_nlp_common.packet.role import Species


def test_judge() -> None:
    value = json.loads(
        """{"day":0,"agent":"ダイスケ","target":"ミサキ","result":"WEREWOLF"}""",
    )
    judge = Judge.from_dict(value)

    assert judge.day == 0
    assert judge.agent == "ダイスケ"
    assert judge.target == "ミサキ"
    assert judge.result == Species.WEREWOLF
