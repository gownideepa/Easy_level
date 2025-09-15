nums=int(input('Enter a number:'))
sum=0 
while nums!=0:
    digit=int(nums%10)
    sum=sum+digit
    nums=nums/10
print('sum is',sum)
