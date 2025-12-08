"""Data cleaning for ISM2411.

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

# This function should remove rows where price or quantity is negative.
# Copilot: write this function.
def remove_invalid_rows(df: pd.DataFrame) -> pd.DataFrame:
	"""Remove rows with invalid data.

	Args:
		df: Input DataFrame.

	Returns:
		DataFrame with invalid rows removed.
	"""
	return df[(df['price'] >= 0) & (df['quantity'] >= 0)]

def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Standardize column names."""
    df = df.copy()
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    return df

#This function should strip whitespace from string columns.
# Copilot: write this function.
def strip_whitespace_from_strings(df: pd.DataFrame) -> pd.DataFrame:
	"""Strip leading and trailing whitespace from string columns.

	Args:
		df: Input DataFrame.
	Returns:
		DataFrame with whitespace stripped from string columns.
	"""
	df = df.copy()
	str_cols = df.select_dtypes(include=['object']).columns
	for col in str_cols:
		df[col] = df[col].str.strip()
	return df	

#This function should handle missing values by filling them with the column mean for numeric columns.
# Copilot: write this function.
def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
	"""Handle missing values in the DataFrame.

	Args:
		df: Input DataFrame.

	Returns:
		DataFrame with missing values handled.
	"""
	df = df.copy()
	num_cols = df.select_dtypes(include=['number']).columns
	for col in num_cols:
		mean_value = df[col].mean()
		df[col] = df[col].fillna(mean_value)
	return df		