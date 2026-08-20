from abc import ABC, abstractmethod

class Database(ABC):

    @abstractmethod
    def connect(self):
        pass

    def display_database_name(self):
        print("Database: MySQL")


class MySQLDatabase(Database):

    def connect(self):
        print("Connected to MySQL database")


obj = MySQLDatabase()
obj.connect()
obj.display_database_name()