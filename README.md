## General information

I focused mostly to demonstrate CI/CD processes here then make an amazing application. As my field of interest is DevOps. So the app is not even elegant.
But my application still passes the requirements and with little adjustments can be used in production.

I did not have too much free time to do it more elegantly due to my other life/work responsibilities at the moment, but I put in comments on what I would improve in the future. They are marked with the `TODO` tag in the comments in source files. Especially `parser.py`, `finder.py`.

I have bread experience with GitLab CI/CD from my professional experience, but I wanted to try and learn something new here, this is why I choose GitHub and his Actions, also due to fact that you are using them and all my personal repos are on GitHub.

I made an app in much production manner as possible with few shortcuts to save time.

## Bonus Questions

### 1. How would you modify your program if we knew that the gentleman had multiple ways to get to some of the rooms?

I would use the first occurrence if these two path would be equal by length or used the shorter one. Or apply some shortest pathfinding methods like Dijkstra's, Bellman-Ford, or Floyd-Warshall algorithm.

### 2. Assuming multiple paths, how would you modify the program if walking up the staircase was more strenuous than walking down the same?

Same as in 1. I would give weight to the path's actions between two points and then applied some advanced algorithm or other path-finding algorithms.

## Application Information

This is a simple application that finds a path between your position and the object you're finding in your house. It helps you remember when you left your stuff!

Written in Python3

CI/CD made using GitHub Actions

app.py - Main file with algorithm core

configs/ - config files with Estate description

tests/ - test files

src/parser.py - Parsing configs to 2D array

### Examples of run

```
ormos@ormos-Latitude-5490:~/Personal/simple-path-finder/src$ python3 finder.py path-to-object bedroom keys
You are in bedroom
Go to the Stairs
Go to the Basement
Go to the Hallway
Get the keys

ormos@ormos-Latitude-5490:~/Personal/simple-path-finder/src$ python3 finder.py path-to-object bedroom knife
You are in bedroom
Go to the Stairs
Go to the Basement
Go to the House
Go to the Garden
Go to the Toolshed
Get the knife

ormos@ormos-Latitude-5490:~/Personal/simple-path-finder/src$ python3 finder.py path-to-object Hallway knife
You are in Hallway
Go to the House
Go to the Garden
Go to the Toolshed
Get the knife
```

### How to run

#### Localy

1. `python3 python3 app.py path-to-object <room> <object>`

### How to contribute

Make a git clone.

Choose a branch to which you want to contribute.

Make the desired changes or create an Issue, then make a pull request.

Repo maintainer @Ormi will take a look and will approve after it will pass the pipeline.

## Infrasturcture information

The pipeline consists of three stages:

1. Test including unit-test, integration-test, lint test, and build test
2. Application build

Only demonstration, not real tests run.

See GitHub actions.

![Screenshot from 2021-03-27 18-21-45](https://user-images.githubusercontent.com/3997725/112728811-56f10800-8f29-11eb-8ddc-7e668f364458.png)

## Things to improve

1. Divide pipeline for dev and production, make main production branch and dev branch as development branch.
2. Prepare some clusters on Kubernetes where this will be deployed.
3. Write real unit, application, and integration tests.
4. Take a look at the security of this application.
5. Improve everything that has a TODO tag inside the application.
6. Catch all exceptions.

