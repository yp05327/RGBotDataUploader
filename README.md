# RGBotDataUploader
For test now

## Install 
- python 3.7
- mitmproxy
- pip install -r requirements.txt

## Usage

- Register an account: https://rgbot.peryp.com
- Contact to me and i will add an uuid to your account
- open 'settings.py', input your uuid
- run this command and will start a http proxy server on your computer  
python runProxyServer.py
- set this http proxy server to your smart phone or other device which bangdream application is installed
- install the Certificates:https://docs.mitmproxy.org/stable/concepts-certificates/
- open 'bangdream' and watch your event info
- you can see some logs on your computer like: 
{"errorcode": 0, "detail": "Success.", "data": "xxxxxx"}  

## Bugs
- no ssl certificate verify now, i don't know the reason
