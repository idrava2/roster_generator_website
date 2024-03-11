

from flask import Flask


def create_app(**config):
    app = Flask(__name__)
    app.config.from_mapping(**config)
    
    return app



app = create_app() 


@app.route("/")
def index():
    return "IDRAVA WAS HERE"

