##*********************************************** IMPORTS ***************************************************
from tkinter import *
from tkinter import ttk
##***********************************************************************************************************
#Create a variable to store the account balance
Nikaus_balance = 300
Hanas_balance = 300
Tias_balance = 300
##**************************************** FUNCTIONS AND SETUP **********************************************
#Create a function that will update the balance.
def update_balance():
    global Nikaus_balance, Hanas_balance, Tias_balance
    account = chosen_account.get()
    mode = chosen_action.get()

    if account == "Nikau":
        if mode == "Deposit":
            Nikaus_balance += amount.get()
        else:
            Nikaus_balance -= amount.get()

    elif account == "Hana":
        if mode == "Deposit":
            Hanas_balance += amount.get()
        else:
            Hanas_balance -= amount.get()

    elif account == "Tia":
        if mode == "Deposit":
            Tias_balance += amount.get()
        else:
            Tias_balance -= amount.get()
    balance_string = "Nikau's Account: ${}\nHana's Account: ${}\nTia's Account: ${}".format(Nikaus_balance.balance, Hanas_balance.balance, Tias_balance.balance)
    account_details.set(balance_string)
##******************************************** GUI CODE ***************************************************
root = Tk()
root.title("Clothing Allowance App")

#Create the top frame
top_frame = ttk.LabelFrame(root, text="Clothing Allowance Account Details")
top_frame.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

#Create and set the message text variable
message_text = StringVar()
message_text.set("Welcome! You can deposit or withdraw money from your account and check whether you will be allocated a bonus at the end of this year.")

#Create and pack the message label
message_label = ttk.Label(top_frame, textvariable=message_text, wraplength=250)
message_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

#Create and set the account details variable
account_details = StringVar()
account_details.set("Nikaus's Account: $300 \nHana's Account: $300\nTia's Account: $300")

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
account_names = ["Nikau", "Hana", "Tia"]
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
amount_entry = ""

#Create a submit button
submit_button = ttk.Button(bottom_frame, text="Submit", command=update_balance)
submit_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

#Run the mainloop
root.mainloop()

