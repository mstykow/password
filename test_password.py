#! python3
# Test file for password function.

from password import check_password_strength

passwords = ['ImY0urFavorIte','ImYourFavorIte','ImY0urF','imy0urfavorite','IMY0URFAVORITE']

assert check_password_strength(passwords[0]) == 'strong', 'Function evaluated incorrectly.'
for password in passwords[1:]:
    assert check_password_strength(password) == 'weak', 'Function evaluated "' + password + '" incorrectly.'
