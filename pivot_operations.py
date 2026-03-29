""" 
pivot_operations.py

This module provides functions for performing pivot table operations 
using pandas, including creating pivot tables, cross tabulations, and 
pivoting with fill options and margin support.
"""

import pandas as pd
from pandas import DataFrame, PivotTable


def create_pivot(data: DataFrame, index: list, columns: list, values: str, aggfunc: str = 'mean', margins: bool = False) -> PivotTable:
    """
    Create a pivot table from the given DataFrame.

    Parameters:
    data (DataFrame): The input data for pivoting.
    index (list): Column(s) to use as the index for the pivot table.
    columns (list): Column(s) to use as the columns for the pivot table.
    values (str): Column to aggregate.
    aggfunc (str): The aggregation function to apply (default is 'mean').
    margins (bool): Whether to add row/column margins (default is False).

    Returns:
    PivotTable: A pivot table as a DataFrame.
    """
    return pd.pivot_table(data, index=index, columns=columns, values=values, aggfunc=aggfunc, margins=margins)


def cross_tabulation(data: DataFrame, row_var: str, col_var: str, values: str = None, aggfunc: str = 'count', margins: bool = False) -> DataFrame:
    """
    Perform a cross tabulation of two variables.

    Parameters:
    data (DataFrame): The input data for cross tabulation.
    row_var (str): The variable for rows.
    col_var (str): The variable for columns.
    values (str): Column to aggregate (optional).
    aggfunc (str): The aggregation function to apply (default is 'count').
    margins (bool): Whether to add row/column margins (default is False).

    Returns:
    DataFrame: A cross-tabulated DataFrame.
    """
    return pd.crosstab(data[row_var], data[col_var], values=data[values] if values else None, 
                       aggfunc=aggfunc, margins=margins)


def pivot_and_fill(data: DataFrame, index: list, columns: list, values: str, fill_value: any = None, aggfunc: str = 'mean', margins: bool = False) -> DataFrame:
    """
    Create a pivot table and fill missing values.

    Parameters:
    data (DataFrame): The input data for pivoting.
    index (list): Column(s) to use as the index for the pivot table.
    columns (list): Column(s) to use as the columns for the pivot table.
    values (str): Column to aggregate.
    fill_value (any): Value to fill missing data with (default is None).
    aggfunc (str): The aggregation function to apply (default is 'mean').
    margins (bool): Whether to add row/column margins (default is False).

    Returns:
    DataFrame: A pivot table with filled missing values.
    """
    pivot_table = create_pivot(data, index, columns, values, aggfunc, margins)
    return pivot_table.fillna(fill_value) if fill_value is not None else pivot_table