#Gary Machorro
#8/18/17
#Project 3:Pizza ordering
##
# This program computes of a pizza store
#
def main():
    size=getSize()
    extra=getCrust()
    discount=applyDiscount()
    total=cost(size,extra,discount)
    print("Your total will be $%2.2f"%total)
## gets the size of the pizza
# @return the size of the pizza
#
def getSize():
    print("Pizza Size(inches)--Cost")
    print("10 inches-----$10.99")
    print("12 inches-----$12.99")
    print("14 inches-----$14.99")
    print("16 inches-----$16.99")
    n=0
    error=-1
    while n<3:
        n=n+1
        size=int(input("Enter your desired pizza size:"))
        if size==10:
            return size
            break
        elif size==12:
            return size
            break
        elif size==14:
            return size
        
            break
        elif size==16:
            return size
            break
        else:
            print("Invalid:Try Again")
    if n==3:
        print("very sorry")
        quit()
        return error
## gets the crust type 
# @return the extra charge
#
def getCrust():
    print("Crust Choice----Charge")
    print("Hand-Tossed----NO Charge")
    print("Thin-Crust----$1.00")
    print("Deep-Dish----$2.00")
    extra=0
    handTossed=0
    thinCrust=1
    deepDish=2
    crust=input("Enter your desired crust:")
    if crust=="Hand-Tossed" or crust=="hand-tossed":
        extra=handTossed
        return extra
    elif crust=="Thin-Crust" or crust=="thin-crust":
        extra=thinCrust
        return extra
    elif crust=="Deep-Dish" or crust=="deep-dish":
        extra=deepDish
        return extra
    else:
        return extra
## gets the discount from code entered
# @return the discount that a code will give
#
def applyDiscount():
    discount=0
    holiday10=0.1
    winter20=0.2
    vipmax=0.25
    coupon=input("Enter coupon code:")
    if coupon=="Holiday10" or coupon=="holiday10":
        discount=holiday10
        return discount
    elif coupon=="Winter20" or coupon=="winter20":
        discount=winter20
        return discount
    elif coupon=="VIPmax" or coupon=="vipmax":
        discount=vipmax
        return discount
    else:
        return discount
## computes the total cost of the pizza
# @param size of the pizza, the extra charge, and the discount given
#
def cost(size,extra,discount):
    tenInch=10.99
    twelveInch=12.99
    fourteenInch=14.99
    sixteenInch=16.99
    if size==10:
        cost=(tenInch+extra)-((tenInch+extra)*discount)
        return cost
    elif size==12:
        cost=(twelveInch+extra)-((twelveInch+extra)*discount)
        return cost
    elif size==14:
        cost=(fourteenInch+extra)-((fourteenInch+extra)*discount)
        return cost
    elif size==16:
        cost=(sixteenInch+extra)-((sixteenInch+extra)*discount)
        return cost
    else:
        print("An error ocurred, try again")
    
main()

#OUTPUTS
'''
Pizza Size(inches)--Cost
10 inches-----$10.99
12 inches-----$12.99
14 inches-----$14.99
16 inches-----$16.99
Enter your desired pizza size:15
Invalid:Try Again
Enter your desired pizza size:17
Invalid:Try Again
Enter your desired pizza size:11
Invalid:Try Again
very sorry
>>> 
============ RESTART: ============
Pizza Size(inches)--Cost
10 inches-----$10.99
12 inches-----$12.99
14 inches-----$14.99
16 inches-----$16.99
Enter your desired pizza size:17
Invalid:Try Again
Enter your desired pizza size:16
Crust Choice----Charge
Hand-Tossed----NO Charge
Thin-Crust----$1.00
Deep-Dish----$2.00
Enter your desired crust:deepdihs
Enter coupon code:Winter20
Your total will be $13.59
>>> 
============ RESTART: ============
Pizza Size(inches)--Cost
10 inches-----$10.99
12 inches-----$12.99
14 inches-----$14.99
16 inches-----$16.99
Enter your desired pizza size:12
Crust Choice----Charge
Hand-Tossed----NO Charge
Thin-Crust----$1.00
Deep-Dish----$2.00
Enter your desired crust:Deep-Dish
Enter coupon code:
Your total will be $14.99
>>> 
============ RESTART: ============
Pizza Size(inches)--Cost
10 inches-----$10.99
12 inches-----$12.99
14 inches-----$14.99
16 inches-----$16.99
Enter your desired pizza size:14
Crust Choice----Charge
Hand-Tossed----NO Charge
Thin-Crust----$1.00
Deep-Dish----$2.00
Enter your desired crust:Thin-Crust
Enter coupon code:VIPmax
Your total will be $11.99
>>> 
============ RESTART: ============
Pizza Size(inches)--Cost
10 inches-----$10.99
12 inches-----$12.99
14 inches-----$14.99
16 inches-----$16.99
Enter your desired pizza size:10
Crust Choice----Charge
Hand-Tossed----NO Charge
Thin-Crust----$1.00
Deep-Dish----$2.00
Enter your desired crust:
Enter coupon code:
Your total will be $10.99
>>> 
============ RESTART: ============
Pizza Size(inches)--Cost
10 inches-----$10.99
12 inches-----$12.99
14 inches-----$14.99
16 inches-----$16.99
Enter your desired pizza size:14
Crust Choice----Charge
Hand-Tossed----NO Charge
Thin-Crust----$1.00
Deep-Dish----$2.00
Enter your desired crust:deep-dish
Enter coupon code:
Your total will be $16.99

'''

    
    
      
    
    
