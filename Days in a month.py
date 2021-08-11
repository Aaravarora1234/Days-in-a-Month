input_month_name = str(input("Enter the name of the month : "))
monthname = input_month_name.lower()
if(monthname == "january"):
  print("31 Days")
elif(monthname == "february"):
  print("29 or 28 Days")
elif(monthname == "march"):
  print("31 Days")
elif(monthname == "april"):
  print("30 Days")
elif(monthname == "may"):
  print("31 Days")
elif(monthname == "june"):
  print("30 Days")
elif(monthname == "july"):
  print("31 Days")
elif(monthname == "august"):
  print("31 Days")
elif(monthname == "september"):
  print("30 Days")
elif(monthname == "october"):
  print("31 Days")
elif(monthname == "november"):
  print("30 Days")
elif(monthname == "december"):
  print("31 Days")
else :
  print('Invalid Input')
