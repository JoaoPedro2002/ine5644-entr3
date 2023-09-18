import pandas as pd
import missingno as msno


def common_graphics(df: pd.DataFrame):
    df.hist()


def missing_values(df: pd.DataFrame):
    msno.matrix(df)
