import logging
from logging.handlers import RotatingFileHandler


def setup_logging(debug: bool = False) -> None:
    """
    Configure application logging with multiple handlers and rotation.

    Args:
        debug (bool): Enable DEBUG logs in console if True, else INFO only.
    """

    # Master logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)  # Always keep lowest here

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    # 🔹 Rotating App Log (all logs)
    app_handler = RotatingFileHandler(
        "app.log", maxBytes=5_000_000, backupCount=3
    )
    app_handler.setLevel(logging.DEBUG)
    app_handler.setFormatter(formatter)

    # 🔹 Rotating Error Log
    error_handler = RotatingFileHandler(
        "error.log", maxBytes=2_000_000, backupCount=2
    )
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(formatter)

    # 🔹 Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG if debug else logging.INFO)
    console_handler.setFormatter(formatter)

    # Clear old handlers
    logger.handlers.clear()

    # Add handlers
    logger.addHandler(app_handler)
    logger.addHandler(error_handler)
    logger.addHandler(console_handler)
