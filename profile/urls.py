# django
from django.conf.urls import url

# local django
from profile.views import ProfileRetrieveAPIView, ProfileFollowAPIView


urlpatterns = [
    url(r'^retrieve/(?P<username>\w+)/?$', ProfileRetrieveAPIView.as_view()),
    url(r'^(?P<username>\w+)/follow/?$', ProfileFollowAPIView.as_view())
]
