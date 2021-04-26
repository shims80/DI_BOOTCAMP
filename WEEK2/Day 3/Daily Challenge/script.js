// using one loop :

var star = ("*", "**", "***", "****", "*****", "******");
var text = "";
var i;
for (i = 0; i < 6; i++) {
    text += star[i];
    console.log(text)
}

// using two nested for loops :

// var star = "*";
// for (i = 0; i < 6; i++) {
//     let star = "";
//     for (j = 0; j < i + 1; j++) {
//         star += "*"
//     }
//     console.log(star)
// }