from collections import Counter 
class Text(): 
    def __init__(self):
        with open('my_text.txt') as text:
            self.allwords = (text.read().strip().split())
        self.allwordsonce = list(set(self.allwords))


    def frequency(self,word): 
        word1 = self.allwords.count(f"{word}")
        print(word1)


    def most_common(self):
        with open('my_text.txt') as text:
            counter = Counter(text.read().strip().split())
        print(counter.most_common(5))

    def uniqe_words(self): 
        print(self.allwordsonce) 
      
 


# mytext = Text()
# mytext.most_common()  








class TextModification(): 
    
    def __init__(self): 
        with open('my_text.txt') as text:
            self.allwords = (text.read().strip().split())
        with open('stopwords.txt') as sw:
            self.stopwords = (sw.read().strip().split())

    
    def no_stopwords(self): 
        without = []
        delete_list = self.stopwords
        for line in self.allwords:
            for word in delete_list:
                line = line.replace(word, "")
            without.append(line)
        print(" ".join(without)) 
        
      

    def no_punctuation(self): 
        without = []
        delete_list = [".", "," , "?" , "!" , ":", ";", '"', "'", "—", ")", "("]
        for line in self.allwords:
            for word in delete_list:
                line = line.replace(word, "")
            without.append(line)
        print(" ".join(without)) 
       


    def no_special(self): 
        without = []
        delete_list = ["♦"]
        for line in self.allwords:
            for word in delete_list:
                line = line.replace(word, "")
            without.append(line)
        print(" ".join(without)) 
        
      




mytext = TextModification()
mytext.no_punctuation() 
 



