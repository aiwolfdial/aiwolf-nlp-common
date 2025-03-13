import json

from aiwolf_nlp_common.packet import Packet
from aiwolf_nlp_common.packet.request import Request


def test_packet() -> None:
    value = json.loads(
        """{"request":"INITIALIZE"}""",
    )
    packet = Packet.from_dict(value)

    assert packet.request == Request.INITIALIZE
