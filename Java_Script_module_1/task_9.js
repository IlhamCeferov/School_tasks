const input = prompt("Enter an integer:");
const number = Number(input);
const result = document.getElementById("result");

if (input === null) {
  result.textContent = "No number was entered.";
} else if (!Number.isInteger(number)) {
  result.textContent = "Please enter a valid integer.";
} else {
  let isPrime = number >= 2;

  for (let divisor = 2; isPrime && divisor <= Math.sqrt(number); divisor++) {
    if (number % divisor === 0) {
      isPrime = false;
    }
  }

  result.textContent = isPrime
    ? `${number} is a prime number.`
    : `${number} is not a prime number.`;
}