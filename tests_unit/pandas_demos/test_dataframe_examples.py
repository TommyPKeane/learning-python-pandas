import logging

import pandas

from pandas_demos.dataframe_examples import hecate_info, hecate_names


module_logs = logging.getLogger(__name__)


def test_dataframe_factory_dict():
    module_logs.info("Creating Example DataFrame")
    example_df = pandas.DataFrame(hecate_info)
    assert example_df is not None
