from prometheus_client import Gauge, start_http_server
from drift_detector import run_drift_detection
import numpy as np
import time

# Define the Prometheus metric
drift_metric = Gauge('model_drift_score', 'Drift score from Alibi Detect')

def load_reference_data():
    # Dummy reference data (replace with actual loading logic)
    return np.random.rand(100, 5)

def load_new_data():
    # Dummy new data (replace with live batch or sample logic)
    return np.random.rand(100, 5)

def export_metrics_loop():
    # Start Prometheus metrics HTTP server on port 8000
    start_http_server(8000)
    print("Prometheus metrics available at http://localhost:8000")

    reference_data = load_reference_data()

    while True:
        new_data = load_new_data()
        drift_score = run_drift_detection(reference_data, new_data)
        print(f"Drift score: {drift_score:.4f}")
        drift_metric.set(drift_score)
        time.sleep(60)  # wait 1 minute before next check

if __name__ == "__main__":
    export_metrics_loop()
