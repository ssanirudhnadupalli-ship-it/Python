from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        return "Connected to MySQL Database."

class PostgreSQLDatabase(Database):
    def connect(self):
        return "Connected to PostgreSQL Database."

print(MySQLDatabase().connect())
print(PostgreSQLDatabase().connect())
