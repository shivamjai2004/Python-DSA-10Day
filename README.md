# 10-Day Python DSA Program

Notes and practice code from a 10-day Data Structures & Algorithms program using Python.

---

## Program Structure

| Day | Topics Covered |
|-----|---------------|
| Day 1 | Python Basics — Data Types, Type Casting, Collections, Conditions, Loops, Membership Operators, Practice Problems |
| Day 2 | Strings, Tuples, Dictionaries, Practice Problems |
| Day 3 | DSA Intro & Time Complexity, Functions, Practice Problems |
| Day 4 | Binary Search, Bubble Sort, OOP, Stack, Practice Problems |
| Day 5 | *(coming soon)* |
| Day 6 | *(coming soon)* |
| Day 7 | *(coming soon)* |
| Day 8 | *(coming soon)* |
| Day 9 | *(coming soon)* |
| Day 10 | *(coming soon)* |

---

## Day 1 — Python Fundamentals

### Topics

- **Data Types** (`dataType.py`) — Strings, integers, floats, booleans, `type()`, `len()`, `id()`, immutability and memory referencing
- **Type Casting** (`Casting1.py`) — Converting between `int`, `float`, `complex`, and `bool`; valid and invalid casts
- **Collections** (`Collections.py`) — Lists: indexing, slicing, append, insert, remove, copy, sort, aliasing, nested lists
- **Conditions** (`Conditions.py`) — `if`, `elif`, `else` statements; user input
- **Iteration** (`Iteration.py`) — `for` loops with `range()`, nested loops, `continue`, logical operators (`and`, `or`)
- **Membership Operators** (`Membership.py`) — `in`, `not in`, `is`, `is not`
- **Practice Problems** (`Problems.py`) — Day/weekend checker, character type (uppercase/lowercase/digit/special), move zeros to end, second largest in array, list slicing challenges, aliasing vs copy, common elements, custom array difference sum

---

## Day 2 — Strings, Tuples & Dictionaries

### Topics

- **Strings** (`string.py`) — String methods: `lower()`, `upper()`, `title()`, `swapcase()`, `capitalize()`; f-strings and `format()`; string reversal; validation methods: `isalnum()`, `isalpha()`, `isspace()`, `islower()`, `isupper()`, `isdigit()`; `startswith()`, `endswith()`, `find()`, `index()`, `count()`
- **Tuples** (`tuple.py`) — Tuple creation and immutability, `len()`, `type()`, `id()`; tuple concatenation and repetition; nested tuples; slicing; difference between string and tuple repetition
- **Dictionaries** (`dict.py`) — Creating dictionaries, accessing by key, iterating keys/values/items; updating and adding entries; `pop()`; using tuples as keys; `copy()` vs aliasing; sorting by keys; identity comparison with `id()`; memory management with `del`
- **Practice Problems** (`problems.py`) — Remove duplicates from string, reverse a string, palindrome check, count vowels and consonants, anagram check, count special symbols and whitespaces, title case a sentence, printing patterns (square, triangle, pyramid, alphabet), product of array except self, find max/min key in dictionary, frequency count using dict, reverse a number, currency denomination breakdown

---

## Day 3 — DSA Introduction, Functions & Problem Solving

### Topics

- **DSA Intro & Time Complexity** (`DSA/first.py`) — What are Data Structures; Big-O notation: O(1) Constant, O(logN) Logarithmic, O(N) Linear, O(N²) Quadratic, O(2^N) Exponential; finding maximum element in array, linear search, row-wise maximum in a 2D grid, string manipulation with character filtering, run-length encoding concept
- **Functions** (`function.py`) — While loop; defining and calling functions; returning multiple values as tuple; types of arguments: positional, keyword, default, variable-length (`*args`); modular approach — building a menu-driven calculator with separate functions for add, subtract, multiply, divide
- **Practice Problems** (`Problems.py`) — Maximum consecutive 1s in an array, counting occurrences of a substring using sliding window

---

## Day 4 — Searching, Sorting, OOP & Stack

### Topics

- **Binary Search** (`BinarySearch.py`) — Iterative binary search using left/right/mid pointers; O(logN) time complexity; returns index of target or -1 if not found
- **Bubble Sort** (`BubbleSort.py`) — Bubble sort with nested loops and adjacent element swapping; O(N²) time complexity; security key problem — finding duplicate digits in a number using dictionary
- **Object Oriented Programming** (`OOps.py`) — Classes and objects; class attributes; default `__init__` constructor; parameterized constructor; `self` keyword; instance methods; creating multiple objects
- **Stack** (`Stack.py`) — Stack data structure implemented using a list; operations: `push()`, `pop()`, `display()`, `isEmpty()`, `peek()`, `delete()`; menu-driven stack program; stack with size limit (overflow handling); digit frequency count problem
- **Practice Problems** (`problems.py`) — Run-length encoding (character frequency in string), employee salary increment based on performance rating, gross salary calculator with HRA (20%) + TA (30%) + DA (45%)

---

## How to Run

Make sure Python 3 is installed:

```bash
python --version
```

Run any file like this:

```bash
# Day 1
python Day_1/dataType.py
python Day_1/Casting1.py
python Day_1/Collections.py
python Day_1/Conditions.py
python Day_1/Iteration.py
python Day_1/Membership.py
python Day_1/Problems.py

# Day 2
python Day_2/string.py
python Day_2/tuple.py
python Day_2/dict.py
python Day_2/problems.py

# Day 3
python Day_3/DSA/first.py
python Day_3/function.py
python Day_3/Problems.py

# Day 4
python Day_4/BinarySearch.py
python Day_4/BubbleSort.py
python Day_4/OOps.py
python Day_4/Stack.py
python Day_4/problems.py
```

---

## Requirements

- Python 3.x
- No external libraries needed — all standard Python

---

## Author

**Mentor:** Prashant Jha
