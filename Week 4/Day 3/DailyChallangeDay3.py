letters = ["a","b","c","d","e", "f", "g","h","i","j","k","l","m", "n","o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y","z"] 
ask = input('Please type "e" to Encrypt and "d" to Decrypt: ') 
encrypt = []
decrypt = []
num = 0
if ask == "e":
    ask2 = input("what do you want to Encrypt?  ")
    for letter in ask2: 
        if letter != "x" and letter != "y" and letter != "z" and letter != " ":
            a = letters.index(letter)
            encrypt.append(letters[a + 3])
        elif letter == " ": 
            encrypt.append(" ")
        else:
            a = letters.index(letter)
            encrypt.append(letters[num]) 
            num = num + 1

    print("".join(encrypt))

num2 = 17
if ask == "d":
    ask2 = input("what do you want to Decrypt?  ")
    for letter in ask2: 
        if letter != "u" and letter != "v" and letter != "w" and letter != " ":
            a = letters.index(letter)
            decrypt.append(letters[a - 3]) 
        elif letter == " ": 
            decrypt.append(" ") 
        else:
            a = letters.index(letter)
            decrypt.append(letters[num2]) 
            num2 = num2 + 1
    
    print("".join(decrypt))

