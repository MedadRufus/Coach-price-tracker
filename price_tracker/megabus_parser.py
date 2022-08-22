from datetime import datetime, time


def get_specific_price(data, time_of_day: time):
    for i in data["journeyCommand"]:
        if check_if_correct_day(i["departureDateTime"], time_of_day):
            return i["fare"]["amountInPennies"] / 100


def check_if_correct_day(datestring, time_of_day: time):

    timestamp = datetime.fromisoformat(datestring)
    return timestamp.hour is time_of_day.hour and timestamp.minute is time_of_day.minute
