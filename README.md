## General information

I focused mostly to demonstrate CI/CD processes here then make an amazing application. As my field of interest is DevOps. So the app is not even elegant.
But my application still passes the requirements and with little adjustments can be used in production.

I did not have too much free time to do it more elegantly due to my other life/work responsibilities at the moment, but I put in comments on what I would improve in the future. They are marked with the `TODO` tag in the comments in source files. Especially `parser.py`, `finder.py`.

I have bread experience with GitLab CI/CD from my professional experience, but I wanted to try and learn something new here, this is why I choose GitHub and his Actions, also due to fact that you are using them and all my personal repos are on GitHub.

I made and app is much production manner as possible with few shortcuts to save time.

## Bonus Questions

# 1. How would you modify your program if we knew that the gentleman had multiple ways to get to some of the rooms?

I would use the first occurrence if this two path would be equal by length or used the shorter one. Or apply some shortest path finding methods like Dijkstra's, Bellman-Ford or Floyd-Warshall algorithm.

# 2. Assuming multiple paths, how would you modify the program if walking up the staircase was more strenuous than walking down the same?

Same as in 1. I would give a weight to the paths actions between two points and then applied some advanced algorithm or other path finding algorithms.

## Application Information

This is a simple application which find path between your position and object you're finding in your house. It helps you remember when you left you stuff!

Written in Python3
CI/CD made using GitHub Actions

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

1. `python3 `

### How to contribute

Make a git clone.

Choose a branch in which you want to contribure.

Make a desired changes or create an Issue, then make a pull request.

Repo maintainer @Ormi will take a look and will approve after it will pass the pipeline.

## Infrasturcture information

The pipeline consists of three stages:

1. Test including unit-test, integration-test, lint test, and build test
2. Application build

## Things to improve

1. Divide pipeline for dev and production, make main production branch and dev branch as development branch.
2. Prepare some cluster on Kubernetes where this will be deployed.
3. Write unit, application, and integration tests.
4. Take a look at security of this application.
5. Improve everything what has TODO tag inside the applicaion.

