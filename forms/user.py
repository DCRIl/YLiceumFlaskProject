from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, EmailField, BooleanField, IntegerField
from wtforms.validators import DataRequired, InputRequired


class RegisterForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired(), InputRequired()])
    password = PasswordField('Пароль', validators=[DataRequired(), InputRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired(), InputRequired()])
    name = StringField('Ваше ФИО', validators=[DataRequired(), InputRequired()])
    submit = SubmitField('Зарегистрироваться')


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired(), InputRequired()])
    password = PasswordField('Пароль', validators=[DataRequired(), InputRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class CodeFromMailForm(FlaskForm):
    code = IntegerField("Код с почты ", validators=[DataRequired(), InputRequired()])
    submit = SubmitField("Подтвердить регистрацию")