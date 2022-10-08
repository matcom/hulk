---
layout: default
title: Expressions
nav_order: 2
permalink: /expressions
---

# Expressions

HULK is ultimately an expression-based language. Most of the syntactic constructions in HULK are expressions, including the body of all functions, loops, and any other block of code.

The body of a program in HULK always ends with a single global expression (and, if necessary, a final semicolon) that serves as the entrypoint of the program. This means that, of course, a program in HULK can consist of just one global expression.

For example, the following is a valid program in HULK:

```js
42;
```

Obviously, this program has no side effects. A slightly more complicated program, probably the first one that does something, is this:

```js
print(42);
```

In this program, `print` refers to a builtin function that prints the result of any expression in the output stream. We will talk about functions in a later section.

The rest of this section explains the basic expressions in HULK.

## Arithmetic expressions

HULK defines three types of literal values: **numbers**, **strings** and **booleans**.
We will leave strings and booleans for later.

Numbers are 32-bit floating-point and support all basic arithmetic operations with the usual semantics: `+` (addition), `-` (subtraction), `*` (multiplication), `/` (floating-point division), `^` (power), and parenthesized sub-expressions.

The following is a valid HULK program that computes and prints the result of a rather useless arithmetic expression:

```js
print((((1 + 2) ^ 3) * 4) / 5);
```

All usual syntactic and precedence rules apply.

## Strings

String literals in HULK are defined within enclosed double-quotes (`"`), such as in:

```js
print("Hello World");
```

A double-quote can be included literally by escaping it:

```js
print("The message is \"Hello World\"");
```

Other escaped characters are `\n` for line endings, and `\t` for tabs.

Strings can be concatenated with other strings (or the string representation of numbers) using the `@` operator:

```js
print("The meaning of life is " @ 42);
```

## Builtin math functions and constants

Besides `print`, HULK also provides some common mathematical operations encapsulated as builtin functions with their usual semantics. The list of builtin math functions is the following:

- `sin(<angle>)` computes the sine of an angle in radians.
- `cos(<angle>)` computes the cosie of an angle in radians.
- `exp(<value>)` computes the value of `e` raised to a value.
- `log(<base>, <value>)` computes the logarithm of a value in a given base.

Besides these functions, HULK also ships with two global constants: `PI` and `E` which represent the floating-point value of these mathematical constants.

As expected, functions can be nested in HULK (provided the use of types is consistent, but so far all we care about is functions from numbers to numbers, so we can forget about types until later on). Hence, the following is a valid HULK program.

```js
print(sin(2 * PI) ^ 2 + cos(3 * PI / log(4, 64)));
```

More formally, function invocation is also an expression in HULK, so everywhere you expect an expression you can also put a call to builtin function, and you can freely mix arithmetic expressions and mathematical functions, as you would expect in any programming language.

## Expression blocks

Anywhere an expression is allowed (or almost), you can also use an expression block, which is nothing but a series of expressions between curly braces (`{` and `}`), and separated by `;`.

The most trivial usage of expression blocks is to allow multiple `print` statements as the body of a program. For example, the following is a valid HULK program:

```js
{
    print(42);
    print(sin(PI/2));
    print("Hello World");
}
```

When you use an expression block instead of a single expression, it is often not necessary to end with a semicolon (`;`), but it is not erroneous to do so either.
