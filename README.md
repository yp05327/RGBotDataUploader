# RGBotDataUploader
For test now

## Install 
- python 3.7
- pip install mitmproxy

## Usage

- Register an account: https://rgbot.peryp.com
- Contact to me and i will add an uuid to your account
- open 'run.py', input your uuid
- run 'mitmdump  -s yourPath/run.py -p 8888' and will start a http proxy server on your computer
- set this http proxy server to your smart phone or other device which bangdream application is installed
- install the pem
- open 'bangdream' and watch your event info
- you can see some logs on your computer like: 
{"errorcode": 0, "detail": "Success.", "data": "xxxxxx"}  

## Bugs
- no ssl certificate verify now, i don't know the reason
