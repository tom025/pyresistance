from collections.abc import Generator
from socket import socket
from threading import Thread

from httpx import Client
from fastapi import FastAPI
from uvicorn import Config, Server

import pytest

from app import app


class TestServer:
    @classmethod
    def random_port(cls, application: FastAPI):
        s = socket()
        s.bind(("127.0.0.1", 0))
        return cls(application, s)

    def __init__(self, application: FastAPI, s: socket):
        self._server = Server(Config(app=application))
        self._socket = s
        self._thread = Thread(target=self._server.run, kwargs={'sockets': [self._socket]})

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._server.should_exit = True
        self._thread.join()

    @property
    def url(self):
        host, port = self._socket.getsockname()
        return f"http://{host}:{port}"


@pytest.fixture(scope='module')
def client() -> Generator[Client, None, None]:
    with TestServer.random_port(app) as server:
        with Client(base_url=server.url) as client:
            yield client
