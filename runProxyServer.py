import os

from settings import proxyPort

os.system("mitmdump -s ./proxyInjector.py -p %d" % proxyPort)
