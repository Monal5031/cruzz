# local django
from core.renderers import VConnectJSONRenderer


class ProfileJSONRenderer(VConnectJSONRenderer):
    object_label = 'profile'
