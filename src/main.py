from dotenv import load_dotenv
from utils.logger import logger
import os
import requests
import schedule
import time

load_dotenv()


def main():
    route = "/cof-predict/critical/raw-update/"
    url = os.getenv("RISK_MATRIX_API_KEY") + route

    logger.info(f"Sending request to {url}")
    response = requests.patch(url)

    if response.status_code == 200:
        logger.info("Request successful")
    else:
        logger.error("Request failed")


def schedule_task():
    schedule.every(1).hour.do(main)
    logger.info("Schedule task started")
    while True:
        try:
            schedule.run_pending()
            time.sleep(1)
        except Exception as e:
            logger.error(f"Error: {e}")
            time.sleep(1)


if __name__ == "__main__":
    schedule_task()
