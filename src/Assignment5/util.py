def  final(string,k):
    temp=[]
    len_temp=0
    for i in string:
        len_temp +=1
        if i not in temp:
            temp.append(i)
        if len_temp==k:
            res= ''.join(temp)
            print(res)
            temp=[]
            len_temp=0