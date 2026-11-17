    const participantCount = Number(prompt("Enter the number of participants:"));
    const participants = [];

    for (let i = 0; i < participantCount; i++) {
    const name = prompt(`Enter the name of participant ${i + 1}:`);
    participants.push(name.trim());
    }

    participants.sort((first, second) => first.localeCompare(second));

    const orderedList = document.createElement("ol");

    for (const name of participants) {
    const listItem = document.createElement("li");
    listItem.textContent = name;
    orderedList.appendChild(listItem);
    }

    document.body.appendChild(orderedList);