# ----------------------Question 10 -----
# Without taking input from user ------

pet = "Cat"   # Enter cat
year = 8

if pet == "Dog":
  if year < 3:
    print("Recommend : Puppy Food")
  else:
    print("Recommend: Adult Dog Food")

elif pet == "Cat":
  if year > 5:
    print("Recommend: Senior Cat Food")
  else:
    print("Recommend: Adult Cat Food")

else:
  print("Pet not Find yet")


# With Taking Input From User :------

pet = input("Enter Your Pet: ").lower()
year = int(input("Enter your age: "))

if pet == "dog":
    if year < 2:
        print("Recommend: Puppy Dog Food")

    else:
        print("Recommend: Adult Dog Food")

elif pet == "cat":
    if year > 5:
        print("Recommend: Senior Cat Food")
    else:
        print("Recommend: Adult Cat Food")

else:
    print("Pet is not valid yet")
