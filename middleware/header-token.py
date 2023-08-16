import re
from uuid import UUID
from flask import request, abort

uuid_regex = re.compile('[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}', re.IGNORECASE)

def api_token_required(func):
    def wrapper(*args, **kwargs):
        token = request.headers.get('x-api-token')
        if not token:
            abort(401, 'Missing x-api-token header')
        if not uuid_regex.match(token):
            abort(401, 'Invalid x-api-token header')
        return func(*args, **kwargs)
    return wrapper