from __future__ import annotations

import json
import sys

import websocket

from aiwolf_nlp_common import _version
from aiwolf_nlp_common.packet.packet import Packet


class Client:
    """対戦サーバーとの通信を行うクライアントクラス.

    Attributes:
        url (str): 対戦サーバーのURL.
        token (str | None): 対戦サーバーに接続するためのトークン.
        socket (websocket.WebSocket): WebSocketクライアント.

    Args:
        url (str): 対戦サーバーのURL.
        token (str | None): 対戦サーバーに接続するためのトークン.

    Examples:
        >>> from aiwolf_nlp_common.client import Client
        >>> client = Client("ws://localhost:10000", "token")
        >>> client.connect()
        >>> packet = client.receive()
        >>> print(packet.request)
        Request.INITIALIZE
        >>> client.close()
    """

    def __init__(self, url: str, token: str | None) -> None:
        super().__init__()
        websocket.enableTrace(traceable=False)
        self.socket = websocket.WebSocket()
        self.url = url
        self.headers = [
            f"User-Agent: aiwolf-nlp-common/{_version.__version__} Python/{sys.version}",
        ]
        if token is not None:
            self.token = token
            self.headers.append(f"Authorization: Bearer {self.token}")

    def connect(self) -> None:
        """対戦サーバーに接続します."""
        self.socket.connect(
            self.url,
            header=self.headers,
        )

    def receive(self) -> Packet:
        """対戦サーバーからパケットを受信します.

        Returns:
            Packet: 受信したパケット.
        """
        resp = self.socket.recv()
        resp_str = ""
        if isinstance(resp, (bytes, bytearray, memoryview)):
            resp_str = bytes(resp).decode("utf-8")
        else:
            resp_str = resp
        resp_dict = json.loads(resp_str)
        return Packet.from_dict(resp_dict)

    def send(self, req: str) -> None:
        """対戦サーバーにリクエストを送信します.

        Args:
            req (str): 送信するリクエスト.
        """
        if not req.endswith("\n"):
            req += "\n"
        self.socket.send(req)

    def close(self) -> None:
        """対戦サーバーとの接続を閉じます."""
        self.socket.close()
