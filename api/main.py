from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

# your routes here...

Instrumentator().instrument(app).expose(app)
