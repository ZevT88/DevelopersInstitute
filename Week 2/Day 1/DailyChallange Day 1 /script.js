let fruits = ["Banana", "Apples", "Oranges", "Blueberries"];
fruits.splice(0,1) 
fruits.sort()
fruits.push("Kiwi")
fruits.splice(0,1)
fruits.reverse()
console.log(fruits) 




let fruits2 = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];

console.log(fruits2[1][1])

