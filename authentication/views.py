# Django
from django.contrib.auth import login
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import View
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

# Local Django
from authentication.models import User
from authentication.serializers import RegistrationSerializer, LoginSerializer, UserUpdateSerializer
from authentication.renderers import UserJSONRenderer
from core.tokens import account_activation_token


def land(request):
    return render(request, 'home.html')


class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')


class RegistrationAPIView(APIView):
    # Allow any user (authenticated or not) to hit this endpoint.
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data.get('user', {})

        # The create serializer, validate serializer, save serializer pattern
        # below is common.
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user = User.objects.get(email=serializer.data['email'])

        current_site = get_current_site(request)
        print(current_site)
        mail_subject = 'Activate your Vconnect account.'
        message = render_to_string('acc_active_email.html', {
            'user': user,
            'domain': current_site,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
            'token': account_activation_token.make_token(user),
        })
        print(message)
        to_email = serializer.data['email']
        email = EmailMessage(
            mail_subject, message, to=[to_email]
        )
        print(email, to_email)

        # email.send()

        serializer.data['is_active'] = False
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data.get('user', {})

        # Notice here that we do not call `serializer.save()` like we did for
        # the registration endpoint. This is because we don't have
        # anything to save. Instead, the `validate` method on our serializer
        # handles everything we need.
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = UserUpdateSerializer

    def get(self, request, *args, **kwargs):
        # There is nothing to validate or save here. Instead, we just want the
        # serializer to handle turning our `User` object into something that
        # can be JSONified and sent to the client.
        serializer = self.serializer_class(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        user_data = request.data.get('user', {})

        serializer_data = {
            'first_name': user_data.get('first_name', None if request.user.first_name is None else request.user.first_name),
            'last_name': user_data.get('last_name', None if request.user.last_name is None else request.user.last_name),
            'city': user_data.get('city', None if request.user.city is None else request.user.city),
            'state': user_data.get('state', None if request.user.state is None else request.user.state),
            'country': user_data.get('country', None if request.user.country is None else request.user.country),
            'username': user_data.get('username', None if request.user.username is None else request.user.username),
            'email': user_data.get('email', None if request.user.email is None else request.user.email),
            'is_staff': user_data.get('is_staff', None if request.user.is_staff is None else request.user.is_staff),
            'is_superuser': user_data.get('is_superuser', None if request.user.is_superuser is None else request.user.is_superuser),
            'bio': user_data.get('bio', None if request.user.profile.bio is None else request.user.profile.bio),
            'image': user_data.get('image', None if request.user.profile.image is None else request.user.profile.image),
            'cover': user_data.get('cover', None if request.user.profile.cover is None else request.user.profile.cover),
            'official_page': user_data.get('official_page', None if request.user.official_page is None else request.user.official_page)
        }

        # Here is that serialize, validate, save pattern we talked about
        # before.
        serializer = self.serializer_class(
            request.user, data=serializer_data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


def activate(request, uidb64, token, backend='django.contrib.auth.backends.ModelBackend'):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return render(request, 'email_confirmed.html')
    else:
        return HttpResponse('Activation link is invalid!')
