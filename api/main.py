# FastAPI server with endpoints
from fastapi import FastAPI
from llm.trainer import run_fine_tuning
from monitoring.drift_detector import run_drift_detection
from llm.model_registry import load_registry

app = FastAPI(title="FinSight Copilot API")

@app.get("/")
def root():
    return {"message": "Welcome to FinSight AI Copilot 🚀"}

@app.post("/tune")
def fine_tune():
    run_fine_tuning()
    return {"status": "Fine-tuning completed."}

@app.get("/registry")
def get_model_versions():
    registry = load_registry()
    return {"models": registry}

@app.post("/drift-check")
def check_drift():
    run_drift_detection()
    return {"status": "Drift report generated."}

from prometheus_fastapi_instrumentator import Instrumentator

instrumentator = Instrumentator().instrument(app).expose(app)
