# standard libs
import json

# django
from rest_framework.renderers import JSONRenderer


class VConnectJSONRenderer(JSONRenderer):
    charset = 'utf-8'
    object_label = 'object'

    def render(self, data, media_type=None, renderer_content=None):
        # If the view throws an error (such as the user can't be authenticated)
        # `data` will contain an `errors` key. We want
        # the default JSONRenderer to handle rendering errors, so we need to
        # check for this case.
        errors = data.get('errors', None)

        if errors is not None:
            # As mentioned above, we will let the default JSONRenderer handle
            # rendering errors.
            return super(VConnectJSONRenderer, self).render(data)

        return json.dumps({
            self.object_label: data
        })
