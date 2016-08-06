# branching
import random
choice = random.choice(["1", "2", "3"])

if choice == "1":
    print "There's a giant bear here eating a cheese cake.  What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    choice = random.choice(["1", "2"])

    choices = {"1": "The bear eats your face off.  Good job!",
               "2": "The bear eats your legs off.  Good job!"}

    print choices[choice]
elif choice == "2":
    print "choice 2..."
else:
    print "bad choice.."

