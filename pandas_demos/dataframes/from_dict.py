import copy
import logging
import typing

import pandas


module_log = logging.getLogger(__name__)


def dataframe_from_dict(data: dict) -> pandas.DataFrame:
    module_log.debug("Creating new pandas.DataFrame instance")
    example_df: pandas.DataFrame = pandas.DataFrame(data)
    module_log.debug(f"Created pandas.DataFrame with shape: {example_df.shape} | (rows, cols)")
    return example_df


def dataframe_from_union_of_dicts(*args) -> pandas.DataFrame:
    unioned_dict = {}
    module_log.debug(f"Unioning {len(args)} dict Objects")
    for param in args:
        unioned_dict.update(param)
    example_df: pandas.DataFrame = dataframe_from_dict(unioned_dict)
    return example_df


def dataframe_from_extension_of_dicts(*args) -> pandas.DataFrame:
    extended_dict: typing.Optional[dict] = None
    module_log.debug(f"Unioning {len(args)} dict Objects")
    for param in args:
        if extended_dict is None:
            extended_dict = copy.deepcopy(param)
        else:
            for key in param:
                extended_dict[key].extend(param[key])
    example_df: pandas.DataFrame = pandas.DataFrame(extended_dict)
    return example_df


def dataframe_from_multiple_dicts(*args) -> pandas.DataFrame:
    indexed_dict: dict = {}
    module_log.debug(f"Unioning {len(args)} dict Objects")
    for index, param in enumerate(args):
        indexed_dict[index] = param
    example_df: pandas.DataFrame = pandas.DataFrame.from_dict(
        data=indexed_dict,
        orient="index",
    )
    return example_df
