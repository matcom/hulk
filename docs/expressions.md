---
layout: default
title: Expressions
nav_order: 2
permalink: /expressions
---

# Expressions

HULK is ultimately an expression-based language. Most of the syntactic constructions in HULK are expressions, including the body of all functions, loops, and any other block of code.


The body of a program in HULK always ends with a single global expression that serves as the entrypoint of the program. This means that, of course, a program in HULK can consist of just one global expression.

For example, the following is a valid program:

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

Numbers are 32-bit floating-point and support all basic arithmetic operations with the usual semantics: `+`, `-`, `*`, `\`, `^`, and parenthesized expressions.
We will talk about strings later.

The following is a valid HULK program that computes a rather useless arithmetic expression:

```
print((((1 + 2) ^ 3) * 4) / 5)
```

All usual syntactic and precedence rules apply.