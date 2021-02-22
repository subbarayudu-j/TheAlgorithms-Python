def guessnumber(maximum,minimum):
    smallestnumber = minimum
    biggestnumber = maximum
    numgot = False
    while not numgot == True:
        if (biggestnumber - smallestnumber <= 1 and biggestnumber - smallestnumber > 0) or (smallestnumber - biggestnumber <= 1 and smallestnumber - biggestnumber > 0):
           print("Is your number ", smallestnumber, "?")
           userinput = input("")
           if userinput == "y":
                print("Your number is... ",smallestnumber,"!")
                numgot = True
           elif userinput == "n":
                print("Your number is... ",biggestnumber,"!")
                numgot = True
        elif not ((biggestnumber - smallestnumber <= 1 and biggestnumber - smallestnumber > 0) or (smallestnumber - biggestnumber <= 1 and smallestnumber - biggestnumber > 0)):
            print("Is your number larger than or equal to ",(smallestnumber+biggestnumber)/2,"?")
            userinput = inpàut("")
            if userinput == "n":
                smallestnumber = round((smallestnumber+biggestnumber)/2)
            elif userinput == "y":
                    biggestnumber = round((smallestnumber+biggestnumber)/2)
            else:
                print("Use y or n")
        else:
            print("Use y or n")
