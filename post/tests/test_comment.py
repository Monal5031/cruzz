from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from rest_framework.test import APIRequestFactory


class CommentTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        # stuff to do
        super(CommentTests, cls).setUpClass()

    def setUp(self):
        # stuff to do
        pass

    def tearDown(self):
        # stuff to do
        pass

    @classmethod
    def tearDownClass(cls):
        # stuff to do
        super(CommentTests, cls).tearDownClass()

    def test_create_comment(self):
        pass

    def test_view_all_comments(self):
        pass

    def test_view_single_comment(self):
        pass

    def test_update_comment(self):
        pass

    def test_delete_comment(self):
        pass
