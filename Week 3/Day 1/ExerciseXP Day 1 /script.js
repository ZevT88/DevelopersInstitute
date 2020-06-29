// // Exercise #1 

// // function myFunction() {
// //     document.getElementsByTagName("div")[0].setAttribute("class", "socialNetworkNavigation"); 
// //   }

// Exercise #2 
document.getElementsByClassName("list")[0].children[1].innerHTML = "Richard"
document.getElementsByClassName("list")[0].children[0].innerHTML = "Zev"
document.getElementsByClassName("list")[1].children[0].innerHTML = "Zev"
let li = document.createElement("LI")
let li2 = document.createElement("LI")  
li.innerHTML = "Hey Students"
li2.innerHTML = "Hey Students"
document.getElementsByClassName("list")[0].appendChild(li)
document.getElementsByClassName("list")[1].appendChild(li2)

let sarah = document.getElementsByClassName("list")[1].children[1] 
document.getElementsByClassName("list")[1].removeChild(sarah)

 





