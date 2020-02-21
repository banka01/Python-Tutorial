"""
Logging Format
https://docs.python.org/3/library/logging.html#logrecord-attributes
https://docs.python.org/3/library/time.html#time.strftime
"""
import logging

logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s :%(filename)s :%(funcName)s:%(lineno)d',
                    datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.DEBUG)
logging.warning("warning message")
logging.info("info message")
logging.error("error message")

def sample_test():
    logging.info('in test message')
    print('in test')
sample_test()