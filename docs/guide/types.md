# Types

HULK is ultimately an object-oriented language with simple inheritance and nominal typing. It also has features of structural typing via [protocols](/protocols), which support language features such as [iterables](/iterables), which we will explain later.

This section explains the basics of HULK's nominal typing system.

A type in HULK is basically a collection of attributes and methods, encapsulated under a type name. Attributes are always private, which means they can't be read or writen to from any code outside the type in which they are defined (not even inheritors), while methods are always public and virtual.

## Declaring types

A new type is declared using the `type` keyword followed by a name, and a body composed of attribute definitions and method definitions. All attributes must be given an initialization expression. Methods, like functions, can have a single expression or an expression block as body;

```js
type Point {
    x = 0;
    y = 0;

    getX() => self.x;
    getY() => self.y;

    setX(x) => self.x := x;
    setY(y) => self.y := y;
}
```

The body of every method is evaluated in a namespace that contains global symbols plus an especial symbol named `self` that references the current instance. The `self` symbol is **not** a keyword, which means it can be hidden by a `let` expression, or by a method argument.

However, when referring to the current instance, `self` is not a valid assignment target, so the following code should fail with a semantic error:

```js
type A {
    // ...
    f() {
        self := new A(); // <-- Semantic error, `self` is not a valid assignment target
    }
}
```

## Instantiating types

To instantiate a type you use the keyword `new` followed by the type name:

```js
let pt = new Point() in
    print("x: " @ pt.getX() @ "; y: " @ pt.getY());
```

As you can see, type members are accessed by dot notation (`instance.member`).

You can pass arguments to a type, that you can use in the initialization expressions. This achieves an effect similar to having a single constructor.

```js
type Point(x, y) {
    x = x;
    y = y;

    // ...
}
```

Then, at instantiation time, you can pass specific values:

```js
let pt = new Point(3,4) in
    print("x: " @ pt.getX() @ "; y: " @ pt.getY());
```

Each attribute initialization expression is evaluated in a namespace that contains the global symbols and the type arguments, but no the `self` symbol. This means you cannot use other attributes of the same instance in an attribute initialization expression. This also means that you cannot assume any specifc order of initialization of attributes.

## Inheritance

Types in HULK can inherit from other types. The base of the type hierarchy is a type named `Object` which has no public members, which is the type you implicitely inherit from by default. To inherit from a specific type, you use the `inherits` keyword followed by the type name:

```js
type PolarPoint inherits Point {
    rho() => sqrt(self.getX() ^ 2 + self.getY() ^ 2);
    // ...
}
```

By default, a type inherits its parent type arguments, which means that to construct a `PolarPoint` you have to pass the `x` and `y` that `Point` is expecting:

```js
let pt = new PolarPoint(3,4) in
    print("rho: " @ pt.rho());
```

If you want to define a different set of type arguments, then you have to provide initialization expressions for the parent type at the declaration:

```js
type PolarPoint(phi, rho) inherits Point(rho * sin(phi), rho * cos(phi)) {
    // ...
}
```

During construction, the expressions for type arguments of the parent are evaluated in a namespace that contains global symbols plus the type arguments of the inheritor. Like before, you cannot assume a specific order of evaluation.

In HULK, the three builtin types (`Number`, `String`, and `Boolean`) implicitely inherit from `Object`, but it is a semantic error to inherit from these types.

## Polymorphism

All type methods in HULK are virtual by definition, and can be redefined by an inheritor provided the exact same signature is used:

```js
type Person(firstname, lastname) {
    firstname = firstname;
    lastname = lastname;

    name() => self.firstname @@ self.lastname;
}
```

> **NOTE**: `@@` is equivalent to `@ "  " @`. It is a shorthand to insert a whitespace between two concatenated strings. There is no `@@@` or beyond, we're not savages.

```js
type Knight inherits Person {
    name() => "Sir" @@ base();
}

let p = new Knight("Phil", "Collins") in
    print(p.name()); // prints 'Sir Phil Collins'
```

The `base` symbol in every method refers to the implementation of the parent (or the closest ancestor that has an implementation).
