from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from social_django.models import UserSocialAuth

from  .forms import ProfileForm


def land(request):
    return render(request, 'base.html')


class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')


# only4 testing
def test_func():
    return True
