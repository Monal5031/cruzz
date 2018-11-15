# Django
from django.conf.urls import url

# local django
from authentication.views import RegistrationAPIView, LoginAPIView, UserRetrieveUpdateAPIView
from authentication import views


urlpatterns = [
    url(r'^users/registration/?$', RegistrationAPIView.as_view()),
    url(r'^users/login/?$', LoginAPIView.as_view()),
    url(r'^users/update/?$', UserRetrieveUpdateAPIView.as_view()),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),
]
