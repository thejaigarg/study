from time import time

class logMessage:

    def __init__(self, logLevel, message):
        self.logLevel = logLevel
        self.message = message
        self.time = int(time.time()*1000)
    
    def get_level(self):
        return self.logLevel

    def get_message(self):
        return self.message
    
    def get_time(self):
        return self.time
    
    def __str__(self):
        return f"[{self.get_level}] {self.get_time} - {self.get_message}"