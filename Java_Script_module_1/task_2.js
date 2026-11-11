const nimi = prompt("What is your name?");

if (nimi !== null) {
  document.getElementById("greeting").textContent = `Hello, ${nimi}!`;
}