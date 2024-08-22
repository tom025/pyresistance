from http import HTTPStatus

from httpx import Client


def test_single_black_band_returns_0R(client: Client):
    response = client.get("/resistance", params={"bands": ["black"]})
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"shorthand": "0R"}
