import random
def hang():
    name = input("What is your name? ")
    print ("Hello, " + name, "Welcome to  hangman! ")
    print ("Start guessing a letter...")
    Wlist=["secret","good","excellence","this","google","dell"]
    word = random.choice(Wlist)
    guesses = ''
    #determine the number of turns
    turns = len(word) + 3
    while (turns > 0):
        failed = 0
        for char in word:
            if char in guesses:
                print (char,end=" ")
            else:
                print ("_",end=" ")
                failed =failed+1
        if (failed == 0):
            print ("You won")
            break
        guess = input("\nguess a character:")
        # set the players guess to guesses
        guesses =guesses + guess
        if guess not in word:
         # turns counter decreases with 1 (now 9)
            turns=turns-1
        # print wrong
            print ("Wrong")
        # how many turns are left
            print ("You have",+ turns,"more guesses left")
        # if the turns are equal to zero
            if(turns == 0):
            # print "You Loose"
                print ("You Loose")
    if input("Play again (y/n)\n") == "y":
                print()
                hang()
hang()
