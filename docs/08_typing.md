---
layout: default
title: Type checking
nav_order: 8
permalink: /typing
---

# Type checking

HULK is a statically-typed language with optional type annotations. So far you haven't seen any because HULK has a powerful [type inference system](/inference) which we will talk about later on. However, all symbols in HULK have a static type, and all programs in HULK are statically checked during compilation.

Tye annotations can be added anywhere a symbol is defined, that is:

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

## Type conforming