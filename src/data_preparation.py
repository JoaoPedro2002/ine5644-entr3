from typing import Any

import pandas as pd


def map_column(df: pd.DataFrame, column: str, new_values: dict[Any, Any], new_type: type):
    df[column] = df[column].map(new_values).fillna(-1).astype(new_type)


def binarize_column(df: pd.DataFrame, columns: list[str]) -> dict[str, dict]:
    columns_map = {}
    for column in columns:
        df[column] = df[column].astype("category")
        columns_map[column] = {category: index for index, category in enumerate(df[column].cat.categories)}
        df[column] = df[column].cat.codes
    return columns_map


def merge_dataframes(df1: pd.DataFrame, df2: pd.DataFrame, on: str) -> pd.DataFrame:
    return pd.merge(df1, df2, on=on)
