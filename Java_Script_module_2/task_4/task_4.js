const numbers = [];
let number = Number(prompt("Enter a number (0 to stop):"));

while (number !== 0) {
  numbers.push(number);
  number = Number(prompt("Enter a number (0 to stop):"));
}

numbers.sort((first, second) => second - first);

for (const number of numbers) {
  console.log(number);
}