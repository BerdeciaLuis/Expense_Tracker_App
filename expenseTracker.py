#Budget/Expense Tracker 
categories = []

class Category:

    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        self.expenses = []

    
    def remaining_budget(self):
        return self.budget - self.total_expenses()
    
    def add_expense(self, amount, description=""):
        self.expenses.append((amount, description))

    def total_expenses(self):
        return sum(amount for amount, _ in self.expenses)
    
    def __str__(self):
        return f"Category: {self.name}, Budget: {self.budget}, Spent: {self.total_expenses()}, Remaining: {self.remaining_budget()}"



def Setup_budget():
    
    totalRemainingBudget = 0
    budgetForWeek = 0.00

    print("\n\nWhich type of weekly budget would you like to setup: ")
    print("1 = Detailed Weekly Budget")
    print("2 = Simple Weekly Budget")

    answer = input("\n\nPlease select one of the options above (1 - 2): ")

    if answer == "1":       
        
        name = input("Enter the category name: ")
        budget = float(input("Enter budget for this category: "))
        budgetForWeek += budget
        print(budgetForWeek)
        new_category = Category(name, budget)
        categories.append(new_category)

        while True:

            cont = input("\n\nWould you like to continue to enter categories? (Y/N): ")

            if cont == "N" or cont == "n":
                break

            elif cont == "Y" or cont == "y" :
                
                name = input("Enter the category name: ")
                budget = float(input("Enter budget for this category: "))
                budgetForWeek += budget
                print(budgetForWeek)
                new_category = Category(name, budget)
                categories.append(new_category)     
            
            else:  
                print("\n\nInvalid Input. Please try again!")


        print("\n\n")
        print("\nExpense Tracker For Week of \n")
        print(f"{'Category':<15}{'Budget':<10}{'Spent':<10}{'Remaining':<10}")
        print("-" * 45)

        for category in categories:
            print(f"{category.name:<15}{category.budget:<10}{category.total_expenses():<10}{category.remaining_budget():<10}")
            totalRemainingBudget += category.remaining_budget()

        print("-" * 45)
        print(f"{'TOTAL':<15}{budgetForWeek:<10}{budgetForWeek-totalRemainingBudget:<10}{totalRemainingBudget:<10}")

       
  
    elif answer == "2":

        budget = float(input("Please enter the amount you would like to setup for this week's budget: "))
        print("The Budget you have allocated for this week is: ", budget)

    else: 

        print("\n\nInvalid Input. Please try again!")



while True:

    print("\n\nWelcome to the Expense/Budget Tracker What would you like to do?")
    print("1 = Setup Weekly Budget")
    print("2 = Enter an Expense")
    print("3 = View Current Weekly Budget")
    print("4 = Provide Report")
    print("5 = EXIT ")

    choice = input("\n\nPlease select one of the options above (1 - 4): ")

    if choice == "1":

        Setup_budget()

    elif choice == "2":

        print()
    
    elif choice == "3":

        if not categories:
            print("\nNo budget had been set yet.")
            continue

        

        print()


    elif choice == "4":

        print("\n\n")

    elif choice == "5":

        print("\n\nThank you for using our application. Goodbye!")
        break

    else:

        print("\n\nInvalid Input. Please try again!")
