// JavaScript Module 2
//
// Tehtävä 2.1
function reverseList() {
  let numbers = [];
  for (let i = 0; i < 5; i++) {
    numbers.push(parseInt(prompt("Enter a number:")));
  }
  for (let i = 5; i > 0; i--) {
    console.log(numbers[i - 1]);
  }
  document.querySelector("#reverseListTarget").innerHTML =
    "Check JavaScript console!";
}

// Tehtävä 2.2

function participantList() {
  const count = Number(prompt("How many participants?"));
  const names = [];

  for (let i = 0; i < count; i++) {
    names.push(prompt(`Enter name for participant ${i + 1}:`));
  }

  names.sort();

  let html = "<ol>";
  for (const name of names) {
    html += `<li>${name}</li>`;
  }
  html += "</ol>";

  document.querySelector("#participants").innerHTML = html;
}

export default {
  reverseList,
  participantList,
};
