from dotenv import load_dotenv
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(module)s:%(lineno)d - %(message)s',
    handlers=[
        logging.FileHandler('flq.log'),
        logging.StreamHandler()
    ],
    encoding='utf-8'
)

load_dotenv()
