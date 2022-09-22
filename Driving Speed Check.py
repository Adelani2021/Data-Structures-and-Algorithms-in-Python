Question 1 (Driving Speed Check)
Speed_limit = int(input("Enter speed limit: "))
Driver_speed = int(input("Enter driver's speed: "))
x = Driver_speed - Speed_limit
if Driver_speed <= Speed_limit:
    print("Driver's speed is within the legal limit")
elif 1 <= x <=9:
  print ("Driver is speeding! Clocked at", x,"mph over the limit. Issue a warning.")
elif 10 <= x <= 19:
  print ("Driver is speeding! Clocked at", x,"mph over the limit. Issue a ticket with a $50 fine.")
elif 20 <= x <= 29:
  print ("Driver is speeding! Clocked at", x,"mph over the limit. Issue a ticket with a $75 fine.")
elif x >=30:
  print ("Driver is speeding! Clocked at", x,"mph over the limit. Issue a ticket with a $100 fine.")


