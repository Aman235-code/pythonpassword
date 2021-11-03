import random
import sys


def generate():
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "@$_"
    total = lower + upper + numbers + symbols
    length = 8
    password = "".join(random.sample(total, length))
    write(password)

def write(password):
    f = open('passwords.txt','a')
    f.write("New Password is ----->   "+password+"\n")
    print("Your new password saved in passwords.txt file sucessfully\n")
    f.close()


def read():
    f = open('passwords.txt','r')
    print(f.read())
    f.close()
    menu()





def menu():
    print("1.Generate a password and save to a file (press 1 for it)\n")
    print("2.View your passwords file (press 2 for it)\n")
    print("3.Exit (press 3 for it)\n")
    result = int(input("Enter your choice:  "))
    if result == 1:
        generate()
        menu()
    elif result == 2:
        read()
    elif result == 3:
        print("Thanks for using my password saver app.Have a nice day\n")
        sys.exit()
    else:
        print("Invalid option.(Please select 1,2 or 3\n")




print("Hello Welcome to password generator menu.We can generate an password for you so that it come handy when you are signing up to a website.\n")
menu()



