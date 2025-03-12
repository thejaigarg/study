from logAppender import logAppender

class fileAppender(logAppender):

    def __init__(self, path):
        self.path = path

    def append(self, message):
        with open(self.path, "a") as file:
            file.write(str(message))