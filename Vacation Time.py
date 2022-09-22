Question 2 (Vacation Time)
Company_name = input("Enter Company Name: ")
Number_of_years = float(input("Enter Number of Years: "))
if Company_name == ("Facebook"):
    print("All Employees have 4 weeks of vacation.")
if Company_name == ("Amazon") and Number_of_years >= 1:
  print ("Employees have 3 weeks of vacation.")
elif Company_name == ("Amazon") and Number_of_years < 1:
  print ("New Employees have 2 weeks of vacation.")
if Company_name == ("Google") and Number_of_years >=5:
  print ("Employees have 5 weeks of vacation.")
elif Company_name == ("Google") and 3 <= Number_of_years < 5:
  print ("Employees have 4 weeks of vacation.")
elif Company_name == ("Google") and Number_of_years < 3:
  print ("New Employees have 3 weeks of vacation.")
  
