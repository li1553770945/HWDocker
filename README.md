# 基于VUE和Django的作业管理系统-部署
## 本部署方法不适用于所有linux系统，请注意适当调整
## 部署方法：
1. 首先在您的服务器上安装依赖项。
```
sudo apt-get update && sudo apt-get install -y vim python3-pip curl git
pip3 install --upgrade pip
pip install docker-compose
```
2. 克隆本项目。
```
git clone https://gitee.com/li1553770945/hwdocker
```
3. 克隆完成后，您还需要以下操作：
+ 修改`./nginx/dist/statis/config.js`，将其中的网址替换为您的服务器地址，请注意不要删掉`/api/`。
+ 修改mysql密码：修改根目录`docker-compose.yml`中`MYSQL_ROOT_PASSWORD: `后面的`"root123456"`为您自己的密码，同时修改`'/django/code/main.ini`中密码为相同密码。（请保证密码符合mysql8.0标准）
+ 修改admin密码：修改`./django/sh/web.sh`中第4行最后面的`'admin123456'`为您的admin用户密码。
4. 完成以上操作后，安装docker。
```
sudo curl -sSL https://get.daocloud.io/docker | sh
```
5. 启动服务
```
docker-compose up -d
```