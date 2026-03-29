# ------------Question 3 -------------
# Without Taking Input from User
score = 1001

if score >= 101:
    print(
        "Plese Enter Vaild Number",
    )
    exit()


if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Your Score", grade)


# Taking Input from User :---

score = int(input("Enter Your Score "))

if score >= 101:
  print("Please Enter Your Vaild Score")
  exit()

if score >= 90:
  grade = "A"
elif score >= 80:
  grade = "B"
elif score >= 70:
  grade = "C"
elif score >= 60:
  grade = "D"
else:
  grade = "F"

print("Your Score is :", grade)

