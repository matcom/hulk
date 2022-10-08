---
layout: default
title: Variables
nav_order: 6
permalink: /loops
---

# Loops

HULK defines two kinds of loops, the `while` expression and the `for` expression.
Both loop constructions are expressions, returning the value of the last body expression.

## The `while` loop

A `while` loop evaluates a condition and its body while the condition is true. The body can be a simple expression or an expression block.

```js
let a = 10 in while (a >= 0) {
    print(a);
    a := a - 1;
}
```

Since the return value of the `while` loop is the return value of its expression body, it can often be used directly as the body of a function.

```js
gcd(a, b) => while (a > 0)
    let m = a % b in {
        b := a;
        a := m;
    };
```

## The `for` loop

A `for` loop iterates over an _iterable_ of elements of a certain type. We will [talk about iterables](/iterables) later on, but for now it suffices to say that if some expression evaluates to a collection, then the `for` loop can be used to iterate it.

For example, the builtin `range(<start>, <end>)` function evaluates to an iterable of numbers between `<start>` (inclusive) and `<end>` (non-inclusive).

```js
for (x in range(0, 10)) print(x);
```

The `for` loop is semantically and operationally equivalent to the following:

```js
let iterable = range(0, 10) in
    while (iterable.next())
        let x = iterable.current() in
            print(x);
```

In fact, what the reference implementation of the HULK compiler does in `for` loops is to transpile them into their `while` equivalent. This also effectively means that, just like the `while` loop, the `for` loop returns the last value of its body expression.
