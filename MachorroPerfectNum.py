#Gary Machorro
#8/13/17
#Perfect number, project 2, problem 2
num=int(input("Enter a number:"))
sum=0
for x in range(1,num):
    if num%x==0:
        sum=sum+x
if sum==num:
    print(num,"is a perfect number")
else:
    print(num,"is not a perfect number")
#OUTPUTS
'''
=========== RESTART: ===========
Enter a number:6
6 is a perfect number
>>> 
=========== RESTART: ===========
Enter a number:28
28 is a perfect number
>>> 
=========== RESTART: ===========
Enter a number:325
325 is not a perfect number
>>> 
=========== RESTART: ===========
Enter a number:496
496 is a perfect number
>>> 
'''
