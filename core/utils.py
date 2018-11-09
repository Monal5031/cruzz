# standard libs
import random
import string

from authentication.models import User
from post.models import Post, Comment, Tag

DEFAULT_CHAR_STRING = string.ascii_lowercase + string.digits


def generate_random_string(chars=DEFAULT_CHAR_STRING, size=6):
    return ''.join(random.choice(chars) for _ in range(size))


def create_valid_user():
    user = User.objects.create(
        username=generate_random_string(size=10),
        email=generate_random_string(size=6)+'@test.com',
        password=generate_random_string(size=10),
        is_active=True,
        is_staff=False,
        is_superuser=False,
        first_name=generate_random_string(size=12),
        last_name=generate_random_string(size=12),
        city=generate_random_string(size=15),
        state=generate_random_string(size=15),
        country=generate_random_string(size=15),
        official_page=False
    )

    user.save()
    return user


def create_invalid_user():
    user = User.objects.create(
        username=generate_random_string(size=10),
        email=generate_random_string(size=6),
        password=generate_random_string(size=10),
        is_active=True,
        is_staff=False,
        is_superuser=False,
        first_name=generate_random_string(size=12),
        last_name=generate_random_string(size=12),
        city=generate_random_string(size=15),
        state=generate_random_string(size=15),
        country=generate_random_string(size=15),
        official_page=False
    )

    user.save()
    return user


def create_custom_user(user_data):
    user = User.objects.create(
        username=user_data['username'],
        email=user_data['email'],
        password=user_data['password'],
        is_active=user_data['is_active'],
        first_name=user_data['first_name'],
        last_name=user_data['last_name'],
        city=user_data['city'],
        state=user_data['state'],
        country=user_data['country'],
        official_page=user_data['official_page']
    )

    user.save()
    return user


def create_superuser():
    user = User.objects.create(
        username='admin',
        email='admin@admin.com',
        password='admin12345',
        is_active=True,
        is_staff=True,
        is_superuser=True,
        first_name='admin',
        last_name='admin',
        city='admin_city',
        state='admin_state',
        country='admin_country',
        official_page=False
    )

    user.save()
    return user


def create_official_page():
    user = User.objects.create(
        username=generate_random_string(size=10),
        email=generate_random_string(size=6) + '@test.com',
        password=generate_random_string(size=10),
        is_active=True,
        is_staff=False,
        is_superuser=False,
        first_name=generate_random_string(size=12),
        last_name=generate_random_string(size=12),
        city=generate_random_string(size=15),
        state=generate_random_string(size=15),
        country=generate_random_string(size=15),
        official_page=True
    )

    user.save()
    return user


def create_profile(user_data=None):
    if not user_data:
        return create_custom_user(user_data).profile
    return create_valid_user().profile


def create_post():
    post = Post.objects.create(
        slug=None,
        title=generate_random_string(size=10),
        description=generate_random_string(size=50),
        body=generate_random_string(size=40),
        author=create_profile(),
        tags=create_tag()
    )

    post.save()
    return post


def create_custom_post(post_data):
    post = Post.objects.create(
        slug=post_data['slug'],
        title=post_data['title'],
        description=post_data['description'],
        body=post_data['body'],
        author=create_profile(post_data['author']),
        tags=create_tag()
    )

    post.save()
    return post


def create_comment():
    comment = Comment.objects.create(
        body=generate_random_string(size=30),
        post=create_post(),
        author=create_profile()
    )

    comment.save()
    return comment


def create_custom_comment(comment_data):
    comment = Comment.objects.create(
        body=comment_data['body'],
        post=create_custom_post(comment_data['post']),
        author=create_profile(comment_data['author'])
    )

    comment.save()
    return comment


def create_tag():
    tags = Tag.objects.create(
        tag=generate_random_string(7)
    )

    tags.save()
    return tags


def create_custom_tags(tags=None):
    return [Tag.objects.create(tag=tag).save() for tag in tags]
