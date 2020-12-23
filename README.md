<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/IAbeteEtMechante/Dynamic_programming">
    <img src="Images/fibonacci-naive.png" alt="Logo" width="160" height="160">
  </a>

  <h3 align="center">Dynamic programming</h3>

  <p align="center">
    Solutions to some Dynamic Programming problems from Codeforces (with Python)
    <br />
    <a href="https://codeforces.com/gym/302977"><strong>List of problems »</strong></a>
    <br />
    <br />
    <a href="https://github.com/IAbeteEtMechante/Dynamic_programming">Solutions</a>
    ·
    <a href="https://github.com/IAbeteEtMechante/Dynamic_programming/issues">Report Bug</a>
    ·
    <a href="https://github.com/IAbeteEtMechante/Dynamic_programming/issues">Ask a question</a>
  </p>
</p>

<br>
<br>

The goal of this repo is to solve a list of DP problems from Codeforces with Python.
<br>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [General concepts](#general-concepts)
* [When to use DP?](#when-to-use-dp)
* [Tips](#tips)
* [List of problems with solutions](#list-of-problems-with-solutions)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)


<!-- GENERAL CONCEPTS -->
## General Concepts

### Memoization

### Bottom up

### Push DP
Kind of easier to implement, we just try to see how the current value contributes to future values, according to transitions.

### Bitmask DP

Bitmask DP is a type of dynamic programming that uses bitmasks, in order to keep track of our current state in a problem.
It is just a fancy way to say that we represent the current state (or part of the current state) as a binary number. 

Imagine we have 3 booleans to describe the current state. We could use that. But we can also say that each of those 3 represent a digit of a binary number between 0 and 7. And the code will be easier and faster to write.

To sum up: Bitmask DP can be usefull if we have a bunch of booleans to describe the current state. A binary number can then group them together to make the state and the redaction of the code more manageable.

<!-- WHEN TO USE DP -->
## When to use DP?

If there is no plausible state to store the answer, it probably isn't DP.

The way to determine if you can use DP is just....to check if you can use DP.

When you are trying to solve a problem you just try different directions. With experience you get a better intuition on which direction is more likely to work than others.

<!-- TIPS -->
## Tips

### Tip 1

Often it is better to start by finding the transitions. Then find the base cases. Because it is easy to know how many bases cases you need once you have all the transitions.


### Tip 2

If you cannot do DP with a simple state, you need to try to "fix" = determinate one variable in the problem.

### Tip 3

Is knapsack DP?
Yes

### Tip 4

Is greedy DP?
Sometimes, but generally not

<!-- LIST OF PROBLEMS WITH SOLUTIONS -->
## List of problems with solutions

Here is the list of DP problems on Codeforces:
https://codeforces.com/gym/302977

Solutions to problems are in this repo. All solutions in this repo have been "Approved" on Codeforces.

<!-- CONTACT -->
## Contact

Feel free to contact us on this repo, I am happy to hear from you.

Project Link: [https://github.com/IAbeteEtMechante/Dynamic_programming](https://github.com/IAbeteEtMechante/Dynamic_programming)




<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
Great video from Galen Colin:
https://www.youtube.com/watch?v=zDEQaDl3cso
<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[fibo-logo]: Images/fibonacci-naive.png

