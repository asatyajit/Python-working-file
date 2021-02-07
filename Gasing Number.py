print("Well Come to Guessing Number Game")
Gs_Number = 57
No_Attempt = 8
Game_loop = True
Guess = 0
try:
    while Game_loop:
        U_Number = int(input("Enter Guessing Number: "))
        Guess += 1
        No_Attempt -= 1
        if U_Number == Gs_Number:
            print("You wine the Game in ", Guess, "Attempt")
            Game_loop = False
        elif U_Number < Gs_Number:
            print("Please increase your Guessing Number")
            print("Number of guess left"
                  "", No_Attempt)
        elif U_Number > Gs_Number:
            print("Please decrease your Guessing Number")
            print("Number of guess left", No_Attempt)

        if No_Attempt == 0:
            print("SORRY", "You are Looser ")
            print("You Loose your all Attempt ", "Try to next time")
            Game_loop = False
except Exception as e:
    print(e)
