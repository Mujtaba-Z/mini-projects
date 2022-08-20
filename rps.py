import random
##print("Enter 1 (rock), 2(paper), or 3 (scissors) /n")
##user = int(input())

opt = ["rock", "paper", "scissors"]

bot = random.randint(1,3)
play = 1
botscore = 0
score = 0


while play == 1:
    print("Enter 1 (rock), 2(paper), or 3 (scissors) /n")
    user = int(input())
    bot = random.randint(1,3)
    if user == 1:
        if bot == 1:
            print("Bot guessed rock. Tie")
        elif bot == 2:
            print("Bot guessed paper. Loss")
            botscore += 1
        else:
            print("Bot guessed scissors. Win")
            score += 1
    elif user == 2:
        if bot == 2:
            print("Bot guessed paper. Tie")
        elif bot == 3:
            print("Bot guessed scissors. Loss")
            botscore += 1
        else:
            print("Bot guessed rock. Win")
            score += 1
    else:
        if bot == 3:
            print("Bot guessed scissors. Tie")
        elif bot == 1:
            print("Bot guessed rock. Loss")
            botscore += 1
        else:
            print("Bot guessed paper. Win")
            score += 1
    print("Botscore:", botscore, "\t Your Score:", score)
    play = int(input("Play again? (1 for yes, 0 for no) \n"))
    
