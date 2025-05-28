# Buffer and prepare spilled data for training
import os
import pandas as pd
from typing import List

SPILL_DATA_DIR = "data/spill_data/"

def load_spill_data() -> List[pd.DataFrame]:
    """Load all spill data files from the directory."""
    dataframes = []
    for file in os.listdir(SPILL_DATA_DIR):
        if file.endswith(".csv"):
            path = os.path.join(SPILL_DATA_DIR, file)
            df = pd.read_csv(path)
            dataframes.append(df)
    return dataframes

def chunk_dataframe(df: pd.DataFrame, chunk_size: int = 1000) -> List[pd.DataFrame]:
    """Split large DataFrame into chunks."""
    return [df[i:i+chunk_size] for i in range(0, df.shape[0], chunk_size)]

def buffer_chunks() -> List[pd.DataFrame]:
    """Full pipeline: load, concat, and chunk all spill data."""
    dfs = load_spill_data()
    combined = pd.concat(dfs, ignore_index=True)
    return chunk_dataframe(combined)
