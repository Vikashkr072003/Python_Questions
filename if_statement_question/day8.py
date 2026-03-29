#  ------------------Questiion 8 --------------------
# Without output from user :------


pas = "vickey@12345"

length = len(pas)

if length < 6:
  print("Weak Password")

elif length <= 10:
  print("Medium Password")

else:
  print("Strong Password")


# With take input from user :-
 
password = input("Enter your password ")

length = len(password)

if length < 6:
  print("Weak password")

elif length <= 10:
  print("Medium Password")

else:
  print("Strong Password")
