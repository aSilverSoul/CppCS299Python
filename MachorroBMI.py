#Gary Machorro
#8/8/17
#Project 1:BMI calculator with bonus
print("Welcome to BMI(Body Mass Index) calculator")
print("Please make a selection below")
choiceSelection=int(input("Press 1 for the English system or Press 2 for the Metric System."))
if choiceSelection==1:
  pounds=float(input("Enter your weight in pounds:"))
  inches=float(input("Enter your height in inches:"))
  englishBMI=((pounds)/(inches*inches))*703
  if englishBMI<=18.5:
    print("Unhealthy low BMI of %2.1f"%(englishBMI))
  elif englishBMI<=24:
    print("Healthy BMI of %2.1f"%(englishBMI))
  elif englishBMI<=29:
    print("Overweight BMI of %2.1f"%(englishBMI))
  elif englishBMI<=39:
    print("Obese BMI of %2.1f"%(englishBMI))
  elif englishBMI>40:
    print("Extreme obesity BMI of %2.1f"%(englishBMI))
elif choiceSelection==2:
  kilograms=float(input("Enter your weight in kilograms:"))
  meters=float(input("Enter your height in meters:"))
  metricBMI=(kilograms)/(meters*meters)
  if metricBMI<=18.5:
    print("Unhealthy low BMI of %2.1f"%(metricBMI))
  elif metricBMI<=24:
    print("Healthy BMI of %2.1f"%(metricBMI))
  elif metricBMI<=29:
    print("Overweight BMI of %2.1f"%(metricBMI))
  elif metricBMI<=39:
    print("Obese BMI of %2.1f"%(metricBMI))
  elif metricBMI>40:
    print("Extreme obesity BMI of %2.1f"%(metricBMI))
else:
  print("invalid please try again")

#OUTPUTS

"""
Welcome to BMI(Body Mass Index) calculator
Please make a selection below
Press 1 for the English system or Press 2 for the Metric System.1
Enter your weight in pounds:150
Enter your height in inches:70
Healthy BMI of 21.5
>>> 
============== RESTART ==============
Welcome to BMI(Body Mass Index) calculator
Please make a selection below
Press 1 for the English system or Press 2 for the Metric System.1
Enter your weight in pounds:180
Enter your height in inches:65
Obese BMI of 30.0
>>> 
============== RESTART ==============
Welcome to BMI(Body Mass Index) calculator
Please make a selection below
Press 1 for the English system or Press 2 for the Metric System.2
Enter your weight in kilograms:120
Enter your height in meters:1.7
Extreme obesity BMI of 41.5
>>> 
============== RESTART ==============
Welcome to BMI(Body Mass Index) calculator
Please make a selection below
Press 1 for the English system or Press 2 for the Metric System.2
Enter your weight in kilograms:180
Enter your height in meters:1.62
Extreme obesity BMI of 68.6
>>> 
============== RESTART ==============
Welcome to BMI(Body Mass Index) calculator
Please make a selection below
Press 1 for the English system or Press 2 for the Metric System.1
Enter your weight in pounds:0
Enter your height in inches:1
Unhealthy low BMI of 0.0
>>> 
============== RESTART ==============
Welcome to BMI(Body Mass Index) calculator
Please make a selection below
Press 1 for the English system or Press 2 for the Metric System.1
Enter your weight in pounds:1
Enter your height in inches:0
Traceback (most recent call last):
  File "C:\\Users\garym\Desktop\GaryMProject1.py", line 10, in <module>
    englishBMI=((pounds)/(inches*inches))*703
ZeroDivisionError: float division by zero
>>> 
============== RESTART ==============
Welcome to BMI(Body Mass Index) calculator
Please make a selection below
Press 1 for the English system or Press 2 for the Metric System.2
Enter your weight in kilograms:0
Enter your height in meters:0
Traceback (most recent call last):
  File "C:\\Users\garym\Desktop\GaryMProject1.py", line 24, in <module>
    metricBMI=(kilograms)/(meters*meters)
ZeroDivisionError: float division by zero
>>> 
============== RESTART ==============
Welcome to BMI(Body Mass Index) calculator
Please make a selection below
Press 1 for the English system or Press 2 for the Metric System.3
invalid please try again
"""
