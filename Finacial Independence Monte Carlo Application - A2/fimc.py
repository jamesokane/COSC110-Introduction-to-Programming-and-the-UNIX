#!/usr/bin/env python3

"""
The purpose of this application is to determine how ready an individual is for retirement
by determining their level of financial independnce over a period of time. The level of
independence is determined by implementing a Monte Carlo experiemnet and is based on the
individuals spending rate, inflation rate, current savings, interest rate, number of years,
infalation rate change and interest rate change.
"""

import random

# Prompts to be used throughout the program
# Prompt for annual cost of living
ANNUAL_PROMPT = "How much did you spend last year to support your current lifestyle? "

# Prompt for inflation rate
INFLATION_PROMPT = "Please enter the expected inflation rate: "

# Prompt for inflation rate change
INFLATION_CHANGE_PROMPT = "Please enter the expected maximum change for inflation in a given year: "

# Prompt for for current savings
SAVINGS_PROMPT = "How much do you currently have saved for investment? "

# Prompt for interest rate
INTEREST_RATE_PROMPT = "Please enter the base annual interest rate: "

# Prompt for interest rate change
INTREST_CHANGE_PROMPT = "Please enter the expected maximum change for interest in a given year: "

# Prompt for number of years to test for
YEAR_PROMPT = "How many years do you want to test? "

# Prompt for number of simulations to run
SIMULATIONS_PROMPT = "How many simulations do you want to run? "


def is_valid_non_negative_integer(request_prompt, error_prompt):
    """
    Presents the given request prompt to the user and reads in a non-negative integer value.
    If an invalid value is entered, the error_prompt is displayed and the process repeats.

    Arguments:
    request_prompt -- The prompt displayed to the user when asked to enter a non-negative integer
    error_prompt -- The prompt displayed to the user if they enter an invalid value

    Returns the non-negative integer value entered by the user, as an int
    """
    valid = False
    while not valid:
        value_string = input(request_prompt)
        try:
            value = int(value_string)
            if value < 0:
                print(error_prompt)
            else:
                valid = True
        except (ValueError):
            print(error_prompt)
    return value


def is_valid_positive_integer(request_prompt, error_prompt):
    """
    Presents the given request prompt to the user and reads in a positive integer value.
    If an invalid value is entered, the error_prompt is displayed and the process repeats.

    Arguments:
    request_prompt -- The prompt displayed to the user when asked to enter a positive integer
    error_prompt -- The prompt displayed to the user if they enter an invalid value

    Returns the positive integer value entered by the user, as an int
    """
    valid = False
    while not valid:
        value_string = input(request_prompt)
        try:
            value = int(value_string)
            if value <= 0:
                print(error_prompt)
            else:
                valid = True
        except (ValueError):
            print(error_prompt)
    return value


def is_valid_integer(request_prompt, error_prompt):
    """
    Presents the given request prompt to the user and reads in an integer value.
    If an invalid value is entered, the error_prompt is displayed and the process repeats.

    Arguments:
    request_prompt -- The prompt displayed to the user when asked to enter an integer
    error_prompt -- The prompt displayed to the user if they enter an invalid value

    Returns the integer value entered by the user, as an int
    """
    valid = False
    while not valid:
        value_string = input(request_prompt)
        try:
            value = int(value_string)
            valid = True
        except (ValueError):
            print(error_prompt)
    return value


def is_valid_float(request_prompt, error_prompt):
    """
    Presents the given request prompt to the user and reads in a real value.
    If an invalid value is entered, the error_prompt is displayed and the process repeats.

    Arguments:
    request_prompt -- The prompt displayed to the user when asked to enter a real
    error_prompt -- The prompt displayed to the user if they enter an invalid value

    Returns the real value entered by the user, as a float
    """
    valid = False
    while not valid:
        value_string = input(request_prompt)
        try:
            value = float(value_string)
            valid = True
        except (ValueError):
            print(error_prompt)
    return value


def modify_rate(rate, change):
    """
    Calculate a random value within change of the given rate

    Arguments:
    rate -- The initial rate to change from
    change -- The maximum amount to add or subtract from the rate

    Returns a random value within change of the given rate

    Explanation:
    random.random() calculates a random value between 0 and 1.
    Thus random.random() * 2 gives a value between 0 and 2,
    so 1 - random.random() * 2 gives a value between -1 and 1.
    Multiplying by change gives a value between -change and change,
    which is then added to the rate.
    """
    return rate + change * (1 - random.random() * 2)


def run_simulation(annual_spend, inflation_rate, savings_balance, interest_rate, num_years, inflation_change, interest_change):
    """
    Calculate the expeceted savings balance for each year within a given time range through the use of a
    Monte Carlo experiement.

    Arguments:
    annual_spend -- The amount the user spent last year to live at their current lifestyle
    inflation_rate -- The inflation rate at which the user's cost of living increases each year
    savings_balance -- The amount the user currently has saved for investment
    interest_rate -- The interest rate at which the user's savings grow each year
    num_years -- The number of years for which the simulation should be run
    inflation_change -- The maximum amount the inflation rate can change in a single year
    interest_change -- The maximum amount the interest rate can change in a single year

    Returns a list containing one entry for each year of the simulation.
    """
    balance_list = []
    for year in range(1, num_years+1):
        annual_spend += (inflation_rate * annual_spend)
        savings_balance = (savings_balance - annual_spend) * (1 + interest_rate)
        balance_list.append("{:.2f}".format(savings_balance))
        inflation_rate = modify_rate(inflation_rate, inflation_change)
        interest_rate = modify_rate(interest_rate, interest_change)
    return balance_list


def main():
    """
    Takes in financial information from financial prompts and writes the outputs from
    run_simulation() to a text file, output.txt.
    """
    annual_spend = is_valid_non_negative_integer(ANNUAL_PROMPT, "Please enter a non-negative integer")
    inflation_rate = is_valid_float(INFLATION_PROMPT, "Please enter a real number")
    inflation_change = is_valid_float(INFLATION_CHANGE_PROMPT, "Please enter a real number")
    savings_balance = is_valid_integer(SAVINGS_PROMPT, "Please enter an integer")
    interest_rate = is_valid_float(INTEREST_RATE_PROMPT, "Please enter a real number")
    interest_change = is_valid_float(INTREST_CHANGE_PROMPT, "Please enter a real number")
    num_years = is_valid_positive_integer(YEAR_PROMPT, "Please enter a positive integer")
    num_simulations = is_valid_positive_integer(SIMULATIONS_PROMPT, "Please enter a positive integer")

    success_count = 0
    # Opens output.txt file. If there is an existing output.txt it will be overwritten
    with open('output.txt', 'w') as f:
        for num in range(num_simulations):
            simulation = run_simulation(annual_spend, inflation_rate, savings_balance, interest_rate, num_years, inflation_change, interest_change)
            # The list from run_simulation() will be written to a line in output.txt
            f.write(' '.join(item for item in simulation))
            # Check if the final item in the simulation list is negative
            # If negative write "unsuccessful" to end of existing line and go to new line
            # Else write "successful" to end of existing line and go to new line
            if float(simulation[-1]) < 0:
                f.write(" unsuccessful\n")
            else:
                f.write(" successful\n")
                success_count += 1

    # Outputs final message stating number of successful simulations
    print("Simulation was successful in {}/{} runs ({}%)".format(success_count, num_simulations, (success_count/num_simulations)*100))


if __name__ == "__main__":
    main()
