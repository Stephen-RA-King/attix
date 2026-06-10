#!/usr/bin/env python3
"""Top-level package for attix."""

# Core Library modules
import logging.config
from importlib.metadata import version

# Third party modules
import yaml  # type: ignore

__version__ = version("attix")

LOGGING_CONFIG = """
version: 1
disable_existing_loggers: False
handlers:
  console:
    class: logging.StreamHandler
    level: DEBUG
    stream: ext://sys.stdout
    formatter: basic
  file:
    class: logging.handlers.RotatingFileHandler
    level: DEBUG
    filename: logs/log.txt
    maxBytes: 1048576    # 1MB
    backupCount: 3       # keeps log.txt, log.txt.1, log.txt.2, log.txt.3
    formatter: timestamp
    encoding: utf-8

formatters:
  basic:
    style: "{"
    format: "{message:s}"
  timestamp:
    style: "{"
    format: "{asctime} - {levelname} - {filename}:{lineno} - {message}"

loggers:
  init:
    handlers: [console, file]
    level: DEBUG
    propagate: False
"""

logging.config.dictConfig(yaml.safe_load(LOGGING_CONFIG))
logger = logging.getLogger("init")
