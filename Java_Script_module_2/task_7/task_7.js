function rollDice(numberOfSides) {
  return Math.floor(Math.random() * numberOfSides) + 1;
}

const sidesInput = prompt("Enter the number of sides on the dice:");

if (sidesInput !== null) {
  const numberOfSides = Number(sidesInput);

  if (!Number.isInteger(numberOfSides) || numberOfSides < 1) {
    alert("Enter a positive whole number of sides.");
  } else {
    const rollsList = document.createElement("ul");
    let result;

    do {
      result = rollDice(numberOfSides);
      const listItem = document.createElement("li");
      listItem.textContent = result;
      rollsList.appendChild(listItem);
    } while (result !== numberOfSides);

    document.body.appendChild(rollsList);
  }
}