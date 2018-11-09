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
    first_name = serializers.SerializerMethodField(required=False, allow_null=True)
    last_name = serializers.SerializerMethodField(required=False, allow_null=True)
    city = serializers.SerializerMethodField(required=False, allow_null=True)
    state = serializers.SerializerMethodField(required=False, allow_null=True)
    country = serializers.SerializerMethodField(required=False, allow_null=True)
    official_page = serializers.SerializerMethodField(required=False, allow_null=True)
    followingCount = serializers.SerializerMethodField(method_name='get_following_count')
    followersCount = serializers.SerializerMethodField(method_name='get_followers_count')

    class Meta:
        model = Profile
        fields = ('username', 'bio', 'image', 'following', 'cover',
                  'first_name', 'last_name', 'city', 'state', 'country',
                  'official_page', 'followingCount', 'followersCount')
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

    def get_first_name(self, obj):
        return obj.user.first_name

    def get_last_name(self, obj):
        return obj.user.last_name

    def get_city(self, obj):
        return obj.user.city

    def get_state(self, obj):
        return obj.user.state

    def get_country(self, obj):
        return obj.user.country

    def get_official_page(self, obj):
        return obj.user.official_page

    def get_following_count(self, obj):
        return obj.follows.count()

    def get_followers_count(self, obj):
        print(Profile.objects.all().filter(follows__user__username=obj.user.username))
        return Profile.objects.all().filter(follows__user__username=obj.user.username).count()
