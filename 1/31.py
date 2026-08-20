from abc import ABC, abstractmethod

class Database(ABC):

    @abstractmethod
    def connect(self):
        pass


class MySQL(Database):
    def connect(self):
        print("Connected to MySQL database")


class PostgreSQL(Database):
    def connect(self):
        print("Connected to PostgreSQL database")


class MongoDB(Database):
    def connect(self):
        print("Connected to MongoDB database")


class SQLite(Database):
    def connect(self):
        print("Connected to SQLite database")


MySQL().connect()
PostgreSQL().connect()
MongoDB().connect()
SQLite().connect()