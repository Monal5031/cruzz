from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from rest_framework.test import APIRequestFactory

from core.utils import create_superuser, create_custom_user, create_official_page, create_valid_user


class PagesTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        cls.superuser = create_superuser()
        super(PagesTests, cls).setUpClass()

    def setUp(self):
        self.dummy_page1 = create_official_page()
        self.dummy_page2 = create_official_page()
        self.dummy_user = create_valid_user()

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.superuser.delete()
        super(PagesTests, cls).tearDownClass()

    def test_create_official_page(self):
        test_user_data = {
            'username': 'iiitvcc',
            'email': 'codingclub@iiitvadodara.ac.in',
            'password': 'ccOfficecp',
            'first_name': 'IIITV',
            'last_name': 'Coding Club',
            'city': 'Gandhinagar',
            'state': 'Gujarat',
            'country': 'India',
            'official_page': True,
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

    def test_discover_official_pages(self):
        pass

