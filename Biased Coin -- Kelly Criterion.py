import random
from sys import exit

# Global Variables
Tries_left = 30
Money = 25
High_Score = 0

# Functions


def h_or_t():
    if Tries_left == 0:
        print("let's see the results"), results()
    # User chooses which side of Coin to bet on
    global coin_prediction # By default variables inside functions are local, to overwrite this "global" is used.
    coin_prediction = []
    binp1 = str(input("Heads or tails? Enter h or t: \n \u25ba "))
    if binp1 == "h" or binp1 == "t":
        coin_prediction.append(binp1)
        print(coin_prediction)
        return coin_prediction, placebet()
    else:
        print("Error, invalid input.")
        h_or_t()


def placebet():
    global Tries_left
    try:
        bet = int(input("You currently have £" + str(Money) + ", how much of this will you bet? \n \u25ba "))
    except ValueError:
        print("Error. Invalid input. Try again"), placebet()

    if bet > Money:
        print("Error you can't bet more than you have!")
        placebet()
    elif bet == 0:
        print("You chose to forfeit 1 try")
        Tries_left -= 1
        h_or_t()
    elif bet <= Money and Money > 0:
        Tries_left -= 1
        print("Now, let's see if you won...")
        return flipcoin(coin_prediction, bet)
    else:
        print("Error, try again")
        placebet()


def flipcoin(coin_prediction, bet):
    print("Flipping the Coin...")
    coin_outcome = random.choice([1, 1, 1, 1, 1, 1, 2, 2, 2, 2])
    if coin_outcome == 1:
        print("The Coin landed on heads!")
        if str(coin_prediction[0]) == "h":
            global Money
            Money += bet
            print("You won the bet!")
            print("You now have £ " + str(Money) + " and " + str(Tries_left) + " tries left"), h_or_t()
        elif str(coin_prediction[0]) == "t":
            Money -= bet
            print("Oh no! You lost...")
            if 0 >= Money:
                print("You lost all the money. Game over!"), exit()
            else:
                print("You now have £ " + str(Money) + " left and " + str(Tries_left) + " tries left"), h_or_t()
            # Add options -Next bet, -Check balance -Check tries left
    elif coin_outcome == 2:
        print("The Coin landed on tails!")
        if str(coin_prediction[0]) == "t":
            Money += bet
            print("You won the bet!")
            print("You now have £ " + str(Money) + " and " + str(Tries_left) + " tries left"), h_or_t()
        elif str(coin_prediction[0]) == "h":
            Money -= bet
            print("Oh no! You lost...")
            if 0 >= Money:
                print("You lost all the money. Game over!"), exit()
            else:
                print("You now have £ " + str(Money) + " left and " + str(Tries_left) + " tries left")
                h_or_t()

def results():
    global High_Score
    High_Score = Money - 20
    print("Your score is £" + str(High_Score))
    if High_Score < 250:
       print("Your score is pitifully low. Maybe Coin simulator isn't for you.. Grade E")
    elif 250 < High_Score < 350:
        print("Congrats you have been graded an A* for your risk management!"),
    elif 350 < High_Score < 500:
        print("You have taken more risks than necessary and this time they paid off. You are Graded a B+")
    elif High_Score > 2000:
        print("WOW! you take massive risks but you have reaped a massive reward! You only get a C for risk "
              "management though")
    else:
        print("Very Good! Your graded A-")
    return exit()

print("\u25ba ---------- Biased Coin Kelly Criterion Simulator 2020\u2122 ---------- \u25c4")
print("                     MADE BY: Magnanimoose")
print(
"You have to bet money on the flip of a biased coin. The biased coin has a 60% chance to land on heads." 
"\n You are allowed " + str(Tries_left) + " Tries, if you run out of money early the game ends. "
"\n You start with £" + str(Money) + ", the aim is to be as safe as possible with your investment while making a return\n"
)

h_or_t()
