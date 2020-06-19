def check(n):
    count=0
    while(n>10):
        n=n//10
        count+=1
    count+=1
    if(count==1000):
        return 1


def fibonacci(n):
    list1=[0]*(n+1)
    list1[0]=0
    list1[1]=1
    list1[2]=1
    for i in range(3,n+1):
        list1[i]=list1[i-1]+list1[i-2]
        if(check(list1[i])==1):
            return i-1





n=5000

print(fibonacci(n))