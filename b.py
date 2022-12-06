i=1
while i<=5:
    name=input("Enter the name :")
    if len(name)<6:
        print("less than 6 characters,enter it again")
    else:
        print(name)
        i=i+1
