x=float(input("gross income: "))#this will ask the user his or her gross income
y=10000#this is the standard deduction
z=3000#this is the dependable deduction
a=float(input("number of dependents: "))#this will ask the user the number of dependants 
TI = x-y-(z*a)#this equation will give us the taxable income 
b=0.2#this is the tax rate
tax=TI*b#this equation  will calculate the tax 
print("tax: ",tax)#this will then print the calculated tax