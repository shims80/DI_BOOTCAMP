function playTheGame() {
    let answer = confirm("would you like to play the game ?");
    // console.log(answer);
    let inputenumbers = +prompt("enter a number between 0 and 10");
    if (answer) {
        if (isNaN(inputenumbers)) {
            alert("Sorry Not a number, Goodbye");
        } else if (inputenumbers > 10) {
            console.log("Sorry it’s not a good number, Goodby");
        }
        else {
            let computerNumber = Math.floor(Math.random() * 10);
        }
    }
    else {
        alert("goodbye!");
    }
}

// Second Part :
function test(userNumber, computerNumber) {
    let turn = 0;
    while (turn < 3) {
        let computernum = Math.floor(Math.random() * 11);
        let userNumber = +prompt("0 - 10");
        if (computernum === userNumber) {
            console.log("winner");
            break;
        }
        turn += 1;
    }

}

