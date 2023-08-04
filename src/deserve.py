"""Deserve is a nanoframework for serving ML models"""

__version__ = '0.1'

import json
import sys

async def desend(send, response, status=200):
    payload = json.dumps(response).encode()

    await send({
        'type': 'http.response.start',
        'status': status,
        'headers': [
            (b'content-type', b'application/json'),
            (b'content-length', str(len(payload)).encode()),
        ],
    })

    await send({
        'type': 'http.response.body',
        'body': payload,
    })

def deserve(app):

    async def wrapper(scope, receive, send):
        # if scope['type'] != 'http':
        #     return
        #
        # if (b'content-type', b'application/json') not in scope['headers']:
        #     return

        event = await receive()

        # if event['type'] != 'http.request':
        #     return

        try:
            request = json.loads(event['body']) if event['body'] else None

        except json.JSONDecodeError as e:
            response = { 'error': f'JSON decode error. {e}' }
            return await desend(send, response, 400)

        response = await app(request)

        await desend(send, response)

    return wrapper

sys.modules[__name__] = deserve
