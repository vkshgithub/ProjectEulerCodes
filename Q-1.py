def solve(n):
    list1=[]
    for i in range(0,n):
        if(i%3==0 or i%5==0):
            list1.append(i)
    sum=0
    for i in list1:
        sum+=i
    return sum

n=1000
print(solve(n))