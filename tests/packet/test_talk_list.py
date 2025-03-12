import json

from aiwolf_nlp_common.packet.talk import Talk


def test_talk_list() -> None:
    value = json.loads(
        """{"talkHistory":[{"idx":0,"day":0,"turn":0,"agent":"Agent[05]","text":"1567e6fc799ebd6393180fb64e99681b","skip":false,"over":false},{"idx":1,"day":0,"turn":0,"agent":"Agent[01]","text":"6c97a4a02204110b549d3d176d283392","skip":false,"over":false},{"idx":2,"day":0,"turn":0,"agent":"Agent[03]","text":"abfc69161ca6f4f8123579810037f8ef","skip":false,"over":false}]}""",
    )
    talk_history = (
        [Talk.from_dict(y) for y in value.get("talkHistory")]
        if value.get("talkHistory") is not None
        else None
    )

    assert talk_history is not None

    assert talk_history[0].idx == 0
    assert talk_history[0].day == 0
    assert talk_history[0].turn == 0
    assert talk_history[0].agent == "Agent[05]"
    assert talk_history[0].text == "1567e6fc799ebd6393180fb64e99681b"
    assert talk_history[0].skip is False
    assert talk_history[0].over is False

    assert talk_history[1].idx == 1
    assert talk_history[1].day == 0
    assert talk_history[1].turn == 0
    assert talk_history[1].agent == "Agent[01]"
    assert talk_history[1].text == "6c97a4a02204110b549d3d176d283392"
    assert talk_history[1].skip is False
    assert talk_history[1].over is False

    assert talk_history[2].idx == 2
    assert talk_history[2].day == 0
    assert talk_history[2].turn == 0
    assert talk_history[2].agent == "Agent[03]"
    assert talk_history[2].text == "abfc69161ca6f4f8123579810037f8ef"
    assert talk_history[2].skip is False
    assert talk_history[2].over is False
