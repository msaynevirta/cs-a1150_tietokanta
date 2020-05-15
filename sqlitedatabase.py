import sqlite3

class SqliteDatabase:
    def __init__(self, filepath):
        self.db = sqlite3.connect(filepath)
        self.cursor = self.db.cursor()