# RGBotDataUploader
目前是测试阶段

## 安装 
- python 3.7以上
- mitmproxy
- 下载项目后，执行
pip install -r requirements.txt

## 使用方法
- 在 https://rgbot.peryp.com 上注册账户
- 点击用户图标->你的用户名，将会显示你的token和uuid  
token用于RGBot绑定账号，uuid请妥善保存，请勿给其他人，用于上传数据的授权
- 打开'settings.py'，输入你的uuid
- 执行下面这条命令，将会在你的电脑上运行一个代理服务器
python runProxyServer.py
- 在你的手机上设置这个代理服务器
- 安装证书，参考链接:https://docs.mitmproxy.org/stable/concepts-certificates/
- 打开邦邦，查看你的活动页面
- 然后你就可以看到如下所示的log，说明数据上传成功
{"errorcode": 0, "detail": "Success.", "data": "xxxxxx"}  

## 自动上传
- 打开 'settings.py', 你可以修改这个参数来设定间隔多久上传一次数据，请勿设置的过小（这是一个警告）
autoUpdateTimer = 3600
- 执行下面这个命令，将开始自动上传数据
python autoUpdate.py
- 此后你可以将你的手机恢复正常状态，期间退出邦邦等重新登录的操作将会导致上传信息变动，需要重新设定（设置代理，访问你的活动页面）

## Bugs
- 暂时不验证证书，我也不知道为什么一直报错
