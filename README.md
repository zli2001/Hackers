flaskcms系统
`部分相关：`
三方登陆：微博登陆 三方登陆流程(https://blog.csdn.net/qq_42239520/article/details/85851232)
支付：PaysApi
基于Pyhon3.6的大型CMS管理系统
内容存储：mysql
图片存储：阿里云对象存储oss
邮箱注册: flask_email  邮件支持流程(https://blog.csdn.net/qq_42239520/article/details/80368733)
邮箱验证码：redis
celery email task
...... 

** How to use **
```bash
# 克隆到本地
git clone https://github.com/1417766861/mycms

# 安装依赖
pip install -r requirements.txt
```
[pip安装MarkupSafe==1.0失败解决过程 ](https://blog.csdn.net/h106140873/article/details/104794744/)
安装mysql以及redis并启动。
修改config.py中的配置。

```bash
# 数据库迁移
python manage.py db migrate
```
[如果遇到数据库迁移错误](https://stackoverflow.com/questions/32798937/cant-migrate-or-upgrade-database-with-flask-migrate-alembic)
```bash
# 映射数据库
python manage.py db upgrade

#管理员创建：
python manage.py add_cms_user -u your_username -p your_passowrd -e your_email

#快捷创建前端用户
python manage.py add_front_user -u your_username -p your_passowrd -e your_email

```