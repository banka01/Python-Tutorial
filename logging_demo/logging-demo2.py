    import logging
import inspect
# import loggingpackage.custom_logger as cl

def customLogger(logLevel):
    # Gets the name of the class / method from where this method is called
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)

    # By default, log all messages
    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler("{0}.log".format(loggerName), mode='a')
    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger
class LoggingDemo2():

    log = customLogger(logging.DEBUG)

    def method1(self):
        self.log.debug('debug message')
        self.log.info('info message')
        self.log.warning('warn message')
        self.log.error('error message')
        self.log.critical('critical message')

    def method2(self):
        m2Log = customLogger(logging.INFO)
        m2Log.debug('debug message')
        m2Log.info('info message')
        m2Log.warn('warn message')
        m2Log.error('error message')
        m2Log.critical('critical message')
    #
    # def method3(self):
    #     m3Log = customLogger(logging.INFO)
    #     m3Log.debug('debug message')
    #     m3Log.info('info message')
    #     m3Log.warn('warn message')
    #     m3Log.error('error message')
    #     m3Log.critical('critical message')

demo = LoggingDemo2()
demo.method1()
demo.method2()
demo.method1()
demo.method2()
# demo.method3()