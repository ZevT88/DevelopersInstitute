let numbers =  [10, 20, 30, 40, 50]

for (let i = 0; i < numbers.length ;i++) { 
    numbers[i] = numbers[i] + 5
} 
console.log(numbers)   




for (let index in numbers ) {
    numbers[index] = numbers[index] + 5 
}

console.log(numbers)




for (let element of numbers) { 
    let position = numbers.indexOf(element)
    numbers[position] = element + 5
}
 
console.log(numbers)