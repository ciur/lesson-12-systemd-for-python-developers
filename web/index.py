import logging
from datetime import datetime


logging.basicConfig(filename='/demo/web/index.log', level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info(f"[{datetime.now()}]Recurring indexing")
# Indexing...
