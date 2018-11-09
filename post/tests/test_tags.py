from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from rest_framework.test import APIRequestFactory


class TagsTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        # stuff to do
        super(TagsTests, cls).setUpClass()

    def setUp(self):
        # stuff to do
        pass

    def tearDown(self):
        # stuff to do
        pass

    @classmethod
    def tearDownClass(cls):
        # stuff to do
        super(TagsTests, cls).tearDownClass()

    def test_retrive_all_tags(self):
        pass
