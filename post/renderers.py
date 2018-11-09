# local django
from core.renderers import VConnectJSONRenderer


class PostJSONRenderer(VConnectJSONRenderer):
    object_label = 'post'
    object_label_plural = 'posts'
    pagination_object_label = 'posts'
    pagination_count_label = 'postsCount'


class CommentJSONRenderer(VConnectJSONRenderer):
    object_label = 'comment'
    object_label_plural = 'comments'
    pagination_object_label = 'comments'
    pagination_count_label = 'commentsCount'
