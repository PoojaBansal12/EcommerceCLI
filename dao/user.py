from utils import conn
from dao import category
from dao import admin
import pymysql

class user():
    def login_user(self):
        try :
            success = False
            con = conn.get_connection()
            my_cursor = con.cursor()
            cat_obj = category.category()
            admin_obj = admin.admin()

            for i in range(3):
                username = input("Username: ")
                password = input("Password: ")
                check = "SELECT username, password,user_type from users where username=%s AND password=%s"
                details = [username, password]
                my_cursor.execute(check, details)
                catch = my_cursor.fetchone()
                #print(catch)
                if 'None' not in str(catch):
                    name, passw ,userType = catch
                    print("login succeeded")
                    if 'customer' in str(userType):
                        print("Categories are listed below: \n")
                        cat_obj.customerCategories()
                    else :
                        admin_obj.adminActions()

                    success = True
                    break
                else:
                    print("login failed")
            if not success:
                print("\nYour login failures have reached maximum, please try again in 10 minutes!")

            con.close()
        except BaseException:
            print("Error in connection")

    def register_user(self, name, passwd):
        try:
            con = conn.get_connection()
            user_type = 'customer'
            my_cursor = con.cursor()
            sqlformula = "Insert into users(username,password,user_type) values(%s,%s,%s)"

            employees = [name, passwd,user_type]

            my_cursor.execute(sqlformula, employees)
            con.commit()
            con.close()
            print("Yay! You can now Login.Happy Shopping")
            user.login_user(self)
        except pymysql.err.IntegrityError:
            print('Username  already exists try a new one!!!!')
        except BaseException:
            print("Got a insert error")
