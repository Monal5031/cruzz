from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from rest_framework.test import APIRequestFactory

from core.utils import create_superuser, create_profile


class ProfileTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        cls.superuser = create_superuser()
        super(ProfileTests, cls).setUpClass()

    def setUp(self):
        self.dummy_profile1 = create_profile()
        self.dummy_profile2 = create_profile()

    def tearDown(self):
        self.dummy_profile1.delete()
        self.dummy_profile2.delete()

    @classmethod
    def tearDownClass(cls):
        cls.superuser.delete()
        super(ProfileTests, cls).tearDownClass()

    def test_profile_created(self):
        profile_data = {
            'user': {
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
            },
            'bio': 'dummy bio',
            'cover': 'dummy cover',
            'image': 'dummy image'
        }
        profile = create_profile(profile_data)

        self.assertEqual(profile.bio, profile_data['bio'])
        self.assertEqual(profile.image, profile_data['image'])
        self.assertEqual(profile.cover, profile_data['cover'])

    def test_follow_profile(self):
        self.assertEqual(self.dummy_profile2.follows.count(), 0)

        self.dummy_profile2.follow(self.dummy_profile1)

        self.assertEqual(self.dummy_profile2.follows.count(), 1)

    def test_unfollow_profile(self):
        self.dummy_profile2.follow(self.dummy_profile1)

        self.assertEqual(self.dummy_profile2.follows.count(), 1)

        self.dummy_profile2.unfollow(self.dummy_profile1)

        self.assertEqual(self.dummy_profile2.follows.count(), 0)

    def test_following(self):
        pass

    def test_followers(self):
        pass
