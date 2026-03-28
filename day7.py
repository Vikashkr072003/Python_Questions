# -----Without take input from user----

order_size = "Medium"
extra_shot = True

if extra_shot:
  coffee = order_size + " Coffee with an extra shot"

else:
  coffee = order_size + "coffee"

print("Order: ", coffee)




# ----- With Taking input from user

order_size = input("Enter size (Small/Medium/Large): ")
extra_shot = input("Do you want extra shot? (yes/no): ")

if extra_shot.lower() == "yes":
    coffee = order_size + " coffee with an extra shot"
else:
    coffee = order_size + " coffee"

print("Order:", coffee)