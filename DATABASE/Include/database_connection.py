import sqlite3
class Database:
    def __init__(self,name):
        self.name=name
        self.connection=None
    def __enter__(self):
        self.connection=sqlite3.connect(self.name)
        return self.connection
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()

