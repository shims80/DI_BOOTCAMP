// Exercise 1 : Keyless Car:
function myBill(shoppingList) {
    let stock = {
        "banana": 6,
        "apple": 0,
        "pear": 12,
        "orange": 32,
        "blueberry": 1
    }
    let prices = {
        "banana": 4,
        "apple": 2,
        "pear": 1,
        "orange": 1.5,
        "blueberry": 10
    }
    let availabeItems = []
    let totalPrice = 0;
    for (let i of shoppingList) {
        if (i in stock == false) {
            availabeItems.push(`${i} not in stock`);
        } else {
            for (let j in stock) {
                if (i == j && stock[j] > 0) {
                    totalPrice += prices[j];
                    stock[j] -= 1;
                    availabeItems.push(`${i} is in stock`);
                }
                else if (i == j && stock[j] == 0) {
                    availabeItems.push(`${i} is not in stock`);
                }
            }
        }
    }
    console.log(availabeItems);
    console.log(totalPrice);
    console.log(stock);
}
let add = true;
let shopList = []
// let con;
while (add == true) {
    item = prompt('Add Item to shopping list:')
    shopList.push(item);
    add = confirm("Do you wish to add more items?");
}
myBill(shopList);


