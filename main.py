from termcolor import colored, cprint

error = lambda x: cprint(x, "red", attrs=["bold"])
menu = colored("[ Menu ]", "cyan", attrs=["bold"])

# Menu
menu_exit = colored("[0] Exit", "red", attrs=["bold"])
menu_all_expenses = colored("[1] View all expenses", "green", attrs=["bold"])
menu_add = colored("[2] Add expense", "yellow", attrs=["bold"])
menu_stats = colored("[3] Statistics", "blue", attrs=["bold"])

Finanse_App = colored("[ Finanse App ]", "magenta", attrs=["bold"])

expenses = []

# Dictionary of months
months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12,
}

# Functions


def show_expenses(month):
    for expense_amoumnt, expense_type, expense_month in expenses:
        if expense_month == month:
            print(
                f"{colored(expense_type, 'green')}: {colored(expense_amoumnt, 'green')}"
            )


def add_expense(month):
    print()
    expense_amount = int(input("Enter expense amount [zł]: "))
    expense_type = input("Enter the type of expense(jedzenie, rozrywka, dom, inny): ")

    expense = (expense_amount, expense_type, month)
    expenses.append(expense)


def show_stats(month):
    total_amount_month = sum(
        expense_amount
        for expense_amount, _, expense_month in expenses
        if expense_month == month
    )
    total_amount_all = sum(expense_amount for expense_amount, _, _ in expenses)
    number_of_expeneses_this_month = sum(1 for _, _, expense_month in expenses)
    average_expense_month = total_amount_month / number_of_expeneses_this_month
    average_expense_all = total_amount_all / len(expenses)
    print()
    print(colored("[ Statistics ]", "blue", attrs=["bold"]))
    print()
    print(
        f"Total amount of {colored(month, 'green')} expenses: {colored(total_amount_month, 'green')}"
    )
    print(f"Average spend this month: ", average_expense_month)
    print("All expenses: ", total_amount_all)
    print("Average expenses: ", average_expense_all)
    print()


################################

while True:
    print()
    print(Finanse_App)
    print()
    month = int(input("Enter month [1-12]: "))
    if month == 0:
        break
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
