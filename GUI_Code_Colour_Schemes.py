##*********************************************** IMPORTS ***************************************************
from tkinter import *
from tkinter import ttk
import os
import tkinter
##********************************************** CLASSES ****************************************************
#Create the Account class
class Account:
    #The Account class stores the details of each account and has methods to deposit and withdraw money from their account
    def __init__(self, name, balance):
        self.name = name
        self.balance = float(balance)
        account_list.append(self)

    #Deposit method adds money to balance
    def deposit(self, amount):
        #Doesn't accept values of less than a cent 
        if amount >= 0.01:
            self.balance += amount
            return True
        else:
            return False

    #Withdraw method subtracts money from balance
    def withdraw(self, amount):
        if amount >= 0.01 and amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False

##******************************************  FUNCTIONS AND SETUP *****************************************
#Create a function to read data from the file
def get_data():
    #Checks whether the file exists and if so reads the file and separtes it to find the accounts and their balance
    if os.path.exists("clothing_allowance_app_file.txt"):
        if os.path.isfile("clothing_allowance_app_file.txt"):
            account_file = open("clothing_allowance_app_file.txt","r")
            line_list = account_file.readlines()
            for line in line_list:
                account_data = line.strip().split(",")
                Account(*account_data)

            account_file.close()
    #If the file doesn't exist a new file is created and set at the initial amounts set by the parents for the clothing allowance app
    else:
        print("File is not present new account file is being set up.")
        account_file = open("clothing_allowance_app_file.txt","w")
        account_file.write("Nikau's Account,300.0\nHana's Account,300.0\nTia's Account,300.0")
        account_file.close()
        get_data()

#Create a function to get account names list
def create_name_list():
    name_list = []
    for account in account_list:
        name_list.append(account.name)
    return name_list

#Checks if balance of the account is above $50, if so then bonus message pops up else message to encourage saving money will pop up
def bonus_check(self):
    if self.balance >= 50.00:
        bonus_message.set("                                       You're on track to recieve you're allocated bonus.\nMake sure to keep at least $50.00 in your account till the end of the year to recieve the bonus! :)")
    else:
        bonus_message.set("                                     You're not on track to receive you're allocated bonus.\nTry save up at least $50.00 in your account till then end of the year to recieve the bonus! :)")

#Create a function that will update the balance.
def update_balance():
    balance_string = ""
    account_file = open("clothing_allowance_app_file.txt", "w")
    #Append each accounts balance to the specific account name
    for account in account_list:
        balance_string += "{}: ${:.2f}     ".format(account.name, account.balance)
        account_file.write("{},{}\n".format(account.name, account.balance))
    account_details.set(balance_string)
    account_file.close()

#Create the deposit function
def deposit_money(account):
    #Provides appropriate error and feedback messages regarding transactions 
    if account.deposit(amount.get()):
        action_feedback.set("Your transaction has been completed. Total of ${:.2f} has been deposited into {}".format(amount.get(), account.name))
    else:
        action_feedback.set("Please enter a positive number/a number larger or equal to 0.01")

#Create the withdraw function
def withdraw_money(account):
    #Provides appropriate error and feedback messages regarding transactions 
    if account.withdraw(amount.get()):
        action_feedback.set("Your transaction has been completed. Total of ${:.2f} has been withdrawn from {}".format(amount.get(), account.name))
    else:
        action_feedback.set("Sorry, you either do not have enough money in {} or have written an invalid amount".format(account.name))

#Create the manage action function
def manage_action():
    try:
        for account in account_list:
            if chosen_account.get() == account.name:
                if chosen_action.get() == "Deposit":
                    deposit_money(account)
                else:
                    withdraw_money(account)
                bonus_check(account)

        #Update the GUI
        update_balance()
        amount.set("")

    #Add an exception for text input
    except:
        action_feedback.set("Please enter a positive number (a number larger or equal to 0.01). Special characters and letters will not be accepted!")

#Set up Lists
account_list = []

#Create instances of the class
get_data()
account_names = create_name_list()
##******************************************** GUI CODE ***************************************************
root = Tk()
root.title("Clothing Allowance App")
root.configure(bg='#000000')

#Create the top frame
top_frame = tkinter.LabelFrame(root, text="Account Details", font=("Georgia", 12, "bold"), bg='#000000', fg='#FFFFFF') #Georgia, Georgia, Georgia
top_frame.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

#Create and set the message text variable
message_text = StringVar()
message_text.set("Welcome! You can deposit or withdraw money from your account and check whether you will be allocated a bonus at the end of this year \n(if you have $50.00 or more left in your account).")

#Create and pack the message label
message_label = tkinter.Label(top_frame, textvariable=message_text, wraplength=1000, font=("Georgia", 11), bg='#000000', fg='#FFFFFF')
message_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

#Create and set the account details variable
account_details = StringVar()

#Create the details label and pack it into the GUI
details_label = tkinter.Label(top_frame, textvariable=account_details, font=("Georgia", 11, "bold"), bg='#2F8EA1', fg='#FFFFFF')
details_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

#Create the bottom frame
bottom_frame = tkinter.LabelFrame(root, bg='#000000', fg='#FFFFFF')
bottom_frame.grid(row=1, column=0, padx=10, pady=10, sticky="NSEW")

#Create a label for the account combobox
account_label = tkinter.Label(bottom_frame, text="Account: ", font=("Georgia", 11, "bold"), bg='#000000', fg='#FFFFFF')
account_label.grid(row=3, column=0, padx=10, pady=3)

#Set up a variable and option list for the account Combobox
chosen_account = StringVar()
chosen_account.set(account_names[0])

#Create a Combobox to select the account
account_box = ttk.Combobox(bottom_frame, textvariable=chosen_account, state="readonly", font=("Georgia", 9))
account_box['values'] = account_names
account_box.grid(row=3, column=1, padx=10, pady=3, sticky="WE")

#Create a label for the action Combobox
action_label = tkinter.Label(bottom_frame, text="Action:", font=("Georgia", 11, "bold"), bg='#000000', fg='#FFFFFF')
action_label.grid(row=4, column=0)

#Set up a variable and option list for the action Combobox
action_list = ["Deposit", "Withdraw"]
chosen_action = StringVar()
chosen_action.set(action_list[0])

#Create the Combobox to select the action
action_box = ttk.Combobox(bottom_frame, textvariable=chosen_action, state="readonly", font=("Georgia", 10))
action_box['values'] = action_list
action_box.grid(row=4, column=1, padx=10, pady=3, sticky="WE")

#Create a label for the amount field and pack it into the GUI
amount_label = tkinter.Label(bottom_frame, text="Amount:", font=("Georgia", 11, "bold"), bg='#000000', fg='#FFFFFF')
amount_label.grid(row=5, column=0, padx=10, pady=3)

#Create a variable to store the amount
amount = DoubleVar()
amount.set("")

#Create an entry to type in amount
amount_entry = tkinter.Entry(bottom_frame, textvariable=amount, font=("Georgia", 10), bg='#FFFFFF', fg='#000000')
amount_entry.grid(row=5, column=1, padx=10, pady=3, sticky="WE")

#Create a submit button
submit_button = tkinter.Button(bottom_frame, text="Submit", command=manage_action, font=("Georgia", 11, "bold"), bg='#2F8EA1', fg='#FFFFFF')
submit_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
root.bind('<Return>', lambda event:manage_action())

#Create an action feedback label
action_feedback = StringVar()

action_feedback_label = tkinter.Label(bottom_frame, textvariable=action_feedback, font=("Georgia", 12), bg='#000000', fg='#FFFFFF')
action_feedback_label.grid(row=7, column=0, columnspan=2)

#Create an allocated bonus message when accounts have more than $50 left in it
bonus_message = StringVar()

#Create a savings message when accounts have less than $50 left in it
savings_message = StringVar()

#Create and pack the bonus label
bonus_label = tkinter.Label(bottom_frame, textvariable=bonus_message, wraplength=1000, font=("Georgia", 12), bg='#000000', fg='#FFFFFF')
bonus_label.grid(row=10, column=0, columnspan=4, padx=100, pady=10)
##**********************************************************************************************************
#Run the mainloop
update_balance()
root.mainloop()
##**********************************************************************************************************
#Inputs from file to copy for trials 
#Nikau's Account, 300
#Hana's Account, 300
#Tia's Account, 300