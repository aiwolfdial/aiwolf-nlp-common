"""
This type stub file was generated by pyright.
"""

from dataclasses import dataclass
from typing import Any
from aiwolf_nlp_common.packet.judge import Judge
from aiwolf_nlp_common.packet.role import Role
from aiwolf_nlp_common.packet.status import Status
from aiwolf_nlp_common.packet.vote import Vote

"""
This type stub file was generated by pyright.
"""
@dataclass
class Info:
    """パケット内のゲームの現状態を示す情報の構造体.

    Attributes:
        game_id (str): ゲームの識別子.
        day (int): 現在の日数.
        agent (str): 自分のエージェントの名前.
        profile (str | None): 自分のエージェントのプロフィール. (リクエストの種類が INITIALIZE の場合のみ). 設定されない場合は None.
        medium_result (Judge | None): 霊能者の結果 (エージェントの役職が霊媒師であるかつ霊能結果が設定されている場合のみ).
        divine_result (Judge | None): 占い師の結果 (エージェントの役職が占い師であるかつ占い結果が設定されている場合のみ).
        executed_agent (str | None): 昨日の追放結果 (エージェントが追放された場合のみ).
        attacked_agent (str | None): 昨夜の襲撃結果 (エージェントが襲撃された場合のみ).
        vote_list (list[Vote] | None): 投票の結果 (投票結果が公開されている場合のみ).
        attack_vote_list (list[Vote] | None): 襲撃の投票結果 (エージェントの役職が人狼かつ襲撃投票結果が公開されている場合のみ).
        status_map (dict[str, Status]): 各エージェントの生存状態を示すマップ.
        role_map (dict[str, Role]): 各エージェントの役職を示すマップ (自分以外のエージェントの役職は見えません).
        remain_count (int | None): 残りのトークもしくは囁きリクエストを受信する可能性のある最大の回数. (リクエストの種類が TALK | WHISPER の場合のみ).
        remain_length (int | None): 残りのトークもしくは囁きリクエストで消費することのできる文字数. 最低文字数を除く. (リクエストの種類が TALK | WHISPER の場合のみ). 制限がない場合は None.
        remain_skip (int | None): 残りのトークもしくは囁きリクエストでスキップすることのできる回数. (リクエストの種類が TALK | WHISPER の場合のみ).
    """
    game_id: str
    day: int
    agent: str
    profile: str | None
    medium_result: Judge | None
    divine_result: Judge | None
    executed_agent: str | None
    attacked_agent: str | None
    vote_list: list[Vote] | None
    attack_vote_list: list[Vote] | None
    status_map: dict[str, Status]
    role_map: dict[str, Role]
    remain_count: int | None = ...
    remain_length: int | None = ...
    remain_skip: int | None = ...
    @staticmethod
    def from_dict(obj: Any) -> Info:
        ...
    


