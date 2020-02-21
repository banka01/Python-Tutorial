## logging

"""
Logging Demo 1
Logging Levels: kind of information to write.
DEBUG : when we are debugging some info. detailed info
INFO : only some information. conformation
WARNING
ERROR
CRITICAL

https://docs.python.org/3/library/logging.html
"""
# threshold set to warning
import logging
# logger = logging.getLogger()
# logger.info('aaa')
# logger.warning('warning')
## loglevel is default set to Warning.
# logging.basicConfig(filename='test_logging.log',level=logging.INFO)
logging.basicConfig(level=logging.DEBUG,filename='test_logging.log')
# logging.debug('This is debug message')
# logging.info('This is info message')
# logging.warning('This is warning message')
# logging.error('This is error')
# logging.critical('This is critical')

# logging.basicConfig(filename="test.log", level=logging.DEBUG)
# # logging.warning("warning message")
# # logging.info("info message")
# # logging.error("error message")
if __name__ == '__main__':
    logging.info('in main method')
    number = int(input('Enter a no:'))
    print('no enetered is ',number)
    logging.info('nuumber entered is {}'.format(number))
