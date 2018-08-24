from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
import landing.views
admin.autodiscover()

urlpatterns = [
    url('home', login_required(landing.views.HomeView.as_view()), name='home'),
    path('admin/', admin.site.urls),
    path('', include('pwa.urls')),
    url(r'^$', landing.views.land, name='land'),
]
