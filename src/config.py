import configparser
from pathlib import Path

CONFIG_FILE = Path(__file__).resolve().parent.parent / "config.ini"

def load_fares():
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)

    stopped = config.getfloat("fares", "stopped")
    moving = config.getfloat("fares", "moving")

    return {
        "stopped": stopped,
        "moving": moving,
    }