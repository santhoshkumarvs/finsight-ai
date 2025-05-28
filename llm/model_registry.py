# Register and retrieve model metadata
import json
import os
from datetime import datetime

REGISTRY_PATH = "llm/model_registry.json"

def load_registry():
    if os.path.exists(REGISTRY_PATH):
        with open(REGISTRY_PATH, "r") as f:
            return json.load(f)
    return []

def save_model_metadata(model_path: str, accuracy: float):
    registry = load_registry()
    new_record = {
        "model_path": model_path,
        "accuracy": accuracy,
        "timestamp": datetime.utcnow().isoformat()
    }
    registry.append(new_record)
    with open(REGISTRY_PATH, "w") as f:
        json.dump(registry, f, indent=4)
    print(f"[model_registry] Model saved: {new_record}")
