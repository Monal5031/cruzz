# local django
from core.renderers import VConnectJSONRenderer


class ProfileJSONRenderer(VConnectJSONRenderer):
    object_label = 'profile'
    object_label_plural = 'profiles'
    pagination_object_label = 'profiles'
    pagination_count_label = 'profilesCount'
