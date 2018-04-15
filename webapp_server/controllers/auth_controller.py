import connexion
import six

from webapp_server.database.data_access import create_user
from webapp_server.models.user import User  # noqa: E501
from webapp_server import util


def sign_up_user(user):  # noqa: E501
    """Create user account

    This creates user account and triggers. # noqa: E501

    :param user: Created user object
    :type user: dict | bytes

    :rtype: None
    """
    user_obj = User.from_dict(user)  # noqa: E501
    result = create_user(user_obj)
    if result > 0:
        user_obj.id = result
        user_obj.password = ''
        return user_obj
    else:
        return 500
