from flask import Flask
from src.routes.routes import blueprint as app_routes

app = Flask(__name__)

app.register_blueprint(app_routes)

if __name__ == "__main__":
    app.run(debug=True)


