# Deserve

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

```py
# Save this as example.py
import deserve

model = ... # Load your model

@deserve
async def predict(request: object) -> object:
  ... # Preprocess input
  output = model.predict(input)
  ... # Postprocess output
  return response
```

Run the server using the names of your file (`example.py`) and function (`predict`).

```sh
$ hypercorn example:predict

[INFO] Running on http://127.0.0.1:8000
```
