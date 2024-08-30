import re


email_regex = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
string = 'search this inside of this text please! George'
pattern = re.compile(r"([a-zA-Z]).([a])")

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string)

print(a.span())
print(a.start())
print(a.end())
print(a.group())
print(a.groups())

print(b)
print(c)
print(d.group())
