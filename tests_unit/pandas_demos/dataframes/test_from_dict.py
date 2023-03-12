import logging

import pytest

from pandas_demos.data.hecate import (
    hecate_info,
)
from pandas_demos.dataframes.from_dict import (
    dataframe_from_dict,
    dataframe_from_union_of_dicts,
    dataframe_from_multiple_dicts,
)


module_log = logging.getLogger(__name__)


def test_dataframe_from_dict() -> None:
    _ = dataframe_from_dict(hecate_info)
    return None


def test_dataframe_from_union_of_dicts() -> None:
    return None


def test_dataframe_from_multiple_dicts() -> None:
    _ = dataframe_from_multiple_dicts(
        hecate_info,
        hecate_info,
        hecate_info,
        hecate_info,
    )
    return None
