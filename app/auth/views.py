# encoding: utf-8
from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required, \
    current_user
from . import auth
from .. import db,github
from ..models import User
from ..email import send_email
from .forms import LoginForm, RegistrationForm, ChangePasswordForm,\
    PasswordResetRequestForm, PasswordResetForm, ChangeEmailForm


@auth.before_app_request
def before_request():
    if current_user.is_authenticated:
        current_user.ping()
        if not current_user.confirmed \
                and request.endpoint \
                and request.blueprint != 'auth' \
                and request.endpoint != 'static':
            return redirect(url_for('auth.unconfirmed'))


@auth.route('/unconfirmed')
def unconfirmed():
    if current_user.is_anonymous or current_user.confirmed:
        return redirect(url_for('main.index'))
    return render_template('auth/unconfirmed.html')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.lower()).first()
        if user is not None:
            if user.password_hash is None:#若密码为空则表示是第三方账号登录
                flash('请使用第三方账号登录')
                return redirect(url_for('/login'))
            elif user.verify_password(form.password.data):
                login_user(user, form.remember_me.data)
                next = request.args.get('next')
                if next is None or not next.startswith('/'):
                    next = url_for('main.index')
                return redirect(next)
        flash('无效邮箱或密码')
    return render_template('auth/login.html', form=form)

#20220504
#添加github登录模块
@auth.route('/')
def github_login():
    return github.authorize(redirect_uri='http://127.0.0.1:5000/auth/callback/github')

@auth.route('/callback/github')
@github.authorized_handler
def authorized(access_token):
    #access_token = github.authorize_access_token()
    """
    接受到GitHub返回的响应后，GitHub-Flask会调用这个authorized()函数，
    并传入access_token的值。如果授权失败，access_token的值会是None，
    这时我们重定向到主页页面，并显示一个错误消息。
    如果access_token不为None，我们会进行创建新用户，
    保存访问令牌，登入用户等操作
    """

    if access_token is None:
        flash('登录失败')
        return redirect(url_for('main.index'))
    # 下面会进行创建新用户，保存访问令牌，登入用户等操作，具体见后面
    else:
        response = github.get('user', access_token=access_token)
        # 判断是否已存在该用户
        username = response['login']
        user = User.query.filter_by(username=username).first()
        if user is None:
            user = User(username=username, email=response['email'])
        db.session.add(user)
        db.session.commit()
        # 登入此用户
        # log the user in
        # if you use flask-login, just call login_user() here.
        login_user(user)
        #login_user(user, form.remember_me.data)
        next = request.args.get('next')
        if next is None or not next.startswith('/'):
            next = url_for('main.index')
        return redirect(next)
    return render_template('auth/login.html', form=form)
    return redirect(url_for('main.index'))
## 20220504



@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('您已登出')
    return redirect(url_for('main.index'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data.lower(),
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        token = user.generate_confirmation_token()
        send_email(user.email, '验证您的邮箱',
                   'auth/email/confirm', user=user, token=token)
        flash('一封验证邮件已发往您的邮箱')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)


@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('main.index'))
    if current_user.confirm(token):
        db.session.commit()
        flash('您已经成功验证邮箱，谢谢！')
    else:
        flash('此验证链接已失效。')
    return redirect(url_for('main.index'))


@auth.route('/confirm')
@login_required
def resend_confirmation():
    token = current_user.generate_confirmation_token()
    send_email(current_user.email, '验证您的邮箱',
               'auth/email/confirm', user=current_user, token=token)
    flash('一封新的验证邮件已发往您的邮箱')
    return redirect(url_for('main.index'))


@auth.route('/change-password', methods=['GET', 'POST'])
@login_required
def change_password():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        if current_user.verify_password(form.old_password.data):
            current_user.password = form.password.data
            db.session.add(current_user)
            db.session.commit()
            flash('您的密码已更新。')
            return redirect(url_for('main.index'))
        else:
            flash('无效密码')
    return render_template("auth/change_password.html", form=form)


@auth.route('/reset', methods=['GET', 'POST'])
def password_reset_request():
    if not current_user.is_anonymous:
        return redirect(url_for('main.index'))
    form = PasswordResetRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.lower()).first()
        if user:
            token = user.generate_reset_token()
            send_email(user.email, 'Reset Your Password',
                       'auth/email/reset_password',
                       user=user, token=token)
        flash('一封引导您更改密码的邮件已发往您的邮箱')
        return redirect(url_for('auth.login'))
    return render_template('auth/reset_password.html', form=form)


@auth.route('/reset/<token>', methods=['GET', 'POST'])
def password_reset(token):
    if not current_user.is_anonymous:
        return redirect(url_for('main.index'))
    form = PasswordResetForm()
    if form.validate_on_submit():
        if User.reset_password(token, form.password.data):
            db.session.commit()
            flash('您的密码已更新')
            return redirect(url_for('auth.login'))
        else:
            return redirect(url_for('main.index'))
    return render_template('auth/reset_password.html', form=form)


@auth.route('/change_email', methods=['GET', 'POST'])
@login_required
def change_email_request():
    form = ChangeEmailForm()
    if form.validate_on_submit():
        if current_user.verify_password(form.password.data):
            new_email = form.email.data.lower()
            token = current_user.generate_email_change_token(new_email)
            send_email(new_email, '验证您的邮箱',
                       'auth/email/change_email',
                       user=current_user, token=token)
            flash('一封验证邮件已发往您的邮箱')
            return redirect(url_for('main.index'))
        else:
            flash('无效邮箱或密码')
    return render_template("auth/change_email.html", form=form)


@auth.route('/change_email/<token>')
@login_required
def change_email(token):
    if current_user.change_email(token):
        db.session.commit()
        flash('您的邮箱已更新')
    else:
        flash('无效请求')
    return redirect(url_for('main.index'))


