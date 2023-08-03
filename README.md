# Deserve

Deserve is a nanoframework for serving ML models. Flasker than Flask, faster than FastAPI, Deserve is asynchronous, lightweight and simple.

### Quickstart

In a file `server.py`

```py
import deserve

model = ... # Load your model

@deserve
async def predict(request: object) -> object:
  ... # Preprocess input
  output = model.predict(input)
  ... # Postprocess output
  return response
```

With an ASGI web server of your choice

```sh
$ hypercorn server:predict
```

Done

```sh
curl localhost:8000
```

### Design

* Remote procedure call (RPC) architecture
* JSON in, JSON out
