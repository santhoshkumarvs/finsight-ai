import argparse
from prometheus_client import start_http_server, Gauge
import time
from .drift_detector import run_drift_detection

# Prometheus gauge metric
drift_metric = Gauge('model_drift_score', 'Score indicating model drift severity')

def export_metrics_loop():
    reference_data = [...]  # Replace with real or mock reference data
    new_data = [...]        # Replace with real or mock current data
    while True:
        drift_score = run_drift_detection(reference_data, new_data)
        print(f"model_drift_score {drift_score}")
        drift_metric.set(drift_score)
        time.sleep(15)  # Refresh every 15 seconds

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--return-only-score", action="store_true", help="Output only the drift score for CI/CD")

    args = parser.parse_args()

    # Mock data (replace with real in prod)
    reference_data = [[0.1], [0.2], [0.3]]
    new_data = [[0.15], [0.25], [0.35]]

    drift_score = run_drift_detection(reference_data, new_data)

    if args.return_only_score:
        print(drift_score)
    else:
        print("Prometheus metrics available at http://localhost:8000")
        start_http_server(8000)
        drift_metric.set(drift_score)
        while True:
            drift_score = run_drift_detection(reference_data, new_data)
            print(f"model_drift_score {drift_score}")
            drift_metric.set(drift_score)
            time.sleep(15)
