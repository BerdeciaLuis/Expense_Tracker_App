#Budget/Expense Tracker 

#This 'Application' is being use to learn and allow me to feel more comfortable using Python.
#Might have a readMe.txt to write my thought process and changes that I might add to the code.

#This will be the MAIN class for the 'application'

from budgetManager import budgetManager                            

manager = budgetManager()

while True:

    print("\n\nWelcome to the Expense/Budget Tracker What would you like to do?")
    print("1 = Setup Weekly Budget")
    print("2 = Enter an Expense")
    print("3 = View Current Weekly Budget")
    print("4 = Provide Report")
    print("5 = EXIT ")

    choice = input("\n\nPlease select one of the options above (1 - 5): ")

    if choice == "1":

        manager.Setup_budget()

    elif choice == "2":

        manager.enterExpense()
    
    elif choice == "3":

        manager.viewCurentBudget()

    elif choice == "4":

        print("\n\n")

    elif choice == "5":

        print("\n\nThank you for using our application. Goodbye!")
        break

    else:

        print("\n\nInvalid Input. Please try again!")

    
