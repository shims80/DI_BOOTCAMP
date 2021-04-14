// Exercise 1 : Your Favorite Colors :
// let colors = ["blue", "yellow", "red", "orange"];
// let suffix = ["st ", "nd ", "rd ", "th "];
// for (let i = 0; i < colors.length; i++) {
//     console.log(`my ${i + 1}${suffix[i]} color is ${colors[i]}`);
// }

// // Exercise 2 : List Of People:
let people = ["Greg", "Mary", "Devon", "James"]
people.shift();
console.log(people);

people.splice(2, 1, 'jason');
console.log(people);

people.push("shimon");
console.log(people);

for (let i = 0; i < people.length; i++) {
    if (i === 3) {
        break
    }
    console.log(people[i]);
}

let copy = people.slice(1, 3);
console.log(copy);

console.log(people.indexOf("Mary"));

console.log(people.indexOf("Foo"));
//Why does it return -1? because foo is not in the list?

let last = people[people.length - 2];
console.log(last);

// Exercise 3 : Repeat The Question:
// let number = 10;
// while (number < 10) {
//     prompt("please enter a new number")
//     if (typeof number === "number")
//         console.log("by by")
// }