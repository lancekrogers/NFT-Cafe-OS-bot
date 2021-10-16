import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def initialize_database():
    database = r"os_floor_bot.db"

    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                        project_id VARCHAR(65) NOT NULL,
                                        project_name VARCHAR(100) NOT NULL,
                                        desc TEXT,
                                        os_endpoint VARCHAR NOT NULL,
                                        UNIQUE (project_id, os_endpoint)
                                        ); """

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        create_table(conn, sql_create_projects_table
                     )

    else:
        print("Error! cannot create the database connection.")
    conn.close()


if __name__ == '__main__':
    initialize_database()
