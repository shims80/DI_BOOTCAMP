// Exercise 1
// let age;
// age = +prompt('Enter a number your age!');
// if (age<18) {
//     alert('Sorry, You are too young to drive this car. Powering off.');
// } else if (age==18) {
//     alert('Congrts on your first year of driving. Enjoy!');
// } else if (age>18) {
//     alert('Powering On. Enjoy the ride!');
// }

let age;
let b = false;
let c = false;
while (b==false || c==false) {
//+prompt takes arguable and makes it an integer
    age = +prompt('Enter a number your age!');
    b = confirm('Confirm Your Choice!');
    c = Number.isInteger(age);
    if (c==false) {
        alert('NEXT TIME ENTER AN AGE!')
    }
}
if (age<18) {
    alert('Sorry, You are too young to drive this car. Powering off.');
} else if (age==18) {
    alert('Congrts on your first year of driving. Enjoy!');
} else if (age>18) {
    alert('Powering On. Enjoy the ride!');
}