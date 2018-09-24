import pandas as pd
# reads csv file column data, prompts user to input which column
print('Please enter the target column of your csv file you wish to count.')
title = input('Column title: ')

try:
  pand = pd.read_csv('domains.csv', index_col=0)
  pand1 = pand.loc[:,title]
except:
    print('Something went wrong, either your column name is incorrect or out of range, did you check the spelling?')
newlist = []
nullacc = 0
for i in pand1:
    if type(i) == str:
        newlist.append(i)
        # only adds non-empty cells
    else:
        nullcount +=1
        # counts empty cells
newlist =  sorted(newlist)

print(newlist)
# optional print statement for the column's data
groups = []

for i in newlist:
    if i not in groups:
        groups.append(i)
for v in groups:
    print(v, newlist.count(v))

print('There are %s missing %s values.' % (nullcount, title))
