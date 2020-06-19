def amicable(n):
    list1=[]
    for i in range(1,n):
        if(n%i==0):
            list1.append(i)
    sum=0
    for i in list1:
        sum+=i
    n1=sum
    list2=[]
    for i in range(1,n1):
        if(n1%i==0):
            list2.append(i)
    sum1=0
    for i in list2:
        sum1+=i
    if(sum1==n and n1!=n):
        return True

list=[]
for i in range(1,10000):
    if(amicable(i)==True):
        list.append(i)
sum=0
for i in list:
    sum+=i
print(sum)
print(list)
