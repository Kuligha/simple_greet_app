msg = input("Please tell me your name: ")
print("Nice to meet you %s " % msg)
invite_drink = input(
    "Sorry, %s would you like something to drink, Yes or No? " % msg)
# invitationResp = ("Yes", "No")
drinkType = ["Tea", "Coffee", "Water"]

if invite_drink == ("Yes"):
    choiceofdrink = input("What would you like to have %s ?" % drinkType)
    for drinkChoice in drinkType:
        if choiceofdrink.startswith(drinkChoice):
            # problem of looping over the list and compare it to available inputs
            print("%s will be served in a few. Have a seat" % drinkChoice)
        else:
            print("Sorry sir, we dont have that, kindly have a seat")
else:
    print("Okay, have a seat over there")
