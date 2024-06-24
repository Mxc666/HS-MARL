"""Logging helpers."""
import logging
import os
import sys
try:
    import colorlog
except ImportError:
    pass

LOGGER = logging.getLogger('pddl')


def setup_logging(level=logging.DEBUG):
    """Setup the logging infrastructure.

    :param level: the logging level
    """
    LOGGER.setLevel(level)
    log_format = '%(asctime)s - %(levelname)-8s - %(name)s - %(message)s'
    date_format = '%Y-%m-%d %H:%M:%S'
    if 'colorlog' in sys.modules and os.isatty(2):
        cformat = '%(log_color)s' + log_format
        formatter = colorlog.ColoredFormatter(cformat, date_format,
              log_colors = {'DEBUG': 'thin_yellow',
                            'INFO': 'reset',
                            'WARNING': 'bold_yellow',
                            'ERROR': 'bold_red',
                            'CRITICAL': 'bold_red'
                            })
    else:
        formatter = logging.Formatter(log_format, date_format)
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    LOGGER.addHandler(handler)
