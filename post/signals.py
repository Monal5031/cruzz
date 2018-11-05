# django
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

# local django
from core.utils import generate_random_string
from post.models import Post


@receiver(pre_save, sender=Post)
def add_slug_to_article_if_not_exists(sender, instance, *args, **kwargs):
    MAXIMUM_SLUG_LENGTH = 255

    if instance and not instance.slug:
        slug = slugify(instance.title)
        unique = generate_random_string()

        if len(slug) > MAXIMUM_SLUG_LENGTH:
            slug = slug[:MAXIMUM_SLUG_LENGTH]

        while len(slug + '-' + unique) > MAXIMUM_SLUG_LENGTH:
            parts = slug.split('-')

            if len(parts) is 1:
                # the slug has no hyphens
                # to append the unique string we must remove characters from the end of the string
                slug = slug[:MAXIMUM_SLUG_LENGTH - len(unique) - 1]
            else:
                slug = '-'.join(parts[:-1])

        instance.slug = slug + '-' + unique
