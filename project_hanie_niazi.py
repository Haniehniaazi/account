'''
salam ostad :)
lotfan ba mehrabani va lotf va cheeshm pooshi tashih shavad :)
mersi <3

'''




#for reading an excel file
import pandas as pd

import csv

df = pd.read_csv('C:/Users/HI-TECH/Desktop/Users.csv')

#for buildung a window
from tkinter import *


#window details:
    
bank_acc = Tk()
bank_acc.title ('Account')
bank_acc.geometry('400x400')

#delete func:

def temp_text(e):
   u_entry.delete(0,"end")

# loging procces


    
def login():
    global balance 
    global i
    usern = u_entry.get()
    passw = p_entry.get()
    for username in df['username']:
        if ( usern == username ) :
            if passw == df.loc[df['username'] == usern, 'password'].iloc[0]:
                name = df.loc[df['username'] == usern, 'name'].iloc[0]  #find the given username in excel
                w_label = Label(bank_acc, text = f'welcome {name}', justify = 'center', font = ('AmericanTypewriter', 20))
                w_label.pack()
                w_label.place( x = 32, y = 110)
                switch()
                balance = df.loc[df['username'] == usern, 'balance'].iloc[0] # balance for the given username
                balance_entry.insert (0, balance )
                i = df['username'][df['username'] == usern].index[0] # user index
                return True
            
            else:
                w_label = Label(bank_acc, text = 'wrong username/password', font = ('AmericanTypewriter', 20))
                w_label.pack()
                w_label.place( x = 32, y = 110)


# when a user wants to make a deposit:
    
def deposit():
    global balance
    global i
    given_balance = int(deposit_entry.get())
    new_balance = int(balance) + given_balance
    balance_entry.delete(0,'end')
    balance_entry.insert (0, new_balance)
    balance = new_balance # update the balance variable
    df.loc[i, 'balance'] = balance #update the column in excel
    read_excel()
    
# when a user wants to make a withdraw :    
def withdrawal():
    global i
    global balance
    given_balance = int(withdrawal_entry.get())
    new_balance = int(balance) - given_balance
    
    if given_balance > int(balance):
        withdrawal_entry.delete(0,'end')
        withdrawal_entry.insert (0, 'low balance')
    else:
        balance_entry.delete(0,'end')
        balance_entry.insert (0, new_balance)
        balance = new_balance 
        df.loc[i,'balance'] = balance
        read_excel()
      
    
# apply the changes on excel file :    
def read_excel():
    df.to_csv('C:/Users/HI-TECH/Desktop/Users.csv')
        
    

    



                
#disable/enable the buttons and entries :
            
def switch():
    deposit_button.config(state = NORMAL)
    withdrawal_button.config(state = NORMAL)
    balance_entry.config(state = NORMAL)
    deposit_entry.config(state = NORMAL)
    withdrawal_entry.config(state = NORMAL)
    login_button.config(state = DISABLED)
    u_entry.config(state = DISABLED)
    p_entry.config(state = DISABLED)  
    
    
    
#Entries :

u_label = Label( bank_acc, text = 'Usename: ', font = ('AmericanTypewriter', 10))
u_label.place (x = 30, y = 4)
u_entry = Entry( bank_acc , bd = 4, justify = 'left', width = 14, font = ('AmericanTypewriter', 12), bg = 'grey')
u_entry.place (x = 30, y = 28)
u_entry.bind("<FocusIn>", temp_text)



p_entry = Entry( bank_acc, show = '*', bd = 4, justify = 'left', width = 14, font = ('AmericanTypewriter', 12), bg = 'grey')
p_entry.place (x = 230, y = 28)
p_label = Label( bank_acc, text = 'Password: ', font = ('AmericanTypewriter', 10))
p_label.place (x = 230, y = 4)



b_label = Label( bank_acc, text = 'Your Balance: ', font = ('AmericanTypewriter', 10))
b_label.place (x = 32, y = 185)
balance_entry = Entry( bank_acc, state = DISABLED,bd = 4, justify = 'center', width = 11, font = ('AmericanTypewriter', 40), bg = 'dark grey')
balance_entry.place (x = 32, y = 210)

deposit_entry = Entry( bank_acc, state = DISABLED, bd = 4, justify = 'left', width = 14, font = ('AmericanTypewriter', 16), bg = 'grey')
deposit_entry.place (x = 32, y = 290)



withdrawal_entry = Entry( bank_acc, state = DISABLED, bd = 4, justify = 'left', width = 14, font = ('AmericanTypewriter', 16), bg = 'grey')
withdrawal_entry.place (x = 32, y = 340)    
withdrawal_entry.bind("<FocusIn>", temp_text)

labelRight = Label(bank_acc, text="Created By Hanie Niazi", font=('Poppins bold', 7))
labelRight.place(x=10,y=376)


#buttons :
    
login_button = Button( bank_acc, command = login, bg = 'orange', text = 'Login', font = ('AmericanTypewriter', 12), justify = 'center', width = 13)
login_button.place( x = 135, y = 70)


deposit_button = Button( bank_acc, command = deposit, state = DISABLED, bg = 'orange', text = 'Make a Deposit', font = ('AmericanTypewriter', 10), justify = 'center', width = 13)
deposit_button.place( x = 230, y = 293)

withdrawal_button = Button( bank_acc, state = DISABLED, command = withdrawal, bg = 'orange', text = 'Make a withdraw', font = ('AmericanTypewriter', 10), justify = 'center', width = 13)
withdrawal_button.place( x = 230, y = 343)





bank_acc.mainloop()