from django.conf.urls import include, url

from rest_framework.routers import DefaultRouter

from post.views import (PostViewSet, PostsFavoriteAPIView,
                        CommentsListCreateAPIView, CommentsDestroyAPIView,
                        TagListAPIView, PostsFeedAPIView)

router = DefaultRouter(trailing_slash=False)
router.register(r'posts', PostViewSet)

urlpatterns = [
    url(r'^feed/?$', PostsFeedAPIView.as_view()),
    url(r'^(?P<article_slug>[-\w]+)/favorite/?$', PostsFavoriteAPIView.as_view()),
    url(r'^(?P<article_slug>[-\w]+)/comments/?$', CommentsListCreateAPIView.as_view()),
    url(r'^(?P<article_slug>[-\w]+)/comments/(?P<comment_pk>[\d]+)/?$', CommentsDestroyAPIView.as_view()),
    url(r'^tags/?$', TagListAPIView.as_view()),
    url(r'^$', include(router.urls)),
]