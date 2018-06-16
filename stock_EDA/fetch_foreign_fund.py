import pandas as pd
import requests
import json
import time
import pdb
import datetime

url = 'http://www.twse.com.tw/fund/BFI82U'
headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OSX 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko)' +\
                'Chrome/58.0.3029.110 Safari/537.36'
        }
today = datetime.datetime.today()

for i in range(0,6):
    day = today + datetime.timedelta(days = -i)
    date_str = day.strftime('%Y-%m-%d')
    payloads = {
            'response':'json',
            'dayDate':day.strftime('%Y%m%d'),
            '_':day.strftime('%s')
            }
    page = requests.get(url, headers = headers, params = payloads)
    pdb.set_trace()
    obj = json.loads(page.text)
    print(date_str)
    print(page.url)
    #check whether the data for this date
    if obj['stat'] != 'OK' or not obj['stat']:
        print('No data for' + date_str)
        time.sleep(3)
        continue
    #get data
    pdb.set_trace()
    


