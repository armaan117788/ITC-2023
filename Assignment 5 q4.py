a =input()
b= ['a','b','c','d','e','f','g','h','i','j','k','l','m','o','n','p','q','r','s','t',' ','u','v','w','x','y','z']
c=[]
for i in a:#we will use for loop to get our output
    if i not in c:
        c.append(i)
    
if sorted(b)==sorted(c):#using if else statment
    print('yes')
else:
    print("no")