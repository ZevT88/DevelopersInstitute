def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]

class AnagramChecker(): 
    def __init__(self): 
        self.allwords = [] 
        for line in open('Anagrams.txt'):
            self.allwords.append(line.strip()) 



    def get_anagrams(self, word):  
        anagrams = []
        word_perms = list(all_perms(f"{word}"))  

        for perm in word_perms: 
            if perm in self.allwords: 
                anagrams.append(perm) 
        
        
        print(f'YOUR WORD: "{word}"')
        if word in self.allwords: 
            anagrams.pop(0)
            print("This is a valid English word")
        else: 
            print("This is not a valid English word")
        print(f"Anagrams for your word: {', '.join(anagrams)}")


  

anagram = AnagramChecker() 
anagram.get_anagrams("MEAT") 