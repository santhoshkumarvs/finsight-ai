# Entrypoint for running the service
from fastapi import FastAPI, UploadFile, File
import pandas as pd
from io import StringIO
from monitoring.drift_detector import run_drift_detection

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Welcome to FinSight AI Copilot 🚀"}


@app.post("/detect-drift/")
async def detect_drift(
    reference: UploadFile = File(...), current: UploadFile = File(...)
):
    ref_df = pd.read_csv(StringIO((await reference.read()).decode()))
    curr_df = pd.read_csv(StringIO((await current.read()).decode()))

    result = run_drift_detection(ref_df, curr_df)
    return {"result": result}
