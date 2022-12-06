def diff(h1 , m1 , h2 , m2):
   if(m1 > m2):
       m2 +=60
       --h2
   m = m2 - m1
   h = h2 - h1
   print("Time for which vehicle was in parking = " , h , " : " , m)
   return h

print("1.Truck/Bus")
print("2.Car")
print("3.Cycle/ Motor Cycle / Scooter")
#vehicle = input("Enter '1' for car, '2' for bus/truk and '3' for scooter/cycle/motor cycle: ")
vehicle=int(input("Enter the Choice :"))
h_entry = int(input("Enter at what hour vehicle has entered : "))
m_entry = int(input("Enter at what minute vehicle has entered : "))
h_exit = int(input("Enter at what hour vehicle has exit : "))
m_exit = int(input("Enter at what minute vehicle has exit : "))

if(vehicle == 1):
   if(diff(h_entry,m_entry,h_exit,m_exit)<=3):
       print("Charge : ",20)
   else:
       print("Charge : ",30)

elif(vehicle == 2):
   if(diff(h_entry,m_entry,h_exit,m_exit)<=3):
       print("Charge : ",10)
   else:
       print("Charge : ",20)

elif(vehicle == 3):
   if(diff(h_entry,m_entry,h_exit,m_exit)<=3):
       print("Charge : ",5)
   else:
       print("Charge : ",10)

else:
       print("Invalid vehicle choice")
