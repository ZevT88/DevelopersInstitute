import os
import time


def animate_text(text):
  numberOfCharacters=1
  for i in range(len(text)):
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print(text[0:numberOfCharacters])
    numberOfCharacters += 1
    time.sleep(0.2)
    os.system('clear')

  
  
animate_text("c") 
