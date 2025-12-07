# Game-Theory-Fox-and-Holes

This repository contains all the code used to analyse the **Fox and Holes game** studied in the accompanying report. 
All figures appearing in the report were generated using the Python scripts of this repository. 

We approached this game using three different methods:

1. A farmer picking a random hole each day, and a fox hiding randomly in adjacent holes.

2. A farmer picking a specific hole each day using the double-sweep strategy, with a randomly moving fox.

3. A farmer using the double-sweep strategy, and a smart fox responding strategically.


## Usage
The scripts are **independent**. 
Each one produces a specific figure or simulation related to the game : 

### RandomFarmerStrategyValidation.py
Implements a random Farmer strategy to validate the theoretical result (this theoretical result claims that the expected cost of the random farmer strategy is equal to the number of holes n).

### randomOneGameHistory.py
Runs a single instance of the game with random behaviour from both players, and displays a plot of the full history.

### optimalFarmerStrategy.py
Implements the Farmer’s optimal *double-sweep* search strategy. It provides the deterministic sequence of positions that guarantees eventual capture of any Fox hiding randomly in adjacent holes. It also implements the evaluation of the average performance of this approach compared to the random one. 

### optimalFarmerStratHistory.py
Simulates the game when the Farmer uses the optimal strategy (fox using random strategy) and displays a plot of the full history of positions. 

### OptimalFoxOptimalFarmer.py
Analyzes the scenario where **both the Farmer and the Fox behave optimally**. In this case both strategies are pure strategies and the payoffs and costs depend only on n. 

You may adjust the parameters:

- `n` — number of holes.
- `N` — number of simulated plays of the game. 

to reproduce or extend the results.
