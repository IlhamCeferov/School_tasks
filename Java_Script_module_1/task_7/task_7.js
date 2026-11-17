const input = prompt("How many dice rolls?");
const numberOfRolls = Number(input);
const result = document.getElementById("result");

if (input === null) {
  result.textContent = "Dice were not rolled.";
} else if (!Number.isInteger(numberOfRolls) || numberOfRolls < 1) {
  result.textContent = "Enter a positive whole number of rolls.";
} else {
  let sum = 0;

  for (let roll = 0; roll < numberOfRolls; roll++) {
    sum += Math.floor(Math.random() * 6) + 1;
  }

  result.textContent = `Sum of the dice rolls: ${sum}`;
}