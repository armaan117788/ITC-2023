m = float(input( "Enter your Grade here: "))  #this will ask the user to enter his or her grade

if m>=0 and m<25:
    print("Your Grade is F")

elif m>=25 and m<45:
    print("Your Grade is E")

elif m>=45 and m<50:
    print("Your Grade is D")

elif m>=50 and m<60:
    print("Your Grade is C")

elif m>=60 and m<80:
    print("Your Grade is B")

elif m>=80 and m<=100:
    print("Your Grade is A")

else:
    print("Invalid")#as value should only lie between 0 and 100

