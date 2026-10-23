print("welcome to treasure island\n")
direction = input("which direction so you wanna go? Write Right or Left\n").upper()
if direction == "RIGHT":
    print("Game Over!")
    quit()
elif direction == "LEFT":
    print("well done.")
else:
    print("you typed the wrong word. please try again!")
    quit()
river = input("there is a river on your way. do you want to wait for boat or swim? type wait or swim\n").upper()
if river == "SWIM":
    print("Eaten by crocodies. game over!")
elif river == "WAIT":
    print("well done")
door = input("there are three doors colored red, blue and yellow. wich one do you wantto inter?\nwrite red or blue or yellow.\n").upper()
if door == "BLUE" or door == "YELLOW":
    print("wrong door! game over!")
elif  door == "RED":
    print("You win!!!\nCONGRATULATIONS!!!")
    quit()
else:
    print("you typed the wrong word. please try again!")
    quit()


