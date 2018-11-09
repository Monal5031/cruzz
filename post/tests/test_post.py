from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from rest_framework.test import APIRequestFactory


class PostTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        # stuff to do
        super(PostTests, cls).setUpClass()

    def setUp(self):
        # stuff to do
        pass

    def tearDown(self):
        # stuff to do
        pass

    @classmethod
    def tearDownClass(cls):
        # stuff to do
        super(PostTests, cls).tearDownClass()

    def test_create_post(self):
        pass

    def test_view_all_posts(self):
        pass

    def test_view_single_post(self):
        pass

    def test_update_post(self):
        pass

    def test_delete_post(self):
        pass

    def test_favorite_post(self):
        pass

    def test_unfavorite_post(self):
        pass

    def test_upvote_post(self):
        pass

    def test_remove_upvote_from_post(self):
        pass

    def test_downvote_post(self):
        pass

    def test_remove_downvote_from_post(self):
        pass
