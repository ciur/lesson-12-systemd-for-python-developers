import time
import logging

logging.basicConfig(filename='/demo/hello.log', level=logging.INFO)
logger = logging.getLogger(__name__)

count = 0
while True:
    logger.info(f"Script says: {count} hello, systemd!")
    time.sleep(1)
    count += 1


