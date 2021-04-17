// Exercise 1 : Keyless Car:
// let age = parseInt(prompt("what is your age?"));

// function checkDriverAge(age) {

//     if (age < 18) {
//         alert("Sorry, you are too young to drive this car. Powering off");
//     }
//     else if (age === 18) {
//         alert("Congratulations on your first year of driving. Enjoy the ride!");
//     }
//     else if (age > 18) {
//         alert("You are old enough to drive, Powering On. Enjoy the ride!");
//     }
// }
// checkDriverAge(age)


// // Exercise 2 : What’s In My Wallet ?:
// let values = [0.25, 0.10, 0.05, 0.01];
// function changeEnough(change, itemCost) {
//     var sum = 0;
//     for (let i = 0; i < change.length; i++) {
//         sum += change[i] * values[i];
//     }
//     if (sum >= itemCost) {
//         console.log(true);
//     } else {
//         console.log(false);
//     }
// }
// changeEnough([2, 0, 20, 100], 1.00);
// 
// 
// Exercise 3: Find The Multiples Of 23:
// let sum = 0;
// for (let i = 0; i < 500; i++) {
//     if (i % 23 === 0) {
//         sum += i;
//         console.log(i);
//     }
// }
//
// Exercise 4 : Amazon Shopping
// function checkBasket(basket) {
//     let item = prompt('Enter an item');
//     if (item in basket) {
//         return true;
//     } else {
//         return false;
//     }
// }

// let amazonBasket = {
//     glasses: 1,
//     books: 2,
//     floss: 100
// };
// console.log(checkBasket(amazonBasket));
//
// Exercise 5 : Shopping List
// function myBill(shoppingList) {
//     let stock = {
//         "banana": 6,
//         "apple": 0,
//         "pear": 12,
//         "orange": 32,
//         "blueberry": 1
//     }
//     let prices = {
//         "banana": 4,
//         "apple": 2,
//         "pear": 1,
//         "orange": 1.5,
//         "blueberry": 10
//     }
//     let availabeItems = []
//     let totalPrice = 0;
//     for (let i of shoppingList) {
//         if (i in stock == false) {
//             availabeItems.push(`${i} not in stock`);
//         } else {
//             for (let j in stock) {
//                 if (i == j && stock[j] > 0) {
//                     totalPrice += prices[j];
//                     stock[j] -= 1;
//                     availabeItems.push(`${i} is in stock`);
//                 }
//                 else if (i == j && stock[j] == 0) {
//                     availabeItems.push(`${i} is not in stock`);
//                 }
//             }
//         }
//     }
//     console.log(availabeItems);
//     console.log(totalPrice);
//     console.log(stock);
// }
// let add = true;
// let shopList = []
// // let con;
// while (add == true) {
//     item = prompt('Add Item to shopping list:')
//     shopList.push(item);
//     add = confirm("Do you wish to add more items?");
// }
// myBill(shopList);
//
// Exercise 6 : Tips:
// fanction calculator (tips) {
//     let bill = $("#bill").value;
//     let tip = bill * 0.2;
//     let Final bill = bill + tip;
// {
//     if (bill < 50 * 0.2) {
//
//     }else if {
//         (bill is === 50 || tips is < 200 * 0.15 )
//     }
//     else (if bill > 200 0.1)
//     }
// }
//

