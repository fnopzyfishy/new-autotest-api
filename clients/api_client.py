from httpx import Client, URL, Response, QueryParams
from typing import Any
from httpx._types import RequestData, RequestFiles

class APIClient:
    def __init__(self, client: Client):
        self.client = client

    def get(self, url: URL | str, params: QueryParams | None = None) -> Response:
        """
        Берет данные юзера
        :param url:
        :param params:
        :return:
        """
        return self.client.get(url=url, params=params)

    def post(
            self,
            url: URL | str,
            json: Any | None = None,
            data: RequestData | None = None,
            params: QueryParams | None = None,
            files: RequestFiles | None = None
    ) -> Response:
        """
        Записывает юзера
        :param url:
        :param json:
        :param data:
        :param params:
        :param files:
        :return:
        """
        return self.client.post(url=url, json=json, data=data, params=params, files=files)

    def patch(self, url: URL | str, json: Any | None = None ) -> Response:
        """
        Обновляет данные юзера
        :param url:
        :param json:
        :return:
        """
        return self.client.patch(url=url, json=json)

    def delete(self, url: URL | str) -> Response:
        """
        Удаляет юзера

        :param url:
        :return:
        """
        return self.client.delete(url=url)