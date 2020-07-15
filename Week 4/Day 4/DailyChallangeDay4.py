def decrypt_matrix(codelist): 
    code = []
    for piece in codelist: 
        if piece[0] != " ":
            code.append(piece[0])

    for piece in codelist: 
        if piece[1] != " ":
            code.append(piece[1])
    
    for piece in codelist: 
        if piece[2] != " ":
            code.append(piece[2])

    codestring =  "".join(code)
    codelist2 = []
    for letter in codestring: 
        if letter.isalnum() is True: 
            codelist2.append(letter)
        else: 
            codelist2.append(' ')
    
    codestring2 = "".join(codelist2)
    print(codestring2) 



decrypt_matrix(["7 3", "Tsi", "h%x", "i #", "sM " ,"$a ", "#t%", "ir!"]) 


