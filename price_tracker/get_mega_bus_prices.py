from datetime import date, datetime, timedelta, time
import requests
from megabus_parser import get_specific_price


def do_scraping(date: datetime):
    """
    Get the json data raw, and return as a json object
    """

    cookies = {
        "JSESSIONID": "5E20DFEF5C2F774046742848292D9216",
        "visid_incap_159597": "+Ko+QvaeTlq39xROvRn3b/zwA2MAAAAAQUIPAAAAAACkXMnq/xZh8a5tUgq2TGyN",
        "incap_ses_1582_159597": "aWHke680WnP809nnxWT0FfzwA2MAAAAA7rfmE8qeB1Ro8wYhtk0NvA==",
        "nlbi_159597_1392533": "mOQHR5pXT2jPECQiCMMOFwAAAACGJhMjo7fMhtYlL832FAn2",
        "visid_incap_1247305": "5eU5kqTkQ1yOE0sg4BSIUQzxA2MAAAAAQUIPAAAAAAAm+dO/MWiPcu5QDb5FLcmY",
        "incap_ses_1582_1247305": "mBXTD7vmVRGk6NnnxWT0FQzxA2MAAAAAHzCOC8MSbD0dz4enBUly2g==",
        "Cookie": "srv-p88joNk0XMj2NKuVM8c8qg|YwPxZ",
        "gig_canary": "false",
        "gig_canary_ver": "13363-3-27686655",
        "apay-session-set": "hm4g1e%2BEcd5Al9xh87%2F4Bn1FNKAVCdKopyS38p8qJ7IV8BQckTemaFDctSr09q0%3D",
        "gig_bootstrap_3_wb57-4uy5-rwYQ15uvcuwnK9R9QZ41KEn9cFe3w1o6iQuNDH-CSO3E1pFQJOzhRu": "_gigya_ver4",
        "ADRUM_BTa": "R:39|g:f86b7877-14fd-4b12-aa97-e444db216434|n:NationalExpress_0deb1def-06c4-4fa9-9e8a-6ef13388c73d",
        "ADRUM_BT1": "R:39|i:649851|e:1",
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-GB,en;q=0.5",
        # 'Accept-Encoding': 'gzip, deflate, br',
        # Already added when you pass json=
        # 'Content-Type': 'application/json',
        "Origin": "https://book.nationalexpress.com",
        "DNT": "1",
        "Connection": "keep-alive",
        "Referer": "https://book.nationalexpress.com/coach/",
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'JSESSIONID=5E20DFEF5C2F774046742848292D9216; visid_incap_159597=+Ko+QvaeTlq39xROvRn3b/zwA2MAAAAAQUIPAAAAAACkXMnq/xZh8a5tUgq2TGyN; incap_ses_1582_159597=aWHke680WnP809nnxWT0FfzwA2MAAAAA7rfmE8qeB1Ro8wYhtk0NvA==; nlbi_159597_1392533=mOQHR5pXT2jPECQiCMMOFwAAAACGJhMjo7fMhtYlL832FAn2; visid_incap_1247305=5eU5kqTkQ1yOE0sg4BSIUQzxA2MAAAAAQUIPAAAAAAAm+dO/MWiPcu5QDb5FLcmY; incap_ses_1582_1247305=mBXTD7vmVRGk6NnnxWT0FQzxA2MAAAAAHzCOC8MSbD0dz4enBUly2g==; Cookie=srv-p88joNk0XMj2NKuVM8c8qg|YwPxZ; gig_canary=false; gig_canary_ver=13363-3-27686655; apay-session-set=hm4g1e%2BEcd5Al9xh87%2F4Bn1FNKAVCdKopyS38p8qJ7IV8BQckTemaFDctSr09q0%3D; gig_bootstrap_3_wb57-4uy5-rwYQ15uvcuwnK9R9QZ41KEn9cFe3w1o6iQuNDH-CSO3E1pFQJOzhRu=_gigya_ver4; ADRUM_BTa=R:39|g:f86b7877-14fd-4b12-aa97-e444db216434|n:NationalExpress_0deb1def-06c4-4fa9-9e8a-6ef13388c73d; ADRUM_BT1=R:39|i:649851|e:1',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    json_data = {
        "coachCard": False,
        "campaignId": "DEFAULT",
        "partnerId": "NX",
        "outboundArriveByOrDepartAfter": "DEPART_AFTER",
        "inboundArriveByOrDepartAfter": "DEPART_AFTER",
        "journeyType": "RETURN",
        "operatorType": "DOMESTIC",
        "leaveDateTime": {
            "date": date.strftime("%d/%m/%Y"),
            "time": "17:00",
        },
        "passengerNumbers": {
            "numberOfAdults": 1,
            "numberOfBabies": 0,
            "numberOfChildren": 0,
            "numberOfDisabled": 0,
            "numberOfSeniors": 0,
            "numberOfEuroAdults": 0,
            "numberOfEuroSeniors": 0,
            "numberOfEuroYoungPersons": 0,
            "numberOfEuroChildren": 0,
        },
        "coachCardNumbers": {
            "numberOnDisabledCoachcard": 0,
            "numberOnSeniorCoachcard": 0,
            "numberOnYouthCoachcard": 0,
        },
        "returnDateTime": {
            "date": "26/08/2022",
            "time": "00:00",
        },
        "fromToStation": {
            "fromStationId": "41065",
            "toStationId": "57366",
        },
        "onDemand": False,
        "fromStationName": "BRISTOL Bus & Coach Station",
        "toStationName": "LONDON VICTORIA Coach Station",
        "languageCode": "en",
        "channelsKey": "DESKTOP",
    }

    response = requests.post(
        "https://book.nationalexpress.com/nxrest/journey/search/OUT",
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    return response.json()


if __name__ == "__main__":
    d = date(year=2022, month=9, day=2)
    t = time(hour=17, minute=45)
    for i in range(24):
        date_queried = d + timedelta(weeks=i)
        data = do_scraping(date_queried)
        print(date_queried, "£", get_specific_price(data=data, time_of_day=t))
