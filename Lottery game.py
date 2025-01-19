def menu():
    print("*******************")
    print ("Menu")
    print ("1. Enter lottery \n 2. Run lottery \n 3. See the odds \n 4. Quit")
    answer = int(input("Enter a choice"))
    if answer == 1:
        Enterlottery()
    elif answer == 2:
        Runlottery()
    elif answer == 3:
        SeeOdds()
    elif answer == 4:
        print ("Thanks for playing")
    else:
        print ("Error")

menu()