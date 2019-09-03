#Gary Machorro
#8/8/17
#Lab4 Report Grades
valid = False
count=0
while not valid and count<3:
    count+=1
    score=int(input("Enter a score:"))
    if score >= 0 and score <=100:
        valid=True
        if score>=0 and score<=59:
           print("F")
           print("Thank you for using this program!")
        elif score>=60 and score<=69:
            print("D")
            print("Thank you for using this program!")
        elif score>=70 and score<=79:
            print("C")
            print("Thank you for using this program!")
        elif score>=80 and score<=89:
            print("B")
            print("Thank you for using this program!")
        elif score>=90 and score<=100:
            print("A")
            print("Thank you for using this program!")   
    else:
        print("Invalid input, try again")
    if count==3:
        print("program will close")


#OUTPUT
'''
>>> ================================ RESTART ================================
>>> 
Enter a score:122
Invalid input, try again
Enter a score:1000
Invalid input, try again
Enter a score:132
Invalid input, try again
program will close
>>> ================================ RESTART ================================
>>> 
Enter a score:-1
Invalid input, try again
Enter a score:0
F
Thank you for using this program!
>>> ================================ RESTART ================================
>>> 
Enter a score:50
F
Thank you for using this program!
>>> ================================ RESTART ================================
>>> 
Enter a score:60
D
Thank you for using this program!
>>> ================================ RESTART ================================
>>> 
Enter a score:69
D
Thank you for using this program!
>>> ================================ RESTART ================================
>>> 
Enter a score:70
C
Thank you for using this program!
>>> ================================ RESTART ================================
>>> 
Enter a score:80
B
Thank you for using this program!
>>> ================================ RESTART ================================
>>> 
Enter a score:90
A
Thank you for using this program!
>>> ================================ RESTART ================================
>>> 
Enter a score:100
A
Thank you for using this program!
>>> 
'''
