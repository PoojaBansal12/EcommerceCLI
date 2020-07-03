from utils import conn
from dao import category

class cart():

    def insertCart(self,productID, username):
        category_obj = category.category()

        con = conn.get_connection()

        my_cursor = con.cursor()
        cartObj = cart()
        productList = []
        productList = str(productID).split(",")
        sql = ("select user_id from users where username=%s")
        my_cursor.execute(sql,username)
        user_id = my_cursor.fetchone()
        status = 'Pending'
        for item in productList:
            insert = ("INSERT INTO cart(product, user, purchase_indicator) VALUES (%s, %s, %s)")
            details = [item, user_id, status]
            my_cursor.execute(insert, details)
            con.commit()
        userId = str(user_id[0])
        my_cursor.close()
        con.close()

        cart().cartData(userId)
        #cart operations
        print("1. Buy the Product.")
        print("2. Remove the Product from Cart.")
        print("3. Return to Category options")
        choice = input("Enter the choice")
        if '1' in choice:
            product_id = input("Enter the comma separated product id to buy")
            cart().buyCart(product_id, userId)
        elif '2' in choice:
            product_id = input("Enter the comma separated product id to delete from cart")
            cart().deleteCartItem(product_id, user_id)
        elif '3' in choice:
            category_obj.customerCategories()
        else:
            print("Invalid choice!!!")


    def cartData(self,userId):
        con = conn.get_connection()

        my_cursor = con.cursor()

        sql = ("select a.product_id ,a.product_name, a.prod_price,b.purchase_indicator from products a inner join (select product,purchase_indicator from cart where user= %s) b on a.product_id = b.product")
        my_cursor.execute(sql, userId)
        prodList = my_cursor.fetchall()

        for item in prodList:
            print('Id: ' + str(item[0]) + '\n' + 'Name: ' + str(item[1]) + '\n' + 'Price: ' + str(
                item[2]) + '\n' + 'Purchace Indicator : ' + str(item[3]))
        my_cursor.close()
        con.close()

    def buyCart(self,product_id,user_id):

        category_obj = category.category()
        con = conn.get_connection()
        my_cursor = con.cursor()

        productList = []
        productList = str(product_id).split(",")
        for item in productList:
            sql = ("UPDATE cart SET purchase_indicator = 'Purchased' WHERE product=%s and user=%s")
            details = [product_id, user_id]
            my_cursor.execute(sql, details)
            con.commit()

        print("****************************Your Final Bill********************************")
        sql = ("SELECT SUM(prod_price) from products INNER JOIN (SELECT product from cart where purchase_indicator='Purchased' AND user=%s) cart ON products.product_id = cart.product")

        my_cursor.execute(sql,user_id)
        result = my_cursor.fetchone()

        total_amount = int(result[0])
        discount = 0

        if total_amount > 10000:
            discount = 500
        print("Actual amount: "+ str(total_amount))
        print("Discount amount: "+ str(discount))
        print("Final Amount: "+ str((total_amount - discount)))
        print("**************************END***************************")

        my_cursor.close()
        con.close()

        cart.furtherQuestion(self)

    def deleteCartItem(self, product_id, user_id):

        con = conn.get_connection()

        my_cursor = con.cursor()

        category_obj = category.category()

        productList = []
        productList = str(product_id).split(",")
        for item in productList:
            sql = ("delete from cart WHERE product=%s and user=%s")
            details = [product_id, user_id]
            my_cursor.execute(sql, details)
            con.commit()
        my_cursor.close()
        con.close()

        cart().cartData(user_id)
        cart.furtherQuestion(self)


    def furtherQuestion(self):
        print("What do you want to ?")
        print("1. Keep shopping\n2. Exit\n")
        choice = input()
        if '1' in choice:
            category_obj.customerCategories()
        elif '2' in choice:
            print("Thank you for shopping")
        else:
            print("Invalid input")