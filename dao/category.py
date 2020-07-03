from utils import conn
from dao import product
import pymysql

# define Python user-defined exceptions
class ChoiceError(Exception):
    """Base class for other exceptions"""
    pass

class category():
    #conn = conn.get_connection()

        def customerCategories(self):
            try:
                con = conn.get_connection()
                #con = pymysql.connect(host="localhost", user="root", passwd="", db="cart_db")
                my_cursor = con.cursor()
                prodObj = product.product()
                category_items = ("SELECT category_name FROM categories")
                my_cursor.execute(category_items)
                catch = my_cursor.fetchall()
                count = 1
                itemDict={}
                for item in catch:
                    itemDict[count]= str(item[0])
                    print(str(count)+ "." + str(item[0]), end='\n')
                    count = count + 1
                choice_id = int(input("Choose a category : "))
                if choice_id not  in  itemDict.keys():
                    choice = int(input("Choose a category a valid category : "))
                    if choice not in itemDict.keys():
                        raise ChoiceError
                    choice_id = choice
                choice = itemDict[choice_id]
                my_cursor.close()
                con.close()
                prodObj.customerProduct(choice)
            except KeyError:
                print("Input Error !!!!! Got a wrong input")
            except ChoiceError:
                print("Entered wrong category twice!!! Visit Again")
            except BaseException:
                print("Got a exception")
