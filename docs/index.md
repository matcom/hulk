---
layout: default
title: Introduction
nav_order: 1
permalink: /
---

**HULK** (Havana University Language for Kompilers) is a didactic, type-safe, object-oriented and incremental programming language, designed for the course Introduction to Compilers in the Computer Science major at University of Havana.

A simple "Hello World" in HULK looks like this:

```
print("Hello World");
```

## What is HULK

In a bird's eye view HULK is an object-oriented programming language, with simple inheritance, polymorphism, and encapsulation at the class level. Also, in HULK it is possible to define global functions outside the scope of all classes. It is also possible to define a _single global expression_ that constitutes the entry point to the program.

Most of the syntactic constructions in HULK are expressions, including conditional instructions and cycles. HULK is a statically typed language with optional type inference, which means that some (or all) parts of a program can be annotated with types, and the compiler will verify the consistency of all operations.

## A didactic language

The HULK language has been designed to be used as a mechanism for learning and evaluating a colege course about compilers. For this reason, certain language design decisions respond more to didactic questions than to theoretical or pragmatic questions. An illustrative example is the inclusion of a single basic numerical type. In practice, programming languages have several numeric types (`int`, `float`, `double`, `decimal`) to cover the wide range of trade-off between efficiency and expressivity. However, from the didactic point of view, it is enough complexity to have to deal with a numerical type, and the inclusion of others does not bring anything new from our point of view.

Another important decision is the static typing with type inference, which will be explained later in detail. The motivation behind this feature is to allow students to first implement an evaluator for the language, and then worry about type verification. Likewise, the decision to have global expressions, global functions, and classes, responds to the need to introduce the various elements of language little by little. By having global expressions, it is possible to implement an expression interpreter without the need to solve context-sensitive problems. Later, students can implement functions and finally the object-oriented features. In this way students can learn on the fly as they add characteristics to the language, always having a valid subset of the language implemented.

## An incremental language

The HULK language really is a set of closely related programming languages. What we will call basic HULK consists of a minimum subset that is defined by an extensive set of additional features. The basic language contains expressions, global functions and a unified system of types with simple inheritance. The extensions include from support for arrays, to delegates, inference of types, iterators, among other characteristics. Each of these extensions has been designed to be compatible with the rest of HULK, including the rest of the extensions. It should be possible, once a basic compiler is implemented, to add any subset of these extensions.

This design has been conceived to allow the use of HULK in a wide range of learning levels. As a language of expressions and functions, it is useful for introductory courses on parsing and basic compilation techniques. Object orientation introduces a whole universe of semantic complexities; however, the HULK type system is simple enough to illustrate the most common problems in semantic type verification. On the other hand, each one of the extensions introduces advanced and interesting problems. Arrays introduce problems related to memory management, while anonymous functions and iterators are fundamentally problems of transpilation and code generation. The inference of types and the verification of null-safety is an exercise in logical inference, which can be used in advanced courses. The idea is that each course defines its objectives of interest, and can use an appropriate subset of HULK to illustrate and evaluate them.
