# RGBotDataUploader
For test now  
[中文说明](https://github.com/yp05327/RGBotDataUploader/blob/master/README_CN.md)

## Install 
- python 3.7
- mitmproxy
- pip install -r requirements.txt

## Usage

- Register an account: https://rgbot.peryp.com
- Click the user icon, and click your username, then you can get your token and uuid 
- open 'settings.py', input your uuid
- run this command and will start a http proxy server on your computer  
python runProxyServer.py
- set this http proxy server to your smart phone or other device which bangdream application is installed
- install the Certificates:https://docs.mitmproxy.org/stable/concepts-certificates/
- open 'bangdream' and watch your event info
- you can see some logs on your computer like: 
{"errorcode": 0, "detail": "Success.", "data": "xxxxxx"}  

## AutoUpdate
- open 'settings.py', you can change this variable as you like but don't be too fast(this is a warning)
autoUpdateTimer = 3600
- run this command and will start to update
python autoUpdate.py

## Bugs
- no ssl certificate verify now, i don't know the reason
