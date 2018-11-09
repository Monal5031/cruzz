from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from rest_framework.test import APIRequestFactory


class ProfileTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        # stuff to do
        super(ProfileTests, cls).setUpClass()

    def setUp(self):
        # stuff to do
        pass

    def tearDown(self):
        # stuff to do
        pass

    @classmethod
    def tearDownClass(cls):
        # stuff to do
        super(ProfileTests, cls).tearDownClass()

    def test_profile_created(self):
        pass

    def test_follow_profile(self):
        pass

    def test_unfollow_profile(self):
        pass

    def test_following(self):
        pass

    def test_followers(self):
        pass
