def Gematria():
    numbers = [50,20,1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100,200,300,400,0]
    letters = [' ','ת','ש','ר','ק','צ','פ','ע','ס','נ','מ','ל','כ','י','ט','ח','ז','ו','ה','ד','ג','ב','א','ך','ן']  
    word = input("A Hebrew word:   ") 
    total = 0 
    letters.reverse()
    for i in word: 
       index_num = letters.index(i)
       total += numbers[index_num]
       print(f"{i} is {numbers[index_num]}")
    print(f"your total gematria is {total}")
    
   
Gematria() 



