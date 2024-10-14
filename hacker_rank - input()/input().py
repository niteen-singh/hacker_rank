# Enter your code here. Read input from STDIN. Print output to STDOUT
info = input()
x, y = info.split()
z = int(y)
data = input()

n = data.replace('x', str(x))
m = n.replace(" ", "")

o = eval(m)

if o == z:
    print("True")
else:
    print("False")