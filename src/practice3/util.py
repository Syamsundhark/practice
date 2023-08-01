def li(*num):
    lis=[]
    for i in num:
        lis.append(i)
    max=lis[0]
    min=lis[0]
    for i in range(len(lis)):
        if(lis[i]>max):
            max=lis[i]
    print("Maximum number is",max)
    for i in range(len(lis)):
        if(lis[i]<min):
            min=lis[i]
    print("Minimun number is ",min)