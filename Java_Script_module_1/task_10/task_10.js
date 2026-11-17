const diceInput = prompt("How many dice?");
const sumInput = diceInput === null ? null : prompt("What sum are you interested in?");
const result = document.getElementById("result");

if (diceInput === null || sumInput === null) {
  result.textContent = "The simulation was cancelled.";
} else {
  const numberOfDice = Number(diceInput);
  const targetSum = Number(sumInput);

  if (
    !Number.isInteger(numberOfDice) ||
    numberOfDice < 1 ||
    !Number.isInteger(targetSum)
  ) {
    result.textContent = "Enter a positive whole number of dice and an integer sum.";
  } else {
    const simulations = 10000;
    let matchingRolls = 0;

    for (let simulation = 0; simulation < simulations; simulation++) {
      let sum = 0;

      for (let die = 0; die < numberOfDice; die++) {
        sum += Math.floor(Math.random() * 6) + 1;
      }

      if (sum === targetSum) {
        matchingRolls++;
      }
    }

    const probability = (matchingRolls / simulations) * 100;
    result.textContent =
      `Probability to get sum ${targetSum} with ${numberOfDice} dice is ${probability.toFixed(2)}%`;
  }
}