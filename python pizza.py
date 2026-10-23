# small pizza ==$15
# medium pizza ==$20
# larg pizza ==$25
# pepperoni for small pizza == $2
# pepperoni for medium or large pizza == $3
# extra cheese == $1


print("welcome to python pizza!\n")
pizza_size = input("what size your pizza you would like to be?\npress S for small, press M for Medium and Press L for large.\n")
pepperoni = input("do yoou want pepperoni on your pizza?\npress Y for Yes press N for No.\n")
extra_cheese = input("do you want extra cheese on your pizza?\n")

bill = 0
if pizza_size == "S":
    bill += 15
elif pizza_size == "M":
    bill += 20
elif pizza_size == "L":
    bill += 25
else:
    print("you typed the wrong letter. please try again!")

if pepperoni == "Y":
    if pizza_size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"your total bill is: ${bill}")
