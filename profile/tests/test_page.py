from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from rest_framework.test import APIRequestFactory


class PagesTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        # stuff to do
        super(PagesTests, cls).setUpClass()

    def setUp(self):
        # stuff to do
        pass

    def tearDown(self):
        # stuff to do
        pass

    @classmethod
    def tearDownClass(cls):
        # stuff to do
        super(PagesTests, cls).tearDownClass()

    def test_create_official_page(self):
        pass

    def test_discover_official_pages(self):
        pass

