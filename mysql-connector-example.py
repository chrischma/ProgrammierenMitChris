import mysql.connector
import credentials


def connect_to_database():
    
    global mydb

    mydb = mysql.connector.connect(       # login credentials are loaded from a custom file named "credentials".
        host=credentials.host,
        user=credentials.user,
        password=credentials.pw,
        database="meine_datenbank"
    )


def load_all_items():

    my_cursor = mydb.cursor()
    my_cursor.execute("SELECT * FROM all_2dos")
    res = my_cursor.fetchall()

    for _ in res:
        print(_)

    return res


def insert_item(id, body):
    my_cursor = mydb.cursor()
    sql = "INSERT INTO all_2dos (id, body) VALUES (%s, %s)"
    val = (id, body)
    my_cursor.execute(sql, val)
    mydb.commit()
    

if __name__ == "__main__":
    connect_to_database()
    load_all_items()
    insert_item("123", 'Das ist ein Body.')
