from flask import Flask


def start_app():
    
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'H432HDF832HBDNGGFYG'

    from frt import frt
    from auth import auth

    app.register_blueprint(frt, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app