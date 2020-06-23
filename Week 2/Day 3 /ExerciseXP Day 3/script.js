     
// //Exercise #1
// let favs = [" blue", " green", " yellow", " purple"]
//      if (color = favs[0]) { 

//         console.log("My first choice is" + favs[0]) 
//      }
//      if (color = favs[2]) { 
//                 console.log("My second choice is" + favs[1])

//      }

//      if (color = favs[2]) { 
//         console.log("My third color is" + favs[2])

//         }
    
//      if (color = favs[3]) { 
//          console.log("My fourth choice is" + favs[3])

//     } 
//Exercise  #1  2 
// let colors = ["blue", "green", "purple", "orange"]
// for (let favs in  colors) {
//          console.log(`My #${parseInt(favs) + 1} choise is ${colors[favs]}`)
//    }

// //Exercise #2 
// let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"] 
// names.sort()
// let final_name = "";
// for (let name of names) { 

//     final_name = final_name + name.charAt(0)


// }

// console.log(final_name);



//Exercise #2 2 
// let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"] 
// names.sort()
// let names1 = (`${names[0].charAt(0)}${names[1].charAt(0)}${names[2].charAt(0)}${names[3].charAt(0)}${names[4].charAt(0)}${names[5].charAt(0)}`)
// console.log(names1) 


// //Exercise #3 
// let ask;
// do
// {
//     ask = parseFloat(prompt("Give me a number"))
// } while (ask < 11);
   
// Exercise #4 
let people = ["Greg", "Mary", "Devon", "James"] 
for (let person of people) { 

      console.log(person)

}
let people1 = people.splice(0, "")
console.log(people1)
