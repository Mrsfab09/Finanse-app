from termcolor import colored, cprint

expenses = []

# Colors
error = lambda x: cprint(x, "red", attrs=["bold"])
green = lambda x: cprint(x, "green")
dark_grey = lambda x: cprint(x, "dark_grey")

# Dictionary of months
months = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}

# Dictionary of category types
category = {
    "food": "Food",
    "house": "house",
    "phones": "Phones",
    "entertainment": "entertainment",
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
    selected_month = months.get(month)

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
    print(
        colored("[ Statistics ]", "blue", attrs=["bold"]),
        "-",
        colored("[", "green"),
        colored(selected_month, "green"),
        colored("]", "green"),
    )
    print()
    print(
        colored(f"Total spend amount: ", "dark_grey"),
        colored(total_amount_month, "green"),
        colored("zł", "green"),
    )
    print(f"Average spend this month: ", round(average_expense_month, 2))
    print(
        colored("All expenses: ", "dark_grey"),
        colored(total_amount_all, "green"),
        colored("zł", "green"),
    )
    print("Average expenses: ", round(average_expense_all, 2))
    print()


####################
