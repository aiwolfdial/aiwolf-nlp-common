import json

from aiwolf_nlp_common.packet.talk import Talk


def test_talk_list() -> None:
    value = json.loads(
        """{"talk_history":[{"idx":0,"day":1,"turn":0,"agent":"ヴィクトリア","text":"866cd7648816a1c51fb0817996400a6c","skip":false,"over":false},{"idx":1,"day":1,"turn":0,"agent":"リュウジ","text":"5ad0c6227b9b5352ef3a824ccdcf509e","skip":false,"over":false},{"idx":2,"day":1,"turn":0,"agent":"セルヴァス","text":"f71e4e6cd69d79794c96900092d75900","skip":false,"over":false}]}""",
    )
    talk_history = (
        [Talk.from_dict(y) for y in value.get("talk_history")]
        if value.get("talk_history") is not None
        else None
    )

    assert talk_history is not None

    assert talk_history[0].idx == 0
    assert talk_history[0].day == 1
    assert talk_history[0].turn == 0
    assert talk_history[0].agent == "ヴィクトリア"
    assert talk_history[0].text == "866cd7648816a1c51fb0817996400a6c"
    assert talk_history[0].skip is False
    assert talk_history[0].over is False

    assert talk_history[1].idx == 1
    assert talk_history[1].day == 1
    assert talk_history[1].turn == 0
    assert talk_history[1].agent == "リュウジ"
    assert talk_history[1].text == "5ad0c6227b9b5352ef3a824ccdcf509e"
    assert talk_history[1].skip is False
    assert talk_history[1].over is False

    assert talk_history[2].idx == 2
    assert talk_history[2].day == 1
    assert talk_history[2].turn == 0
    assert talk_history[2].agent == "セルヴァス"
    assert talk_history[2].text == "f71e4e6cd69d79794c96900092d75900"
    assert talk_history[2].skip is False
    assert talk_history[2].over is False
