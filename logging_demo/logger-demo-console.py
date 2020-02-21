"""
Logger Demo
"""
import logging

class LoggerDemoConsole():

    def testLog(self):
        # create logger
        logger = logging.getLogger(LoggerDemoConsole.__name__)
        logger.setLevel(logging.DEBUG)

        # create console handler and set level to info
        consoleHandler = logging.StreamHandler()
        consoleHandler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                    datefmt='%Y/%d/%m %I:%M:%S %p')

        fileHandler = logging.FileHandler("sample_log_file.log", mode='a')
        fileHandler.setLevel(logging.DEBUG)
        fileHandler.setFormatter(formatter)
        # add formatter to console handler
        consoleHandler.setFormatter(formatter)

        # add console handler to logger
        logger.addHandler(consoleHandler)
        logger.addHandler(fileHandler)

        # logging messages
        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warn message')
        logger.error('error message')
        logger.critical('critical message')



demo = LoggerDemoConsole()
demo.testLog()