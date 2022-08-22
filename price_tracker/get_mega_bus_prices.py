from datetime import date, datetime, timedelta
import requests
from megabus_parser import get_specific_price


def do_scraping(date: datetime):
    """
    Get the json data raw, and return as a json object
    """

    params = {
        "originId": "56",
        "destinationId": "13",
        "departureDate": date.strftime("%Y-%m-%d"),
        "totalPassengers": "1",
        "concessionCount": "0",
        "nusCount": "0",
        "otherDisabilityCount": "0",
        "wheelchairSeated": "0",
        "pcaCount": "0",
        "days": "1",
    }
    url = "https://uk.megabus.com/journey-planner/api/journeys"
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-GB,en;q=0.5",
        "Connection": "keep-alive",
        "Host": "uk.megabus.com",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0",
    }

    conn = requests.get(url=url, headers=headers, params=params)
    return conn.json()


if __name__ == "__main__":
    start_date = date(year=2022, month=9, day=2)
    for i in range(24):
        date_queried = start_date + timedelta(weeks=i)
        data = do_scraping(date_queried)
        print(date_queried, "£", get_specific_price(data=data))
