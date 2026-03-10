# Principles of Programming Languages Design and Implementation

## I. Motivation & Rationale

Computer science education often suffers from a fatal dichotomy: students learn the elegant, mathematical theory of computation in one vacuum, and the gritty, unprincipled reality of software engineering in another. This book bridges that gap. It is the definitive systems engineering pillar within the broader *Computist Compendium*, turning abstract automata theory into living, breathing, executable tools.

The pedagogical vehicle is **HULK** (Havana University Language for Kompilers). The thesis is that every mainstream programming language is a truce in the ancient war between C (the machine-focused imperative structure) and LISP (the math-focused functional flexibility). HULK forces students to navigate this dialectic: it borrows the structural familiarity of C (curly braces, infix math) but demands the functional soul of LISP (everything is an expression, immutable bindings).

By building HULK, we don't just teach the algorithms of parsing; we teach the philosophy of language design.

## II. Architectural Philosophy

Most compiler textbooks force a single host language, compromising either the frontend theory or the backend performance. We mirror industrial compilers (like LLVM) by adopting a **Split-Brain Architecture**:

1. **The Architect (Frontend - Python):** Language design is fundamentally about graphs and trees. Python excels at tree manipulation, rapid prototyping, and dynamic structures. We will handle Lexing, Recursive Descent Parsing, Semantic Analysis, and Type Inference in Python. Crucially, this allows native integration with tools like `tesserax` to generate live, visually stunning representations of Abstract Syntax Trees (ASTs) and scope chains directly in the textbook.
2. **The Bridge (IR - BANNER):** The frontend does not execute code. It emits BANNER (Basic Address Notation for N-ary Evaluation and Runtime), a strict 3-address intermediate representation.
3. **The Engineer (Backend - Rust):** The backend is pure systems engineering. We take the BANNER IR and ingest it into Rust, building a high-performance Virtual Machine. This isolates the lessons of cache locality, memory layout, stack manipulation, and garbage collection in a language built for the metal.

## III. Product & Publishing Strategy

This project leverages an **Open Core / Director's Cut** publishing model, driven by literate programming via Quarto.

* **The Shadow Course:** The initial draft is serialized live via a weekly newsletter. This provides public accountability, immediate beta-tester feedback from readers, and a rigid 14-week "semester" cadence.
* **The Web Edition (Free):** The compiled HTML Quarto book remains permanently free online to ensure open access to knowledge for students globally.
* **The Director's Cut (Paid):** The monetized tier ($30-$100+). This includes the offline, beautifully typeset PDF/ePub, the complete chapter-by-chapter source code archives, high-resolution vector diagrams, and an exclusive "Solutions & Deep Dives" manual for the chapter exercises. It ultimately bundles into the full *Computist Compendium*.

## IV. The 14-Week Syllabus & Structure

The book is structured into three distinct phases, moving from abstract text to raw execution.

### Part I: The Architect (Python Frontend)

* **Chapter 1: The Dual Ancestry:** The C vs. LISP dialectic. Setting up the project and the REPL.
* **Chapter 2: The Atomization:** Lexical analysis, tokens, and regular languages.
* **Chapter 3: The Structure:** Context-Free Grammars, operator precedence, and Recursive Descent parsing.
*
* **Chapter 4: The Evaluation:** The Tree-Walking Interpreter and the "Everything is an Expression" philosophy.
* **Chapter 5: The Binding:** Lexical scoping, symbol tables, and the `let-in` construct.
* **Chapter 6: The Shield:** Semantic analysis, gradual typing, and basic type inference.

### Part II: The Bridge (Intermediate Representation)

* **Chapter 7: The Lowering:** Designing BANNER (3-Address Code) to decouple syntax from execution.
* **Chapter 8: The Transpiler:** Walking the Python AST to emit flat, linear BANNER instructions.

### Part III: The Engineer (Rust Backend)

* **Chapter 9: The Metal Sandbox:** Transitioning to Rust. Project setup, loading IR, and defining the VM architecture.
* **Chapter 10: The Stack Machine:** Implementing the instruction cycle (`PUSH`, `POP`, `ADD`, `JMP`).
* **Chapter 11: The Heap & Memory Layout:** Representing HULK's dynamic values safely in Rust's strict memory model.
* **Chapter 12: The Garbage Collector:** Managing dynamic lifecycles (Reference Counting vs. Mark-and-Sweep).
* **Chapter 13: The Standard Library:** Bridging HULK calls to native Rust system functions (I/O, Math).
* **Chapter 14: The Final Polish:** End-to-end execution, optimizations, and the philosophy of what to build next.

## V. Execution Protocol

To defeat the "Chapter 2 Curse," the drafting process relies on high consistency and low friction:

1. **Voice-to-Text Drafting:** Core theoretical prose and historical context are drafted via audio recordings during transit/downtime, transcribed, and structured before formal editing.
2. **The 15-Minute Rule:** Daily micro-contributions to the codebase or prose to maintain context persistence.
3. **The Weekly Forge:** A single, uninterrupted 4-hour block dedicated strictly to implementing the week's core logic and ensuring the Quarto literate build passes all tests.
