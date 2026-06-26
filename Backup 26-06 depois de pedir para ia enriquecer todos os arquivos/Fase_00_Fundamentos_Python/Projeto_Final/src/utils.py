import time
import functools
import logging

def setup_logger():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        logging.info(f"Execução [{func.__name__}]: {time.time()-start:.4f}s")
        return res
    return wrapper
