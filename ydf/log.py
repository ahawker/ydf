"""
    ydf/log
    ~~~~~~~

    Package logger.
"""

import logging


__all__ = ['get_logger']


ROOT_LOGGER = None


def get_logger(name=None):
    global ROOT_LOGGER

    if ROOT_LOGGER is None:
        ROOT_LOGGER = logging.getLogger()

    return ROOT_LOGGER.getChild(name)
