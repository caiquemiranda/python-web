__author__ = "Miranda"

def age_program():
    use_age = input('Enter your age: ')
    age_seconds = int(use_age) * 365 * 24 * 60 * 60

    print(f'You age in seconds is: {age_seconds}')
    
age_program()