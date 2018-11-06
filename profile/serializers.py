# Django
from rest_framework import serializers

# local
from profile.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', required=False)
    bio = serializers.CharField(allow_blank=True, required=False)
    image = serializers.SerializerMethodField()
    following = serializers.SerializerMethodField()
    cover = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField(required=False)

    class Meta:
        model = Profile
        fields = ('username', 'bio', 'image', 'following', 'cover', 'user')
        read_only_fields = ('username',)

    def get_image(self, obj):
        if obj.image:
            return obj.image

        return 'https://thumb.ibb.co/eN5O0f/temp.jpg'

    def get_cover(self, obj):
        if obj.cover:
            return obj.cover

        return 'https://thumb.ibb.co/eN5O0f/temp.jpg'

    def get_following(self, instance):
        request = self.context.get('request', None)

        if request is None:
            return False

        if not request.user.is_authenticated:
            return False

        follower = request.user.profile
        followee = instance

        return follower.is_following(followee)

    def get_user(self, obj):
        print(obj)
