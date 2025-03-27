# app/__init__.py
from flask import Flask
from flask_mail import Mail
from app.config import Config
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)

# Initialize Flask-Mail
mail = Mail(app)

# Import views after initializing app and mail to avoid circular imports
from app import views