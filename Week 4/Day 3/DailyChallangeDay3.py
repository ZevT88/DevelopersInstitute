letters = ["a","b","c","d","e", "f", "g","h","i","j","k","l","m", "n","o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y","z"] 
ask = input('Please type "E" to Encrypt and "D" to Decrypt: ') 
encrypt = []
decrypt = []
if ask == "E":
    ask2 = input("what do you want to Encrypt?  ")
    for letter in ask2: 
        if letter != "x" and letter != "y" and letter != "z":
            a = letters.index(letter)
            encrypt.append(letters[a + 3])
        else:
            a = letters.index(letter)
            encrypt.append(letters[a - 3]) 
       

    print(encrypt) 


if ask == "D":
    ask2 = input("what do you want to Decrypt?  ")
    for letter in ask2: 
        if letter != "u" and letter != "v" and letter != "w":
            a = letters.index(letter)
            encrypt.append(letters[a - 3]) 
        else:
            a = letters.index(letter)
            encrypt.append(letters[a + 3]) 
       

    print(encrypt) 


