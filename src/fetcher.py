import time
import requests
from .settings import ERROR_SLEEP_TIME
import json

def fetch_data(body, url, headers):
    while True:
        try:
            serialized_body = json.dumps(body)
            start_time = time.perf_counter()
            response = requests.post(url, data=serialized_body, headers=headers)
            end_time = time.perf_counter()
            response_time = (end_time - start_time) * 1000
            break
        except requests.RequestException as error:
            print(f"[{time.strftime('%d %b %Y %H:%M:%S', time.localtime())}] {error}")
            time.sleep(ERROR_SLEEP_TIME)

    return "{:.3f}".format(response_time).replace('.', ',')
