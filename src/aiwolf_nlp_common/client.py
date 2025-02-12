from __future__ import annotations

import sys

import websocket

from aiwolf_nlp_common import _version


class Client:
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
        self.socket.connect(
            self.url,
            header=self.headers,
        )

    def receive(self) -> str:
        resp = self.socket.recv()
        resp_str = ""
        if isinstance(resp, (bytes, bytearray, memoryview)):
            resp_str = bytes(resp).decode("utf-8")
        else:
            resp_str = resp
        return resp_str

    def send(self, req: str) -> None:
        if not req.endswith("\n"):
            req += "\n"
        self.socket.send(req)

    def close(self) -> None:
        self.socket.close()
        self.socket.close()
