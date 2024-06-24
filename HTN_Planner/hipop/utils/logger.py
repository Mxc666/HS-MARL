import logging
import os
import sys
try:
    import colorlog
except ImportError:
    pass

def setup_logging(level=logging.DEBUG, without=[]):
    root = logging.getLogger()
    root.setLevel(level)
    format      = '%(asctime)s - %(levelname)-8s - %(name)s - %(message)s'
    date_format = '%Y-%m-%d %H:%M:%S'
    if 'colorlog' in sys.modules and os.isatty(2):
        cformat = '%(log_color)s' + format
        f = colorlog.ColoredFormatter(cformat, date_format,
              log_colors = { 'DEBUG'   : 'thin_yellow',       'INFO' : 'reset',
                             'WARNING' : 'bold_yellow', 'ERROR': 'bold_red',
                             'CRITICAL': 'bold_red' })
    else:
        f = logging.Formatter(format, date_format)
    ch = logging.StreamHandler()
    ch.setFormatter(f)
    root.addHandler(ch)
    for logger in without:
        logging.getLogger(logger).setLevel(level+10)