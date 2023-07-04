from flask import Flask
from .portfolio import bp

def create_app(test_config=None):
    app = Flask(__name__)
    app.secret_key = 'h432hi5ohi3h5i5hi3o2hi'

    
    app.register_blueprint(bp)

    return app