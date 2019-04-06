import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'emr.db')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Easy-EMR'

    SQLALCHEMY_TRACK_MODIFICATIONS=False
    FLASK_ENV='development'
    BOOTSTRAP_SERVE_LOCAL=True