# ----------------Question 9 ----------
# Without taking input from user---

year = 2024
# if year % 4 == 0 or year % 400 == 0:

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")

# elif year % 4 != 0:
#    print("Not leap year")

else:
    print("Not Leap Year")


# With Taking input from user----

year = int(input("Enter your year "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("This year is Leap year, thank you ")

else:
    print("This is not Leap year Thank you ")
