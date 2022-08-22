from price_tracker.megabus_parser import get_specific_price
import json


def test_parser():
    with open("tests/sample_data.json") as json_file:
        data = json.load(json_file)

        returned_price = get_specific_price(data=data)

        assert 8.13 == returned_price
