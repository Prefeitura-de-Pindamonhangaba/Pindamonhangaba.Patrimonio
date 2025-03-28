from flask import Flask
from flask_cors import CORS
from database import db
from controllers.item_controller import item_bp
from controllers.physical_location_controller import physical_location_bp
import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

app = Flask(__name__)
CORS(app, 
     resources={r"/*": {
         "origins": ["http://localhost:3000"],
         "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
         "allow_headers": ["Content-Type", "Authorization"],
         "supports_credentials": True
     }})

app.config['DATABASE_HOST'] = f'{os.getenv('DB_HOST')}'
app.config['DATABASE_NAME'] = f'{os.getenv('DB_NAME')}'
app.config['DATABASE_USER'] = f'{os.getenv('DB_USER')}'
app.config['DATABASE_PASSWORD'] = f'{os.getenv('DB_PASSWORD')}'

db.init_app(app)

app.register_blueprint(item_bp)
app.register_blueprint(physical_location_bp)

@app.route('/')
def index():
    return "Olá do seu backend Flask com PostgreSQL!"

if __name__ == '__main__':
    app.run(debug=True)