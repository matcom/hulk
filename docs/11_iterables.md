---
layout: default
title: Iterables
nav_order: 11
permalink: /iterables
---

# Iterables

An iterable in HULK is any object that follows the iterable protocol, which is defined as follows:

```js
protocol Iterable {
    next() : Boolean;
    current() : Object;
}
```

An example of iterable is the builtin `range` function, which returns an instance of the builtin `Range` type, defined as follows:

```js
type Range(min:Number, max:Number) {
    min = min;
    max = max;
    current = min - 1;

    next(): Boolean => (self.current := self.current + 1) < max;
    current(): Number => self.current;
}
```

Notice that since protocols are covariant in the return types of the methods, the `Range` type correctly implements the `Iterable` protocol.

## Using iterables with the `for` loop

As explained in [the loops section](/loops), the `for` loop works with the `Iterable` protocol, which means you can apply `for` on any instance of a type that implements the protocol.

In compile-time, `for` is transpiled to a code that is equivalent, but explicitely uses the `Iterable` protocol.

For example, the code:

```js
for (x in range(0,10)) {
    // code that uses `x`
}
```

Is transpiled to:

```js
let iterable = range(0, 10) in
    while (iterable.next())
        let x = iterable.current() in {
            // code that uses `x`
        }
```

This transpilation guarantees that even though the `Iterable` protocol defines the `current` method with return type `Object`, when you use a `for` loop you will get the exact covariant type inferred in `x`.

As a matter of fact, due to the transpilation process, the `Iterable` protocol itself is not even necessary, since nowhere is a symbol annotated as `Iterable`. However, the protocol is explicitely defined as a builtin type so that you can explicitly use it if you need to annotate a method to receive a black-box iterable.

Keep in mind, thought, that when you annotate something explicitely as `Iterable`, you are effectively forcing the type inferrer to assign `Object` as the type of the iteration variable (`x` in this example). This is one of the  reasons it is often better to let HULK infer types than annotating them yourself.