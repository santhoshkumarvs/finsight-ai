from alibi_detect.cd import MMDDrift
import numpy as np

def run_drift_detection(reference_data, new_data):
    detector = MMDDrift(p_val=0.05, backend='pytorch')  # or 'tensorflow'
    detector.fit(reference_data)
    prediction = detector.predict(new_data)
    drift_score = prediction['data']['p_val']
    return drift_score

