---
layout: default
title: Type checking
nav_order: 8
permalink: /typing
---

# Type checking

HULK is a statically-typed language with optional type annotations. So far you haven't seen any because HULK has a powerful [type inference system](/inference) which we will talk about later on. However, all symbols in HULK have a static type, and all programs in HULK are statically checked during compilation.

Type annotations can be added anywhere a symbol is defined, that is:

- in variable declarations with `let` expressions;
- in function or method arguments and return type;
- in type attributes; and,
- in type arguments.

Let's see an example of each case.

## Typing variables

Variables can be explicitely type-annotated in `let` expressions with the following syntax:

```js
let x: Number = 42 in print(x);
```

The type checker will verify that the type inferred for the initialization expression is compatible with (formally, [conforms to](/#type-conforming)) the annotated type.

## Typing functions and methods

All or a subset of a function's or method's arguments, and its return value, can be type-annotated with a similar syntax:

```js
tan(x: Number): Number => sin(x) / cos(x);
```

On the declaration side, the type checker will verify that the body of the method uses the types in a way that is consistent with their declaration. The exact meaning of this consistency is defined in the section about [type semantics](/type_semantics). The type checker will also verify that the return type of the body conforms to the annotated return type.

On the invocation side, the type checker will verify that the values passed as parameters conform to the annotated types.

Inside methods of a type `T`, the implicitly defined `self` symbol is always assumed as if annotated with type `T`.

## Typing attributes and type arguments

In type definitions, attributes and type arguments can be type-annotated as follows:

```js
type Point(x: Number, y: Number) {
    x: Number = x;
    y: Number = y;

    // ...
}
```

The type checker will verify that type arguments are used consistently inside attribute initialization expressions, and that the inferred type for each attribute initialization expression conforms to the attribute annotation.

## Type conforming

The basic type relation in HULK is called *conforming* (`<=`). A type `T1` is said to *conform to* to another type `T2` (writen as `T1 <= T2`) if a variable of type `T2`  can hold a value of type `T1` such that every possible operation that is semantically valid with `T2` is guaranteed to be semantically valid with `T1`.

In general, this means that the type checker will verify that the inferred type for any expression conforms to the corresponding type declared for that expression (e.g., the type of a variable, or the return type of a function).

The following rules provide an initial definition for the *conforming* relationship. The formal definition is given in the section about [type semantics](/type_semantics).

- Every type conforms to `Object`.
- Every type conforms to itself.
- If `T1` inherits `T2` then `T1` conforms to `T2`.
- If `T1` conforms to `T2` and `T2` conforms to `T3` then `T1` conforms to `T3`.
- The only types that conform to `Number`, `String`, and `Boolean`, are respectively those same types.

Types in HULK form a single hierarchy rooted at `Object`. In this hierarchy the *conforming* relationship is equivalent to the *descendant* relationship. Thus, if `T1` conforms to `T2` that means that `T1` is a descendant of `T2` (or trivially the same type). Thus, we can talk of the lowest common ancestor of a set of types `T1`, `T2`, ..., `Tn`, which is the most specific type `T` such that all `Ti` conform to `T`. When two types are in different branches of the type hierarchy, they are effectively incomparable.
