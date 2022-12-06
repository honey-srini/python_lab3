c_units=int(input("Enter the electricity consumption in Units :"))
charges=0

if(c_units >=0 and c_units <=150):
    rate=3
    charges=c_units*rate
    
elif(c_units >=151 and c_units <=350):
    rate=3.75
    units=c_units-150
    charges=100+(units*rate)

elif(c_units >=351 and c_units <=450):
    rate=4
    units=c_units-350
    charges=250+(units*rate)

elif(c_units >=451 and c_units <=600):
    rate=4.25
    units=c_units-450
    charges=300+(units*rate)

else:
    rate=5
    units=c_units-600
    charges=400+(units*rate)
    
print("The Electricit Bill")
print("Consumed Units :",c_units)
print("Bill : INR",charges)
