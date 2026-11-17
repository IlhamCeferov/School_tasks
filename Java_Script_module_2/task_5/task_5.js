const numbers = [];

while (true) {
  const number = Number(prompt("Enter a number:"));

  if (numbers.includes(number)) {
    alert("That number has already been given.");
    break;
  }

  numbers.push(number);
}

numbers.sort((first, second) => first - second);

for (const number of numbers) {
  console.log(number);
}