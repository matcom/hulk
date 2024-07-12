# Protocols

Protocols are special types which support a limited form of structural typing in HULK. The difference between structural and nominal typing in HULK, is that the latter is explicit while the former is implicitely defined. That is, a type doesn't need to explicitely declare that it conforms to a protocol.

Protocols have a syntax similar to that of types, except that they only have method declarations, and they have no body, only signatures. Hence, protocols define the methods that a type must have in order to support some operation.

Protocols don't exist at runtime, they are compile-time only concept that helps writing more flexible programs. After type checking, all information about protocols can be safely removed.

## Defining protocols

A protocol is defined with the keyword `protocol` followed by a collection of method declarations:

```js
protocol Hashable {
    hash(): Number;
}
```

A protocol can have any number of method declarations. For obvious reasons, all method declarations in protocol definitions must be fully typed, as it is impossible to infer any types since they have no body.

A protocol can extend anoter protocol by adding new methods, but never overriding (since there is no actual body) or removing any method (althought you can override the types of some method arguments or return types provided with some restrictions explained below).

```js
protocol Equatable extends Hashable {
    equals(other: Object): Boolean;
}
```

## Implementing protocols

A type implements a protocol implicitely, simply by having methods with the right signature. There is no need to explicitely declare which types implement which protocols.

Thus, you can annotated a variable or argument with a protocol type, and the type checker will correctly verify the consistency of both the method body and the invocation.

```js
type Person {
    // ...

    hash() : Number {
        // ...
    }
}

let x : Hashable = new Person() in print(x.hash());
```

Anywhere you can annotate a symbol with a type (variables, attributes, function, method and type arguments, and return values), you can also use a protocol. For the purpose of type inference, protocols are treated as types.

## Variance in protocol implementation

In order to implementing a protocol, a type doesn't necessarily have to match the exact signature of the protocol. Instead, method and type arguments are considered *contravariant*, and return values *covariant*. This means that arguments can be of the same type or higher, and the return values of the same type or lower than as defined in the protocol.

Similarly, when you extend a protocol, you can override some of the methods as long as you respect the variance constraints.

## Conforming with protocols

More formally, protocols extend the notion of type conforming by adding the following rules:

- A type `T` conforms to a protocol `P` if `T` has all the method defined in `P` with the appropriate types (respecting the variance constraints explained before).
- If a protocol `P1` extends a protocol `P2`, then trivially `P1 <= P2`.
- A protocol `P1` also conforms to another protocol `P2` if any type that conforms to `P1` would also conform to `P2`, even if there is no explicit extension declared.
