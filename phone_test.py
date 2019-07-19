import re

def extract_all_phones(input):
    phone_regex = re.compile(r"\b\d{2}\s\d{4}\s\d{4}\b")
    return phone_regex.findall(input) # search instead of find all for single input.

def is_valid_phone(input):
    phone_regex = re.compile(r"^\d{2}\s\d{4}\s\d{4}$")
    match = phone_regex.search(input)
    return True if match else False

print( extract_all_phones("My Number is 95 8281 4240 or call me at 88 0074 2105") )
print( extract_all_phones("My Number is 95 8281 424000 or call me at 1288 0074 2105") )

print( is_valid_phone("95 8281 4240") )
print( is_valid_phone("ads 95 8281 4240") )
print( is_valid_phone("95 8281 4240 ads") )

