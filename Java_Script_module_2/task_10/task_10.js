function runVoting() {
  const candidateCount = Number(prompt("Enter the number of candidates:"));
  if (!Number.isInteger(candidateCount) || candidateCount < 1) {
    alert("Enter a positive whole number of candidates.");
    return;
  }

  const candidates = [];

  for (let i = 0; i < candidateCount; i++) {
    const name = prompt(`Name for candidate ${i + 1}:`);
    if (name === null) {
      return;
    }

    candidates.push({ name: name.trim(), votes: 0 });
  }

  const voterCount = Number(prompt("Enter the number of voters:"));
  if (!Number.isInteger(voterCount) || voterCount < 0) {
    alert("Enter a non-negative whole number of voters.");
    return;
  }

  for (let i = 0; i < voterCount; i++) {
    const vote = prompt(`Voter ${i + 1}, enter the candidate's name:`);
    if (vote === null || vote.trim() === "") {
      continue;
    }

    const candidate = candidates.find(
      (item) => item.name.toLowerCase() === vote.trim().toLowerCase()
    );

    if (candidate) {
      candidate.votes++;
    } else {
      alert(`No candidate named "${vote.trim()}". This vote was not counted.`);
    }
  }

  const results = [...candidates].sort(
    (first, second) => second.votes - first.votes
  );
  const winner = results[0];

  console.log(`The winner is ${winner.name} with ${winner.votes} votes.`);
  console.log("results:");

  for (const candidate of results) {
    console.log(`${candidate.name}: ${candidate.votes} votes`);
  }
}

runVoting();