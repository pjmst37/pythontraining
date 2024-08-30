# Password validator
# At least 8 characters long
# Contain any sort of letters, numbers and '$' '% '#' '@'

import re

pwd_regex = r"[A-Za-z0-9@#$%]{8,}\d"
pattern = re.compile(pwd_regex)


while True:
    user_pwd = input('Please enter password for validation: ')

    if not pattern.match(user_pwd).find():
        print('Sorry, there were characters not allowed in that password')
    else:
        print('Thanks, that\'s a great password!')
        break
