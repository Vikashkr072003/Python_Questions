# -------------------Question 2 --------------
# With out taking User Input.

age = 7
day = "Tuesday"

if age >= 18:
    price = 20
else:
    price = 8

if day == "Wednesday":
     price = price - 2

print("The Ticket Price $", price)


# taking Input from User :----

age = int(input("Enter Your age : "))
day = input("Enter your day :")

if age >= 18:
    price = 20
else:
    price = 10

if day.lower() == "Wednesday":
    price = price - 2

# elif day !=  "Wednesday":
#     print("The Offer Only Wednesday")    # With Using this Method

else:
    print("The Offer Only Wednesday")


print("The Price of Your Ticket $", price)
