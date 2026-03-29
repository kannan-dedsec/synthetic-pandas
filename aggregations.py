"""
aggregations.py

This module provides various aggregation functions for pandas DataFrames.
Functions include summary statistics, grouped aggregations, and custom
aggregations using named aggregation syntax.
"""

import pandas as pd
from typing import Dict, Any, Optional, List


def summaryStats(df: pd.DataFrame, numericCols: Optional[List[str]] = None) -> pd.DataFrame:
    """
    Calculate summary statistics for the specified numeric columns in a DataFrame.

    Args:
        df (pd.DataFrame): The input DataFrame.
        numericCols (Optional[List[str]]): List of numeric column names to summarize.
            If None, all numeric columns will be used.

    Returns:
        pd.DataFrame: A DataFrame containing summary statistics.
    """
    if numericCols is None:
        numericCols = df.select_dtypes(include='number').columns.tolist()
    
    return df[numericCols].describe()


def groupedAgg(df: pd.DataFrame, groupBy: List[str], aggFuncs: Dict[str, Any]) -> pd.DataFrame:
    """
    Perform grouped aggregation on a DataFrame.

    Args:
        df (pd.DataFrame): The input DataFrame.
        groupBy (List[str]): List of column names to group by.
        aggFuncs (Dict[str, Any]): Dictionary specifying aggregation functions.

    Returns:
        pd.DataFrame: A DataFrame containing the aggregated results.
    """
    return df.groupby(groupBy).agg(aggFuncs).reset_index()


def custom_agg(df: pd.DataFrame, group_by: List[str], **agg_kwargs: Dict[str, Any]) -> pd.DataFrame:
    """
    Perform custom aggregation on a DataFrame using named aggregation syntax.

    Args:
        df (pd.DataFrame): The input DataFrame.
        group_by (List[str]): List of column names to group by.
        **agg_kwargs (Dict[str, Any]): Named aggregation functions.

    Returns:
        pd.DataFrame: A DataFrame containing the aggregated results.
    """
    return df.groupby(group_by).agg(**agg_kwargs).reset_index()