import threading
import requests
import json
from .settings import *
from .handler import *
from .fetcher import *

class AddRowThread(threading.Thread):
    def __init__(self, dataset, thread, rows, headers, payload, url):
        threading.Thread.__init__(self)
        self.dataset = dataset
        self.thread = thread
        self.rows = rows
        self.headers = headers
        self.payload = payload
        self.url = url

    def fetch_row(self):
        for data in self.dataset:
            body = {}
            if self.payload == "1":
                body = PAYLOAD_CONFIGURATION_1
            elif self.payload == "2":
                body = PAYLOAD_CONFIGURATION_2
            elif self.payload == "3":
                body = PAYLOAD_CONFIGURATION_3
            if self.url == "1":
                self.url = URL_SYNC
            elif self.url == "2":
                self.url = URL_ASSYNC
            body.update({'data': [data]})
            row = ["thread-" + str(self.thread), len(self.rows) + 1]
            row.extend([fetch_data(body, self.url, self.headers) for _ in range(5)])
            self.rows.append(row)

    def run(self):
        self.fetch_row()

def run(archive, threads, payload, url):
    rows = []
    active_threads = []

    headers = {'Content-type': 'application/json'}
    body = json.dumps({"username": USERNAME, "password": PASSWORD})

    post = requests.post(LOGIN_URL, data=body, headers=headers)

    if post.status_code == 401:
        post = requests.post(REGISTER_URL, data=body, headers=headers)

    response = json.loads(post.text)
    headers.update({'Authorization': 'Token ' + response['token']})

    for i in range(int(threads)):
        thread = i + 1
        dataset = read_file(archive)
        t = AddRowThread(dataset, thread, rows, headers, payload, url)
        t.start()
        active_threads.append(t)

    for t in active_threads:
        t.join()

    write_file(threads, archive, rows, payload, url)
