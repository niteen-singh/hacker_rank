import re

n = int(input())

css = ""
for i in range(n):
    css += input()

rsection = r"{.*?}"
rhexcode = r"#[0-9A-Fa-f]{6}|#[0-9A-Fa-f]{3}"

sections = re.findall(rsection, css)

for s in sections:
    hexcodes = re.findall(rhexcode, s)
    for hc in hexcodes:
        print(hc)