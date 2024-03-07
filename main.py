import os
import random

from flask import Flask, render_template, redirect, url_for
from data import db_session
from data.users import User
from data.ideas import Ideas
from forms.user import RegisterForm, LoginForm, CodeFromMailForm
from forms.idea import IdeasForm
from mail import send_registration_code
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'admin_arise_pythonanywhere'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/')
def index():
    db_sess = db_session.create_session()
    ideas = db_sess.query(Ideas).all()
    return render_template('index.html', title='Все идеи и предложения', ideas=ideas)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        filename = form.email.data + ".txt"
        code = random.randrange(10000, 100000)
        with open(filename, "w", encoding="utf8") as file:
            file.write(form.name.data + "\n")
            file.write(form.email.data + "\n")
            file.write(form.password.data + "\n")
            file.write(str(code))
        send_registration_code(filename)
        return redirect(f'/code_for_register/{filename}')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/code_for_register/<filename>', methods=['GET', 'POST'])
def code_for_register(filename):
    form = CodeFromMailForm()
    try:
        with open(filename, encoding="utf-8") as file:
            f = list(map(str.strip, file.readlines()))
            us_name = f[0]
            us_mail = f[1]
            us_password = f[2]
            code = int(f[3])
    except Exception:
        return redirect("/404")
    if form.validate_on_submit():
        if form.code.data == code:
            db_sess = db_session.create_session()
            user = User(
                name=us_name,
                email=us_mail,
                picture=url_for("static", filename="users_pictures/standart.png")
            )
            user.set_password(us_password)
            db_sess.add(user)
            db_sess.commit()
            os.remove(filename)
            return redirect("/")
        else:
            return render_template('code_from_mail.html', title='Введите код с почты',
                                   form=form, mail=us_mail, message="Не правильный код, попробуйте снова")
    return render_template("code_from_mail.html", title="Введите код с почты", form=form, mail=us_mail)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/ideas', methods=['GET', 'POST'])
@login_required
def add_idea():
    form = IdeasForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        ideas = Ideas()
        ideas.title = form.title.data
        ideas.content = form.content.data
        current_user.ideas.append(ideas)
        db_sess.merge(current_user)
        db_sess.commit()
        return redirect('/')
    return render_template('ideas.html', title='Добавление новости',
                           form=form)


@app.route("/ideas_like/<int:id>", methods=["GET", "POST"])
@login_required
def ideas_like(id):
    db_sess = db_session.create_session()
    ideas = db_sess.query(Ideas).filter(Ideas.id == id).first()
    if ideas:
        ideas.likes += 1
        db_sess.commit()
    else:
        return redirect("/404")
    return redirect("/")


@app.route('/ideas_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def ideas_delete(id):
    db_sess = db_session.create_session()
    ideas = db_sess.query(Ideas).filter(Ideas.id == id,
                                        Ideas.user == current_user
                                        ).first()
    if ideas:
        db_sess.delete(ideas)
        db_sess.commit()
    else:
        return redirect("/404")
    return redirect('/')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/404')
def error404():
    return render_template('404.html', title='ОШИБКА 404')


if __name__ == '__main__':
    db_session.global_init("db/ideas_and_more.db")
    app.run(debug=True)
