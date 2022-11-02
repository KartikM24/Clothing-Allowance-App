##*********************************************** IMPORTS ***************************************************
from tkinter import *
from tkinter import ttk
##**********************************************************************************************************
#Create the Account class
class Account:
    #The Account class stores the details of each account and has methods to deposit and withdraw money from their account
    def __init__(self, name, balance):
        self.name = name
        self.balance = float(balance)
        account_list.append(self)
    
    #Deposit method adds money to balance
    def deposit(self, amount):
        if amount > 0.1:
            self.balance += amount
            return True
        else:
            return False

    #Withdraw method subtracts money from balance
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False
##******************************************  FUNCTIONS AND SETUP *****************************************
#Create a function to read data from the file
def get_data():
    account_file = open("clothing_allowance_app_file.txt","r")
    line_list = account_file.readlines()

    for line in line_list:
        account_data = line.strip().split(",")
        Account(*account_data)


    account_file.close()

#Create a function to get account names list
def create_name_list():
    name_list = []
    for account in account_list:
        name_list.append(account.name)
    return name_list
   
#Create a function that will update the balance.
def update_balance():
    balance_string = ""

    #Append each accounts balance to the specific account name
    for account in account_list:
        balance_string += "{}: ${:.2f} - ".format(account.name, account.balance)
    account_details.set(balance_string)

#Create the deposit function
def deposit_money(account):
    if account.deposit(amount.get()):
        action_feedback.set("Your transaction has been completed. Total of ${:.2f} has been deposited into {}".format(amount.get(), account.name))
    else:
        action_feedback.set("Please enter a positive number")

#Create the withdraw function
def withdraw_money(account):
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

        #Update the GUI
        update_balance()
        amount.set("")

    #Add an exception for text input
    except ValueError:
        action_feedback.set("Please enter a valid number")

#Set up Lists
account_list = []

#Create instances of the class
Nikaus_balance = Account("Nikau's Account", 300)
Hanas_balance = Account("Hana's Account", 300)
Tias_balance = Account("Tia's Account", 300)
account_names = create_name_list()
##******************************************** GUI CODE ***************************************************
root = Tk()
root.title("Clothing Allowance App")

#Create the top frame
top_frame = ttk.LabelFrame(root, text="Account Details")
top_frame.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

#Create and set the message text variable
message_text = StringVar()
message_text.set("Welcome! You can deposit or withdraw money from your account and check whether you will be allocated a bonus at the end of this year.")
#Create and pack the message label
message_label = ttk.Label(top_frame, textvariable=message_text, wraplength=250)
message_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

#Create and set the account details variable
account_details = StringVar()

#Create the details label and pack it into the GUI
details_label = ttk.Label(top_frame, textvariable=account_details)
details_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

#Create the bottom frame
bottom_frame = ttk.LabelFrame(root)
bottom_frame.grid(row=1, column=0, padx=10, pady=10, sticky="NSEW")

#Create a label for the account combobox
account_label = ttk.Label(bottom_frame, text="Account: ")
account_label.grid(row=3, column=0, padx=10, pady=3)

#Set up a variable and option list for the account Combobox
chosen_account = StringVar()
chosen_account.set(account_names[0])

#Create a Combobox to select the account
account_box = ttk.Combobox(bottom_frame, textvariable=chosen_account, state="readonly")
account_box['values'] = account_names
account_box.grid(row=3, column=1, padx=10, pady=3, sticky="WE")

#Create a label for the action Combobox
action_label = ttk.Label(bottom_frame, text="Action:")
action_label.grid(row=4, column=0)

#Set up a variable and option list for the action Combobox
action_list = ["Deposit", "Withdraw"]
chosen_action = StringVar()
chosen_action.set(action_list[0])

#Create the Combobox to select the action
action_box = ttk.Combobox(bottom_frame, textvariable=chosen_action, state="readonly")
action_box['values'] = action_list
action_box.grid(row=4, column=1, padx=10, pady=3, sticky="WE")

#Create a label for the amount field and pack it into the GUI
amount_label = ttk.Label(bottom_frame, text="Amount:")
amount_label.grid(row=5, column=0, padx=10, pady=3)

#Create a variable to store the amount
amount = DoubleVar()
amount.set("")

#Create an entry to type in amount
amount_entry = ttk.Entry(bottom_frame, textvariable=amount)
amount_entry.grid(row=5, column=1, padx=10, pady=3, sticky="WE")

#Create a submit button
submit_button = ttk.Button(bottom_frame, text="Submit", command=manage_action)
submit_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

#Create an action feedback label
action_feedback = StringVar()

action_feedback_label = ttk.Label(bottom_frame, textvariable=action_feedback)
action_feedback_label.grid(row=7, column=0, columnspan=2)

#Run the mainloop
update_balance()
root.mainloop()