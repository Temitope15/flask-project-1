from flask import Flask
from .extensions import db, ma
from .routes import auth, dashboard

def create_app(config_objects):
    app = Flask(__name__)
    
    app.config.from_object(config_objects)

    #initialize extensions

    db.init_app(app)
    ma.init_app(app)

    #register blueprints

    app.register_blueprint(auth.bp)
    app.register_blueprint(dashboard.bp)

    return app


