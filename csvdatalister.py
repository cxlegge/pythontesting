import pandas as pd

aread = pd.read_csv('data.csv', index_col=0)
#input target columns in the list below
targetcols = ['column1','column2']
f = open('dataset.txt', 'w+')
#begins column looping, writes title of column to file, bounded by 20 dashes
for targetcol in targetcols:
    list1 = list((aread.loc[:,targetcol]))
    f.write(('-'*20) + '\n' + targetcol + ' total: ' + str(len(list1)) + '\n' + ('-'*20) + '\n')
    #creates holding list('group') for transfer to file
    groups = []
    #adds unique, non-NaN values to the 'groups' list
    for i in list1:
        if i not in groups and str(i) != 'nan':
            groups.append(i)
    #writes the number of items in the column, indexed by item in holding list('group'), then writes group item name
    for v in groups:
        f.write(str(list1.count(v)))
        f.write(' '+str(v)+'\n')
