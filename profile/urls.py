# django
from django.conf.urls import url

# local django
from profile.views import ProfileRetrieveAPIView


urlpatterns = [
    url(r'^retrieve/(?P<username>\w+)/?$', ProfileRetrieveAPIView.as_view())
]
