f=open("data_Q-13.txt")
list1=f.readlines()
f.close()
# print(list1)

sum=0

for item in list1:
    sum+=int(item)
# print(sum)
n=sum

while(n>10000000000):
    n=n//10

print(n)