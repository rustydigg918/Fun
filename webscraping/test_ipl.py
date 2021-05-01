import requests
import json
import pandas as pd

url = "https://cricketapi.platform.iplt20.com//fixtures/23488/scoring"

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0',
  'Accept': '*/*',
  'Accept-Language': 'en-US,en;q=0.5',
  'account': 'ipl',
  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'Origin': 'https://www.iplt20.com',
  'Referer': 'https://www.iplt20.com/',
  'Connection': 'keep-alive',
  'If-None-Match': 'W/0992feda07ade54a6a23f00869b5bc8d2',
  'TE': 'Trailers'
}

response = requests.get(url, headers=headers)

player_data = response.json()
# df = pd.json_normalize(player_data)
print(player_data.jsonify())