"""
Environment Variable Utility
===========================

This module provides utilities for retrieving and validating environment variables using Pydantic.

Functions
---------
get_settings: Retrieve an environment variables with optional default value.


classes
-------
Setting : BaseSettings
    A class for handling environment variable.
"""

# Standard library imports
import logging
from functools import lru_cache

# Related third party imports
from pydantic_settings import BaseSettings


__author__ = "Praveen Kumar G"

LOGGER = logging.getLogger(__name__)


class Setting(BaseSettings):
    """Data model for configuration settings."""

    # Default Logging configuration file path
    logger_configuration_file: str

    class Config:
        env_file = "./config/.env"


@lru_cache()
def get_settings():
    """
    Return the configuration settings read from the os environment, using pydantic's base settings class

    Returns
    -------
    Settings
        The configuration settings read from the os
    """

    LOGGER.debug("New Request for environment variable")
    return Setting()
