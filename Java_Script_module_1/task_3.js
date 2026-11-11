function promptInteger(message) {
  while (true) {
    const input = prompt(message);

    if (input === null) {
      return null;
    }

    const number = Number(input);
    if (Number.isInteger(number)) {
      return number;
    }

    alert("Please enter an integer.");
  }
}

const first = promptInteger("Enter the first integer:");
const second = first === null ? null : promptInteger("Enter the second integer:");
const third = second === null ? null : promptInteger("Enter the third integer:");

if (third !== null) {
  const sum = first + second + third;
  const product = first * second * third;
  const average = sum / 3;

  document.getElementById("results").textContent =
    `Sum: ${sum}\nProduct: ${product}\nAverage: ${average}`;
}