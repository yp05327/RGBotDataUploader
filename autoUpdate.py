from proxyInjector import eventTopRequestHeaders, eventTopRequestUrl, postData
from settings import proxyPort

import requests
import os

from apscheduler.schedulers.blocking import BlockingScheduler

# 1 hour don't be too fast
delta = 3600


def autoRequest():
    print('Start to send request.')
    if eventTopRequestHeaders == {} or eventTopRequestUrl == '':
        return

    proxies = {
        'http': 'http://localhost:%d' % proxyPort,
        'https': 'http://localhost:%d' % proxyPort,
    }
    data = requests.get(eventTopRequestUrl, b'', headers=eventTopRequestHeaders, proxies=proxies, verify=False)
    result = postData(eventTopRequestUrl, data.content)
    print(result)
    print('Start to send request.')


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(autoRequest, 'interval', seconds=delta)
    print('Service start. Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C    '))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
