import React from "react";
import "./index.css";
import mod1 from "./JS/JSmod1.js";
import mod2 from "./JS/JSmod2.js";

function App() {
  return (
    <div className="hstack">
      <div className="box">
        <h2>JavaScript Module 1</h2>

        <button onClick={mod1.printToConsole}>Console Printer</button>
        <p id="consoleTarget"></p>

        <button onClick={mod1.greetUser}>Greeting Program</button>
        <p id="target"></p>

        <button onClick={mod1.calculateNumbers}>Number Calculator</button>
        <p id="INTtarget"></p>

        <button onClick={mod1.assignHogwartsHouse}>House Assigner</button>
        <p id="house"></p>

        <button onClick={mod1.isLeapYear}>Leap Year Calculator</button>
        <p id="year"></p>

        <button onClick={mod1.calculateSquareRoot}>
          Square Root Calculator
        </button>
        <p id="square"></p>

        <button onClick={mod1.rollDice}>Dice Roller</button>
        <p id="diceResult"></p>

        <button onClick={mod1.printLeapYears}>Leap Year Printer</button>
        <p id="leapYearsList"></p>

        <button onClick={mod1.checkPrime}>Prime Checker</button>
        <p id="primeResult"></p>

        <button onClick={mod1.simulateDiceProbability}>Dice Simulator</button>
        <p id="probabilityResult"></p>
      </div>
      <div className="box">
        <h2>JavaScript Module 2</h2>

        <button onClick={mod2.reverseList}>Reverse List</button>
        <p id="reverseListTarget"></p>
      </div>
    </div>
  );
}

export default App;
