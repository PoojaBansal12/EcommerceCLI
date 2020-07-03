from utils import conn

class admin():
    conn = conn.get_connection()

    def adminActions(self):
        print("Enter your choice: ")
        print("1. Add Product\n2. Delete Product\n3. Add Category\n4. Delete Category\n5. View All Costumer Cart\n6. View All Custoomer Bills\n0. Exit")
        choice = input()

        if '1' in choice:
            admin.updateProduct(self)
        elif '3' in choice:
            admin.updateCategory(self)
        elif '5' in choice:
            admin.viewDetails(self)
        elif '6' in choice:
            admin.viewBills(self)
        elif '2' in choice:
            admin.deleteProduct(self)
        elif '4' in choice:
            admin.deleteCategory(self)
        elif '0' in choice:
            print("Bye Bye")
        else:
            print("Invalid Input")


    def updateProduct(self):
        con = conn.get_connection()
        my_cursor = con.cursor()
        prod_name = input("Product name: ")
        category = input("Category name: ")
        Price = input("Product Price: ")
        sql = ("SELECT cat_id FROM categories WHERE category_name = %s")
        my_cursor.execute(sql,category)
        catch = my_cursor.fetchone()
        category = catch[0]
        sql_add = (" INSERT INTO products (product_name, category, prod_price) VALUES (%s,%s,%s)")
        details = [prod_name,category,Price]
        my_cursor.execute(sql_add, details)
        con.commit()

        print("Updated Product List:\n")
        check = ("select product_id, product_name,category, prod_price from products")
        my_cursor.execute(check)
        catch = my_cursor.fetchall()
        for item in catch:
            print("ProductId: " + str(item[0]) + '\n' + "Name: " + str(item[1]) + '\n' + "CategoryID: " + str(item[2]) + '\n'"Price: " + str(item[3]), end='\n')
            print('\n')
        my_cursor.close()
        con.close()

        admin.confirmation(self)



    def updateCategory(self):
        con = conn.get_connection()
        my_cursor = con.cursor()
        category = input("Category: ")
        sql_add = ("INSERT INTO categories (category_name) VALUES (%s)")
        details = [category]
        my_cursor.execute(sql_add, details)
        con.commit()

        print("Updated Category List:\n")
        check = ("select cat_id, category_name from categories")
        my_cursor.execute(check)
        catch = my_cursor.fetchall()
        for item in catch:
            print("CategoryID: " + str(item[0]) + '\n' + "Name: " + str(item[1]), end='\n')
            print('\n')
        my_cursor.close()
        con.close()

        admin.confirmation(self)

    def viewDetails(self):
        con = conn.get_connection()
        my_cursor = con.cursor()

        sql_view = ("SELECT price.prod_price,users.username,users.user_id,price.purchase_indicator FROM  (SELECT prod_price, cart.user,cart.purchase_indicator from products INNER JOIN (SELECT product,user,purchase_indicator from cart) cart ON products.product_id = cart.product) price INNER JOIN users ON price.user = users.user_id")

        my_cursor.execute(sql_view)

        cart_details = my_cursor.fetchall()
        for item in cart_details:
            print('Id: ' + str(item[2]) + '\n' + 'Name: ' + str(item[1]) + '\n' + 'Price: ' + str(
                item[0]) + '\n' + 'Purchase Indicator : ' + str(item[3]))
        my_cursor.close()
        con.close()

        admin.confirmation(self)

    def viewBills(self):
        con = conn.get_connection()
        my_cursor = con.cursor()

        sql_view = ("SELECT price.productPrice,users.username,users.user_id FROM (SELECT SUM(prod_price) as productPrice,user FROM (SELECT prod_price, cart.user from products INNER JOIN (SELECT product,user from cart where purchase_indicator='Purchased') cart ON products.product_id = cart.product) grp GROUP BY user) price INNER JOIN users ON price.user = users.user_id")

        my_cursor.execute(sql_view)

        bill_details = my_cursor.fetchall()
        print("*************************All users Bill***************************")
        for item in bill_details:
            print('UserID: '+ str(item[2]) +'\n' + 'Username: '+ str(item[1]))
            total_amount = int(item[0])
            discount = 0

            if total_amount > 10000:
                discount = 500
            print("Actual amount: " + str(total_amount))
            print("Discount amount: " + str(discount))
            print("Final Amount: " + str((total_amount - discount)))
        print("**************************END***************************")
        my_cursor.close()
        con.close()

        admin.confirmation(self)

    def deleteProduct(self):
        con = conn.get_connection()
        my_cursor = con.cursor()
        prod_name = input("Product name: ")

        sql_add = ("DELETE FROM products WHERE product_name=%s")
        details = [prod_name]
        my_cursor.execute(sql_add, details)
        con.commit()

        print("Updated Product List:\n")
        check = ("select product_id, product_name,category, prod_price from products")
        my_cursor.execute(check)
        catch = my_cursor.fetchall()
        for item in catch:
            print("ProductId: " + str(item[0]) + '\n' + "Name: " + str(item[1]) + '\n' + "CategoryID: " + str(
                item[2]) + '\n'"Price: " + str(item[3]), end='\n')
            print('\n')
        my_cursor.close()
        con.close()

        admin.confirmation(self)

    def deleteCategory(self):
        con = conn.get_connection()
        my_cursor = con.cursor()
        category = input("Category: ")

        sql_add = ("DELETE FROM categories WHERE category_name=%s")
        details = [category]
        my_cursor.execute(sql_add, details)
        con.commit()

        print("Updated Category List:\n")
        check = ("select cat_id, category_name from categories")
        my_cursor.execute(check)
        catch = my_cursor.fetchall()
        for item in catch:
            print("CategoryID: " + str(item[0]) + '\n' + "Name: " + str(item[1]), end='\n')
            print('\n')
        my_cursor.close()
        con.close()

        admin.confirmation(self)

    def confirmation(self):
        print("Would you like to make more changes?")
        print("1. Yes\n2. No")
        choice = input()
        if '1' in choice:
            admin.adminActions(self)
        elif '2' in choice:
            print("See ya!!!")
        else:
            print("Invalid input")