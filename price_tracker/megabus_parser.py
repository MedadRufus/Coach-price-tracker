def get_specific_price(data):
    for i in data["journeys"]:
        if i["departureDateTime"] == "2022-09-02T17:30:00":
            return i["price"]
