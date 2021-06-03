import psycopg2
from config import *
from prettytable import PrettyTable

class DataBase:
    def __init__(self):
        self.conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, 
                        password=DB_PASSWORD, host=HOST,port=PORT)
        self.cursor = self.conn.cursor()
        self.createDb()

    def createDb(self):
        self.cursor.execute("SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'users';")
        if len(self.cursor.fetchall()) == 0:
            self.cursor.execute("CREATE TABLE users (id VARCHAR(32) NOT NULL PRIMARY KEY, name VARCHAR(1000) NOT NULL);")
            self.conn.commit()
        self.cursor.execute("SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'companies';")
        if len(self.cursor.fetchall()) == 0:
            self.cursor.execute("CREATE TABLE companies (id SERIAL PRIMARY KEY, name VARCHAR(1000) NOT NULL, user_id VARCHAR(32) NOT NULL);")
            self.conn.commit()

    def createUser(self, id, name):
        try:
            self.cursor.execute("INSERT INTO users (id, name) VALUES (%s, %s);", (id, name))
            self.conn.commit()
        except:
            self.conn.rollback()


    def createCompany(self,name,userId):
        try:
            self.cursor.execute("INSERT INTO companies (name,user_id) VALUES (%s, %s);", (name, userId))
            self.conn.commit()
        except:
            self.conn.rollback()     

    def close(self):
        self.cursor.close()
        self.conn.close()

    def getUsers(self):
        table = PrettyTable()
        table.field_names = ["id", "name"]
        self.cursor.execute("SELECT * FROM users")
        for item in self.cursor.fetchall():
            table.add_row(item)
        print(table)

    def getCompanies(self):
        table = PrettyTable()
        table.field_names = ["id", "name", "user_id"]
        self.cursor.execute("SELECT * FROM companies")
        for item in self.cursor.fetchall():
            table.add_row(item)
        print(table)