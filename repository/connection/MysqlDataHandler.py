import mysql

from mysql import connector

class dbDataHandler:
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    def db_conec(self):
        try:

            self.connection = mysql.connector.connect(
                host = self.host,
                port = self.port,
                user = self.user,
                password = self.password,
                database = self.database
            )

            print("Connection successfull")

        except mysql.connector.Error as err:
            print("no connection error: ", err)

    def db_disconec(self):
        if self.connection:
            self.connection.close()
            print("Connection closed")

    def execute_query(self, query, params= None):
        cursor = self.connection.cursor(buffered= True)
        try:
            cursor.execute(query, params)
            self.connection.commit()
            print("Sign Up Completed")

            if query.lower().startswith('select'):
                result  = cursor.fetchall()
                return result

        except mysql.connector.Error as err:
            print("No releted information: ", err)
            return None

        finally:
            cursor.close()
