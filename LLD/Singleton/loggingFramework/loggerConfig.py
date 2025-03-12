class logConfig():
    def __init__(self, logLevel, logAppender):
        self.logLevel = logLevel
        self.logAppender = logAppender
        
    def getLogLevel(self):
        return self.logLevel

    def setLogLevel(self, logLevel):
        self.logLevel = logLevel

    def getLogAppender(self):
        return self.logAppender

    def setLogAppender(self, logAppender):
        self.logAppender = logAppender