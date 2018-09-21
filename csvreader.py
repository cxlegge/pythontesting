import pandas as pd

pand = pd.read_csv('domains.csv', index_col=0)
pand1 = pand.iloc[:,5]

newlist = []

for i in pand1:
    if type(i) == str:
        newlist.append(i)

newlist =  sorted(newlist, key=lambda x: x)

print(newlist)

groups = []

for i in newlist:
    if i not in groups:
        groups.append(i)
print(groups)
for v in groups:
    print(v, newlist.count(v))
