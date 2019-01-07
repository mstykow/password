#! python3
# Program checks if a password is strong according to four criteria.

import re

checkRegex = [
    re.compile(r'[^\n\s]{8,}'),    # checks for 8+ letters
    re.compile(r'\d'),             # checks has at least one digit
    re.compile(r'.*[a-z].*'),      # checks has at least one lower case character
    re.compile(r'.*[A-Z].*')       # checks has at least one upper case character
]

def check_password_strength(pw):
    for condition in checkRegex:
        mo = condition.search(pw)
        if mo == None:
            ans = 'weak'
            break
        else:
            ans = 'strong'
    return ans
