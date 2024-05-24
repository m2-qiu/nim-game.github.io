def ask_for_move(num):
    usermove = input("There are %s coins left, how many do you want to remove (1, 3, 4)?" % num)
    if(usermove.isnumeric()):
        usermove = int(usermove)
        if (usermove != 1 and usermove != 3 and usermove !=4 or usermove > num):
            print("Try again, only 1 3 or 4 coins can be removed, and you cannot remove more coins then exists")
            return ask_for_move(num)
        #usermove
        num -= usermove
        if(num == 0):
            print("THE USER WINS! CONGRATULATIONS")
            return
        return nim_moves(num)
    else: 
        print("Try again, int number of coins, 1, 3, or 4")
        return ask_for_move(num)

def nim_moves(num):
    choice = 0
    if (num % 7 == 1 or num % 7 == 2 or num % 7 == 3 or num % 7 == 0):
        choice = 1
    elif (num % 7 == 5):
        choice = 3
    elif (num % 7 == 4 or num % 7 == 6):
        choice = 4
    num -= choice
    print("Nim removes %s coin(s)" % choice)
    if (num ==0):
        print("NIM WINS! BWA-HA-HA-HA-HA! NIM TAKES OVER")
        return
    print("The following is the stack of coins after %s coin(s) were removed" % choice)
    for i in range(num):
        if(i == 0):
            print("_____")
        print("|____|" )
    return ask_for_move(num)

#1, 3, 4
ncoin = int(input("Welcome to the infamous name of NIM! In this game, NIM plays first. Each player can alternatively move 1, 3, or 4 coins (with the condition that you are not removing more coins than exists.The player to remove the last coin wins. How many coins do you want to start with? "))
print("nim moves first")
nim_moves(ncoin)
#14 dead , 13 -4, 12 -3, 11 -4, 10 -1, 9 dead, 8 -1
