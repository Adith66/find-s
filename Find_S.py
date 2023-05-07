import csv
with open("hello.csv") as csv_file:
    csvread=csv.reader(csv_file,delimiter=',')
    x=[];y=[];z=[];s=[]
    print('the training dataset is:')
    for row in csvread:
        x.append(row)
        print(row)
    if x[0][-1].upper()!='YES'and'NO':
        x.remove(x[0])
    print('the positive examples are:')
    for i in range(len(x)):
        if x[i][-1].upper()=='YES':
            z.append(x[i])
            print(x[i])
    y=z
    for i in range(len(y)):
        y[i].remove(y[i][-1])
    print('the steps in algorithm are:')
    for i in y:
        for j in range(len(i)):
            if s==[]:
                s=['%']*len(i)
                print(s)
                s=y[0]
            elif s[j]!=i[j]:
                s[j]='?'
        print(s)
    print('the most specific hypothesis is:',s)
