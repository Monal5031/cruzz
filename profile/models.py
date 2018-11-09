# Django
from django.db import models

# local files
from core.models import TimestampedModel


class Profile(TimestampedModel):
    # User and profile relation
    user = models.OneToOneField(
        'authentication.User', on_delete=models.CASCADE
    )

    bio = models.TextField(blank=True, null=True)

    image = models.URLField(blank=True, null=True)
    cover = models.URLField(blank=True, null=True)

    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)
    favorites = models.ManyToManyField('post.Post', related_name='favorited_by')
    upvotes = models.ManyToManyField('post.Post', related_name='upvoted_by')
    downvotes = models.ManyToManyField('post.Post', related_name='downvoted_by')

    def __str__(self):
        return str(self.user.username)

    def follow(self, profile):
        """Follow profile if we're not already following it."""
        self.follows.add(profile)

    def unfollow(self, profile):
        """Unfollow profile if we're already following it."""
        self.follows.remove(profile)

    def is_following(self, profile):
        """True is we're following else False"""
        return self.follows.filter(pk=profile.pk).exists()

    def is_followed_by(self, profile):
        """True if profile is following us else False"""
        return self.followed_by.filter(pk=profile.pk).exists()

    def favorite(self, post):
        """Favorite post if we haven't"""
        self.favorites.add(post)

    def unfavorite(self, post):
        """Unfavorite if we have already"""
        self.favorites.remove(post)

    def has_favorited(self, post):
        """True if favorited else False"""
        return self.favorites.filter(pk=post.pk).exists()

    def upvote(self, post):
        """ Upvote if we haven't and remove from downvote"""
        self.upvotes.add(post)
        self.downvotes.remove(post)

    def downvote(self, post):
        """ downvote if we haven't and remove from upvote"""
        self.downvotes.add(post)
        self.upvotes.remove(post)

    def has_upvoted(self, post):
        """True if upvoted else False"""
        return self.upvotes.filter(pk=post.pk).exists()

    def has_downvoted(self, post):
        """True if downvoted else False"""
        return self.downvotes.filter(pk=post.pk).exists()

    def get_favorites(self):
        """Get all the posts favorited by user"""
        return self.favorites.all()

    def get_upvotes(self):
        """Get all the posts upvoted by user"""
        return self.upvotes.all()

    def get_downvotes(self):
        """Get all the posts downvoted by user"""
        return self.downvotes.all()
