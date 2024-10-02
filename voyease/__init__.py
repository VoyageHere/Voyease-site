from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message


app = Flask(__name__)

app.secret_key = "hardtoguess"

app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Replace with your email provider's SMTP server
app.config['MAIL_PORT'] = 587  # Typically 587 for TLS, 465 for SSL
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'myapptourguide@gmail.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'yppswvcbjonuwpco'  # Replace with your email password
app.config['MAIL_DEFAULT_SENDER'] = 'myapptourguide@gmail.com'

mail = Mail(app)


from . import routes