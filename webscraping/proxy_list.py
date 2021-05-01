import requests
from bs4 import BeautifulSoup
import random
import traceback

def get_free_proxies():
    url = "https://free-proxy-list.net/"
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    
    proxies = []
    for row in soup.find("table", attrs={'id': 'proxylisttable'}).find_all("tr")[1:]:
        tds = row.find_all("td")
        try:
            ip = tds[0].text.strip()
            port = tds[1].text.strip()
            proxies.append(str(ip) +  ":" +str(port))
        except IndexError:
            continue
    return proxies

# print(get_free_proxies())

url = "https://www.cricbuzz.com/"
proxy_list = get_free_proxies()

for i in range(len(proxy_list)):
    print(f"Request no.: {i+1}")
    proxy = proxy_list[i]
    try:
        response = requests.get(url, proxies={'https':proxy, 'https': proxy})
        print(response.json())
        print(response.status_code)
    except:
        print("Not available")
    
        