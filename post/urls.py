from django.conf.urls import url


from post.views import (PostsFavoriteAPIView, CommentsListCreateAPIView,
                        CommentsDestroyAPIView, TagListAPIView,
                        PostsFeedAPIView, PostCreateView,
                        PostDisplayView, PostSingleView, PostUpdateView)


urlpatterns = [
    url(r'^feed/?$', PostsFeedAPIView.as_view()),
    url(r'^(?P<post_slug>[-\w]+)/favorite/?$', PostsFavoriteAPIView.as_view()),
    url(r'^(?P<post_slug>[-\w]+)/comments/?$', CommentsListCreateAPIView.as_view()),
    url(r'^(?P<post_slug>[-\w]+)/comments/(?P<comment_pk>[\d]+)/?$', CommentsDestroyAPIView.as_view()),
    url(r'^tags/?$', TagListAPIView.as_view()),
    url(r'^create/$', PostCreateView.as_view()),
    url(r'^view/?$', PostDisplayView.as_view()),
    url(r'^view/(?P<post_slug>[-\w]+)/?$', PostSingleView.as_view()),
    url(r'^update/(?P<post_slug>[-\w]+)/?$', PostUpdateView.as_view())
]
