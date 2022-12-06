wage = float(input("Enter the hourly wage INR :"))

r_hours = float(input("Enter the regular hours: "))

ot_hours = float(input("Enter the overtime hours: "))

totalPay = (r_hours * wage) + (ot_hours * (wage * 1.5))


print ("The total weekly pay is INR" , totalPay)
