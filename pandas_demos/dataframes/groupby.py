import logging

import pandas

PandasGroupBy = pandas.core.groupby.DataFrameGroupBy


module_log = logging.getLogger(__name__)


def groupby_dataframe_from_columnname(data_df: pandas.DataFrame, column: str) -> PandasGroupBy:
    module_log.debug("Creating new pandas.core.groupby.DataFrameGroupBy instance")
    example_gb: PandasGroupBy = data_df.groupby(column)
    return example_gb


def groupby_to_dataframe(data_gb: PandasGroupBy) -> pandas.DataFrame:
    module_log.debug("Creating new pandas.DataFrame instance")
    example_df: pandas.DataFrame = pandas.concat(
        [data_gb.get_group(key) for key in data_gb.groups],
    )
    return example_df
