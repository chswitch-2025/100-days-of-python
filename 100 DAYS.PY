#DAY ONE!

#Dont Stop It This Time Plase?

# print("You Cant Live With Yur OWn Failures. Where Did That Lead You? Back To Me")

# print("Hello Stranger?")

# print("Hello World! \nI Will Rule The Difital World! \n Prepar Yourselves!!!")

# print(input("Who Are You Agasin?"))

# print("Well, I Am Not Sure Mighty Peoples Go Around And Introduce Themselves.")

# print("hello " + input("can you try agin? without the exaguration thing?") + "!")


# print(len(input("what is your name?")))

# username = input("what is your name?")
# length = len(username)
# print(length)

#first capstone

#print("welcoe to band name generator.")

#city = input("whats the city you grewup in?\n>")

#pet = input("whats your pet's name?\n> ")

#print("your band name could be: " + city + "-" + pet)

#====================================================

#DAY TWO
#data types
            #strings
            #integers
            #floats
            #booleans
#subscripting
    #print("python"[4])
#type checking(checking the type of ofany data)
    #print(type(-123.338))
#-----------------------------------------
# z = type(2 + 3)  

# if type(z) == int:

#     print("True")

# else:
#     print(False)

# #----------------------------------------------
# a = type("master")
# b = type(123)
# c = type(32.5)
# d = True
# print(a)
# print(b)
# print(c)
# print( type(d))

# #-------------------------------------------------
# a = "master"
# b = 123
# c = 32.5
# d = True
# print(type(a))
# print(type(b))
# print(type(c))
# print( type(d))

# #----------------------------------------------------
#tpe conversion/type castin

# user_name = input("enter your name: \n")

# length_of_User_name = len(user_name)

 
# print("the number of letters in your name is: ", length_of_User_name)
# #OR:-

# print("the number of letters in your name is: " + str(length_of_User_name))

# ------------------------------------------------------------------------------

#flooring vs floating vs rounding
#--------------------------------------------------------------------------------


# bill = float(input(" wellcome to the tip calculator \n" + "what is the total bill? \n"))

# tip = int(input("what percentage tip would you like to give? 10, 12, or 15? \n"))

# people = int(input("how many people to split the bill? \n"))

# print("each person should pay: " + str(round((bill + (bill * tip / 100)) / people, 2)))
#------------------------------------------------------------------------------------
# number = int(input("insert any number \n"))
# if number % 2 == 0:
#     print("Yor number is Even")
# else:
#     print("Your number is odd!")
#------------------------------------------------------------------

# height = int(input(print ("welcome to joy ride. \n Please enter your height? \n")))
# if height >= 120:
#     print("your age is legible for joy ride")
#     age = int(input("Please Enter your age? \n"))
#     if age <= 12:
#         print("please pay $5? \n")
#     elif age <= 18:
#         print("please pay $7? \n")
#     else:
#         print("please pay$10?")
# else:
#     print("your age is not legible for joy ride") 

#---------------------------------------------------------------------------------
# direction = input("Welcome to Treasure Island.Your mission is to find the treasure.\nLeft Or Right? \n")

# river = input("Swim Or Wait? \n")

# door = input("Red Or Blur? \n")

# if direction == str("Right"):
#     print("Fall into a hole.\nGame Over.")
# if direction == str("Left"):
#     print("Good choice.\n")
# if river == str("swim"):
#     print("Attacked by trout.\nGame Over")
# if river == str("wait"):
#     print("Good choice.\n")
# if door == str("blue"):
#         print("Eaten by beasts.\nGame Over")
# if door == str("red"):
#         print("You Win!")
    
# else:
#     print("You Win!")

#-----------------------------------------------
print("welcome to python pizza deliveries")
size = input("what size pizza do you want?\npress s for small, press M formedium and press L for large.\n")
pepperoni = input("do you want pepperoni on your pizza?\npress Y for yes and press N for no.\n")
extra_cheese= input("do you want extra cheese?\npress Y for yes and press N for no.\n")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("you typed the wrong letter in pizza selection. please try again?")
    quit()

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your Final Bill Is: ${bill}.")