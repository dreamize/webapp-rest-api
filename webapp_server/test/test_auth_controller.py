# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from webapp_server.database import db
from webapp_server.models.user import User  # noqa: E501
from webapp_server.test import BaseTestCase


class TestAuthController(BaseTestCase):
    """AuthController integration test stubs"""

    def setUp(self):
        db.drop_all()
        db.create_all()

    def test_sign_up_user(self):
        """Test case for sign_up_user

        Create user account
        """
        user = {
            'firstName': 'first',
            'lastName': 'last',
            'email': 'test@test.com',
            'password': '1asd*'
        }
        response = self.client.open(
            '/v1/auth/signup',
            method='POST',
            data=json.dumps(user),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        response_user = User.from_dict(response.json)
        self.assertGreater(response_user.id, 0)
        self.assertEqual(response_user.first_name, user['firstName'])
        self.assertEqual(response_user.last_name, user['lastName'])
        self.assertEqual(response_user.email, user['email'])


if __name__ == '__main__':
    import unittest
    unittest.main()
