from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from rest_framework.test import APIRequestFactory

import post
from core.utils import create_superuser, create_valid_user, create_post, create_custom_comment, create_comment
from post.models import Comment, Post


class CommentTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        cls.superuser = create_superuser()
        super(CommentTests, cls).setUpClass()

    def setUp(self):
        self.dummy_user1 = create_valid_user()
        self.dummy_user2 = create_valid_user()
        self.dummy_profile1 = self.dummy_user1.profile
        self.dummy_profile2 = self.dummy_user2.profile
        self.dummy_post1 = create_post()
        self.dummy_post2 = create_post()

        self.dummy_comment1 = create_comment()
        self.dummy_comment2 = create_comment()

    def tearDown(self):
        self.dummy_post1.delete()
        self.dummy_post2.delete()
        self.dummy_user1.delete()
        self.dummy_user2.delete()
        self.dummy_profile1.delete()
        self.dummy_profile2.delete()

    @classmethod
    def tearDownClass(cls):
        cls.superuser.delete()
        super(CommentTests, cls).tearDownClass()

    def test_create_comment(self):
        comment_data = {
            'body': 'test comment body',
            'author': self.dummy_profile1,
            'post': self.dummy_post1
        }

        comment = create_custom_comment(comment_data)

        self.assertEqual(comment_data['body'], comment.body)

    def test_view_all_comments(self):
        pass

    def test_view_single_comment(self):
        pass

    def test_update_comment(self):
        comment_data = {
            'body': 'test comment body',
            'author': self.dummy_profile1,
            'post': self.dummy_post1
        }

        comment = create_custom_comment(comment_data)

        self.assertEqual(comment_data['body'], comment.body)

        comment.body = 'updated comment'
        comment.save()

        self.assertEqual(comment.body, 'updated comment')

    def test_delete_comment(self):
        count = Comment.objects.count()

        self.dummy_comment2.delete()

        self.assertEqual(Comment.objects.count(), count-1)
