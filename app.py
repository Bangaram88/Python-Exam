from flask import Flask
from dotenv import load_dotenv
from flask_mongoengine import MongoEngine
import os
from api.routes import create_routes
from flask_restful import Api
import sys
from os import path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

load_dotenv()

default_config = {
    "MONGODB_SETTINGS": {
        'db': os.environ["APP"],
        'host': os.environ["HOST"],
        'port': 0,
    }
}



def main_flask_app():
    app = Flask(__name__)


    app.config.update(default_config)

    mongo = MongoEngine(app)

    api = Api(app=app)
    
    api = create_routes(api=api)

    return app

    


if __name__ == '__main__':
    app = main_flask_app()
    app.run(debug=True)
    