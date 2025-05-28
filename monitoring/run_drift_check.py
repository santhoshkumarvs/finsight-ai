import os
import numpy as np
from monitoring.drift_detector import run_drift_detection

# Simulated data – replace with actual file reads or pipeline pulls
reference_data = np.random.normal(0, 1, size=(1000,))
new_data = np.random.normal(0.5, 1, size=(1000,))  # Simulate drift

drift_score = run_drift_detection(reference_data, new_data)

# Set threshold
if drift_score < 0.05:
    print("Drift detected")
    with open(os.environ['GITHUB_ENV'], 'a') as env_file:
        env_file.write('DRIFT_DETECTED=true\n')
else:
    print("No significant drift")
    with open(os.environ['GITHUB_ENV'], 'a') as env_file:
        env_file.write('DRIFT_DETECTED=false\n')
