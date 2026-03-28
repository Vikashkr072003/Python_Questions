# ----------------Question 4 -----------
# Without taking input from user :---

fruit = "Apple"
color = "Red"

if fruit == "Apple":
    if color == "Red":
        print("Your Fruit is unripe")
    elif color == "Yellow":
        print("Your fruits become ripe")
    elif color == "Brown":
        print("Your fruits become overripe")
    else:
        print("Please Enter Valid Fruits and Color")


# Take User Input :----

fruit = input("Enter Fruits name : ").lower()
color = input("Enter Color name : ").lower()

if fruit == "Banana":
    if color == "Green":
        print("Your fruits is unripe")
    elif color == "Yellow":
        print("Your fruits is ripe")
    elif color == "Brown":
        print("Your fruits is overripe")
    else:
        print("Invalid Color for Banana")

elif fruit == "Apple":
    if color == "Green":
        print("Your fruits is unripe")
    elif color == "Red":
        print("Your fruits is ripe")
    elif color == "Brown":
        print("Your fruits is overripe")
    else:
        print("Invalid Color for Apple")
