import requests
from requests.exceptions import ConnectionError

import json
import time
import logging

LOG_FILE_NAME = '/usr/tmp/app/logs.log'
CONFIGURAION_FILE = 'configuration.json'

logging.basicConfig(filename=LOG_FILE_NAME,
                    level=logging.DEBUG,
                    format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')

with open(CONFIGURAION_FILE) as json_file:
    websites_info = json.load(json_file)

    while True:
        for website in websites_info['Records']:
            url = website['url']
            must_have_string = website['must_have_string']

            start_time = int(round(time.time() * 1000))
            try:
                response = requests.get(url)
            except ConnectionError:
                response = 'cannot connect to the website'
                logging.info('[status: NOT OK] [status_code: 404] [url: {url}] [response_time: NA] [reason: {response}]'.format(url=url, response=response))
                continue

            end_time = int(round(time.time() * 1000))

            total_time = end_time - start_time

            if must_have_string in str(response.text).lower():
                status = 'OK'
                status_code = response.status_code
                logging.info('[status: {status}] [status_code: {status_code}] [url: {url}] [response_time: {total_time} ms]'.format(status=status, url=url, total_time=total_time, status_code=status_code))
            else:
                status = 'NOT OK'
                status_code = response.status_code
                logging.info('[status: {status}] [status_code: {status_code}] [url: {url}] [response_time: {total_time} ms] [reason: response not expected]'.format(status=status,  url=url, total_time=total_time, status_code=status_code))

        time.sleep(30)
