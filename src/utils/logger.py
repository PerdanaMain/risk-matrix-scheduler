import logging
import os

# Membuat direktori logs jika belum ada
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/log.log"),
        logging.StreamHandler(),
    ],
)

logger = logging.getLogger(__name__)
