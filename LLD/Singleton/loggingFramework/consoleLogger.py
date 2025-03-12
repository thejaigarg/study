from logAppender import logAppender

class consoleAppender(logAppender):

    def append(self, message):
        print(message)