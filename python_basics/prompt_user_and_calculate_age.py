__author__ = "Miranda"

def ask_age():
    age = input("How old are you? ")
    return int(age)

def calculate_seconds_from_years(age_years):
    return age_years * 365 * 24 * 3600

def prompt_user_and_calculate_age():
    age = ask_age()
    seconds_lived = calculate_seconds_from_years(age)
    print(f'You have lived {seconds_lived} seconds.')

prompt_user_and_calculate_age()