"""Deserve is a nanoframework for serving ML models"""

__version__ = '0.2'

import json
import sys

async def desend(send, body, content, status=200):

    await send({
        'type': 'http.response.start',
        'status': status,
        'headers': [
            (b'content-type', content),
            (b'content-length', str(len(body)).encode()),
        ],
    })

    await send({
        'type': 'http.response.body',
        'body': body,
    })

def deserve(app):

    async def wrapper(scope, receive, send):
        # if scope['type'] != 'http':
        #     return
        #

        headers = dict(scope['headers'])
        content = headers.get(b'content-type', b'')
        accept  = headers.get(b'accept', b'')

        event = await receive()

        # if event['type'] != 'http.request':
        #     return

        if b'text/' in content:
            request = event['body'].decode()
        elif b'image/' in content or b'audio/' in content:
            request = event['body']
        else:
            try:
                request = json.loads(event['body'])
            except json.JSONDecodeError as e:
                if content == b'application/json':
                    return await desend(
                        send,
                        json.dumps({ 'error': f'JSON decode error. {e}' }).encode(),
                        content,
                        status=400
                    )

                request = event['body']

        response = await app(request)

        if b'text/' in accept:
            await desend(send, response.encode(), content=accept)
        elif b'image/' in accept or b'audio/' in accept:
            await desend(send, response, content=accept)
        else:
            if accept == b'application/json' or type(response) not in [bytes, bytearray]:
                await desend(send, json.dumps(response).encode(), content=accept)
            else:
                await desend(send, response, content=b'application/octet-stream')

    return wrapper

sys.modules[__name__] = deserve
