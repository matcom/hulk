---
layout: default
title: Expressions
nav_order: 2
permalink: /expressions
---

# Expressions

HULK is ultimately an expression-based language. Most of the syntactic constructions in HULK are expressions, including the body of all functions, loops, and any other block of code.

The body of a program in HULK always ends with a single global expression (and a final semicolon) that serves as the entrypoint of the program. This means that, of course, a program in HULK can consist of just one global expression.

For example, the following is a valid program in HULK:

```
42;
```

Of course, this program has no side effects. A slightly more complicated program, probably the first one that does something, is this:

```
print(42);
```

In this program, `print` refers to a builtin function that prints the result of any expression in the output stream. We will talk about functions in a later section.

The rest of this section explains all the expressions in HULK.

## Arithmetic expressions

HULK defines two types of literal values: **numbers** and **strings**.
We will leave strings for later.

Numbers are 32-bit floating-point and support all basic arithmetic operations with the usual semantics: `+` (addition), `-` (subtraction), `*` (multiplication), `\` (floating-point division), `^` (power), and parenthesized sub-expressions.

The following is a valid HULK program that computes and prints the result of a rather useless arithmetic expression:

```
print((((1 + 2) ^ 3) * 4) / 5);
```

All usual syntactic and precedence rules apply.

## Builtin math functions and constants

Besides `print`, HULK also provides some common mathematical operations encapsulated as builtin functions with their usual semantics. The list of builtin math functions is the following:

- `sin(<angle>)` computes the sine of an angle in radians.
- `cos(<angle>)` computes the cosie of an angle in radians.
- `exp(<value>)` computes the value of `e` raised to a value.
- `log(<base>, <value>)` computes the logarithm of a value in a given base.

Besides these functions, HULK also ships with two global constants: `PI` and `E` which represent the floating-point value of these mathematical constants.

As expected, functions can be nested in HULK (provided the use of types is consistent, but so far all we care about is functions from numbers to numbers, so we can forget about types until later on). Hence, the following is a valid HULK program.

```
print(sin(2 * PI) ^ 2 + cos(3 * PI / log(4, 64)));
```

More formally, function invocation is also an expression in HULK, so everywhere you expect an expression you can also put a call to builtin function, and you can freely mix arithmetic expressions and mathematical functions, as you would expect in any programming language.

## Inline functions

HULK also lets you define your own functions (of course!). The easiest way is the inline function form. Here's an example:

```
tan(x) => sin(x) / cos(x);
```

In HULK, all functions must be defined before the final global expression. All these functions live in a single global namespace, hence it is not allowed to repeat function names. Similarly, there are no overloads in HULK (at least in "basic" HULK).

Finally, the body of any function can use other functions, regardless of whether they are defined before or after the corresponding function. Thus, the following is a valid HULK program:

```
cot(x) => 1 / tan(x);
tan(x) => sin(x) / cos(x);

print(tan(PI) ** 2 + cot(PI) ** 2);
```

Of course, inline functions (and any other type of function) can call themselves recursively.
