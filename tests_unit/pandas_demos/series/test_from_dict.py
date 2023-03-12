import logging

import pytest

from pandas_demos.data.hecate import (
    hecate_info,
)
from pandas_demos.series.from_dict import (
    series_from_dict,
    series_from_union_of_dicts,
)


module_log = logging.getLogger(__name__)


def test_series_from_dict() -> None:
    _ = series_from_dict(
        column_key="name",
        data=hecate_info,
    )
    return None


def test_series_from_union_of_dicts() -> None:
    _ = series_from_union_of_dicts(
        hecate_info,
        hecate_info,
        hecate_info,
        column_key="name",
    )
    return None
