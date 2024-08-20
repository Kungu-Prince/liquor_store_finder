from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

# Initialize dotenv
load_dotenv()

app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use an in-memory SQLite database
#app.config['GOOGLE_MAPS_API_KEY'] = os.getenv('GOOGLE_MAPS_API_KEY')

# Initialize extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import routes and models
from app import routes, models

@app.context_processor
def inject_globals():
    return dict(GOOGLE_MAPS_API_KEY=os.getenv('GOOGLE_MAPS_API_KEY'))