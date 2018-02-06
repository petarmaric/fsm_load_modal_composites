import logging
from timeit import default_timer as timer

from dynamic_pytables_where_condition import read_from_table
import tables as tb
import yaml


__version__ = '1.0.0'


def load_modal_composites(results_file, **filters):
    logging.info("Loading modal composites from '%s'...", results_file)
    start = timer()
    with tb.open_file(results_file) as fp:
        table = fp.root.parameter_sweep.modal_composites
        modal_composites = read_from_table(table, **filters)

        column_units = yaml.load(table.attrs.column_units_as_yaml)
        column_descriptions = yaml.load(table.attrs.column_descriptions_as_yaml)

        logging.info("Loading completed in %f second(s)", timer() - start)
        return modal_composites, column_units, column_descriptions
