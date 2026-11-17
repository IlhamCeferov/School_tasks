const studentName = prompt("What is the student's name?");

if (studentName !== null && studentName.trim() !== "") {
  const houseNumber = Math.floor(Math.random() * 4) + 1;
  let house;

  switch (houseNumber) {
    case 1:
      house = "Gryffindor";
      break;
    case 2:
      house = "Slytherin";
      break;
    case 3:
      house = "Hufflepuff";
      break;
    default:
      house = "Ravenclaw";
  }

  document.getElementById("result").textContent =
    `${studentName.trim()}, you are ${house}.`;
}