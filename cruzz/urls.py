# Django
from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.contrib import admin

# Local Django
import authentication.views


admin.autodiscover()

urlpatterns = [
    url('home', login_required(authentication.views.HomeView.as_view()), name='home'),
    path('admin/', admin.site.urls),
    path('', include('pwa.urls')),
    url(r'^api/', include(('landing.urls', 'api-views'), namespace='api-views')),
    url(r'^$', authentication.views.land, name='land'),
]
