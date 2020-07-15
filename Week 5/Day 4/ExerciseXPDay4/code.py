def get_words_from_file(file_name): 
    f = open(f'{file_name}')
    print(f.readlines()) 


import random
def get_random_sentence(length): 
    wordlist = []
    sentance = []
    for line in open('wordlist.txt'):
        wordlist.append(line.strip()) 

    for i in range(length):    
        sentance.append(random.choice(wordlist))
    
    print(" ".join(sentance).lower())



def main(): 
    print("This program outputs a random sentance with a desired length from a list of words!") 
    
    def function(): 
        length = int(input("How long would you like your sentance to be? \n(Between 2 and 20 please)  "))  
        if length > 20 or length < 2: 
           print("ERROR INCORECT LENGTH")
        else:  
            get_random_sentence(length)

    function() 


main() 




