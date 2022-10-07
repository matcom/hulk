# Type inference

Since every program in HULK is statically type-checked, and type annotations are optional in most cases, this means that HULK infers types for most of the symbols in a program.

Because the problem of type inference is computationally complex, and ultimately unsolvable in the general case, the HULK reference definition doesn't give precise semantics about how the type inferer must work. Rather, we will give only a set of minimal constraints that the type inferer must assert if a type is inferred at all for a given symbol, or otherwise it must fail to infer types.

## Type inference vs type checking

The type inferer works before the type checker, and assigns type annotations to all symbols that are not explicitly annotated, and to all the expressions. Afterwards, the type checker verifies that all semantic rules are valid.

Thus, even if a program is fully annotated, the type inferer still needs to work, since it needs to infer the type of all expressions. When some symbols are not explicitly annotated, the type inferer must also assign types for them.

Hence, there are two different moments when a semantic error can be reported. First, if the type inferer cannot infer the type of some symbol, a semantic error will be thrown to indicate the programmer that some symbol must be explicitly typed. Second, if the type inferer finished without errors, the type checker will verify that all types are consistent, and will report a semantic error if there is some incompatibilty.

## Type inference of expressions

The first task of the type inferer is to infer the runtime type of any expression that appears in a HULK program. This process is performed bottom-up, starting from atomic sub-expressions (e.g., literals) and working up the AST. The exact rules for type inference of expressions is given in the section a`bout [type semantics](/type_semantics), but an intuitive introduction can be given at this point.

Literals are the easiest to type-infer, because their type comes directly from the parser. Arithmetic expressions are also easy, because their type is always `Number`. Likewise, string and boolean operators are straightforward.

The type of complex expressions that have an expression body is determined by the type of the body. This is the case of `let`, `while`, and `for`. The type of an expression block is the type of the last expresion of the block. The type of a function or method invocation is the type of its body. The type of expressions that have more than one branch (`if`) is the lowest common ancestor of the types of each branch, or ultimately `Object`.

## Type inference of symbols

Once all expressions have been type-inferred, the type inferer will attempt to assing a type to each symbol declaration that is not explicitly annotated. Instead of providing an exact algorithm, we will define a set of constraints that the type inferer must satisfy whenever it succeeds in assigning a type.

Specific implementations of HULK can choose different methods to attempt the type inference of symbols. According to the order in which symbols are processed, and the sophistication of each method, some implementations may succed where others fail. However, if two type inference algorithms are correct, they most agree on all types for which both succeed in the inference.

These are the constraints a type inference algorithm must satisfy to be correct, or otherwise it must report a failed inference.

- In a `let` expression, whenever a variable is not type-annotated, the type inferer must asign a type for the variable that is equivalent to the type infered for its initialization expression.
- Similarly, in an attribute declaration that is not type-annotated, the type inferer must assign a type that is equivalent to the type inferred for its initialization expression.
- In a function or method, whenever an argument is not type-annotated, the type inferer must assign the lowest (most specific) type that would be consistent with the use of that argument in the method or function body. If more than one type in different branches of the type hierarchy would be consistent, the type inferer must fail.
- Similarly, in a type argument, the type inferer must assign the lowest type that is consistent with the use of that argument in all attribute initialization expressions where it is referenced.

If a type inferer satisfies those constraints, we will say it is *sound*. This means that, for example, the simplest sound strategy for type inference is to infer types for all expressions and fail for all symbols. We will call this the *basic inference* strategy.

## Examples of type inference

These are some programs where a sufficiently sophisticated type inference strategy should work.

In the following program the type of the variable `x` should be inferred to `Number` because the type of `42` is trivially `Number`:

```js
let x = 42 in print(x);
```

In the following function, the type of the argument `n` should be inferred as `Number` because it is the only possible type where arithmetic operators (i.e., `+`) are defined, as there is no operator overloading in HULK:

```js
function fib(n) => if (n == 0 | n == 1) 1 else fib(n-1) + fib(n-2);
```

For the same reason, in the following function, the type of the argument `x` should be inferred as `Number`. Likewise, the type of the variable `f` should be inferred as `Number` because the initialization expression is a literal `Number`.

```js
function fact(x) => let f = 1 in for (i in range(1, x+1)) f := f * i;
```

> **TODO**: Add more examples...
