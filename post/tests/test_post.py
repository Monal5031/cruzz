from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from rest_framework.test import APIRequestFactory

from core.utils import create_superuser, create_valid_user, create_post, create_custom_post


class PostTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        cls.superuser = create_superuser()
        super(PostTests, cls).setUpClass()

    def setUp(self):
        self.dummy_user1 = create_valid_user()
        self.dummy_user2 = create_valid_user()
        self.dummy_profile1 = self.dummy_user1.profile
        self.dummy_profile2 = self.dummy_user2.profile
        self.dummy_post1 = create_post()
        self.dummy_post2 = create_post()

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
        super(PostTests, cls).tearDownClass()

    def test_create_post(self):
        post_data = {
            'author': {
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
                'bio': 'test bio',
                'image': 'test image',
                'cover': 'test cover'
            },
            'slug': 'test slug',
            'title': 'test title',
            'description': 'test description',
            'body': 'test body'
        }

        post = create_custom_post(post_data)

        self.assertEqual(post_data['slug'], post.slug)
        self.assertEqual(post_data['title'], post.title)
        self.assertEqual(post_data['description'], post.description)
        self.assertEqual(post_data['body'], post.body)
        self.assertEqual(post_data['title'], str(post))

    def test_view_all_posts(self):
        pass

    def test_view_single_post(self):
        pass

    def test_update_post(self):
        pass

    def test_delete_post(self):
        pass

    def test_favorite_post(self):
        self.assertNotIn(self.dummy_post1, self.dummy_profile1.favorites.all())
        self.assertEqual(self.dummy_profile1.favorites.count(), 0)

        self.dummy_profile1.favorite(self.dummy_post1)

        self.assertIn(self.dummy_post1, self.dummy_profile1.favorites.all())
        self.assertEqual(self.dummy_profile1.favorites.count(), 1)

    def test_unfavorite_post(self):
        self.assertNotIn(self.dummy_post1, self.dummy_profile1.favorites.all())
        self.assertEqual(self.dummy_profile1.favorites.count(), 0)

        self.dummy_profile1.favorite(self.dummy_post1)

        self.assertIn(self.dummy_post1, self.dummy_profile1.favorites.all())
        self.assertEqual(self.dummy_profile1.favorites.count(), 1)

        self.dummy_profile1.unfavorite(self.dummy_post1)

        self.assertNotIn(self.dummy_post1, self.dummy_profile1.favorites.all())
        self.assertEqual(self.dummy_profile1.favorites.count(), 0)

    def test_upvote_post(self):
        self.assertNotIn(self.dummy_post1, self.dummy_profile1.upvotes.all())
        self.assertEqual(self.dummy_profile1.upvotes.count(), 0)

        self.dummy_profile1.upvote(self.dummy_post1)

        self.assertIn(self.dummy_post1, self.dummy_profile1.upvotes.all())
        self.assertEqual(self.dummy_profile1.upvotes.count(), 1)

    def test_remove_upvote_from_post(self):
        self.assertNotIn(self.dummy_post1, self.dummy_profile1.upvotes.all())
        self.assertEqual(self.dummy_profile1.upvotes.count(), 0)

        self.dummy_profile1.upvote(self.dummy_post1)

        self.assertIn(self.dummy_post1, self.dummy_profile1.upvotes.all())
        self.assertEqual(self.dummy_profile1.upvotes.count(), 1)

        self.dummy_profile1.remove_upvote(self.dummy_post1)

        self.assertNotIn(self.dummy_post1, self.dummy_profile1.upvotes.all())
        self.assertEqual(self.dummy_profile1.upvotes.count(), 0)

    def test_downvote_post(self):
        self.assertNotIn(self.dummy_post1, self.dummy_profile1.downvotes.all())
        self.assertEqual(self.dummy_profile1.downvotes.count(), 0)

        self.dummy_profile1.downvote(self.dummy_post1)

        self.assertIn(self.dummy_post1, self.dummy_profile1.downvotes.all())
        self.assertEqual(self.dummy_profile1.downvotes.count(), 1)

    def test_remove_downvote_from_post(self):
        self.assertNotIn(self.dummy_post1, self.dummy_profile1.downvotes.all())
        self.assertEqual(self.dummy_profile1.downvotes.count(), 0)

        self.dummy_profile1.downvote(self.dummy_post1)

        self.assertIn(self.dummy_post1, self.dummy_profile1.downvotes.all())
        self.assertEqual(self.dummy_profile1.downvotes.count(), 1)

        self.dummy_profile1.remove_downvote(self.dummy_post1)

        self.assertNotIn(self.dummy_post1, self.dummy_profile1.downvotes.all())
        self.assertEqual(self.dummy_profile1.downvotes.count(), 0)
