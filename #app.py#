import os
from flask import Flask
from dotenv import load_dotenv
from src.routes.routes import blueprint as app_routes

load_dotenv()

app = Flask(__name__)

flask_secret_key = os.getenv('FLASK_SECRET_KEY')
app.secret_key = flask_secret_key

app.register_blueprint(app_routes)

if __name__ == "__main__":
    app.run(debug=True)


