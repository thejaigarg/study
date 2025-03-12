import psycopg2
from logAppender import logAppender

class databaseAppender(logAppender):
    
    def __init__(self, db_url, username, password):
        self.db_url = db_url
        self.username = username
        self.password = password
    try:
        def append(self, message):
            connection = psycopg2.connect(self.db_url, self.username, self.password)
            cursor = connection.cursor()
            cursor.execute("INSERT INTO logs (level, message, timestamp) VALUES (%s, %s, %s)", 
                            (message.get_level.name(), message.get_message(), message.get_timestamp()))
            connection.commit()
            cursor.close()
            connection.close()
    except psycopg2.Error as e:
        print(f"Error: {e}")