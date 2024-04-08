# Conditionals

The `if` expression allows evaluating different expressions based on a condition.

```js
let a = 42 in if (a % 2 == 0) print("Even") else print("odd");
```

Since `if` is itself an expression, returning the value of the branch that evaluated true, the previous program can be rewritten as follows:

```js
let a = 42 in print(if (a % 2 == 0) "even" else "odd");
```

Conditions are just expressions of boolean type. The following are the valid boolean expressions:

- Boolean literals: `true` and `false`.
- Arithmetic comparison operators: `<`, `>`, `<=`, `>=`, `==`, `!=`, with their usual semantics.
- Boolean operators: `&` (and), `|` (or), and `!` (not) with their usual semantics.

## Expression blocks in conditionals

The body of the `if` or the `else` part of a conditional (or both) can be an expression block as well:

```js
let a = 42 in
    if (a % 2 == 0) {
        print(a);
        print("Even");
    }
    else print("Odd");
```

## Multiple branches

The `if` expression supports multiple branches with the `elif` construction, which introduces another conditioned branch:

```js
let a = 42, mod = a % 3 in
    print(
        if (mod == 0) "Magic"
        elif (mod % 3 == 1) "Woke"
        else "Dumb"
    );
```
