![Deserve](./deserve-logo.svg)

# Deserve ![example workflow](https://github.com/matiasbattocchia/deserve/actions/workflows/test.yml/badge.svg) ![example workflow](https://github.com/matiasbattocchia/deserve/actions/workflows/publish.yml/badge.svg)

Deserve is a nanoframework for serving ML models. Flasker than Flask, faster than FastAPI, Deserve is asynchronous, lightweight and simple.

### Features

* 🤙 Remote procedure call (RPC) architecture. There are no endpoints, methods, paths, nor resources to make decisions about — just the `host`:`port`.
* 📦 Send JSON, receive JSON, client-side. Accept a Python object, return an object, server-side. Conversions happen under the hood.

### Installing

```sh
$ pip install deserve
```

Also install an ASGI server such as [Uvicorn](https://www.uvicorn.org) or [Hypercorn](https://pgjones.gitlab.io/hypercorn).

```sh
$ pip install hypercorn
```

### Quickstart

This example uses the [🤗 Transformers](https://huggingface.co/docs/transformers/quicktour) library.

```py
# Save this as example.py
import deserve
from transformers import pipeline

# Load your model
classifier = pipeline('sentiment-analysis')

@deserve
async def predict(payload: object) -> object:
    return classifier(payload)
```

Run the server using the names of your file (`example.py`) and function (`predict`).

```sh
$ hypercorn example:predict

[INFO] Running on http://127.0.0.1:8000
```

Get some predictions.

```sh
$ curl localhost:8000 --data '["This is the simplest framework.", "You deserve it!"]'

[{"label": "POSITIVE", "score": 0.799}, {"label": "POSITIVE", "score": 0.998}]
```

### Serialization and deserialization

Deserve takes care of converting the request and response payloads based on the **content-type** and **accept** headers of the request.

List of supported **content-types** and the deserialized payload that is passed to the inference handler.

| content-type | Payload |
| ------------ | ------- |
| application/json | `dict`/`list` |
| text/* | raw |
| image/* | binary |
| audio/* | binary |

List of supported **accept** headers and the serialized payload that is returned.

| accept | Payload |
| ------ | ------- |
| application/json | JSON |
| text/* | raw |
| image/* | binary |
| audio/* | binary |

