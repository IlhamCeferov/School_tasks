function even(numbers) {
  return numbers.filter((number) => number % 2 === 0);
}

const numbers = [2, 7, 4];
const evenNumbers = even(numbers);

console.log("Original array:", numbers);
console.log("Even numbers:", evenNumbers);