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

export default {
  reverseList,
};
