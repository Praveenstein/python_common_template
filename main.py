"""
Main Module for Your Application
===============================

This module serves as the starting point for your application. It contains the main function that is
called when your application is executed.

Usage
-----
Run this script to start your application:

    $ python main.py

Ensure that your configuration is set up correctly, and environment variables are configured as needed.

"""

# Standard library imports
import json
import logging

# Local application/library specific imports
from app.util.initializer import initialize_app

__author__ = "Praveen Kumar G"

LOGGER = logging.getLogger(__name__)


def main():
    """
    Main function for Your Application

    This function serves as the entry point for your application. It is called when the script is executed.


    Returns
    -------
    None


    """
    try:
        initialize_app()
    except Exception as e:
        LOGGER.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
