from datetime import datetime
from price_tracker.megabus_parser import get_specific_price, check_if_correct_day
import json


def test_parser():
    with open("tests/sample_data.json") as json_file:
        data = json.load(json_file)

        returned_price = get_specific_price(data=data)

        assert 8.13 == returned_price


def test_datetime_converter():
    assert check_if_correct_day("2022-09-02T17:30:00")
