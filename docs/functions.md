---
layout: default
title: Functions
nav_order: 3
permalink: /functions
---

# Functions

HULK also lets you define your own functions (of course!). A program in HULK can have an arbitrary number of functions defined before the final global expression (or expression block).

## Inline functions

 The easiest way to define a function is the inline form. Here's an example:

```
tan(x) => sin(x) / cos(x);
```

An inline function is defined by an identifier followed by arguments between parenthesis, then the `=>` symbol, and then a simple expression (not an expression block) as body, ending in `;`.

In HULK, all functions must be defined before the final global expression. All these functions live in a single global namespace, hence it is not allowed to repeat function names. Similarly, there are no overloads in HULK (at least in "basic" HULK).

Finally, the body of any function can use other functions, regardless of whether they are defined before or after the corresponding function. Thus, the following is a valid HULK program:

```
cot(x) => 1 / tan(x);
tan(x) => sin(x) / cos(x);

print(tan(PI) ** 2 + cot(PI) ** 2);
```

Of course, inline functions (and any other type of function) can call themselves recursively.

## Full-form functions

Since inline functions only allow for a single expression as body (as complex as that may be), HULK also allows full-form functions, in which the body is an expression block.

Here's an example of a rather useless function that prints 4 times:

```
operate(x, y) {
    print(x + y);
    print(x - y);
    print(x * y);
    print(x / y);
}
```