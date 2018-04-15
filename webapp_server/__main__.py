#!/usr/bin/env python3

import connexion

from webapp_server import encoder
from webapp_server.database import db


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
    app.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.add_api('swagger.yaml', arguments={'title': 'Authentication Service'})
    db.init_app(app.app)
    app.run(port=8080)


if __name__ == '__main__':
    main()
