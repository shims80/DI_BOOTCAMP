let firstNum = [];
let secondNum;
let operation;
function number(num) {
    firstNum.push(num);
}
function operator(op) {
    secondNum = parseInt(firstNum.join(''));
    firstNum = [];
    operation = op;

}
function equal() {
    firstNum = parseInt(firstNum.join(''));
    if (operation === '+') {
        console.log(secondNum + firstNum);
    } else if (operation === '-') {
        console.log(secondNum - firstNum);
    } else if (operation === '*') {
        console.log(secondNum * firstNum);
    } else {
        console.log(secondNum / firstNum);
    }
}
function clr() {
    firstNum = [];
    secondNum = 0;
    operation = ""
}
