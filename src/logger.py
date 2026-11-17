import logging
from pathlib import Path


LOG_DIR = Path(__file__).resolve().parent.parent / "logs"
LOG_FILE = LOG_DIR / "taximeter.log"


def get_logger():
    print(f"Ruta del log: {LOG_FILE}")

    LOG_DIR.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger("taximeter")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    logger.handlers.clear()

    handler = logging.FileHandler(LOG_FILE)
    handler.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger