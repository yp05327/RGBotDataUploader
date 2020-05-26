from mitmproxy import http

import requests

url = "https://rgbot.peryp.com/api/bangdream/upload/"

# input your uuid here
uuid = b''


class Injector:
    def response(self, flow: http.HTTPFlow) -> None:
        if flow.request.host == "api.star.craftegg.jp":
            data = uuid + bytes([len(flow.request.url)]) + flow.request.url.encode() + flow.response.content
            response = requests.post(url, data, headers={'Content-Type': 'application/octet-stream'}, verify=False)
            print(response.content)


addons = [Injector()]
