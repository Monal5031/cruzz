# Django
from rest_framework import serializers

# local django
from authentication.models import User
from profile.serializers import ProfileSerializer
from post.models import Post, Comment, Tag
from post.relations import TagRelatedField


class PostSerializer(serializers.ModelSerializer):
    author = ProfileSerializer(read_only=True)
    description = serializers.CharField(required=False)
    slug = serializers.SlugField(required=False)

    favorited = serializers.SerializerMethodField()
    favoritesCount = serializers.SerializerMethodField(method_name='get_favorites_count')

    tagList = TagRelatedField(many=True, required=False, source='tags')

    # define methods for these fields
    createdAt = serializers.SerializerMethodField(method_name='get_created_at')
    updatedAt = serializers.SerializerMethodField(method_name='get_updated_at')

    class Meta:
        model = Post
        fields = (
            'author', 'body', 'createdAt',
            'description', 'favorited', 'favoritesCount',
            'slug', 'tagList', 'title', 'updatedAt'
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

        if not request.user.is_authenticated():
            return False

        return request.user.profile.has_favorited(instance)

    def get_favorites_count(self, instance):
        return instance.favorited_by.count()

    def get_updated_at(self, instance):
        return instance.updated_at.isoformat()


class CommentSerializer(serializers.ModelSerializer):
    author = ProfileSerializer(required=False)
    createdAt = serializers.SerializerMethodField(method_name='get_created_at')
    updatedAt = serializers.SerializerMethodField(method_name='get_updated_at')

    class Meta:
        model = Comment
        fields = ('id', 'author', 'body', 'createdAt', 'updatedAt',)

    def create(self, validated_data):
        post = self.context['post']
        author = User.objects.get(username=self.context['author'])

        return Comment.objects.create(author=author.profile, post=post, **validated_data)

    def get_created_at(self, instance):
        return instance.created_at.isoformat()

    def get_updated_at(self, instance):
        return instance.updated_at.isoformat()


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('tag',)

    def to_representation(self, obj):
        return obj.tag
