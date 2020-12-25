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

It is some kind of bottom up DP. But we kinda of reverse the transition equations, trying to see how the current value contributes to future values, according to transitions.
This kind of DP is kind of easier to implement most of the time.
By the time we arrive to a specific value, we already have added all the previous contributions, so that we know the current value, and we are ready to use it to update future values.
Can see solutions to DP_mashup_list_Colin_Galen/Problem_A and DP_mashup_list_Colin_Galen/Problem_B for examples of push back DP.

### Bitmask DP

Great playlist about bitmask DP here:
https://www.youtube.com/watch?v=6sEFap7hIl4&list=PLb3g_Z8nEv1icFNrtZqByO1CrWVHLlO5g

I didnt watch yet, but there is also an aglo live on it(more advanced i guess):
https://www.youtube.com/watch?v=rlTkd4yOQpE

Bitmask DP is a type of dynamic programming that uses bitmasks, in order to keep track of our current state in a problem.
It is just a fancy way to say that we represent the current state (or part of the current state) as a binary number. 

Imagine we have 3 booleans to describe the current state. We could use those 3 variables. But we can also say that each of those 3 represent a digit of a binary number between 0 and 7. And the code will be easier and faster to write.

Another very common situation is to describe states that are actually sbusets of something. It makes a lot of sense to represent a given subset as a binaray number, so that we can perform bitwise operation on this binary number later.

To sum up: Bitmask DP can be usefull if we have a bunch of booleans to describe the current state. A binary number can then group them together to make the state and the redaction of the code will be more manageable.

Example: see solutions of DP_mashup_list_Colin_Galen/Problem_C, with and without bitmask, to see how the bitmask simplifies the code



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

Here is the list of mashup DP problems from Colin Galen:
https://codeforces.com/gym/302977

Solutions to all problems are in this repo. All solutions in this repo have been "Approved" on Codeforces.

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

