#Exercise 1 Tempiture Advice
import random
def main(randtemp):
    if randtemp < 0: 
        return "Brrr, that’s freezing! Wear some extra layers today"
    elif randtemp >= 0 and randtemp < 16: 
        return "Quite chilly! Don’t forget your coat!" 
    elif randtemp >= 16 and randtemp <= 23: 
        return "Thats some nice Weather!"
    elif randtemp >= 24 and randtemp < 32: 
         return "Thats kinda warm!" 
    elif randtemp >= 32 and randtemp <= 40: 
         return "Thats really hot!"


def get_random_temp(season):
    if season == "winter":
        n = random.randint(-10,15)
    elif season == "fall":
        n = random.randint(16,23)
    elif season == "spring":
        n = random.randint(24,32)
    elif season == "summer":
        n = random.randint(33,40)
    print("The tempiture is " + f"{n}" + " degrees Celcius")
    print(main(n))

get_random_temp("fall") 