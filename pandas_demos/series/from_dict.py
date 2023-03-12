import logging

import pandas


module_log = logging.getLogger(__name__)


def series_from_dict(column_key: object, data: dict) -> pandas.Series:
    module_log.debug("Creating new pandas.Series instance")
    example_sr: pandas.Series = pandas.Series(
        data[column_key]
    )
    module_log.debug(f"Created pandas.Series with shape: {example_sr.shape} | (rows, cols)")
    return example_sr


def series_from_union_of_dicts(*args, column_key: object = None) -> pandas.DataFrame:
    unioned_dict = {}
    module_log.debug(f"Unioning {len(args)} dict Objects")
    for param in args:
        unioned_dict.update(param)
    example_sr: pandas.Series = series_from_dict(
        column_key=column_key,
        data={
            column_key: unioned_dict[column_key],
        },
    )
    return example_sr
