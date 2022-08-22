from datetime import datetime


def get_specific_price(data):
    for i in data["journeys"]:
        if check_if_correct_day(i["departureDateTime"]):
            return i["price"]


def check_if_correct_day(datestring, hour=17, minute=30):

    timestamp = datetime.fromisoformat(datestring)
    return timestamp.hour is hour and timestamp.minute is minute
