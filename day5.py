# -------------------------Question 5 -------------
# Without take user input

weather = "Sunny"

if weather == "Sunny":
    # activity = "Go For Walk"
    print("Go for walk")
elif weather == "Rainy":
    # activity = "Read a book"
    print("Read a Book")

elif weather == "snowy":
    # activity = "Build a Snowman"
    print("Build a Snowman")

else:
    print("Please Enter your valid weather name")
    exit()


# Take Input From User -----

weather = input("Enter Your Weather(Sunny, Rainy, Snowy):- ").lower()

if weather == "sunny":
    print("Go For Run")

elif weather == "rainy":
    print("Read a book")

elif Warning == "snowy":
    print("Build a Snowman")

else:
    print("Please Enter your valid weather name")