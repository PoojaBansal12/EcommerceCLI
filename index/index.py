from dao import user

class index:

    user = user.user()

    print("1. Login\n2. Register\n0. Exit")
    num = input()
    if num == '1':
        user.login_user()
    elif num is '2':
        name = input("Name: ")
        passwd = input("Password: ")
        user.register_user(name, passwd)
    elif num is '0':
        print("Visit Again!!!!")
    else:
        print("Invalid Input")


