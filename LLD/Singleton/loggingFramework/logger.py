from logAppender import logAppender
from logLevel import logLevel
from consoleLogger import consoleAppender
from loggerConfig import logConfig

class logger():
    _instance = None

    def __init__(self):
        if logger._instance:
            raise Exception("This class is singleton!")
        else:
            logger._instance = self
            self.config = logConfig(logLevel.INFO, logAppender())

    @staticmethod
    def get_instace():
        if logger._instance is None:
            logger()
        return logger._instance
    
    def setConfig(self, config):
        self.config = config

    def log(self, logLevel, message):
        if logLevel.value >= self.config.getLogLevel().value:
            logMessage = logMessage(logLevel, message)
            self.config.getLogAppender().append(logMessage)
    
    def debug(self, message):
        self.log(logLevel.DEBUG, message)