from pprint import PrettyPrinter
import requests
from megabus_parser import get_specific_price


def do_scraping():
    """
    Get the json data raw, and return as a json object
    """
    url = "https://uk.megabus.com/journey-planner/api/journeys?originId=56&destinationId=13&departureDate=2022-09-02&totalPassengers=1&concessionCount=0&nusCount=0&otherDisabilityCount=0&wheelchairSeated=0&pcaCount=0&days=1"
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
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }

    conn = requests.get(url=url, headers=headers)
    return conn.json()



if __name__ == "__main__":
    data = do_scraping()
    print(get_specific_price(data=data))
