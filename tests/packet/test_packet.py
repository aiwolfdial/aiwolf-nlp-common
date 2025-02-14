import json

from aiwolf_nlp_common.packet import Packet
from aiwolf_nlp_common.packet.request import Request


def test_packet() -> None:
    value = json.loads(
        """{"request":"INITIALIZE","info":{"day":0,"agent":"Agent[01]","statusMap":{"Agent[01]":"ALIVE","Agent[02]":"ALIVE","Agent[03]":"ALIVE","Agent[04]":"ALIVE","Agent[05]":"ALIVE"},"roleMap":{"Agent[01]":"WEREWOLF"}},"setting":{"playerNum":5,"maxTalk":5,"maxTalkTurn":20,"maxWhisper":5,"maxWhisperTurn":20,"maxSkip":0,"isEnableNoAttack":false,"isVoteVisible":false,"isTalkOnFirstDay":true,"responseTimeout":120000,"actionTimeout":60000,"maxRevote":1,"maxAttackRevote":1,"roleNumMap":{"BODYGUARD":0,"MEDIUM":0,"POSSESSED":1,"SEER":1,"VILLAGER":2,"WEREWOLF":1}}}""",
    )
    packet = Packet.from_dict(value)

    assert packet.request == Request.INITIALIZE
