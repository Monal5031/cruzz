# Django
from django.db import models

# local django
from core.models import TimestampedModel


class Post(TimestampedModel):
    slug = models.SlugField(db_index=True, max_length=255, unique=True)
    title = models.CharField(db_index=True, max_length=255)

    description = models.TextField()
    body = models.TextField()

    # every post must have an author
    author = models.ForeignKey('profile.Profile', on_delete=models.CASCADE, related_name='posts')

    tags = models.ManyToManyField('Tag', related_name='posts')

    class Meta:
        app_label = 'post'

    def __str__(self):
        return str(self.title)


class Comment(TimestampedModel):
    body = models.TextField()
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey('profile.Profile', related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(str(self.post), str(self.author))


class Tag(TimestampedModel):
    tag = models.CharField(max_length=255)
    slug = models.SlugField(db_index=True, unique=True)

    def __str__(self):
        return str(self.tag)
