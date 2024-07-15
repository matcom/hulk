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

As explained in [the loops section](/guide/loops), the `for` loop works with the `Iterable` protocol, which means you can apply `for` on any instance of a type that implements the protocol.

In compile-time, `for` is transpiled to a code that is equivalent, but explicitely uses the `Iterable` protocol members.

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

## Typing iterables

Since in the `Iterable` protocol we can only define (at this point) the return value of `current()` as `Object`, it is cumbersome to type arguments of a function or method as `Iterable`, because doing so will force you to downcast the elements to a desired type.

For this reason, HULK allows a special syntax for typing iterables of a specific type `T` using the format `T*`:

```js
function sum(numbers: Number*): Number =>
    let total = 0 in
        for (x in numbers)
            total := total + x;
```

What happens under the hood is that when you use of `T*` anywhere in a HULK program, the compiler will insert an implicit protocol definition that looks like this:

```js
protocol Iterable_T extends Iterable {
    current(): T;
}
```

Since protocols can be extended by [overriding some methods with the correct variance constraints](/guide/protocols), the previous code will compile correctly.

## Implementing collections

The iterable protocols defined so far encapsulates the concept of making *a single iteration* over the sequence of elements. In contrast, most collection types you will define allow for multiple iterations, even simultaneously, over the same sequence of elements.

To accomodate for this kind of behaviour, we can define an *enumerable* protocol that simply provides one method to create an iterable for one specific iteration everytime that is needed:

```js
protocol Enumerable {
    iter(): Iterable;
}
```

With this protocol defined, the `for` loop is extended such that, when used with an enumerable instead of directly an iterable, it will transpile to a slightly different code:

```js
let iterable = enumerable.iter() in
    while (iterable.next())
        let x = iterable.current() in {
            // ..
        }
```
