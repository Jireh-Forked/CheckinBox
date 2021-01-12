# CheckinHouqijun
### 后期菌每日签到<br>
每日会自动登录<br>
### 推荐使用腾讯云函数跑，Github Actions跑容易访问网站502<br>
### 使用方法<br>
Github Actions版本<br>
1.点击项目右上角的Fork，Fork此项目<br>
2.到自己Fork的项目点击Setting→Secrets→New secrets<br>
3.username_houqijun填写账号，password_houqijun填写密码<br>
4.在"Actions"中的"run"下点击"Run workflow"即可手动执行签到，后续运行按照schedule，默认在每天凌晨0:30自动签到，可自行修改<br>
5.(可选)New secrets，Name填写SCKEY，Value填写 Server酱推送SCKEY  报错提醒用
<br>