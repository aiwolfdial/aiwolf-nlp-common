# aiwolf-nlp-common

人狼知能コンテスト（自然言語部門） のエージェント向けの共通パッケージです。  
ゲームサーバから送信されるJSON形式のデータをオブジェクトに変換するためのパッケージです。

```python
import json

from aiwolf_nlp_common.packet import Packet

recv: str = """{"request":"INITIALIZE","info":{"statusMap":{"Agent[01]":"ALIVE","Agent[02]":"ALIVE","Agent[03]":"ALIVE","Agent[04]":"ALIVE","Agent[05]":"ALIVE"},"roleMap":{"Agent[02]":"SEER"},"remainTalkMap":{},"remainWhisperMap":{},"day":0,"agent":"Agent[02]"},"setting":{"roleNumMap":{"BODYGUARD":0,"MEDIUM":0,"POSSESSED":0,"SEER":1,"VILLAGER":3,"WEREWOLF":1},"maxTalk":3,"maxTalkTurn":15,"maxWhisper":3,"maxWhisperTurn":15,"maxSkip":3,"isEnableNoAttack":true,"isVoteVisible":false,"isTalkOnFirstDay":true,"responseTimeout":90000,"actionTimeout":60000,"maxRevote":1,"maxAttackRevote":1}}"""
value: dict = json.loads(recv)
packet = Packet.from_dict(value)

print(packet.request)
print(packet.info.agent)
```

```
INITIALIZE
Agent[02]
```

詳細については下記のプロトコルの説明やゲームサーバのソースコードを参考にしてください。  
[プロトコルの実装について](https://github.com/kano-lab/aiwolf-nlp-server/blob/main/doc/protocol.md)

## インストール方法

```
python -m pip install aiwolf-nlp-common
```

## 運営向け

パッケージ管理ツールとしてuvの使用を推奨します。

```
git clone https://github.com/kano-lab/aiwolf-nlp-common.git
cd aiwolf-nlp-common
uv venv
uv sync
```

### パッケージのビルド

```
uv build
```

### パッケージの配布

#### PyPI

```
uv publish --token <PyPIのアクセストークン>
```

#### TestPyPI

```
uv publish --publish-url https://test.pypi.org/legacy/ --token <TestPyPIのアクセストークン>
```


uvを使用しない場合については、パッケージ化と配布については下記のページを参考にしてください。  
[Packaging and distributing projects](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/)
