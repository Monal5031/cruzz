# django
from rest_framework import serializers, status, mixins
from rest_framework.exceptions import NotFound
from rest_framework.generics import RetrieveAPIView, GenericAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

# local django
from authentication.models import User
from authentication.serializers import UserUpdateSerializer
from profile.models import Profile
from profile.renderers import ProfileJSONRenderer
from profile.serializers import ProfileSerializer


class ProfileRetrieveAPIView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    queryset = Profile.objects.select_related('user')
    renderer_classes = (ProfileJSONRenderer,)
    serializer_class = ProfileSerializer
    user_serializer_class = UserUpdateSerializer

    def get(self, request, *args, **kwargs):
        # Try to retrieve the requested profile and throw an exception if the
        # profile could not be found.
        try:
            profile = self.queryset.get(user__username=kwargs['username'])
        except Profile.DoesNotExist:
            raise NotFound('A profile with ' + kwargs['username'] + ' username does not exist.')

        serializer = self.serializer_class(profile, context={
            'request': request
        })

        user_serializer = self.user_serializer_class(request.user)
        new_data = {
            'profile': serializer.data,
            'user': user_serializer.data
        }

        return Response(new_data, status=status.HTTP_200_OK)


class ProfileFollowAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (ProfileJSONRenderer,)
    serializer_class = ProfileSerializer

    def delete(self, request, username=None):
        follower = self.request.user.profile

        try:
            followee = Profile.objects.get(user__username=username)
        except Profile.DoesNotExist:
            raise NotFound('A profile with this username was not found')

        follower.unfollow(followee)

        serializer = self.serializer_class(followee, context={
            'request': request
        })

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, username=None):
        follower = self.request.user.profile

        try:
            followee = Profile.objects.get(user__username=username)
        except Profile.DoesNotExist:
            raise NotFound('A profile with this username was not found.')

        if follower.pk is followee.pk:
            raise serializers.ValidationError('You can\'t follow yourself')

        follower.follow(followee)

        serializer = self.serializer_class(followee, context={
            'request': request
        })

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProfileFollowingAPIView(mixins.ListModelMixin, GenericAPIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (ProfileJSONRenderer,)
    serializer_class = ProfileSerializer

    def get_queryset(self):
        user = self.request.query_params.get('user', None)
        try:
            user = User.objects.get(username=user)
        except User.DoesNotExist:
            raise NotFound('User with this username was not found.')

        profile = Profile.objects.get(user=user)

        return profile.follows.all()

    def get(self, request):
        serializer_context = {'request': request}
        page = LimitOffsetPagination()
        paginated_result = page.paginate_queryset(self.get_queryset(), request)

        serializer = self.serializer_class(paginated_result, context=serializer_context, many=True)

        new_data = {
            'profiles': serializer.data
        }

        return Response(new_data)


class ProfileFollowersAPIView(mixins.ListModelMixin, GenericAPIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (ProfileJSONRenderer,)
    serializer_class = ProfileSerializer

    def get_queryset(self):
        user = self.request.query_params.get('user', None)
        try:
            user = User.objects.get(username=user)
        except User.DoesNotExist:
            raise NotFound('User with this username was not found.')

        query_set = Profile.objects.all()
        query_set = query_set.filter(follows__user__username=user.username)

        # profile = Profile.objects.get(user=user)
        # ids_of_followers = list()
        # for profiler in Profile.objects.all():
        #     if profile in profiler.follows.all() and profile is not profiler:
        #         ids_of_followers.append(profiler.pk)

        return query_set

    def get(self, request):
        serializer_context = {'request': request}
        page = LimitOffsetPagination()
        paginated_result = page.paginate_queryset(self.get_queryset(), request)

        serializer = self.serializer_class(paginated_result, context=serializer_context, many=True)

        new_data = {
            'profiles': serializer.data
        }

        return Response(new_data)


class PageSuggestionAPIView(mixins.ListModelMixin, GenericAPIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (ProfileJSONRenderer,)
    serializer_class = ProfileSerializer

    def get_queryset(self, user):

        profile = Profile.objects.get(user=user)

        query_set = profile.follows.all()
        query_set = Profile.objects.exclude(pk__in=query_set.values_list('pk', flat=True))
        query_set = query_set.filter(user__official_page=True)

        return query_set

    def get(self, request):
        serializer_context = {'request': request}
        serializer = self.serializer_class(self.get_queryset(request.user), context=serializer_context, many=True)

        new_data = {
            'profiles': serializer.data
        }

        return Response(new_data)
