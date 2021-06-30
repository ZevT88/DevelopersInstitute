let str1 = "Mix" 
let str2 = "Pod"


let strA = str2.slice(0,-1) + str1.slice(-1)
let strB = str1.slice(0,-1) + str2.slice(-1) 

let newWord = strA + " " + strB
console.log(newWord)