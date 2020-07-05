let letters = ["F", "E", "D", "C","B", "A","G", "H","I", "J","K", "L","M","N", "O","P", "Q", "R", "S", "T",  "U",  "V",  "W",  "X", "Y" , "Z" ]

makeNbuttons(26) 

let rand26 = letters[Math.floor(Math.random() * 26)]



function red() { 
    for (let i = 1; i < 27; i++) 
    document.children[0].children[1].children[i].style.backgroundColor = "red"
}

for (let i = 1; i < 27; i++) { 
    document.children[0].children[1].children[i].addEventListener("mouseout", red )
}

function createButton(){
    let button = document.createElement("button");
    return button;
}

function changeColor(target){
	if (target.style.backgroundColor == "blue"){
        target.style.backgroundColor = "red"; 
        
    }    
    else {
		target.style.backgroundColor = "blue"
	}
}
function makeNbuttons(n){
	for (let i = 0; i<n; i++){
		let button = createButton();
		button.addEventListener("click", function(event){
			changeColor(event.target);
		});
		document.body.appendChild(button);
	}
} 



function shuffle(array) {
    array.sort(() => Math.random() - 0.5);
  }
shuffle(letters)
for (let i = 1; i < 27; i++) { 
    document.children[0].children[1].children[i].innerHTML = letters[i - 1]

}






function playagain() { 
    window.location.reload();
}


function answer() { 
    for (let i = 1; i < 27; i++) { 
        if (document.children[0].children[1].children[i].innerHTML == rand26) {
            document.children[0].children[1].children[i].style.backgroundColor = "green"
            document.children[0].children[1].children[i].style.color = "blue"
            break 
        }
    }


}
let colors =  ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
let rand7 = letters[Math.floor(Math.random() * 7)]



function shuffle2()  {
    letters.sort(() => Math.random() - 0.5);
    for (let i = 1; i < 27; i++) { 
        document.children[0].children[1].children[i].innerHTML = letters[i - 1]
    } 
}



document.children[0].children[1].children[0].innerHTML = `Find the letter: ${rand26}  <h4> Tries: 0 </h4> <button onclick="answer()" class="answer">  Show Answer </button> <button onclick="shuffle2()" class="shuffle"> Shuffle  </button>`

let tries = 0
function tries2() {     
    tries++
    document.children[0].children[1].children[0].innerHTML = `Find the letter: ${rand26} <h4> Tries: ${tries} </h4>  <button onclick="answer()" class="answer">  Show Answer </button> <button onclick="shuffle2()" class="shuffle"> Shuffle  </button>`
}  

function youwon() {
    document.children[0].children[1].innerHTML = `YOU WON!!  <h3> YOU FOUND ${rand26} <br> in ${tries} tries!! </h3> <button class='again' onclick= 'playagain()'> play again </button>`
    document.children[0].children[1].classList.add("win") 
} 

for (let i = 1; i < 27; i++) { 
    document.children[0].children[1].children[i].addEventListener("click", tries2)
} 

function youLost()  { 
    document.children[0].children[1].innerHTML = `YOU LOSE!!  <button class='again' onclick= 'playagain()'> Try Again </button>`
    document.children[0].children[1].classList.add("win") 
}


function check() { 
    if (event.target.innerHTML == rand26) {
            youwon()
    } 
   else if (tries == 10) { 
       youLost()
   }
} 

for (let i = 1; i < 27; i++) { 
    document.children[0].children[1].children[i].addEventListener("click", check)
} 



