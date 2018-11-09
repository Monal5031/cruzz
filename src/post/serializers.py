# Django
from rest_framework import serializers

# local django
from authentication.models import User
from profile.serializers import ProfileSerializer
from post.models import Post, Comment, Tag
from post.relations import TagRelatedField


class PostSerializer(serializers.ModelSerializer):
    author = ProfileSerializer(read_only=True)
    body = serializers.CharField(required=True)
    description = serializers.CharField(required=False)
    slug = serializers.SlugField(required=False)
    title = serializers.CharField(required=True)

    favorited = serializers.SerializerMethodField()
    favoritesCount = serializers.SerializerMethodField(method_name='get_favorites_count')

    upvoted = serializers.SerializerMethodField()
    upvotesCount = serializers.SerializerMethodField(method_name='get_upvotes_count')

    downvoted = serializers.SerializerMethodField()
    downvotesCount = serializers.SerializerMethodField(method_name='get_downvotes_count')

    commentsCount = serializers.SerializerMethodField(method_name='get_comments_count')

    tagList = TagRelatedField(many=True, required=False, source='tags')

    # define methods for these fields
    createdAt = serializers.SerializerMethodField(method_name='get_created_at')
    updatedAt = serializers.SerializerMethodField(method_name='get_updated_at')

    class Meta:
        model = Post
        fields = (
            'author', 'body', 'createdAt',
            'description', 'favorited', 'favoritesCount',
            'slug', 'tagList', 'title', 'updatedAt',
            'upvoted', 'upvotesCount', 'downvoted', 'downvotesCount',
            'commentsCount'
        )

    def create(self, validated_data):
        author = self.context.get('author', None)
        tags = validated_data.pop('tags', [])

        user = User.objects.get(username=author)
        post = Post.objects.create(author=user.profile, **validated_data)

        for tag in tags:
            post.tags.add(tag)

        return post

    def get_created_at(self, instance):
        return instance.created_at.isoformat()

    def get_favorited(self, instance):
        request = self.context.get('request', None)

        if request is None:
            return False

        if not request.user.is_authenticated:
            return False

        return request.user.profile.has_favorited(instance)

    def get_favorites_count(self, instance):
        return instance.favorited_by.count()

    def get_upvoted(self, instance):
        request = self.context.get('request', None)

        if request is None:
            return False

        if not request.user.is_authenticated:
            return False

        return request.user.profile.has_upvoted(instance)

    def get_upvotes_count(self, instance):
        return instance.upvoted_by.count()

    def get_downvoted(self, instance):
        request = self.context.get('request', None)

        if request is None:
            return False

        if not request.user.is_authenticated:
            return False

        return request.user.profile.has_downvoted(instance)

    def get_downvotes_count(self, instance):
        return instance.downvoted_by.count()

    def get_updated_at(self, instance):
        return instance.updated_at.isoformat()

    def get_comments_count(self, instance):
        return instance.comments.count()


class CommentSerializer(serializers.ModelSerializer):
    author = ProfileSerializer(required=False)
    createdAt = serializers.SerializerMethodField(method_name='get_created_at')
    updatedAt = serializers.SerializerMethodField(method_name='get_updated_at')
    post_slug = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('id', 'author', 'body', 'createdAt', 'updatedAt', 'post_slug')

    def create(self, validated_data):
        print('hello')
        post = self.context['post']
        author = User.objects.get(username=self.context['author'])

        return Comment.objects.create(author=author.profile, post=post, **validated_data)

    def get_created_at(self, instance):
        return instance.created_at.isoformat()

    def get_updated_at(self, instance):
        return instance.updated_at.isoformat()

    def get_post_slug(self, instance):
        return instance.post.slug


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('tag',)

    def to_representation(self, obj):
        return obj.tag
