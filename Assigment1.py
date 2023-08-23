import re
#libaray regilar expression


# boolean function to check validity of number

def validate_contact_number(num):
    # Regular expression pattern to match valid contact numbers
    # ^ ->represents starting with ->(\+?\d{1,3}[-.\s]?) =>used to match coutry code which is optional
    #  (\(?\d{1,3}\)  =>optonal area code enclosed in ()
     # d{3,4}[-.\s]?\d{4} =>to check main part of number
    # $ => end of string, checking pattern matching to end of string

    pattern = r'^(\+?\d{1,3}[-.\s]?)?(\(?\d{1,3}\)?[-.\s]?)?\d{3,4}[-.\s]?\d{4}$'
    
    if re.match(pattern, num):
        return True
    else:
        return False



# Test cases list
numbers = [
    "2124567890",
    "212-456-7890",
    "(212)456-7890",
    "(212)-456-7890",
    "212.456.7890",
    "212 456 7890",
    "+12124567890",
    "+1 212.456.7890",
    "+212-456-7890",
    "1-212-456-7890",
    "++666-15611-9514",
    "*665-05-15155"
]


for num in numbers:
    if validate_contact_number(num):
        print(f"{num} is a valid contact number.")
    else:
        print(f"{num} is an invalid contact number.")
