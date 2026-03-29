"""
window_functions.py

This module provides functions to perform various window operations on pandas DataFrames.
The functions include rolling statistics, expanding mean, and exponentially weighted moving average (EWMA) smoothing.
"""

import pandas as pd
from typing import Optional, Union

def rolling_statistics(data: pd.Series, window: int, min_periods: Optional[int] = None) -> pd.Series:
    """
    Calculate rolling statistics for a given pandas Series.

    Parameters:
    - data (pd.Series): The input data for which to calculate rolling statistics.
    - window (int): The size of the moving window.
    - min_periods (Optional[int]): Minimum number of observations in the window required to have a value.

    Returns:
    - pd.Series: A Series containing the rolling statistics.
    """
    if min_periods is None:
        min_periods = window
    return data.rolling(window=window, min_periods=min_periods).mean()


def expanding_mean(data: pd.Series, min_periods: Optional[int] = None) -> pd.Series:
    """
    Calculate the expanding mean for a given pandas Series.

    Parameters:
    - data (pd.Series): The input data for which to calculate the expanding mean.
    - min_periods (Optional[int]): Minimum number of observations in the window required to have a value.

    Returns:
    - pd.Series: A Series containing the expanding mean.
    """
    if min_periods is None:
        min_periods = 1
    return data.expanding(min_periods=min_periods).mean()


def ewm_smoothing(data: pd.Series, span: int, min_periods: Optional[int] = None) -> pd.Series:
    """
    Calculate exponentially weighted moving average (EWMA) for a given pandas Series.

    Parameters:
    - data (pd.Series): The input data for which to calculate EWMA.
    - span (int): The span for the EWMA calculation.
    - min_periods (Optional[int]): Minimum number of observations in the window required to have a value.

    Returns:
    - pd.Series: A Series containing the EWMA smoothed data.
    """
    if min_periods is None:
        min_periods = 1
    return data.ewm(span=span, min_periods=min_periods).mean()


def apply_window_functions(df: pd.DataFrame, 
                           rolling_window: int, 
                           ewm_span: int, 
                           min_periods: Optional[int] = None) -> pd.DataFrame:
    """
    Apply rolling statistics, expanding mean, and EWMA smoothing to a DataFrame.

    Parameters:
    - df (pd.DataFrame): The input DataFrame containing numerical columns.
    - rolling_window (int): The size of the rolling window for statistics.
    - ewm_span (int): The span for the EWMA calculation.
    - min_periods (Optional[int]): Minimum number of observations in the window required to have a value.

    Returns:
    - pd.DataFrame: A DataFrame with new columns for each window function applied.
    """
    result_df = df.copy()
    for column in df.select_dtypes(include='number').columns:
        result_df[f'{column}_rolling_mean'] = rolling_statistics(df[column], rolling_window, min_periods)
        result_df[f'{column}_expanding_mean'] = expanding_mean(df[column], min_periods)
        result_df[f'{column}_ewm_mean'] = ewm_smoothing(df[column], ewm_span, min_periods)
    
    return result_df