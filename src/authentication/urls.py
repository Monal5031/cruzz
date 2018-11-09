# Django
from django.conf.urls import url

# local django
from authentication.views import RegistrationAPIView, LoginAPIView, UserRetrieveUpdateAPIView


urlpatterns = [
    url(r'^users/registration/?$', RegistrationAPIView.as_view()),
    url(r'^users/login/?$', LoginAPIView.as_view()),
    url(r'^users/update/?$', UserRetrieveUpdateAPIView.as_view()),
]
