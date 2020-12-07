'''
-------------------------------------------------------------------------------
Name:	 problem1.py
Purpose:	Converting Celsius into fahrenheit. 

Author:	Shiu.R

Created:	07/12/2020
------------------------------------------------------------------------------
'''
# welcome the user to the software
print("******* Welcome to the Temperature converter (from celsius to fahrenheit) ********")
# get the celsius
celsius = float(input("Enter the degrees celsius: "))
# calculate the fahrenheit
fahrenheit = 9/5*celsius + 32
# tell the user the fahrenheit of celcius inputted
print("The fahrenheit of " , str(celsius) , "degrees celsius is" , str(fahrenheit) , "fahrenheit" )