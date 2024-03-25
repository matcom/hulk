# Variables

Variables in HULK are lexically-scoped, which means that their scope is explicitely defined by the syntax. You use the `let` expression to introduce one or more variables in and evaluate an expression in a new scope where those variables are defined.

The simplest form is introducing a single variable and using a single expression as body.

```js
let msg = "Hello World" in print(msg);
```

Here `msg` is a new symbol that is defined *only* within the expression that goes after `in`.

## Multiple variables

The `let` expression admits defining multiple variables at once like this:

```js
let number = 42, text = "The meaning of life is" in
    print(text @ number);
```

This is semantically equivalent to the following long form:

```js
let number = 42 in
    let text = "The meaning of life is" in
        print(text @ number);
```

As you can notice, `let` associates to the right, so the previous is also equivalent to:

```js
let number = 42 in (
    let text = "The meaning of life is" in (
            print(text @ number)
        )
    );
```

## Scoping rules

Since the binding is performed left-to-right (or equivalently starting from the outer let), and every variable is effectively bound in a new scope, you can safely use one variable when defining another:

```js
let a = 6, b = a * 7 in print(b);
```

Which is equivalent to (and thus valid):

```js
let a = 6 in
    let b = a * 7 in
        print(b);
```

## Expression block body

You can also use an expression block as the body of a `let` expression:

```js
let a = 5, b = 10, c = 20 in {
    print(a+b);
    print(b*c);
    print(c/a);
}
```

As we said before, semicolons (`;`) are seldom necessary after an expression block, but they are never wrong.

## The `let` return value

As with almost everything in HULK, `let` is an expression, so it has a return value, which is obviously the return value of its body. This means the following is a valid HULK program:

```js
let a = (let b = 6 in b * 7) in print(a);
```

Or more directly:

```js
print(let b = 6 in b * 7);
```

This can be of course nested ad infinitum.

## Redefining symbols

In HULK every new scope hides the symbols from the parent scope, which means you can redefine a variable name in an inner `let` expression:

```js
let a = 20 in {
    let a = 42 in print(a);
    print(a);
}
```

The previous code prints `42` then `20`, since the inner `let` redefines the value of `a` inside its scope, but the value outside its still the one defined by the outer `let`.

And because of the [scoping rules](#scoping-rules), the following is also valid:

```js
let a = 7, a = 7 * 6 in print(a);
```

Which is equivalent to:

```js
let a = 7 in
    let a = 7 * 6 in
        print(a);
```

## Destructive assignment

Most of the time in HULK you won't need to overwrite a variable, but there are cases where you do. In those cases, you can use the destructive assignment operator `:=`, like this:

```js
let a = 0 in {
    print(a);
    a := 1;
    print(a);
}
```

The previous program prints `0` and then `1`, since the value of `a` is overwritten before the second `print`.
This is the **only** way in which a variable can be written to outside of a `let`.

As you would expect, the `:=` operator defines an expression too, which returns the value just assigned, so you can do the following:

```js
let a = 0 in
    let b = a := 1 in {
        print(a);
        print(b);
    };
```

This is useful if you want to evaluate a complex expression to both test it (e.g, to se if its greater than zero) and store it for later use.
