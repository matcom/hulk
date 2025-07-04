# Functors

A functor in HULK is an object that encapsulates a function, which means it supports the `obj()` syntax. This can be accomplished with protocols easily, via transpilation. If you have a type that implements a functor protocol, then HULK will allow you to use the functor syntax. A functor protocol is any protocol that has an `invoke` method with appropriate type annotations.

For example, suppose you declare the following protocol in HULK:

```go
protocol NumberFilter {
    invoke(x: Number): Boolean;
}
```

Then, you can annotate a function to receive an object that implements this protocol:

```go
function count_when(numbers: Number*, filter: NumberFilter) {
    let total = 0 in
        for (x in numbers)
            total := total + if (filter.invoke(x)) 1 else 0;
}
```

But, since that protocol is a functor (it contains an `invoke` method), you can also use it directly as if it where a method, with the following syntax:

```go
function count_when(numbers: Number*, filter: NumberFilter) {
    let total = 0 in
        for (x in numbers)
            total := total + if (filter(x)) 1 else 0;
}
```

To implement a functor protocol, you simply define a type that implements the protocol, as usual, and then you can use it:

```go
type IsOdd {
    invoke(x: Number): Boolean => x % 2 == 0;
}

let numbers = range(0, 100) in
    print(count_when(numbers, IsOdd())); // prints `50`
```

But this syntax is extremely cumbersome, so HULK provides lots of syntax sugar to simplify the declaration and usage of functors.

## Implicit functor implementation

The first aid that HULK provides is by implicitely implementing wrapping functions as functor types upong usage. For example, instead of defining the `IsOdd` type like before, you can simply define an `is_odd` function like the following, and pass it directly to the `count_when` function:

```go
function is_odd(x: Number) => x % 2 == 0;

let numbers = range(0, 100) in
    print(count_when(numbers, is_odd));
```

And then HULK will automatically create an appropriate functor type that implements the desired protocol, which means the previous code is transpiled to something like the following:

```go
function is_odd(x: Number) => x % 2 == 0;

type _IsOddWrapper {
    invoke(x: Number): Boolean => is_odd(x);
}

let numbers = range(0, 100) in
    print(count_when(numbers, _IsOddWrapper()));
```

Naturally, this syntax sugar extends to variable assignment as well, which means the following is valid:

```go
let numbers = range(0, 100), filter: NumberFilter = is_odd in
    print(count_when(numbers, filter));
```

## Lambda expressions

Keeping up with the previous example, we can eliminate the explicit `is_odd` definition and pass a lambda expression, which is an anonymous function defined directly in the place when the functor is needed:

```go
let numbers = range(0, 100) in
    print(count_when(numbers, (x: Number): Boolean => x % 2 == 0));
```

The general syntax for lambda expressions is very similar to the syntax for inline functions, except that you don't need to name the function.

Also, if the type inferrer is good enough, you can almost always drop the explicit type annotations:


```go
let numbers = range(0, 100) in
    print(count_when(numbers, (x) => x % 2 == 0));
```

And of course, lambda expressions can be stored in appropriately typed variables:

```go
let numbers = range(0, 100), filter: NumberFilter = (x) => x % 2 = 0 in
    print(count_when(numbers, filter));
```

And the type inferrer is good enough, since `count_when` requires a `NumberFilter`, you can drop the explicit type annotation:

```go
let numbers = range(0, 100), filter = (x) => x % 2 = 0 in
    print(count_when(numbers, filter));
```

## Typing functors

And finally, we can also skip the protocol definition and use a special syntax for typing functors directly in the type annotaion:

```go
function count_when(numbers: Number*, filter: (Number) -> Boolean) {
    // same code
}
```

The syntax `(Number) -> Boolean` indicates that we expect a functor with a single input of type `Number` and an output of type `Boolean`. Upon finding this definition, HULK will transpile that into something that is very similar to our explicit protocol definition:

```go
protocol _Functor0 {
    invoke(_arg0: Number) : Boolean;
}

function count_when(numbers: Number*, filter: _Functor0) {
    // same code
}
```
