// Tehtävä 1.1
function printToConsole() {
  console.log("I'm printing to console");
}

printToConsole();

// Tehtävä 1.2
function greetUser() {
  document.querySelector("#target").innerHTML =
    "Hello, " + prompt("Type your name.") + "!";
}

// Tehtävä 1.3
function calculateNumbers() {
  let intlist = [];
  for (let i = 0; i < 3; i++) {
    intlist.push(parseInt(prompt("Give a number.")));
  }

  const sum = intlist.reduce((acc, curr) => acc + curr, 0);
  const product = intlist.reduce((acc, curr) => acc * curr, 1);
  const average = Math.round(sum / intlist.length);

  document.querySelector("#INTtarget").innerHTML =
    "Sum of numbers: " +
    sum +
    "<br>Product of numbers: " +
    product +
    "<br>Average of numbers: " +
    average;
}

// Tehtävä 1.4
function assignHogwartsHouse() {
  const houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"];
  const randomHouse = houses[Math.floor(Math.random() * houses.length)];
  document.querySelector("#house").innerHTML =
    prompt("Student's name?") +
    ", you have been sorted into " +
    randomHouse +
    "!";
}

// Tehtävä 1.5
function isLeapYear() {
  const year = parseInt(prompt("Enter a year:"));
  const isLeap = (year % 4 === 0 && year % 100 !== 0) || year % 400 === 0;
  document.querySelector("#year").innerHTML =
    year + " is " + (isLeap ? "a leap year." : "not a leap year.");
}

// Tehtävä 1.6
function calculateSquareRoot() {
  const msg = confirm("Should I calculate the square root?")
    ? ((n) =>
        n >= 0
          ? `The square root of ${n} is ${Math.sqrt(n).toFixed(3)}.`
          : "Cannot calculate the square root of a negative number.")(
        parseFloat(prompt("Enter a number:")),
      )
    : "The square root is not calculated.";
  document.querySelector("#square").innerHTML = msg;
}

// Tehtävä 1.7
function rollDice() {
  let rolls = parseInt(prompt("Enter the number of dice rolls:"));
  let sum = 0;
  for (let i = 0; i < rolls; i++) {
    sum += Math.floor(Math.random() * 6) + 1;
  }
  document.querySelector("#diceResult").innerHTML =
    "Sum of dice is " + sum + ".";
}

// Tehtävä 1.8
function printLeapYears() {
  let start = parseInt(prompt("Enter start year:"));
  let end = parseInt(prompt("Enter end year:"));
  let listElement = document.getElementById("leapYearsList");
  listElement.innerHTML = "";

  for (let year = start; year <= end; year++) {
    if (year % 4 === 0 && (year % 100 !== 0 || year % 400 === 0)) {
      let li = document.createElement("li");
      li.textContent = year;
      listElement.appendChild(li);
    }
  }
}

// Tehtävä 1.9
// Ehkä kerrankin parempi käyttää "f-stringiä"
function isPrime(num) {
  if (num < 2) return false;
  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i === 0) return false;
  }
  return true;
}

function checkPrime() {
  let number = parseInt(prompt("Enter an integer:"));
  let result = isPrime(number)
    ? "is a prime number."
    : "is not a prime number.";
  document.getElementById("primeResult").textContent = `${number} ${result}`;
}

// Tehtävä 1.10
function simulateDiceProbability() {
  let numDice = parseInt(prompt("Enter the number of dice:"));
  let targetSum = parseInt(prompt("Enter the sum of interest:"));
  let trials = 10000;
  let success = 0;

  for (let i = 0; i < trials; i++) {
    let sum = 0;
    for (let j = 0; j < numDice; j++) {
      sum += Math.floor(Math.random() * 6) + 1;
    }
    if (sum === targetSum) success++;
  }

  let probability = ((success / trials) * 100).toFixed(3);
  document.getElementById("probabilityResult").textContent =
    `Probability to get sum ${targetSum} with ${numDice} dice is ${probability}%`;
}

export default {
  greetUser,
  calculateNumbers,
  assignHogwartsHouse,
  isLeapYear,
  calculateSquareRoot,
  rollDice,
  printLeapYears,
  checkPrime,
  simulateDiceProbability,
};
