// JavaScript Module 2
//
// Tehtävä 2.1

function reverseList() {
  let numbers = [];
  for (let i = 0; i < 5; i++) {
    numbers.push(parseInt(prompt("Enter a number:")));
  }
  console.log(numbers.reverse());
  document.querySelector("#reverseListTarget").innerHTML =
    "Check JavaScript console!";
}

export default {
  reverseList,
};
