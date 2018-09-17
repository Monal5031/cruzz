# Django
from django.conf.urls import url

# local django
from landing.views import RegistrationAPIView, LoginAPIView, UserRetrieveUpdateAPIView


urlpatterns = [
    url(r'^users/registration/?$', RegistrationAPIView.as_view()),
    url(r'^users/login/?$', LoginAPIView.as_view()),
    url(r'^user/checklogin/?$', UserRetrieveUpdateAPIView.as_view()),
]
