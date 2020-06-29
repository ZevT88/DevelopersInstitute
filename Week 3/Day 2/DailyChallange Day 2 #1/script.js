let world = document.children[0].children[1].children[0]
function color() { 
    world.classList.add("color")

}
 world.addEventListener("mouseover", color)  


function center() { 

    world.classList.add("center")  

}

world.addEventListener("click", center)  
 


function color2() { 
    
    world.classList.add("color2")

}

world.addEventListener("mouseout", color2)
 
function bigger() { 

    world.classList.add("bigger")
}


world.addEventListener("mousemove", bigger ) 