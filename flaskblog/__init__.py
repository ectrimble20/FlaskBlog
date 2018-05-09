from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = "smtp.googlemail.com"
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('FLASK_EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('FLASK_EMAIL_PASS')
mail = Mail(app)


from flaskblog.users.routes import users
app.register_blueprint(users)

from flaskblog.posts.routes import posts
app.register_blueprint(posts)

from flaskblog.main.routes import main
app.register_blueprint(main)
