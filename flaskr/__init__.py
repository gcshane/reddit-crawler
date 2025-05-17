from . import crawl
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.register_blueprint(crawl.bp)
    return app
    