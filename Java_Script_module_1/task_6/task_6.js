const result = document.getElementById("result");

if (confirm("Should I calculate the square root?")) {
  const number = Number(prompt("Enter a number:"));

  if (number < 0) {
    result.textContent = "The square root of a negative number is not defined";
  } else {
    result.textContent = `The square root is ${Math.sqrt(number)}.`;
  }
} else {
  result.textContent = "The square root is not calculated.";
}