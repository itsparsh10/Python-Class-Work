# wap to calculate parking charges of a vehical.
# enter the type of vehical as a charter (c=car, b=bus) etc .
# and num of houres, then calculate charges as given below

# truck/bus - 20 rs per/hr
# car - 10 rs per/hr
# cycle /scooter/bike -5 rs per/hr

a = "-----Welcome to the Parking Area----"
z = ("c=car", "b=bus", "bike=bike", "s=scooter", "cy=cycle", "t=truck")
print(a)

b = input("Enter Your Vehicle: ")



if b.lower() == "car":
    t = "Enter Check-In time: "
    check_in_time = int(input(t))
    
    check_out_time = int(input("Enter Check-Out time: "))
    h=check_in_time-check_out_time
    
    if check_out_time >3:
        print("Your Amount Is: " ,20)
    else:
        print("Your Amount Is: " ,10)

    h=int(input("How Much Hours"))
    
    
    
elif b.lower() =="bus":
     
    t = "Enter Check-In time: "
    check_in_time = int(input(t))
    
    check_out_time = int(input("Enter Check-Out time: "))
    
    if check_out_time >3:
        print("Your Amount Is: " ,20+30)
    else:
        print("Your Amount Is: " ,30)
         
    # h=int(input("How Much Hours :"))
    # print("Your Total Amount is :",h*20)
    
elif b.lower() =="bike":
    
    t = "Enter Check-In time: "
    check_in_time = int(input(t))
    
    check_out_time = int(input("Enter Check-Out time: "))
    
    if check_out_time >3:
        print("Your Amount Is: " ,5+10)
    else:
        print("Your Amount Is: " ,5)
    # h=int(input("How Much Hours :"))
    # print("Your Total Amount is :",h*5)


elif b.lower() =="cycle":
    
    t = "Enter Check-In time: "
    check_in_time = int(input(t))
    
    check_out_time = int(input("Enter Check-Out time: "))
    
    if check_out_time >3:
        print("Your Amount Is: " ,5+10)
    else:
        print("Your Amount Is: " ,10+)
    # h=int(input("How Much Hours :"))
    # print("Your Total Amount is :",h*5)
# elif b.lower() =="t":
#     h=int(input("How Much Hours :"))
#     print("Your Total Amount is :",h*20)
    


