S = input()
R = []
R.extend(sorted(x for x in S if x.islower()))
R.extend(sorted(x for x in S if x.isupper()))
R.extend(sorted(x for x in S if x.isnumeric() and int(x) % 2 == 1))
R.extend(sorted(x for x in S if x.isnumeric() and int(x) % 2 == 0))
print(''.join(R))