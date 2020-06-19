n=2
pow=1


for i in range(0,1000):
    pow=pow*2


sum=0

while(pow>=10):
    a=pow%10
    sum+=a

    pow=pow//10
sum+=pow

print(sum)
