from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from rest_framework.test import APIRequestFactory

from core.utils import create_superuser, create_custom_tags, create_tag


class TagsTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        cls.superuser = create_superuser()
        super(TagsTests, cls).setUpClass()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.superuser.delete()
        super(TagsTests, cls).tearDownClass()

    def test_retrive_all_tags(self):
        tags = ['newpost', 'dummy test', 'something new']
        created_tags = create_custom_tags(tags)

        self.assertEqual(str(created_tags[0]) in tags, True)
        self.assertIn(str(created_tags[0]), tags)

        new_tag = create_tag()

        self.assertNotIn(str(new_tag), tags)
