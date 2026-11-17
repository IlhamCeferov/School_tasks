const input = prompt("Enter a year:");
const year = Number(input);
const result = document.getElementById("result");

if (input === null) {
  result.textContent = "No year was entered.";
} else if (!Number.isInteger(year) || year <= 0) {
  result.textContent = "Please enter a valid positive year.";
} else if (year % 400 === 0 || (year % 4 === 0 && year % 100 !== 0)) {
  result.textContent = `${year} is a leap year.`;
} else {
  result.textContent = `${year} is not a leap year.`;
}