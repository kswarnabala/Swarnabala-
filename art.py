from random import randint
easyturns=10
hardturns=5

def play(user_guess,real_answer,turns):
    if user_guess<real_answer:
        print("too low")
        return turns-1
    elif user_guess>real_answer:
        print("too high")
        return turns-1
    else:
        print("you got it, congrats")
def difficulty():
    level=input("do u want it easy or hard: ")
    if level == "easy":
        
        return easyturns
    elif level=="hard":
        return hardturns
def game():
    print("welcome to guessgame")
    print("think between 1 to 100")
    answer=randint(1,100)
    turns=difficulty()
    
    
    guess=0
    while guess!=answer:
        print(f"you have {turns} more attempts for guessing ur answer")
        guess=int(input("guess a no: "))
        turns=play(guess,answer,turns)
        if turns==0:
            print("you run out of guesses, you lost")
            return
        elif guess!=answer:
            print("guess again")

game()
        
