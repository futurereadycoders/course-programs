# Tamagotchi in Python | FRC
import time
import random

names = [ # All the potential names for our Tamagotchi.
    "Pippi",
    "Lenny",
    "Bugle",
    "Dream",
    "Abyss",
    "Silent",
    "Nimble",
    "William",
    "Popcorn",
    "Magnum",
    "Moira",
    "Phantom",
    "Jasper",
    "Gravy",
    "Zeek",
    "Tron",
    "Tug",
    "Thistle",
    "Odie",
    "Mega",
    "Bubba",
    "Daz",
    "Tanner",
    "Garth",
    "Twilight",
    "Sam",
    "Noreaga",
    "Peachy",
    "Howard",
    "Pounce",
    "Dirty",
    "Fudge",
    "Raz",
    "Omelette",
    "Twister",
    "Nebula",
    "Mario",
    "Pistol",
    "Stitch",
    "Matrix",
    "Fog",
    "Tug",
    "Booker",
    "Hercules",
    "Treat",
    "Einstein",
    "Leroy",
    "Meatball",
    "Mustard",
    "Derp",
    "Pip",
    "Resin",
    "Meta",
    "Lee",
    "McKenzie",
    "Sarge",
    "Bandicoot",
    "Bunker",
    "Birch",
    "Grit",
    "Destiny",
    "Mario",
    "Mojo",
    "Diesel",
    "Fozzy",
    "Dainty",
    "Resin",
    "Cupcake",
    "Chaos",
    "Amber",
]
breeds = ["Rexotic", "Mythyr", "Shuggle", "Jaegrum", "Norgis"] # Breed names

def main(): # We have a main function so we can have other functions!
    print("Welcome to Tamagotchi! Generating new virtual pet...")
    time.sleep(1)
    print("\nTa-da!")
    name = random.choice(names)
    breed = random.choice(breeds)
    print(f"Your virtual pet is a {breed} named {name}.")
    print("Look after it carefully! Every second its happiness and food levels, starting at 20, will go down.")
    print("If its happiness and food levels reach zero, your pet dies. :(")
    print("In order to feed it or play with it, type 'feed' or 'play'. You'll need to complete short challenges to keep it alive!")
    input("Hit enter to continue.")

    seconds = 0 # Set the number of seconds to 0
    food = 20
    happiness = 20

    while True:
        if random.randint(0,10) == 6:
            impact = sickness() # Trigger a sickness and store impact in a variable
            happiness = happiness - impact
            food = food - impact

        if happiness < 0 or food < 0:
            die() # Kill the animal

        print("\n") # Print 4 \n to put some space between this message and the previous
        print(f"{name} ({breed})  |  Age: {seconds} seconds\nFood: {food}\nHappiness: {happiness}")

        seconds = seconds + 1
        food = food - 1
        happiness = happiness - 1

        action = input("Type 'feed' to feed, 'play' to play, or just hit enter to skip.\n").lower()
        if action == "feed":
            food = food + feed() # If the person completes the feeding task successfully, food levels rise. If not, they drop.
        elif action == "play":
            happiness = happiness + play() # Call the play function: defined later on.
        # Unwritten else: just skip back to the top

def feed():
    number_one = random.randint(0,20)
    number_two = random.randint(0,20)
    print(f"To feed your pet, what is {number_one} + {number_two}?") # Prompt the user
    answer = int(input())

    points_to_winlose = random.randint(3,15) # Randomly pick the number of happiness points the pet will lose or gain if fail/success

    if answer != number_one + number_two:
        print(f"\nWrong! You just lost {points_to_winlose} food points for your pet!")
        return 0 - points_to_winlose # points_to_winlose as a negative
    else:
        print(f"\nCongrats! You got it right. Your pet just gained {points_to_winlose} food points!")
        return points_to_winlose


def play():
    number_one = random.randint(0,15)
    number_two = random.randint(0,15)
    print(f"To feed your pet, what is {number_one} times {number_two}?") # Prompt the user
    answer = int(input())

    points_to_winlose = random.randint(3,15) # Randomly pick the number of happiness points the pet will lose or gain if fail/success

    if answer != number_one * number_two:
        print(f"\nWrong! You just lost {points_to_winlose} happiness points for your pet!")
        return 0 - points_to_winlose # points_to_winlose as a negative
    else:
        print(f"\nCongrats! You got it right. Your pet just gained {points_to_winlose} happiness points!")
        return points_to_winlose #

def die():
    print("Your pet sadly passed away.")
    print("Better luck next time.\n")
    input("Hit enter to continue.")
    main()

def sickness():
    print("Oh, no! Your pet caught a nasty disease!")
    impact = random.randint(10,25)
    print(f"Your pet lost {impact} food and happiness points. Get well soon!")
    return impact

main()


