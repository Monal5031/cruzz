import json

from django.test import TestCase
from rest_framework.test import APIRequestFactory

from authentication import views


class AuthAPITest(TestCase):
    pass

    # def test_register_login_update_user(self):
    #     # create new user
    #     new_user = {
    #         "user":
    #         {
    #             "email": "mohit@yadav.com",
    #             "username": "peace",
    #             "password": "peacepeace",
    #             "is_staff": "True",
    #             "is_superuser": "True"
    #         }
    #     }
    #     view = views.RegistrationAPIView.as_view()
    #     factory = APIRequestFactory()
    #     request = factory.post('/api/authentication/users/registration/', json.dumps(new_user), content_type='application/json')
    #     response = view(request)
    #     response_email = response.data['email']
    #     response_username = response.data['username']
    #     response_code = response.status_code
    #     with self.subTest():
    #         self.assertEqual(response_email, new_user['user']['email'])
    #     with self.subTest():
    #         self.assertEqual(response_username, new_user['user']['username'])
    #     with self.subTest():
    #         self.assertEqual(response_code, 201)
    #
    #     # test for login
    #     new_user = {
    #         "user":
    #         {
    #             "username": "peace",
    #             "password": "peacepeace",
    #             "email": "mohit@yadav.com"
    #         }
    #     }
    #     view = views.LoginAPIView.as_view()
    #     factory = APIRequestFactory()
    #     request = factory.post('/api/authentication/users/login/', json.dumps(new_user), content_type='application/json')
    #     response = view(request)
    #     response_email = response.data['email']
    #     response_username = response.data['username']
    #     response_code = response.status_code
    #     with self.subTest():
    #         self.assertEqual(response_email, new_user['user']['email'])
    #     with self.subTest():
    #         self.assertEqual(response_username, new_user['user']['username'])
    #     with self.subTest():
    #         self.assertEqual(response_code, 200)
