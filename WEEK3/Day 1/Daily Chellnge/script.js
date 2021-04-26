let solar = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"], arrayLength = solar.length;
let colors = ["green", "white", "blue", "red", "yellow", "brown", "turquoise", "darkblue"]

for (let i = 0; i < 7; i++) {
    const solar_name = document.createElement("div")
    document.body.appendChild(solar_name);
    solar_name.setAttribute("class", "plant")
    solar_name.appendChild(document.createTextNode("plant"));
    document.body.appendChild(solar_name);
    console.log(solar_name);
    let plantbackgroundcolor = document.getElementsByClassName("plant")[i].style.backgroundColor = colors[i];
}





