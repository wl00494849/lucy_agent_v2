import logging
from datetime import date
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

today = date.today().strftime("%Y%m%d")

log_fmt = "%(asctime)s [%(levelname)s] %(name)s - %(message)s"
datefmt = "%Y-%m-%d %H:%M:%S"

logging.basicConfig(
    level=logging.INFO,
    format=log_fmt,
    datefmt=datefmt,
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(f"{LOG_DIR}/{today}.log",encoding="utf-8")
    ]
)