import string
import random
import re
import pprint
import time
import os
import math


regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

def home():
    print("\n***Welcome to SNG Bank ERP***\n")
    print("1. Staff Login")
    print("2. Close App")

    reply = input("Please select an option: ")
    if (reply == '1'):
        Login()
    elif (reply == '2'):
        exit()
    else:
        print("Input is not valid")
        Back()

def Back():
    print("1. Return to home page")
    print("2. Exit\n")
    reply = input("Select an option:  \n")
    if (reply == '1'):
        home()
    elif (reply == '2'):
        exit()
    else:
        exit()


def Login():
    username = input("\nPlease enter username: \n").lower()
    Pass = input("\nEnter password: ")
    infoCheck = open(r'Info\staff.txt', "r")
    for line in infoCheck:
        if username in line:
            theString = line
            password = theString.split(" ")[1]
            if Pass == password:
                print("log in successful!\n")
                sName = theString.split(" ")[3] + " " + theString.split(" ")[4]
                infoCheck.close()
                Portal(username, sName)
            else:
                infoCheck.close()
                print("Wrong Username or Password. Want to try again? \nYes or No")
                retryLogIn = input();
                if (retryLogIn == "Yes"):
                    Login()
                elif (retryLogIn == "No"):
                    home();
                else:
                    print("Enter valid input")
                    exit()
        else:
            infoCheck.close()
            print("Wrong Username or Password. Want to try again? \nYes or No")
            retryLogIn = input();
            if (retryLogIn == "Yes"):
                Login()
            elif (retryLogIn == "No"):
                  home();
            else:
               print("Enter valid input")
               exit()

       

def Portal(UserName, name):
    print("Good day" + UserName + "!. Hope you're having an awesome day")
    baconFile = open('info\Session.txt', 'w')
    ts = time.gmtime()
    currentTime = time.strftime("%Y-%m-%d %H:%M:%S", ts)
    Session = name.upper() + " with username " + UserName + " logged in at " + currentTime + "\n"
    baconFile.write(SessionText)
    baconFile.close()
    
    print("\n1. Create new bank account")
    print("2. Check account details")
    print("3. Logout\n")
    option = input("\nPlease select an option: \n")
    if (option == '1'):
        NewAcc(UserName, name)
    elif (option == '2'):
        AccountDetails(UserName, name)
    elif (option == '3'):
        os.remove(r"info\Session.txt")
        Login()
    else:
        os.remove(r"info\Session.txt")
        exit()


def NewAcc(UserName, name):
    accType = ["Savings", "Current", "Domiciliary", "Fixed Deposit"]
    print("\n****CREATE NEW ACCOUNT****\n")
    print("Enter user details\n")
    FirstName = input("First name: \n")
    MiddleName = input("Middle name: \n")
    LastName = input("Last name: \n")
    OpeningBalance = int(input("Opening Amount: $\n"))
    print("Type of Account ")
    Type = accType[int(input("\nFill it here. ")) - 1]
    Email = input("Enter a valid email address: ").lower();
    
    if (re.search(regex, userEmail)):
        AccNumber = AccountGenerator()
        CustomerFile = open('info\customer.txt', 'a')
        customerinfo = AccNumber + " " + str(OpeningBalance) + " " + FirstName + " " + MiddleName + " " + \
                       LastName + " " + Email + " " + Type + "\n"
        CustomerFile.write(customerinfo)
        CustomerFile.close()
        print(f"\nYou just opened a {Type} account for {FirstName} {MiddleName}w\n"
              f"Account number is {AccNumber} with ${Balance: ,} balance")
        print("Account created successfully");
        Portal(UserName, name)
    else:
        print("Invalid Email Address")
        NewAcc(UserName, name)


def AccDetails(UserName,name):
    print("\n*** CHECK ACCOUNT DETAILS ***")
    AccNumber = input("Enter Account Number? ")
    CustomerSearch = open(r'info\customer.txt', "r")
    for line in CustomerSearch:
        if AccNumber in line:
            theString = line
            customerAccountBalance = int(theString.split(" ")[1])
            customerAccountName = theString.split(" ")[2].capitalize()+" " + theString.split(" ")[3].capitalize() + " " + theString.split(" ")[4].capitalize()
            customerAccountEmail = theString.split(" ")[5]
            customerAccountType = theString.split(" ")[6]
            print(f"\nAccount Number: {userAccountNumber}\nAccount Name: {customerAccountName}\n"
                  f"Balance: #{customerAccountBalance:,}\nAccount Type: {customerAccountType}\n"
                  f"Email: {customerAccountEmail}")
            CustomerSearch.close()
            Portal(UserName, name)
        else:
            print("\nInvalid Account Number.Please check details and try again")
            CustomerSearch.close()
            Portal(UserName, name)



def AccGen():
    accPrefix = ["069", "079"]
    size = 7
    chars = string.digits  
    randomString = ''.join(random.choice(chars) for _ in range(size))
    randomPrefix = random.randint(0, 1)
    Accountnum = accPrefix[randomPrefix] + randomString
    return Accountnum


print("Follow the format in the staff.txt file to create and authenticate staff permission")
var = 1
while var == 1:
    home()