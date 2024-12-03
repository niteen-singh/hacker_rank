import re
import email.utils

valid_email = r"^\<[a-zA-Z][\w\.\-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}\>$"

for _ in range(int(input())):
    name_email = input()
    if re.match(valid_email, name_email.split()[1]):
        print(email.utils.formataddr(email.utils.parseaddr(name_email)))