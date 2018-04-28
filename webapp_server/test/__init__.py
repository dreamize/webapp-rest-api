import logging

import connexion
from flask_testing import TestCase

from webapp_server.encoder import JSONEncoder
from webapp_server.database import db

class BaseTestCase(TestCase):

    def create_app(self):
        logging.getLogger('connexion.operation').setLevel('ERROR')
        app = connexion.App(__name__, specification_dir='../swagger/')
        app.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        app.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.app.json_encoder = JSONEncoder
        app.add_api('swagger.yaml')
        db.init_app(app.app)
        return app.app
