from alibi_detect.cd import KSDrift
import numpy as np

def run_drift_detection(reference_data, new_data):
    detector = KSDrift(x_ref=reference_data, p_val=0.05)
    prediction = detector.predict(new_data)
    drift_score = prediction['data']['p_val'].mean()
    return drift_score

