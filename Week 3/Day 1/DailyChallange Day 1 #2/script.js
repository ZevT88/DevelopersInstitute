let planets = ["earth", "jupiter", "neptune", "mars", "saturn", "uranus", "venus", "mercury"]
let class_names = ["turquoise", "pink", "blue", "green", "white", "orange", "red", "lightblue"]
let moons = [1, 69, 14, 2, 62, 27, 0, 0]

let section = document.getElementsByTagName('section')[0]

for (let i = 0; i < planets.length; i++) {
    let div = document.createElement("div")
    let text = document.createTextNode(planets[i])
    div.appendChild(text)
    div.classList.add("planet", class_names[i])
    div.style.backgroundColor = class_names[i]
    section.appendChild(div)

    console.log(moons[i])
    let ml = 120
    if (moons[i] != 0) {
        for (let h = 0; h < moons[i]; h++) {
            ml += 50
            let div_moon = document.createElement("div")
            div_moon.classList.add("moon")
            div_moon.style.marginLeft = ml + "px"
            div.appendChild(div_moon)
        }
    }
}