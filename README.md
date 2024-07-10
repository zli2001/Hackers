# Hackers
Multi-user blog system based on Flask
## Tools

python:3.6.15

Database：mysql

OSS：[Aliyun oss](https://blog.csdn.net/Doudou_Mylove/article/details/107060228)

Email registration: flask_email

Email verification code: redis

celery email task



## ** How to use **
```bash
### 1. Clone to local
git clone ...

### 2. Install dependencies
pip install -r requirements.txt
```
[Solution for pip install MarkupSafe==1.0 failure](https://blog.csdn.net/h106140873/article/details/104794744/)


### 3.Install mysql and redis, then start them.
If you encounter an error when installing redis:
```bash
redis.exceptions.ConnectionError: Error 10061 connecting to 47.107.66.196:6379. No connection could be made because the target machine actively refused it.
127.0.0.1 - - [07/May/2022 21:36:56] "POST /signup/ HTTP/1.1" 500 -
```
(install redis](https://www.cnblogs.com/xiaodai0/p/9761192.html)

solution:Change 47.107.66.196 to 127.0.0.1


### 4.Modify the configuration in config.py. Write related variables to user variables.



### 5.Database
- First, create an empty database named mycms in mysql
- Then migrate the database

`python manage.py db migrate`

If you encounter [database migration error](https://stackoverflow.com/questions/32798937/cant-migrate-or-upgrade-database-with-flask-migrate-alembic)

do this:

```bash
python manage.py db stamp head
python manage.py db migrate
python manage.py db upgrade

```

```bash
# 6.Map the database
python manage.py db upgrade

python manage.py db upgrade

# You can use data/test.sql to establish a test database
# Some example data in the project comes from the Internet. If there is any infringement, please contact me to delete it.

# Create an admin user:
python manage.py add_cms_user -u your_username -p your_passowrd -e your_email

# Quickly create a front-end user:
python manage.py add_front_user -u your_username -p your_passowrd -e your_email

# Start
python manage.py runserver
```
demo：
![main page](pics/img.png)
![post](pics/img_1.png)
![files](pics/img_2.png)
Reference link
[https://github.com/RelaxedDong/mycms](https://github.com/RelaxedDong/mycms)
