"""Utility functions."""

import logging

logger = logging.getLogger(__name__)


def setup_logging(level: str = "INFO"):
    """Configure logging."""
    logging.basicConfig(level=getattr(logging, level.upper()))


def format_timestamp() -> str:
    """Return current timestamp."""
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
