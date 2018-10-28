# standard libs
import json

# django
from rest_framework.renderers import JSONRenderer


class VConnectJSONRenderer(JSONRenderer):
    charset = 'utf-8'
    object_label = 'object'
    pagination_object_label = 'objects'
    pagination_count_label = 'count'

    def render(self, data, media_type=None, renderer_content=None):
        if data.get('results', None) is not None:
            return json.dumps({
                self.pagination_count_label: data['count'],
                self.pagination_object_label: data['results']
            })
        elif data.get('errors', None) is not None:
            return super(VConnectJSONRenderer, self).render(data)
        else:
            return json.dumps({
                self.object_label: data
            })
