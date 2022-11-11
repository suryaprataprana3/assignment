import requests
from bs4 import BeautifulSoup
import time
# Making a GET request
r = requests.get('https://coinmarketcap.com/')
# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

while True:
    data = []

    for tr in soup.table.find_all('tr'):
        data.append([td.text for td in tr.find_all('td') if td.text != ''])
    
    url = 'http://127.0.0.1:8000/save_and_get_data'

    params = []
    for items in data:
        if len(items)==9:
            params.append(
                {"name": items[1],
                "price": items[2],
                "one_hour_per": items[3],
                "twenty_four_hour_per": items[4],
                "seven_day_per": items[5],
                "market_cap": items[6],
                "volume": items[7],
                "supply": items[8]}
            )
    res = requests.post(url, json = {"data":params})
    time.sleep(5)

    
    