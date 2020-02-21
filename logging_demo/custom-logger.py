import inspect
import logging

def customLogger(logLevel):
    # Gets the name of the class / method from where this method is called
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger()#loggerName)
    print(logger)
    # By default, log all messages
    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler("{0}.log".format(loggerName), mode='a')
    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger

class CustomLoggerTest:
    logger = customLogger(logging.DEBUG)

    def methodA(self):
        self.logger.info("calling MethodA")

    def methodB(self):
        self.logger.info("calling MethodB")

class Custom2:
    logger = customLogger(logging.DEBUG)

    def methodA(self):
        self.logger.info("calling MethodA of custom2")


if __name__ == '__main__':
    cl = CustomLoggerTest()
    cl.methodA()
    cl.methodB()
    cl2= Custom2()
    cl2.methodA()

