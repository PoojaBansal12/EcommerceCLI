import pymysql

def get_connection():
    try:
        conn = pymysql.connect(host="localhost", user="root", passwd="", db="cart_db")
        return conn
    except pymysql.err:
        print("MYSQL Exception")
    except BaseException:
        print("Got a exception")



