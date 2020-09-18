import os

from celery import Celery
from celery.utils.log import get_task_logger

from scrapper import Scrapper


REDIS_URL = os.environ['REDIS_URL']
logger = get_task_logger(__name__)

celery_app = Celery('tasks', broker=f'redis://{REDIS_URL}',
                    backend=f'redis://{REDIS_URL}')



@celery_app.task
def count(address):
    logger.info(f'Adding task for {address}')
    s = Scrapper(address)
    err = s.get_page()
    result = None
    if not err:
        result = s.count_matches()
    return result
