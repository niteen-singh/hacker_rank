# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar as cal
m, d, y = map(int, input().split())
print(cal.day_name[cal.weekday(y, m, d)].upper())