# django
from django.conf.urls import url

# local django
from profile.views import ProfileRetrieveAPIView, ProfileFollowAPIView, ProfileFollowingAPIView


urlpatterns = [
    url(r'^retrieve/(?P<username>\w+)/?$', ProfileRetrieveAPIView.as_view()),
    url(r'^(?P<username>\w+)/follow/?$', ProfileFollowAPIView.as_view()),
    url(r'^following/?$', ProfileFollowingAPIView.as_view())
]
