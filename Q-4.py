def isPalin(n):
    list1=[]
    while(n>10):
        a=n%10
        list1.append(a)
        n=n//10
    list1.append(n)
    i=0
    j=len(list1)-1
    while(i<j):
        if(list1[i]!=list1[j]):
            return -1
        i+=1
        j-=1
    return 1


def find():
    list1=[]
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            if (isPalin(i * j) == 1):
                list1.append(i*j)
    return max(list1)

print(find())