# 42 algorithmic/mathematic project: computorv1

The assignment requires us to make a program that solves 2nd degree polynomial equations with one variable. The language is free, and I chose python.

## How to use

* Python is needed obviously (version I used is 2.7 but higher should work too)
* Syntax is important, as the program parses according to a strict pattern (although it's more allowing than the subject's requirements). The variable must be called
`X` (capital letter). The constant part must be separated from the variable part with a `*` (i.e. `42 * X^2`). The parser allows `X^1` to be simplified as `X`, and specifying `X^0`
is not required for the strictly constant part.
* The option `-v` displays the intermediate steps in the solution's computing

Example:
```
python computorv1.py "2 * X^2 + 1 * X^1 + 12 = 0"
```

