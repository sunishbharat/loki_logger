import time
import logging
import sys
from pathlib import Path

# Add project root
sys.path.insert(0, str(Path(__file__).parent.parent))
from loki_logger.core import loki_logger

logger = loki_logger(level=logging.DEBUG, tags={"app": "fastapi", "env":"block"})

logger.info("Info: 1.User logged in", extra={"user_id": 123})
logger.debug("Debg: 2.Debug info")
logger.error("Error: 3.Something went wrong", extra={"error": "details"})
logger.warning("Warning: 4.This is a warning")
logger.critical("Critical: 5.System failure!")
logger.exception("Exception: 6.Unhandled exception")
log_dict = {
    "warn":"Memory full",
    "Cpu": "99%"
}
logger.critical(log_dict)

time.sleep(1)