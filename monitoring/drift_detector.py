import pandas as pd
from scipy.stats import ks_2samp, chi2_contingency
from typing import Tuple
import os
from prometheus_client import Gauge

def is_categorical(series: pd.Series) -> bool:
    return pd.api.types.is_categorical_dtype(series) or pd.api.types.is_object_dtype(series)

def run_drift_detection(reference: pd.DataFrame, current: pd.DataFrame, threshold: float = 0.05) -> Tuple[dict, str]:
    drift_results = {}
    report_lines = ["<h1>FinSight AI - Data Drift Report</h1>"]

    common_columns = set(reference.columns).intersection(set(current.columns))

    for column in common_columns:
        if is_categorical(reference[column]):
            contingency_table = pd.crosstab(reference[column], current[column])
            stat, p_value, _, _ = chi2_contingency(contingency_table, correction=False)
            test_used = "Chi-Square"
        else:
            stat, p_value = ks_2samp(reference[column].dropna(), current[column].dropna())
            test_used = "Kolmogorov–Smirnov"

        drift_detected = p_value < threshold
        drift_results[column] = {
            "test": test_used,
            "p_value": round(p_value, 5),
            "drift": drift_detected
        }

        color = "red" if drift_detected else "green"
        report_lines.append(
            f"<p><b>{column}</b> ({test_used}): "
            f"<span style='color:{color}'>Drift Detected: {drift_detected} (p={round(p_value,5)})</span></p>"
        )

    report_html = "\n".join(report_lines)
    report_path = "drift_report.html"
    with open(report_path, "w") as f:
        f.write(report_html)

    print(f"✅ Drift detection complete. Report saved to: {os.path.abspath(report_path)}")
    return drift_results, report_path


drift_metric = Gauge("drift_score", "Model Drift Score")
drift_metric.set(drift_score)  # Set this after computing
