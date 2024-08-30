import re

email_pattern = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
pattern = re.compile(rf'{email_pattern}')

email1 = 'b@b.com'

a = pattern.search(email1)
print(a.group())
