class PalindromeCheck(): 
    def __init__(self, word): 
        self.word = str(word)  

    def __repr__(self): 
        if self.word == self.word[::-1]: 
            return "True"
        else: 
            return "False"


word1 = PalindromeCheck("mom")
word2 = PalindromeCheck("hello") 
word3 = PalindromeCheck("Mom")
word4 = PalindromeCheck("yobananaboy")


