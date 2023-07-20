from termcolor import colored, cprint
from expenses_functions import show_expenses, add_expense, show_stats

error = lambda x: cprint(x, "red", attrs=["bold"])
menu = colored("[ Menu ]", "cyan", attrs=["bold"])

# Menu
menu_exit = colored("[0] Exit", "red", attrs=["bold"])
menu_all_expenses = colored("[1] View all expenses", "green", attrs=["bold"])
menu_add = colored("[2] Add expense", "yellow", attrs=["bold"])
menu_stats = colored("[3] Statistics", "blue", attrs=["bold"])

# Logo
Finanse_App = colored("[ Finanse App ]", "magenta", attrs=["bold"])


while True:
    print()
    print(Finanse_App)
    print()
    while True:
        try:
            month = int(input("Enter month [1 - 12]: "))
            if 1 <= month <= 12:
                break
            else:
                error("Invalid month. Please enter a number from 1 to 12.")
                print()
        except ValueError:
            error("Invalid input. Please enter a number.")
            print()
    while True:
        print()
        print(menu)
        print()
        print(menu_exit)
        print(menu_all_expenses)
        print(menu_add)
        print(menu_stats)
        print()
        choice = int(input("Select options: "))

        if choice == 0:
            break

        if choice == 1:
            show_expenses(month)

        if choice == 2:
            add_expense(month)

        if choice == 3:
            show_stats(month)
