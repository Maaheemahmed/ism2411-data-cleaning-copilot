"""Data cleaning pipeline starter for ISM2411.

This file is a minimal skeleton you can build from. Add functions such as
`clean_column_names`, `strip_whitespace_from_strings`, `handle_missing_values`,
and `remove_invalid_rows` below as you implement and commit them incrementally.
"""

from __future__ import annotations

import pandas as pd


def load_data(file_path: str) -> pd.DataFrame:
	"""Load CSV at ``file_path`` into a pandas DataFrame.

	Args:
		file_path: Path to the CSV file relative to the project root.

	Returns:
		A pandas DataFrame with the loaded data.
	"""
	return pd.read_csv(file_path)


if __name__ == "__main__":
	raw_path = "data/raw/sales_data_raw.csv"
	df = load_data(raw_path)
	print(f"Loaded rows: {len(df)} from {raw_path}")
	print(df.head())

