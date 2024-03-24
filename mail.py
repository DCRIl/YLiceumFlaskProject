import smtplib
from email.message import EmailMessage

my_email = "kelehsaev.2007@gmail.com"
my_password = "lfze nkkt xhuk rkhy"
smtpObj = smtplib.SMTP(host='smtp.gmail.com', port=587)
smtpObj.starttls()
smtpObj.quit()


def send_registration_code(filename):
    with open(filename, encoding="utf-8") as file:
        f = list(map(str.strip, file.readlines()))
        us_mail = f[1]
        code = int(f[3])
    smtpObj = smtplib.SMTP(host='smtp.gmail.com', port=587)
    smtpObj.starttls()
    smtpObj.login(my_email, my_password)
    mess = f"""<!DOCTYPE html>
                        <html>
                        <head>
                            <link rel="stylesheet" type="text/css" hs-webfonts="true"
                                  href="https://fonts.googleapis.com/css?family=Lato|Lato:i,b,bi">
                            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        </head>
                        <body bgcolor="#F5F8FA" style="width: 100%; font-family:Lato, sans-serif; font-size:18px;">
                        <div id="email">
                            <table role="presentation" width="100%">
                                <tr>
                                    <td bgcolor="#0A4455" align="center" style="color: white;">
                                        <h1>{code}</h1>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>Данное письмо отправлено автоматически,<br>если вы не регистрировались на сайте<br><a
                                                href="http://mbousosh22.pythonanywhere.com/">mbousosh22.pythonanywere.com</a><br>то пожалуйста <b>ПРОИГНОРИРУЙТЕ ЭТО ПИСЬМО</b></p>
                                    </td>
                                </tr>
                            </table>
                        </div>
                        </body>
                        </html>"""
    msg = EmailMessage()
    msg["From"] = my_email
    msg["To"] = us_mail
    msg["Subject"] = f"Код для регистрации на сайт: {code}"
    msg.set_content(mess, subtype="html")
    smtpObj.send_message(msg)
    smtpObj.quit()


def send_edit_code(filename):
    with open(filename, encoding="utf-8") as file:
        f = list(map(str.strip, file.readlines()))
        us_mail = f[0]
        code = int(f[1])
    smtpObj = smtplib.SMTP(host='smtp.gmail.com', port=587)
    smtpObj.starttls()
    smtpObj.login(my_email, my_password)
    mess = f"""<!DOCTYPE html>
                        <html>
                        <head>
                            <link rel="stylesheet" type="text/css" hs-webfonts="true"
                                  href="https://fonts.googleapis.com/css?family=Lato|Lato:i,b,bi">
                            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        </head>
                        <body bgcolor="#F5F8FA" style="width: 100%; font-family:Lato, sans-serif; font-size:18px;">
                        <div id="email">
                            <table role="presentation" width="100%">
                                <tr>
                                    <td bgcolor="#0A4455" align="center" style="color: white;">
                                        <h1>{code}</h1>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p>Данное письмо отправлено автоматически,<br>если вы не совершали этих действий на сайте<br><a
                                                href="http://mbousosh22.pythonanywhere.com/">mbousosh22.pythonanywere.com</a><br>то пожалуйста <b>ПРОИГНОРИРУЙТЕ ЭТО ПИСЬМО</b></p>
                                    </td>
                                </tr>
                            </table>
                        </div>
                        </body>
                        </html>"""
    msg = EmailMessage()
    msg["From"] = my_email
    msg["To"] = us_mail
    msg["Subject"] = f"Код для изменения почты на сайте: {code}"
    msg.set_content(mess, subtype="html")
    smtpObj.send_message(msg)
    smtpObj.quit()


def send_mail_about_new_idea(ideas):
    smtpObj = smtplib.SMTP(host='smtp.gmail.com', port=587)
    smtpObj.starttls()
    smtpObj.login(my_email, my_password)
    mess = f"""<!DOCTYPE html>
    <html>
    <head>
        <link rel="stylesheet" type="text/css" hs-webfonts="true" href="https://fonts.googleapis.com/css?family=Lato|Lato:i,b,bi">
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body bgcolor="#F5F8FA" style="width: 100%; font-family:Lato, sans-serif; font-size:18px;">
    <div id="email">
        <table role="presentation" width="100%">
            <tr>
                <td bgcolor="#00A4BD" align="center" style="color: white;">
                    <h1>Добавлена новая идея!</h1>
                </td>
        </table>
        <table role="presentation" border="0" cellpadding="0" cellspacing="10px" style="padding: 10px 30px 30px 10px;">
            <tr>
                <td>
                    <h3>Пользователь: {ideas.autor.name}<br><br>С почтой: {ideas.autor.email}<br><br>Оставил новую идею:<br><br></h3>
                    <h1>
                        {ideas.title}
                    </h1>
                    <p>
                        {ideas.content}
                    </p>
                </td>
            </tr>
        </table>
    </div>
    </body>
    </html>"""
    msg = EmailMessage()
    msg["From"] = my_email
    msg["To"] = my_email
    msg["Subject"] = "Добавили новую идею!"
    msg.set_content(mess, subtype="html")
    smtpObj.send_message(msg)
    smtpObj.quit()