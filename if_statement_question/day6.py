# ----------------Question 6-----------------
# Without take input from user ------

distance = 91

if distance != 90:
    print("Please enter your valid distance ")
    exit()

if distance < 3:
    transport = "WALK"

elif distance <= 15:
    transport = "Take a Bike"

elif distance >= 16:
    transport = "Take a Car"


print(transport)


# ----- Take Input from User ----------

dis = int(input("Enter Your Distance : "))

if dis >100:
    print("Pleae Enter Valid Distance")
    exit()



if dis <= 3:
    transport = "GO To Walk"

elif dis <= 15:
    transport = "Take a Bike"

elif dis >= 15:
    transport = "take a Car"

print(transport)
