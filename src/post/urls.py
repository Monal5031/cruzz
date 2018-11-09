from django.conf.urls import url


from post.views import (PostsFavoriteAPIView, CommentCreateAPIView,
                        CommentListAPIView, CommentSingleAPIView,
                        CommentUpdateAPIView, CommentsDestroyAPIView, TagListAPIView,
                        PostsFeedAPIView, PostCreateView, PostsUpvoteAPIView, PostsDownvoteAPIView,
                        PostDisplayView, PostSingleView, PostUpdateView, PostDestroyAPIView)


urlpatterns = [
    url(r'^feed/?$', PostsFeedAPIView.as_view()),
    url(r'^(?P<post_slug>[-\w]+)/favorite/?$', PostsFavoriteAPIView.as_view()),
    url(r'^(?P<post_slug>[-\w]+)/upvote/?$', PostsUpvoteAPIView.as_view()),
    url(r'^(?P<post_slug>[-\w]+)/downvote/?$', PostsDownvoteAPIView.as_view()),
    url(r'^(?P<post_slug>[-\w]+)/comments/create/?$', CommentCreateAPIView.as_view()),
    url(r'^(?P<post_slug>[-\w]+)/comments/view/?$', CommentListAPIView.as_view()),
    url(r'^(?P<post_slug>[-\w]+)/comments/view/(?P<comment_pk>[\d]+)?$', CommentSingleAPIView.as_view()),
    url(r'^(?P<post_slug>[-\w]+)/comments/update/(?P<comment_pk>[\d]+)/?$', CommentUpdateAPIView.as_view()),
    url(r'^(?P<post_slug>[-\w]+)/comments/delete/(?P<comment_pk>[\d]+)/?$', CommentsDestroyAPIView.as_view()),
    url(r'^tags/?$', TagListAPIView.as_view()),
    url(r'^create/$', PostCreateView.as_view()),
    url(r'^view/?$', PostDisplayView.as_view()),
    url(r'^view/(?P<post_slug>[-\w]+)/?$', PostSingleView.as_view()),
    url(r'^update/(?P<post_slug>[-\w]+)/?$', PostUpdateView.as_view()),
    url(r'^(?P<post_slug>[-\w]+)/delete/?$', PostDestroyAPIView.as_view()),
]
