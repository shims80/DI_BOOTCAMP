let lastP = document.querySelectorAll("p")[3];
let article = document.querySelector("article");

article.removeChild(lastP);

let h2 = document.querySelector("h2");
h2.addEventListener("click", bgcolor);

function bgcolor() {
    h2.style.backgroundColor = "red";
}

let h1 = document.querySelector("h1");
let fs = Math.floor(Math.random() * 100) + "px";
h1.style.fontSize = fs;


let h3 = document.querySelector("h3");
h3.addEventListener("click", hide);

function hide() {
    h3.style.display = "none";
}

let ps = document.querySelectorAll("p");
function mkbold() {
    for (let p of ps) {
        p.style.fontWeight = "bold";
    }
}

let sub = document.querySelector("#submit");
sub.addEventListener("click", inputinfo);


function inputinfo(e) {
    let sub = document.querySelector("#submit");
    sub.addEventListener("click", inputinfo);
    e.preventDefault();
    let firstName = document.getElementsByTagName("#fname").value;
    let lastName = document.querySelector("#lname").value;
    firstName.appendChild(lastName);
}


// Exercise 2 : Transform The Sentence :

// function getBold_items(){
// let bold_items = document.querySelectorall("p");

// }
