let allBooks = [
    

    book1 = { 
        title : " The Magicians",
        auther : "Written by Lev Grossman",
        image : "book1.jpeg",
        alreadyRead : true
    },

    book2 = { 
        title : "Harry Potter and The Sorcerer's Stone",
        auther : "Written by J.K Rowling",
        image : "book2.jpeg",
        alreadyRead : true
    }

] 


let tab_table = document.createElement("table")
let tabtr = document.createTextNode("tr").innerHTML = "title"
let tab_td1 = document.createElement("td")
let tab_td2 = document.createElement("td")
let tab_td3 = document.createElement("td")
let tab_td4 = document.createElement("td") 

tab_table.appendChild(tabtr)
