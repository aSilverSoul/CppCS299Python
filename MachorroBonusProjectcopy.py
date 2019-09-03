#Gary Machorro
#8/27/17
#Bonus Project :barcodes

import turtle
strDigits=[]
digits=[]
newDigits=[]
encodings=[[1, 1, 0, 0, 0],   # encoding for '0'
         [0, 0, 0, 1, 1],   # encoding for '1'
         [0, 0, 1, 0, 1],   # encoding for '2'
         [0, 0, 1, 1, 0],   # encoding for '3'
         [0, 1, 0, 0, 1],   # encoding for '4'
         [0, 1, 0, 1, 0],   # encoding for '5'
         [0, 1, 1, 0, 0],   # encoding for '6'
         [1, 0, 0, 0, 1],   # encoding for '7'
         [1, 0, 0, 1, 0],   # encoding for '8'
         [1, 0, 1, 0, 0]    # encoding for '9'
        ]
## gets the check digit
# @return the check digit
# @param the list of digits
#
def compute_check_digit(digits):

    sum = 0
    for i in range(len(digits)):
        sum = sum + digits[i]
    check_digit = 10 - (sum % 10)
    if (check_digit == 10):
        check_digit = 0
    return check_digit

## draws the barcodes
# @param turtle graphics and the list of digits with the check digit
#
def draw_bar(turtle, newDigits):
    turtle.left(90)
    turtle.forward(50)
    turtle.up()
    turtle.backward(50)
    turtle.right(90)
    turtle.forward(10)
    turtle.down()
    for i in range(len(newDigits)):
        for j in range(len(encodings[i])):
            digits=encodings[newDigits[i]][j]
            if digits==1:
                turtle.left(90)
                turtle.forward(50)
                turtle.up()
                turtle.backward(50)
                turtle.right(90)
                turtle.forward(10)
                turtle.down()
            elif digits==0:
                turtle.left(90)
                turtle.forward(25)
                turtle.up()
                turtle.backward(25)
                turtle.right(90)
                turtle.forward(10)
                turtle.down()
    turtle.left(90)
    turtle.forward(50)
    turtle.up()
    turtle.backward(50)
    turtle.right(90)
    turtle.forward(10)
    turtle.down()
    
## gets input and makes it into a list and then removes the hyphen
#         
def main():
    inputZip=input("enter zip:")
    enteredDigits=list(inputZip)
    for i in range(len(enteredDigits)):
        if enteredDigits[i]!="-":
            strDigits.append(enteredDigits[i])
            
    for j in range(len(strDigits)):
        num=int(strDigits[j])
        digits.append(num)
        
    check_digit=compute_check_digit(digits)
    digits.append(check_digit)
    for k in range(len(digits)):
        n=digits[k]
        newDigits.append(n)

    drawBars=draw_bar(turtle,newDigits)
    
    

main()
