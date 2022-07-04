<H1 align="center">
    The-Hyperactive-Software-Stack
</H1>

<br>

## Shared data-structures

The hyperactive software stack builds upon some shared data-structures to reliably communicate between packages:

- objective-function
  - A function that returns a single score or a tuple of a score and a dictionary. Its only argument is a dictionary in Gradient-Free-Optimizers and a more complex object that behaves like a dictionary in Hyperactive.
- search-space
  - A dictionary with the names of the dimensions as keys and the content of the dimensions as values. In Gradient-Free-Optimizers the values are numpy arrays and Hyperactive they are lists.
- search-data
  - The search-data always consists of the score and at least one parameter as columns and has as much rows as iterations performed during the optmization run.


## The official Hyperactive software stack

- [Hyperactive](https://github.com/SimonBlanke/Hyperactive)
  - The central library for the Hyperactive software stack.

- [Gradient-Free-Optimizers](https://github.com/SimonBlanke/Gradient-Free-Optimizers)
  - The optimization-backend for Hyperactive.

- [Experimental-Optimization-Strategies](https://github.com/SimonBlanke/Experimental-Optimization-Strategies)
  - An extension with experimental optimization algorithms.

- [optimization-tutorial](https://github.com/SimonBlanke/optimization-tutorial)
  - Interactive documentation for the optimization algorithms.

- [Surfaces](https://github.com/SimonBlanke/Surfaces)
  - A collection of test-objective-functions.

- [Tabular Data Explorer](https://github.com/SimonBlanke/tabular-data-explorer)
  - Dashboard to visually analyse saved search-data.

- [Progress Board](https://github.com/SimonBlanke/ProgressBoard)
  - Visualize the progress of optimization runs in a dashboard.

- [Simple Data Collector](https://github.com/SimonBlanke/simple-data-collector)
  - Thread safe and atomic data collection into csv-files.


