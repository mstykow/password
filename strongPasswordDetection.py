#! python3
# Program checks if a password is strong according to four criteria.

import re

check1Regex = re.compile(r'[^\n\s]{8,}')    # checks for 8+ letters
check2Regex = re.compile(r'.*\d.*')         # checks has at least one digit
check3Regex = re.compile(r'.*[a-z].*')      # checks has at least one lower case character
check4Regex = re.compile(r'.*[A-Z].*')      # checks has at least one upper case character

passwords = ['ImY0urFavorIte','ImY0urF','imy0urfavorite','IMY0URFAVORITE']

def passwordStrength(pw):
    mo1 = check1Regex.search(pw)
    mo2 = check2Regex.search(pw)
    mo3 = check3Regex.search(pw)
    mo4 = check4Regex.search(pw)
    if mo1 == None or mo2 == None or mo3 == None or mo4 == None:
        return 'weak.'
    else:
        return 'strong.'

for i in passwords:
    print('Password ' + i + ' is ' + passwordStrength(i))