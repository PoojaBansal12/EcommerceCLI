from utils import conn
from dao import cart

class product():
    def customerProduct(self,category):
        try:
            con = conn.get_connection()
            my_cursor = con.cursor()
            cart_instance = cart.cart()
            check = ("select product_id, product_name, prod_price from products where category = (select cat_id from categories where category_name = %s )")
            my_cursor.execute(check, category)
            catch = my_cursor.fetchall()
            for item in catch:
                print("Id: "+ str(item[0]) +'\n'+ "Name: " + str(item[1])+'\n' + "Price: "+ str(item[2]), end='\n')
                print('\n')

            productID = input("Enter the product id comma separated to buy: ")
            username = input("Enter username: ")
            my_cursor.close()
            con.close()

            cart_instance.insertCart(productID, username)
        except BaseException:
            print("Got an error")
