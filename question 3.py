seconds=float(input("number of seconds: "))#this will ask the user the number of seconds 
minutes=seconds // 60# this will give us the number of minutes
remainder=seconds%60 #this will give us the remainder seconds after dividing total seconds by 60
print(minutes,'minutes and ',remainder,'seconds')