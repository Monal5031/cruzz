# django
from django.conf.urls import url

# local django
from profile.views import (ProfileRetrieveAPIView, ProfileFollowAPIView,
                           ProfileFollowingAPIView, ProfileFollowersAPIView,
                           PageSuggestionAPIView)


urlpatterns = [
    url(r'^retrieve/(?P<username>\w+)/?$', ProfileRetrieveAPIView.as_view()),
    url(r'^(?P<username>\w+)/follow/?$', ProfileFollowAPIView.as_view()),
    url(r'^following/?$', ProfileFollowingAPIView.as_view()),
    url(r'^followers/?$', ProfileFollowersAPIView.as_view()),
    url(r'^discover/pages/?$', PageSuggestionAPIView.as_view())
]
