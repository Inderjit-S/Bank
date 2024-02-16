
#1 see balance
#2 withdraw
#3 deposit
#4 quit 
#5 gamble add later
def main():
    balance = 0
    total = 0
    withdraw = 0
    deposit = 0
    # gonna have to create a for or while loop to continue this selection. Maybe while true and type 5 to quit
    print("Hello, welcome to the Chabank. Type the number for the action you would like to select: ")
    print("1. TOTAL BALANCE")
    print("2. WITHDRAW")
    print("3. DEPOSIT")
    print("4. EXIT")
    while True:
        #print("Hello, welcome to the Chabank. Type the number for the action you would like to select: ")
        #print("1. TOTAL BALANCE")
        #print("2. WITHDRAW")
        #print("3. DEPOSIT")
        #print("4. EXIT")
        choice = input()
        if choice == "1":
            print()
            print("Your total balance is: $", total)
            print()
        elif choice == "2":
            withdraw = input("Type the amount of money you would like to withdraw from your balance: ")
            if int(withdraw) > total:
                print("You cannot withdraw a greater amount than your balance. Try again") # maybe throw exception? How can we stay in the same screen to try again
                break
            elif int(withdraw) < total:
                total = balance - int(withdraw)
            print("You have withdrawn $", withdraw, "Your total balance is now: $", total)
            #withdraw
            # make case for if withdraw is not number value
        elif choice == "3":
            deposit = input("Type the amount of money you would like to deposit in your balance: ")
            total = balance + int(deposit)
            print("You have deposited $", deposit, "Your total balance is now $", total)
            #deposit
            # make case for if deposit is not number value
            # PROBLEM - BALANCE IS NOT BEING ADDED, total is just being replaced by deposit value.
        elif choice == "4":
            break
main()

# clean up total and balance variables. Think about what is actually happening
# create updating variable for total