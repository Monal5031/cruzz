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
