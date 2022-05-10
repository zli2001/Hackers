#coding:utf-8
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_github import GitHub

mail = Mail()
db = SQLAlchemy()
github = GitHub()
