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
[プロトコルの実装について](https://github.com/aiwolfdial/aiwolf-nlp-server/blob/main/doc/ja/config.md)

## インストール方法

```bash
python -m pip install aiwolf-nlp-common
```

## 運営向け

### パケット定義の更新

`src/aiwolf_nlp_common/packet/_models.py` は手で編集しません。\
ゲームサーバの [`schema/protocol.schema.json`](https://github.com/aiwolfdial/aiwolf-nlp-server/blob/develop/schema/protocol.schema.json) を唯一の定義とし、[datamodel-code-generator](https://github.com/koxudaxi/datamodel-code-generator) で生成しています。\
同じディレクトリの他のモジュール (`talk.py` など) は、従来の import パスを保つための再エクスポートです。

```bash
git clone https://github.com/aiwolfdial/aiwolf-nlp-server.git
cd aiwolf-nlp-server
git checkout "$(tr -d '[:space:]' < ../aiwolf-nlp-common/.schema-ref)"
./schema/generate.sh python ../aiwolf-nlp-common/src/aiwolf_nlp_common/packet
```

参照するサーバのリビジョンは `.schema-ref` に固定されています。\
プロトコルを変更する場合は、先にサーバ側のスキーマを更新してマージし、`.schema-ref` を新しいリビジョンへ書き換えてから上記を実行してください。\
CI (`.github/workflows/schema-check.yml`) が、生成物とスキーマが一致しているかを検査します。

パッケージ管理ツールとしてuvの使用を推奨します。

```bash
git clone https://github.com/aiwolfdial/aiwolf-nlp-common.git
cd aiwolf-nlp-common
uv venv
uv sync
```

### パッケージのビルド

```bash
pyright --createstub aiwolf_nlp_common
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
