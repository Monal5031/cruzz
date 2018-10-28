# local django
from core.renderers import VConnectJSONRenderer


class PostJSONRenderer(VConnectJSONRenderer):
    object_label = 'post'
    pagination_object_label = 'posts'
    pagination_count_label = 'postsCount'


class CommentJSONRenderer(VConnectJSONRenderer):
    object_label = 'comment'
    pagination_object_label = 'comments'
    pagination_count_label = 'commentsCount'
