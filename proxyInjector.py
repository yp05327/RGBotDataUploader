from mitmproxy import http

import requests
import re
import json
import os

from settings import uuid

uploadurl = "https://rgbot.peryp.com/api/bangdream/upload/"

eventTopRequestHeaders = {}
eventTopRequestUrl = ''

if os.path.exists('eventTopRequest.header'):
    with open('eventTopRequest.header', 'r') as f:
        eventTopRequestHeaders = json.loads(f.read().strip())

if os.path.exists('eventTopRequest.url'):
    with open('eventTopRequest.url', 'r') as f:
        eventTopRequestUrl = f.read().strip()


def postData(url, data):
    data = uuid + bytes([len(url)]) + url.encode() + data
    response = requests.post(uploadurl, data, headers={'Content-Type': 'application/octet-stream'}, verify=False)
    return response.content.decode()


class Injector:
    def response(self, flow: http.HTTPFlow) -> None:
        if flow.request.host == "api.star.craftegg.jp":
            filter = re.findall('https://api.star.craftegg.jp/api/user/[0-9]*?/event/[0-9]*?/[a-z_]*?/[a-z]*', flow.request.url)
            if len(filter) > 0:
                print(flow.request.content)
                for name, value in flow.request.headers.items():
                    eventTopRequestHeaders[name] = value

                with open('eventTopRequest.header', 'w') as f:
                    f.write(json.dumps(eventTopRequestHeaders))

                with open('eventTopRequest.url', 'w') as f:
                    f.write(flow.request.url)

                result = postData(flow.request.url, flow.response.content)
                print(result)


addons = [Injector()]
