import json

from aiwolf_nlp_common.packet import Info
from aiwolf_nlp_common.packet.role import Role
from aiwolf_nlp_common.packet.status import Status


def test_info() -> None:
    value = json.loads(
        """{"game_id":"01JQRBM0SBFWKQVMC8EFARBDKW","day":0,"agent":"シオン","profile":"年齢: 16歳n性別: 男性n性格: シオンは非常に自信家で、しばしば冷静かつ計算高い行動を取ります。表向きはおとなしく、他人の動きを観察するのが得意ですが、内心では自分が中心にいることを望んでいます。周囲に対して少し挑戦的な態度を見せることがあり、何事も自分のペースで進めようとする傾向があります。それに加えて、感情をあまり表に出さず、冷徹で論理的に物事を判断するタイプです。たまに見せる不意の微笑みには、周りを驚かせる魅力が隠れています。","status_map":{"シオン":"ALIVE","ジョナサン":"ALIVE","ジョージ":"ALIVE","セルヴァス":"ALIVE","ダイスケ":"ALIVE","トシオ":"ALIVE","ミサキ":"ALIVE","ミドリ":"ALIVE","ミナコ":"ALIVE","ミナト":"ALIVE","メイ":"ALIVE","リュウジ":"ALIVE","ヴィクトリア":"ALIVE"},"role_map":{"シオン":"WEREWOLF","ジョージ":"WEREWOLF","メイ":"WEREWOLF"}}""",
    )
    info = Info.from_dict(value)

    assert info.game_id == "01JQRBM0SBFWKQVMC8EFARBDKW"
    assert info.day == 0
    assert info.agent == "シオン"
    assert info.profile == "年齢: 16歳n性別: 男性n性格: シオンは非常に自信家で、しばしば冷静かつ計算高い行動を取ります。表向きはおとなしく、他人の動きを観察するのが得意ですが、内心では自分が中心にいることを望んでいます。周囲に対して少し挑戦的な態度を見せることがあり、何事も自分のペースで進めようとする傾向があります。それに加えて、感情をあまり表に出さず、冷徹で論理的に物事を判断するタイプです。たまに見せる不意の微笑みには、周りを驚かせる魅力が隠れています。"
    assert info.medium_result is None
    assert info.divine_result is None
    assert info.executed_agent is None
    assert info.attacked_agent is None
    assert info.vote_list is None
    assert info.attack_vote_list is None
    assert info.status_map == {"シオン": Status.ALIVE, "ジョナサン": Status.ALIVE, "ジョージ": Status.ALIVE, "セルヴァス": Status.ALIVE, "ダイスケ": Status.ALIVE, "トシオ": Status.ALIVE, "ミサキ": Status.ALIVE, "ミドリ": Status.ALIVE, "ミナコ": Status.ALIVE, "ミナト": Status.ALIVE, "メイ": Status.ALIVE, "リュウジ": Status.ALIVE, "ヴィクトリア": Status.ALIVE}
    assert info.role_map == {"シオン": Role.WEREWOLF, "ジョージ": Role.WEREWOLF, "メイ": Role.WEREWOLF}
    assert info.remain_count is None
    assert info.remain_length is None
    assert info.remain_skip is None
