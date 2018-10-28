# local django
from core.renderers import VConnectJSONRenderer


class ProfileJSONRenderer(VConnectJSONRenderer):
    object_label = 'profile'
    pagination_object_label = 'profiles'
    pagination_count_label = 'profilesCount'
