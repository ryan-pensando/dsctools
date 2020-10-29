import sqlite3
from sqlite3 import Error
from datetime import date


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e + "table error")
    finally:
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

def create_dsc(conn, dsc):
    """
    Create a new dsc into the dsc inventory table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO dsc_inventory(mac, ip, discovery_date, id, host, network_mode, mgmt_mode, 
            serial_num, sku, kernel, proc )
            VALUES(?,?,?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, dsc)
    conn.commit()
    return cur.lastrowid

def insert_dsc(conn, dsc):

    with conn:
        # create a new dsc
        dsc2 = create_dsc(conn, dsc)

def select_all_dsc(conn):
    """
    Query all rows in the dsc_inventory table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM dsc_inventory")

    rows = cur.fetchall()

    for row in rows:
        print(row)


if __name__ == '__main__':
    conn = create_connection(r"pensando_dsc.db")

    sql_create_dsc_table = """ CREATE TABLE IF NOT EXISTS dsc_inventory (
                                            mac text PRIMARY KEY,
                                            id text NOT NULL,
                                            discovery_date text,
                                            ip text NOT NULL,
                                            host text NOT NULL,
                                            network_mode text NOT NULL,
                                            mgmt_mode text NOT NULL,
                                            serial_num text NOT NULL,
                                            sku text NOT NULL, 
                                            kernel text NOT NULL,
                                            proc text NOT NULL
                                            
                                        ); """

    if conn is not None:

        # create projects table
        create_table(conn, sql_create_dsc_table)

    else:
        print("Error! cannot create the database connection.")

    today = date.today()

    dsc = ('fff1', 'dsc2', today, '192.168.1.2', 'pen17', 'inband', 'network', '5UP9490dj2', 'p18669-001', '4.14.18', 'armv8');

    #insert a dsc
    insert_dsc(conn, dsc)
    select_all_dsc(conn)
