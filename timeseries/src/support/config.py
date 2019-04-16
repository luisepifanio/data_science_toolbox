#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dotenv import find_dotenv, load_dotenv
from support.formatters import ISO8601Formatter
from pathlib import Path
import logging
import os


def main():
    """ Runs entry function for a program
    """
    setup_fomatter()
    logger = logging.getLogger(__name__)
    logger.info(f'main was invoked... from {__name__}')


def setup_fomatter():
    log_fmt = '''[eventdate:%(asctime)s][level:%(levelname)s][module:%(name)s] \
%(message)s'''
    # logging.basicConfig(
    #     level=logging.INFO,
    #     format=log_fmt,
    #     datefmt="%Y-%m-%dT%H:%M:%S.%f%z"
    # )

    logger = logging.getLogger(__name__)
    handler = logging.StreamHandler()
    handler.setFormatter(
        ISO8601Formatter(
            log_fmt,
            "%Y-%m-%dT%H:%M:%S.%f%z"
        )
    )
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    logger.info('logging has been set up')


if __name__ == '__main__':
    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    print("project_dir={project_dir}".format(project_dir=project_dir))

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    print(load_dotenv(find_dotenv()))

    keys = "CONFIG_PATH DOMAIN EMAIL".split()
    for key in keys:
        print(key, os.getenv(key))

    main()
