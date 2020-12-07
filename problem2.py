'''
-------------------------------------------------------------------------------
Name:	 problem2.py
Purpose:	To evenly distribute the chicken wings with the students and find out how many chicken wings are leftover or Mr.Fabroa

Author:	Shiu.R

Created:	07/12/2020
------------------------------------------------------------------------------
'''
# Ask user to input the amount of chicken wings and the anount of students 
chicken_wings = int(input("How many chicken wings are there?: "))
students = int(input("How many students are in your class?: "))
# Calculate how many pieces of chicken wings each studen will get
student_chicken = chicken_wings // students
# Calculate how much leftover chicken wings are left for Mr.Fabroa
fabroa_chicken = chicken_wings % students
# Output the results
print("Each student will receive:" , str(student_chicken) , "chicken wing(s)" , "and Mr.Fabroa will receive:", str(fabroa_chicken) , ("chicken wing(s)"))