#!/usr/bin/env python


"""
The purpose of this application is to determine how ready an individual is for
retirement by determining their level of financial independence over a period
of time.
"""


def is_valid_positive_integer_input(value):
    """
    Returns True if an input value is a postive integer.
    """
    # Checks if value is not a subclass of str or int.
    if not isinstance(value, (str, int)):
        return False
    try:
        value = int(value)
    except (TypeError, ValueError):
        return False
    # Returns True if value is an integer and greater than 0.
    return value > 0


def is_valid_float_input(value):
    """
    Returns True if an input value is a float.
    """
    # Checks if value is not a subclass of str or float.
    if not isinstance(value, (str, float)):
        return False
    try:
        value = float(value)
    except (TypeError, ValueError):
        return False
    # Returns True if the value is a float
    return value


def is_valid_integer_input(value):
    """
    Returns True if an input value is an integer.
    """
    # Checks if value is not a subclass of str or int.
    if not isinstance(value, (str, int)):
        return False
    try:
        value = int(value)
    except (TypeError, ValueError):
        return False
    # Returns True if value is an integer.
    return value


def test_years(amount_last_year, inflation_rate, current_savings, annual_interest_rate, num_year):
    """
    Outputs the expected savings balance for each year in the test range, and advises
    whether an individual is `Financially independent` or `Not financially independent`.

    Takes the `num_year` and loops through this number of times, firstly
    calculating the annual spending amount for that year by multupling the
    `inflation_rate` by the `amount_last_year` and adding this back to the
    `amount_last_year`. The `amount_last_year` is then subtracted from the
    `current_savings`, and finally this is multipled by (1 + `interest_rate`).

    The year number and `current_savings` amount are printed for each year in the loop.
    If the loop is able to be completed without the `current_savings` amount becoming
    negative than `Financially Independent` is printed, however if `current_savings`
    becomes negative at any point the loop stops and "Not financially independent" is
    printed.

    Keyword arguments:
    amount_last_year -- A non-negative integer
    inflation_rate -- A decimal number
    current_savings -- An integer
    annual_interest_rate -- A decimal number
    num_year -- A positive integer
    """
    for year in range(1, num_year+1):
        amount_last_year += (inflation_rate * amount_last_year)
        current_savings = (current_savings - amount_last_year) * (1 + annual_interest_rate)
        # The print result will be aligned to the right by 4 spaces,
        # and the current_savings value will be set to 2 decimal places.
        print('{:>4}'.format(year), " $"+"%.2f" % current_savings)
        if current_savings < 0:
            print("Not financially independent")
            break
    else:
        print("Financially independent")


def main():
    """
    Takes inputs for `amount_last_year`, `inflation_rate`, `current_savings`,
    `annual_interest_rate` and `num_year` and uses them as keyword arguements
    for test_years().
    """
    amount_last_year = input("How much did you spend last year to support your current lifestyle? ")
    # Will continue to loop through until is_valid_positive_integer_input(amount_last_year) is True.
    while not is_valid_positive_integer_input(amount_last_year):
        print("Please enter a non-negative whole number")
        amount_last_year = input("How much did you spend last year to support your current lifestyle? ")
    amount_last_year = int(amount_last_year)

    inflation_rate = input("Please enter the expected inflation rate as a decimal number(e.g. 5% = 0.05): ")
    # Will continue to loop through until is_valid_float_input(inflation_rate) is True.
    while not is_valid_float_input(inflation_rate):
        print("Please enter an amount that is a decimal number")
        inflation_rate = input("Please enter the expected inflation rate as a decimal number(e.g. 5% = 0.05): ")
    inflation_rate = float(inflation_rate)

    current_savings = input("How much do you currently have saved for investment? ")
    # Will continue to loop through until is_valid_integer_input(current_savings) is True.
    while not is_valid_integer_input(current_savings):
        print("Please enter a whole number")
        current_savings = input("How much do you currently have saved for investment? ")
    current_savings = int(current_savings)

    annual_interest_rate = input("Please enter the expected interest rate as a decimal number(e.g. 3% = 0.03): ")
    # Will continue to loop through until is_valid_float_input(annual_interest_rate) is True.
    while not is_valid_float_input(annual_interest_rate):
        print("Please enter an amount that is a decimal number")
        annual_interest_rate = input("Please enter the expected interest rate as a decimal number(e.g. 3% = 0.03): ")
    annual_interest_rate = float(annual_interest_rate)

    num_year = input("How many years do you want to test? ")
    # Will continue to loop through until is_valid_positive_integer_input(num_year) is True.
    while not is_valid_positive_integer_input(num_year):
        print("Please enter a non-negative whole number")
        num_year = input("How many years do you want to test? ")
    num_year = int(num_year)

    # Prints out table headings
    print("Year", " Remaining balance")

    test_years(amount_last_year, inflation_rate, current_savings, annual_interest_rate, num_year)


if __name__ == "__main__":
    main()
