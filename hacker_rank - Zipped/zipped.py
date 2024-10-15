# Enter your code here. Read input from STDIN. Print output to STDOUT

n, s =(input()).split()
res=[]
for _ in range(int(s)):
    x=list(map(float, input().split()))
    res.append(x)
tup=(list(zip(*res)))
for i in tup:
    print(sum(i)/float(s))