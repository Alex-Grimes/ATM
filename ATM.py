import sys

#account balance
account_balance = float(500.25)

# functions that will be called based on user input
def print_balance():
  print ('Your current balance:')
  print(account_balance)

def deposit_amount():
  userchoice = float(input ('How much would you like to deposit today?\n'))
  new_balance = float(account_balance) + float(userchoice)
  statment = ('Deposit was ${:.2f}, current balance is ${}')
  print(statment.format(userchoice, new_balance))

def withdrawl():
  withdrawl_amount = float(input ('How much would you like to withdraw today?\n'))
  if withdrawl_amount > account_balance:
    error = ('${:.2f} is greater than your account balance of ${}')
    print(error.format(withdrawl_amount, account_balance))
  else:
    new_balance = float(account_balance) - float(withdrawl_amount)
    statment = ('Withdrawal amount was ${:.2f}, current balance is ${}')
    print(statment.format(withdrawl_amount, new_balance))

# function designed to allow the user to quit out with Q
def quit():
  print('Thank you for banking with us.')

# prompt for the users choice and run the corrosponding function
userchoice = input ("What would you like to do?\n")

if (userchoice == 'D'):
    deposit_amount ()
elif (userchoice == 'B'):
  print_balance()
elif (userchoice == 'W'):
  withdrawl()
elif (userchoice == 'Q'):
  quit()
