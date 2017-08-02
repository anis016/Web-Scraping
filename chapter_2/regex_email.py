import re

st = "anis.cuet016@gmail.com"

first_part  = "[A-Za-z0-9\._+]+"
second_part = "@"
third_part  = "[A-Za-z]+"
forth_part  = "\."
fifth_part  = "com|edu|org|net"

part = [first_part, second_part, third_part, forth_part, fifth_part]

sep = ""
email_regex = sep.join(part)
# print(email_regex)

result = re.match(email_regex, st)
print(result)