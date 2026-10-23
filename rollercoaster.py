#to ridde the roller coaster, first a person ust be 120cm or greater. then the fee will be depending on the age of the person. 
# child = 5, <12
# teen = $7 and <=18
# adultts pay $12. >18
# also taking a photo will cost additional fee of $3.
print("well come to rollercoaster!\n")
height = int(input("Please enter your Height in cm?\n"))
bill = 0
if height >= 120:
    print("you are leggible for the ride")
    age = int(input("please state your age?\n"))
    if age < 12:
        bill += 5
    elif age <= 18:
        bill += 7
    else:
        bill += 12
    photo = input("do you want a photograph?enter Y if Yes or N for no.\n")
    if photo == "Y":
        bill += 3
        print(f"your total bill is ${bill}")
else:
    print("your height is not legible for the ride!")
