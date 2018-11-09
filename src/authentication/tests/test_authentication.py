from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.core.exceptions import ValidationError
from rest_framework.test import APIRequestFactory

from core.utils import create_valid_user, create_invalid_user, create_custom_user, create_superuser


class AuthenticationTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        cls.superuser = create_superuser()
        super(AuthenticationTests, cls).setUpClass()

    def setUp(self):
        self.dummy_valid_user1 = create_valid_user()
        self.dummy_valid_user2 = create_valid_user()
        self.dummy_invalid_user1 = create_invalid_user()
        self.dummy_invalid_user2 = create_invalid_user()

    def tearDown(self):
        self.dummy_invalid_user1.delete()
        self.dummy_invalid_user2.delete()
        self.dummy_valid_user1.delete()
        self.dummy_valid_user2.delete()

    @classmethod
    def tearDownClass(cls):
        cls.superuser.delete()
        super(AuthenticationTests, cls).tearDownClass()

    def test_create_new_valid_user(self):
        test_user_data = {
            'username': 'test',
            'email': 'test@test.com',
            'password': 'test12345',
            'first_name': 'test_first_name',
            'last_name': 'test_last_name',
            'city': 'Gandhinagar',
            'state': 'Gujarat',
            'country': 'India',
            'official_page': False,
            'is_active': True
        }
        test_user = create_custom_user(test_user_data)
        self.assertEqual(test_user_data['username'], test_user.username)
        self.assertEqual(test_user_data['email'], test_user.email)
        self.assertEqual(test_user_data['password'], test_user.password)
        self.assertEqual(test_user_data['first_name'], test_user.first_name)
        self.assertEqual(test_user_data['last_name'], test_user.last_name)
        self.assertEqual(test_user_data['city'], test_user.city)
        self.assertEqual(test_user_data['state'], test_user.state)
        self.assertEqual(test_user_data['country'], test_user.country)

    def test_create_new_invalid_user(self):
        test_user_data = {
            'username': 'test',
            'email': '',
            'password': 'test12345',
            'first_name': 'test_first_name',
            'last_name': 'test_last_name',
            'city': 'Gandhinagar',
            'state': 'Gujarat',
            'country': 'India',
            'official_page': False,
            'is_active': True
        }
        test_user = create_custom_user(test_user_data)
        self.assertRaisesRegexp(
            ValidationError,
            'This field cannot be blank',
            test_user.full_clean
        )

    def test_login_with_correct_credentials(self):
        pass

    def test_login_with_incorrect_username(self):
        pass

    def test_login_with_incorrect_email(self):
        pass

    def test_login_with_incorrect_password(self):
        pass

    def test_update_user_with_valid_username(self):
        self.dummy_valid_user1.username = 'my_new_username'
        self.dummy_valid_user1.save()

        self.assertEqual(self.dummy_valid_user1.username, 'my_new_username')

    def test_update_user_with_valid_first_name(self):
        self.dummy_valid_user1.first_name = 'new first name'
        self.dummy_valid_user1.save()

        self.assertEqual(self.dummy_valid_user1.first_name, 'new first name')

    def test_update_user_with_valid_last_name(self):
        self.dummy_valid_user1.last_name = 'new last name'
        self.dummy_valid_user1.save()

        self.assertEqual(self.dummy_valid_user1.last_name, 'new last name')

    def test_update_user_with_valid_city(self):
        self.dummy_valid_user1.city = 'new city'
        self.dummy_valid_user1.save()

        self.assertEqual(self.dummy_valid_user1.city, 'new city')

    def test_update_user_with_valid_state(self):
        self.dummy_valid_user1.state = 'new state'
        self.dummy_valid_user1.save()

        self.assertEqual(self.dummy_valid_user1.state, 'new state')

    def test_update_user_with_valid_country(self):
        self.dummy_valid_user1.country = 'new country'
        self.dummy_valid_user1.save()

        self.assertEqual(self.dummy_valid_user1.country, 'new country')

    def test_update_user_with_invalid_details(self):
        self.dummy_valid_user1.email = ''
        self.dummy_valid_user1.save()

        self.assertRaisesRegexp(
            ValidationError,
            'This field cannot be blank',
            self.dummy_valid_user1.full_clean
        )

    def test_create_superuser(self):
        self.assertEqual(self.superuser.username, 'admin')
        self.assertEqual(self.superuser.is_superuser, True)
        self.assertEqual(self.superuser.is_staff, True)
