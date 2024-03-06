# Vectors

The builtin vector type provides a simple but powerful abstraction for creating collections of objects of the same type. In terms of functionality, a vector is close to plain arrays as defined in most programming languages. Vectors implement the [iterable protocol](/iterables) so they can be iterated with a `for` syntax.

Vectors in HULK can be defined with two different syntactic forms: explicit and implicit.

## Explicit syntax

An explicit vector of `Number`, for example, can be defined as follows:

```js
let numbers = [1,2,3,4,5,6,7,8,9] in
    for (x in numbers)
        print(x);
```

Because vectors implement the iterable protocol, you can explicitely find a `next` and `current` methods in case you ever need them. Besides that, vectors also have a `size(): Number` method that returns the number of items in the vector.

Vectors also support an indexing syntax using square brackets `[]`, as in the following example:

```js
let numbers = [1,2,3,4,5,6,7,8,9] in print(numbers[7]);
```

## Implicit syntax

An implicit vector can be created using what we call a generator pattern, which is always an expression  Here's an example:

```js
let squares = [x^2 || x in range(1,10)] in print(x);
// prints 2, 4, 6, 8, 10, ...
```

## Typing vectors

Actually, there is not one single `Vector` type in HULK, at least not in a way that is accesible from HULK code.