from mitmproxy import http

import requests
import re

url = "https://rgbot.peryp.com/api/bangdream/upload/"

# input your uuid here
uuid = b''


class Injector:
    def response(self, flow: http.HTTPFlow) -> None:
        if flow.request.host == "api.star.craftegg.jp":
            filter = re.findall('https://api.star.craftegg.jp/api/user/[0-9]*?/event/[0-9]*?/[a-z_]*?/[a-z]*', flow.request.url)
            if len(filter) > 0:
                data = uuid + bytes([len(flow.request.url)]) + flow.request.url.encode() + flow.response.content
                response = requests.post(url, data, headers={'Content-Type': 'application/octet-stream'}, verify=False)
                print(response.content.decode())


addons = [Injector()]
