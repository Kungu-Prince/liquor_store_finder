from app import app
from dotenv import load_dotenv
import os

load_dotenv()
GOOGLE_MAPS_API_KEY = os.getenv('GOOGLE_MAPS_API_KEY')
if __name__ == '__main__':
    app.run(debug=True)
