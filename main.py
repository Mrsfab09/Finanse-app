from termcolor import colored, cprint

error = lambda x: cprint(x, "red", attrs=["bold"])
expenses = []


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


while True:
    print()
    month = int(input("Enter month [1-12]: "))
    if month == 0:
        break
    while True:
        print()
        print("[0] Exit")
        print("[1] View all expenses")
        print("[2] Add expense")
        print()
        choice = int(input("Select options: "))

        if choice == 0:
            break

        if choice == 1:
            show_expenses(month)

        if choice == 2:
            add_expense(month)
