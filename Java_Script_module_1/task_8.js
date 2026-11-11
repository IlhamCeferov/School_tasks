function isLeapYear(year) {
  return year % 400 === 0 || (year % 4 === 0 && year % 100 !== 0);
}

const startInput = prompt("Enter the start year:");
const endInput = startInput === null ? null : prompt("Enter the end year:");
const results = document.getElementById("results");

if (startInput === null || endInput === null) {
  results.textContent = "Year range was not entered.";
} else {
  const startYear = Number(startInput);
  const endYear = Number(endInput);

  if (
    !Number.isInteger(startYear) ||
    !Number.isInteger(endYear) ||
    startYear <= 0 ||
    endYear <= 0 ||
    startYear > endYear
  ) {
    results.textContent = "Enter a valid range of positive years.";
  } else {
    const list = document.createElement("ul");

    for (let year = startYear; year <= endYear; year++) {
      if (isLeapYear(year)) {
        const item = document.createElement("li");
        item.textContent = year;
        list.appendChild(item);
      }
    }

    results.appendChild(list);
  }
}