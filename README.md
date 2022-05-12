# Hackers 开发者交流学习平台


## TODO:
- [x] 删除支付页面
- [x] 更换图标
- [ ] 上传图片数据
- [ ] 插入本地数据
- [ ] **写文档**
- [ ] ppt:
    0. 找ppt模板
    1. 项目需求
    2. 项目分析与设计开发过程
    3. 项目分工
    4. 项目运行视频





## 相关技术

~~支付：PaysApi~~

内容存储：mysql

图片存储：阿里云对象存储oss

邮箱注册: flask_email 

邮箱验证码：redis

celery email task


## ** How to use **
```bash
# 1.克隆到本地
git clone ...

# 2.安装依赖
pip install -r requirements.txt
```
[pip安装MarkupSafe==1.0失败解决方案](https://blog.csdn.net/h106140873/article/details/104794744/)

3.安装mysql以及redis并启动。

4.修改config.py中的配置。将有关的变量写入环境变量。

```bash
# 5.数据库迁移
python manage.py db migrate
```
如果遇到[数据库迁移错误](https://stackoverflow.com/questions/32798937/cant-migrate-or-upgrade-database-with-flask-migrate-alembic)
do this:

```bash
python manage.py db stamp head
python manage.py db migrate
python manage.py db upgrade

```

```bash
# 6.映射数据库
python manage.py db upgrade

#管理员创建：
python manage.py add_cms_user -u your_username -p your_passowrd -e your_email

#快捷创建前端用户
python manage.py add_front_user -u your_username -p your_passowrd -e your_email

# 启动
python manage.py runserver
```