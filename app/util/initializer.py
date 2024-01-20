"""
Initializer Module
==================

This module contains functions for initializing the project, including
logger configuration and other setup tasks.

Functions
---------
initialize_project : function
    Initialize the project.

Classes
-------
MyClass : SomeClass
    A class for handling special cases in project initialization.
"""

# Standard library imports
import json
import logging.config
import sys

# Local application/library specific imports
from app.datatool.env_util import get_settings

__author__ = "Praveen Kumar G"

LOGGER = logging.getLogger(__name__)


def configure_logging(filepath):
    """
    Configure logging based on the provided JSON configuration file.

    Parameters
    ----------
    filepath : str
        The path to the JSON configuration file.

    Raises
    ------
    FileNotFoundError
        If the specified configuration file is not found.

    Example
    -------
    configure_logging('logging_config.json')
    """

    try:
        with open(filepath, 'r') as file_object:
            config_data = json.load(file_object)
    except FileNotFoundError as err:
        LOGGER.error("Error while configuring logger, the following give full error message")
        LOGGER.error(err)
        LOGGER.error("Exiting the program")
        sys.exit(1)

    logging.config.dictConfig(config_data)

    LOGGER.info("Configured Logging")


def initialize_app():
    """
    Initialize the Application.

    Returns
    -------
    None
        Nothing.
    """

    environment_settings = get_settings()

    configure_logging(environment_settings.logger_configuration_file)
