import logging
import os
import sys


def create_logger(log_file_name):
    """Setup the logging environment"""
    log = logging.getLogger()
    log.setLevel(logging.DEBUG)
    sh_formatter = logging.Formatter("[%(levelname)s] %(name)s - %(message)s")
    fh_formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s - %(message)s", "%Y-%m-%d %H:%M:%S")
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(sh_formatter)
    file_handler = logging.FileHandler(filename=os.path.join(os.path.dirname(__file__), log_file_name+".log"))
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(fh_formatter)
    log.addHandler(stream_handler)
    log.addHandler(file_handler)