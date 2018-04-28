from webapp_server.database import db
from webapp_server.database import models
from webapp_server.models import User


def create_user(user: User) -> int:
    """Method to create user

    :param user: Instance of swagger model's user
    :return: created users id
    """
    db_user = models.User()
    db_user.first_name = user.first_name
    db_user.last_name = user.last_name
    db_user.email = user.email
    db_user.password = user.password
    db.session.add(db_user)
    db.session.commit()
    return db_user.id
