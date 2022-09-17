import pytest
import requests

from config import DOMAIN


class APIClient:
    def __init__(self, base_address):
        self.base_address = base_address

    def get(self, path="/", params=None):
        url = f"{self.base_address}{path}"
        return requests.get(url=url, params=params)


@pytest.fixture
def products_api():
    return APIClient(base_address=f"{DOMAIN}/api/")
