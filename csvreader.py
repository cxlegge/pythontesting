import pandas as pd

pand = pd.read_csv('domains.csv', index_col=0)
pand1 = pand.iloc[:,5]
# where 5 is the target column
newlist = []

for i in pand1:
    if type(i) == str:
        newlist.append(i)
# ^ removes empty cells

newlist =  sorted(newlist)

print(newlist)

groups = []

for i in newlist:
    if i not in groups:
        groups.append(i)
for v in groups:
    print(v, newlist.count(v))
