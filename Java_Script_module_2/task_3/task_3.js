const dogNames = [];

for (let i = 0; i < 6; i++) {
  const name = prompt(`Enter the name of dog ${i + 1}:`);
  dogNames.push(name.trim());
}

dogNames.sort((first, second) => second.localeCompare(first));

const dogList = document.createElement("ul");

for (const name of dogNames) {
  const listItem = document.createElement("li");
  listItem.textContent = name;
  dogList.appendChild(listItem);
}

document.body.appendChild(dogList);