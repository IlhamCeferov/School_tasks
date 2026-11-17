function rollDice() {
  return Math.floor(Math.random() * 6) + 1;
}

const rollsList = document.createElement("ul");
let result;

do {
  result = rollDice();
  const listItem = document.createElement("li");
  listItem.textContent = result;
  rollsList.appendChild(listItem);
} while (result !== 6);

document.body.appendChild(rollsList);