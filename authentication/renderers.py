import json

from rest_framework.renderers import JSONRenderer


class UserJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):
        # If the view throws an error (for example, the user cannot
        # be authenticated), data will contain the error key. We want,
        # for the standard JSONRenderer to handle such errors, so
        # such a case should be checked.
        errors = data.get('errors', None)

        # If we receive the token as part of the response, it will be byte
        # an object. Byte objects do not serialize well, so we need
        # decode them before rendering the User object.
        token = data.get('token', None)

        if errors is not None:
            # Let's the standard JSONRenderer handle the error.
            return super(UserJSONRenderer, self).render(data)

        if token is not None and isinstance(token, bytes):
            # Decodes a token if it is of type bytes.
            data['token'] = token.decode('utf-8')

        # We can display our data in the 'user' namespace.
        return json.dumps({
            'user': data
        })