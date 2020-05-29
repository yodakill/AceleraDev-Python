from main import get_temperature
from unittest.mock import patch
import pytest


"""lista valores Fahrenheit, latitude, longitude e celsus"""
values = \
    (
        (62, -14.235004, -51.92528, 16),
        (62.54, -14.235004, -51.92528, 16),
        (5, 15.58564, -13.85478, -15),
        (-13, 22.8523, 17.358746, -25),
        (0, 22.8523, 17.358746, -17),
    )


@pytest.mark.parametrize('rTemperature, lat, lng, expected', values)
def test_get_temperature(rTemperature, lat, lng, expected):
    """
    Simula objeto formato Json e realiza testes par metodo
    get_temperature
    :param rTemperature: temperatura em Fahrenheit
    :param lat: Latitude
    :param lng: Longitude
    :param expected: Temperatura em Celsus
    :return:
    """
    mock_get_partcher = patch('main.requests.get')
    temperature = {"currently": {"temperature": rTemperature}}

    mock_get = mock_get_partcher.start()
    mock_get.return_value.json.return_value = temperature
    response = get_temperature(lat, lng)
    mock_get_partcher.stop()
    assert expected == response
