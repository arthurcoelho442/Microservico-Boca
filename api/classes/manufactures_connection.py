import psycopg2
from os import environ

class ConnectionFactory():
    @staticmethod
    def connect():

        try:
            db = psycopg2.connect(user=environ["USER_DB"],
                                  password=environ["PASSWORD_DB"],
                                  database=environ["NAME_DB"],
                                  host=environ["HOST_DB"],
                                  port=int(environ["PORT_DB"]),
                                  options="-c search_path=" + environ["SCHEMA"])

            db.set_session(autocommit=environ["AUTOCOMIT_DB"])
            return db
        except Exception as e:
            print("Exxepition", e)
            db = ConnectionFactory.connect_db_delay()
            return db

    @staticmethod
    def create_database(database, cursor):
        sql = "CREATE DATABASE IF NOT EXISTS " + database
        cursor.execute(sql)

    @staticmethod
    def connect_db_delay():
        try:
            db = psycopg2.connect(user=environ["USER_DB"],
                                  password=environ["PASSWORD_DB"],
                                  database=environ["NAME_DB"],
                                  host=environ["HOST_DB"],
                                  port=int(environ["PORT_DB"]),
                                  options="-c search_path=" + environ["SCHEMA"])

            db.set_session(autocommit=environ["AUTOCOMIT_DB"])
            return db
        except:
            try:
                db = psycopg2.connect(user=environ["USER_DB"],
                                      password=environ["PASSWORD_DB"],
                                      host=environ["HOST_DB"],
                                      port=int(environ["PORT_DB"]),
                                      options="-c search_path=" + environ["SCHEMA"])

                db.set_session(autocommit=environ["AUTOCOMIT_DB"])

                if db:
                    ConnectionFactory.create_database(environ["NAME_DB"], db.cursor())
                    print('Criando Banco de Dados ' + environ["NAME_DB"])
                    db.close()

                    db = psycopg2.connect(user=environ["USER_DB"],
                                          password=environ["PASSWORD_DB"],
                                          database=environ["NAME_DB"],
                                          host=environ["HOST_DB"],
                                          port=int(environ["PORT_DB"]),
                                          options="-c search_path=" + environ["SCHEMA"])

                    db.set_session(autocommit=environ["AUTOCOMIT_DB"])
                    return db
            except:
                print('Verifique se existe um banco de dados MYSQL')
