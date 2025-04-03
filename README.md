# aiwolf-nlp-common

人狼知能コンテスト（自然言語部門） のエージェント向けの共通パッケージです。\
ゲームサーバから送信されるJSON形式のデータをオブジェクトに変換するためのパッケージです。

```python
import json

from aiwolf_nlp_common.packet import Packet

value = json.loads(
    """{"request":"INITIALIZE"}""",
)
packet = Packet.from_dict(value)

print(packet.request) # Request.INITIALIZE
```

詳細については下記のプロトコルの説明やゲームサーバのソースコードを参考にしてください。\
[プロトコルの実装について](https://github.com/aiwolfdial/aiwolf-nlp-server/blob/main/doc/protocol.md)

## インストール方法

```bash
python -m pip install aiwolf-nlp-common
```

## 運営向け

パッケージ管理ツールとしてuvの使用を推奨します。

```bash
git clone https://github.com/aiwolfdial/aiwolf-nlp-common.git
cd aiwolf-nlp-common
uv venv
uv sync
```

### パッケージのビルド

```bash
uv build
```

### パッケージの配布

#### PyPI

```bash
uv publish --token <PyPIのアクセストークン>
```

#### TestPyPI

```bash
uv publish --publish-url https://test.pypi.org/legacy/ --token <TestPyPIのアクセストークン>
```

uvを使用しない場合については、パッケージ化と配布については下記のページを参考にしてください。\
[Packaging and distributing projects](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/)
