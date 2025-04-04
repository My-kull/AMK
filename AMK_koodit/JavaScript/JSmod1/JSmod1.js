// Tehtävä 1.1

console.log("I'm printing to console");

// Tehtävä 1.2

document.querySelector("#target").innerHTML =
  "Hello, " + prompt("Type your name.") + "!";

// Tehtävä 1.3

let intlist = [];

for (let i = 0; i < 3; i++) {
  intlist.push(parseInt(prompt("Give a number.")));
}

const sum = intlist.reduce(
  (accumulator, currentValue) => accumulator + currentValue,
  0,
);

const product = intlist.reduce(
  (accumulator, currentvalue) => accumulator * currentvalue,
  1,
);

const average = Math.round(sum / intlist.length);

document.querySelector("#INTtarget").innerHTML =
  "Sum of numbers: " +
  sum +
  "<br>Product of numbers: " +
  product +
  "<br>Average of numbers: " +
  average;

// Tehtävä 1.4

const houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"];
const randomhouse = houses[Math.floor(Math.random() * houses.length)];
document.querySelector("#house").innerHTML =
  prompt("Student's name?") +
  ", you have been sorted into " +
  randomhouse +
  "!";

// Tehtävä 1.5

const year = parseInt(prompt("Enter a year."));
const isLeap = (year % 4 === 0 && year % 100 !== 0) || year % 400 === 0;
document.querySelector("#year").innerHTML =
  year + " is " + (isLeap ? "a leap year." : "not a leap year.");

// Tehtävä 1.6
