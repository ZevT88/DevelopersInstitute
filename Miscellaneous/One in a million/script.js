

function five() { 
    let a = Math.floor(Math.random() * 5 + 1)  
    let b = Math.floor(Math.random() * 5 + 1)  
    let c = Math.floor(Math.random() * 1000001)  
    let d = Math.floor(Math.random() * 1000001)  
    document.children[0].children[1].children[1].innerHTML = `${a}` 
    document.children[0].children[1].children[2].innerHTML = `${b}` 
    if (a == b) { 
         document.children[0].children[1].children[0].innerHTML = "!!!!!!!"
    } 
    else { 
        document.children[0].children[1].children[0].innerHTML = "One in a Five!"
    }

} 

function ten() { 
    let a = Math.floor(Math.random() * 10 + 1)  
    let b = Math.floor(Math.random() * 10 + 1)  
    let c = Math.floor(Math.random() * 1000001)  
    let d = Math.floor(Math.random() * 1000001)  
    document.children[0].children[1].children[1].innerHTML = `${a}` 
    document.children[0].children[1].children[2].innerHTML = `${b}` 
    if (a == b) { 
         document.children[0].children[1].children[0].innerHTML = "!!!!!!!"
    } 
    else { 
        document.children[0].children[1].children[0].innerHTML = "One in a Ten!"
    }

} 


function hundred() { 
    let a = Math.floor(Math.random() * 100 + 1)  
    let b = Math.floor(Math.random() * 100 + 1)  
    let c = Math.floor(Math.random() * 1000001)  
    let d = Math.floor(Math.random() * 1000001)  
    document.children[0].children[1].children[1].innerHTML = `${a}` 
    document.children[0].children[1].children[2].innerHTML = `${b}` 
    if (a == b) { 
         document.children[0].children[1].children[0].innerHTML = "!!!!!!!"
    } 
    else { 
        document.children[0].children[1].children[0].innerHTML = "One in 100!"
    }

}  

function thousand() { 
    let a = Math.floor(Math.random() * 1000 + 1)  
    let b = Math.floor(Math.random() * 1000 + 1) 
    let c = Math.floor(Math.random() * 1000001)  
    let d = Math.floor(Math.random() * 1000001)  
    document.children[0].children[1].children[1].innerHTML = `${a}` 
    document.children[0].children[1].children[2].innerHTML = `${b}` 
    if (a == b) { 
         document.children[0].children[1].children[0].innerHTML = "!!!!!!!"
    } 
    else { 
        document.children[0].children[1].children[0].innerHTML = "One in 1,000!"
    }

}  



function million(){
    let a = Math.floor(Math.random() * 1000000 + 1)  
    let b = Math.floor(Math.random() * 1000000 + 1)  
    document.children[0].children[1].children[1].innerHTML = `${a}` 
    document.children[0].children[1].children[2].innerHTML = `${b}` 
    if (a == b) { 
        document.children[0].children[1].children[0].innerHTML = "HOW"
   } 
   else { 
       document.children[0].children[1].children[0].innerHTML = "One in a 1,000,000!"
   }


} 



function billion() { 
    let a = Math.floor(Math.random() * 10000000000 + 1)  
    let b = Math.floor(Math.random() * 10000000000 + 1)  
    let c = Math.floor(Math.random() * 100000001)  
    let d = Math.floor(Math.random() * 100000001)  
    document.children[0].children[1].children[1].innerHTML = `${a}` 
    document.children[0].children[1].children[2].innerHTML = `${b}` 
    if (a == b) { 
         document.children[0].children[1].children[0].innerHTML = "!!!!!!!"
    } 
    else { 
        document.children[0].children[1].children[0].innerHTML = "One in 1,000,000,000!"
    }

}  

function five2() { 
    for (let i = 1; i < 6; i++)
        five()
}