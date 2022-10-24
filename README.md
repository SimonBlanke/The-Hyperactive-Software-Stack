<br>

<H1 align="center">
    The-Hyperactive-Software-Stack
</H1>

<br>

## Shared data-structures

The hyperactive software stack builds upon some shared data-structures to reliably communicate between packages:

- objective-function
  - A function that returns a single score or a tuple of a score and a dictionary. Its only argument is a dictionary in Gradient-Free-Optimizers and a more complex object that behaves like a dictionary in Hyperactive. This argument is often called `opt`, `para` or `access` in examples.
  
  <br>
  
   ```python
   # Hyperactive objective function
   def parabola_function(access):
       score = -(access["x"] * access["x"] + access["y"] * access["y"])
       return score
   ```
   
- search-space
  - A dictionary with the names of the dimensions as keys and the content of the dimensions as values. In Gradient-Free-Optimizers the values are numpy arrays and Hyperactive they are lists.
  
  <br>
  
   ```python
   # Hyperactive search space
   search_space = {
       "x": list(np.arange(-10, 10, 0.01)),
       "y": list(np.arange(-10, 10, 0.01)),
   }
   ```
  
- search-data
  - The search-data always consists of the score and at least one parameter as columns and has as much rows as iterations performed during the optmization run.
  
  <br>

  <table class="table">
    <thead class="table-head">
      <tr class="row">
        <td class="cell">score</td>
        <td class="cell">x</td>
        <td class="cell">y</td>
      </tr>
    </thead>
    <tbody class="table-body">
      <tr class="row">
        <td class="cell">0.756</td>
        <td class="cell">0.1</td>
        <td class="cell">0.2</td>
      </tr>
      <tr class="row">
        <td class="cell">0.823</td>
        <td class="cell">0.3</td>
        <td class="cell">0.1</td>
      </tr>
      <tr class="row">
        <td class="cell">...</td>
        <td class="cell">...</td>
        <td class="cell">...</td>
      </tr>
      <tr class="row">
        <td class="cell">...</td>
        <td class="cell">...</td>
        <td class="cell">...</td>
      </tr>
    </tbody>
  </table>


<br>

## The official Hyperactive software stack

- [Hyperactive](https://github.com/SimonBlanke/Hyperactive)
  - The central library for the Hyperactive software stack.

- [Gradient-Free-Optimizers](https://github.com/SimonBlanke/Gradient-Free-Optimizers)
  - The optimization-backend for Hyperactive.

- [Surfaces](https://github.com/SimonBlanke/Surfaces)
  - A collection of test-objective-functions.

- [Search Data Explorer](https://github.com/SimonBlanke/search-data-explorer)
  - Dashboard to visually analyse saved search-data.

- [Simple Data Collector](https://github.com/SimonBlanke/simple-data-collector)
  - Thread safe and atomic data collection into csv-files.


