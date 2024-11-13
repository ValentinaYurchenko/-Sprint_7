import pytest
from helpers.helper_data import Courier


@pytest.fixture()
def courier():
    courier_create = Courier().registration_and_courier_data_acquiring()
    yield courier_create

