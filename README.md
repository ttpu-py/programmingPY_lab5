# Laboratory Practice n. 5 - Python (Exercises 1-8)

Turin Polytechnic University in Tashkent - Course of Computer Science

Topics: **lists**, **tuples** and **dictionaries**.

## Getting started in GitHub Codespaces

Open this repository in a Codespace (**Code → Codespaces → Create codespace on main**). Python and the VS Code Python extension are installed automatically.

Each exercise has its own Python file (`ex1.py` ... `ex8.py`). Open the file you are working on and use the **Run Python File** button in the top-right corner of the editor. The program runs in the terminal below the editor.

You can also run a file from the terminal:

```bash
python ex1.py
```

Replace `ex1.py` with the file you want to test. Do not rename the provided files.

Before the deadline, commit and push your work:

```bash
git add .
git commit -m "Solve lab 5"
git push
```

Only work pushed to GitHub is graded. Read input with `input()` and display output with `print()`.

The exercises get harder as you go, so solve them in order. Try to match the example output exactly, and test your programs with your own inputs too, not only the examples.

### Useful reminders

```python
"3 8 1 5".split()          # ['3', '8', '1', '5']
x, y = (4, 7)              # tuple unpacking: x = 4, y = 7
", ".join(["a", "b"])      # 'a, b'
d.get(key, 0)              # value for key, or 0 if key is missing
for key, value in d.items():
    ...
f"{3.14159:.2f}"           # '3.14'
```

---

## Exercise 1 - Number statistics

Repeatedly read integers, one per line, and store them in a list. Stop when the user enters `0` (the `0` is **not** part of the list).

Then display:

- the list itself
- how many numbers were entered
- the sum, the average (2 decimal places), the minimum and the maximum
- a new list with the numbers that are **strictly greater** than the average
- a new list with the values without duplicates, in the order they first appeared

Compute the sum, the minimum and the maximum with a loop. **Do not** use the built-in `sum()`, `min()` or `max()` in this exercise.

If the first number is `0`, print `No numbers entered.` and stop.

Example:

```text
Input a number (0 to stop): 4
Input a number (0 to stop): -2
Input a number (0 to stop): 7
Input a number (0 to stop): 4
Input a number (0 to stop): 9
Input a number (0 to stop): 7
Input a number (0 to stop): 0
Numbers: [4, -2, 7, 4, 9, 7]
Count: 6
Sum: 29
Average: 4.83
Minimum: -2
Maximum: 9
Above average: [7, 9, 7]
Unique values: [4, -2, 7, 9]
```

```text
Input a number (0 to stop): 0
No numbers entered.
```

Write the solution in `ex1.py`.

## Exercise 2 - Matrix

A matrix can be stored as a **list of lists**, where each inner list is one row.

Read the number of rows `r` and the number of columns `c`. Then read `r` rows; each row is one line with `c` integers separated by spaces. If a row does not contain exactly `c` numbers, print `Row must contain c numbers.` (with the real value of `c`) and ask for the same row again.

Then display:

- the matrix, one row per line
- the list of row sums
- the list of column sums
- the transposed matrix (rows become columns)
- the largest element and its position as a tuple `(row, column)`, counting from 1. If the largest value appears more than once, show the first one (top to bottom, left to right).

Example:

```text
Input number of rows: 3
Input number of columns: 4
Row 1: 3 8 1 5
Row 2: 7 2 9
Row must contain 4 numbers.
Row 2: 7 2 9 4
Row 3: 6 0 9 1
Matrix:
3 8 1 5
7 2 9 4
6 0 9 1
Row sums: [17, 22, 16]
Column sums: [16, 10, 19, 10]
Transposed:
3 7 6
8 2 0
1 9 9
5 4 1
Largest element: 9 at position (2, 3)
```

Write the solution in `ex2.py`.

## Exercise 3 - Points on a plane

Read an integer `n` (`n >= 2`), then `n` points. Each point is one line with two integers `x y`. Store every point as a **tuple** `(x, y)` in a list.

Then display:

- the list of points
- how many points are in each quadrant (I, II, III, IV), and how many lie on an axis (`x == 0` or `y == 0`)
- the point farthest from the origin `(0, 0)` and its distance
- the **closest pair** of points and the distance between them

Distances are printed with 2 decimal places. The distance between `(x1, y1)` and `(x2, y2)` is `((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5`.

If there is a tie, keep the point (or pair) that was found first. To find the closest pair, compare every point with every point that comes **after** it in the list.

Quadrants:

```text
        y
   II   |   I
 -------+-------> x
   III  |   IV
```

Example:

```text
Input number of points: 5
Point 1: 1 2
Point 2: -3 4
Point 3: -1 -1
Point 4: 5 0
Point 5: 2 3
Points: [(1, 2), (-3, 4), (-1, -1), (5, 0), (2, 3)]
Quadrant I: 2
Quadrant II: 1
Quadrant III: 1
Quadrant IV: 0
On an axis: 1
Farthest from origin: (-3, 4), distance 5.00
Closest pair: (1, 2) and (2, 3), distance 1.41
```

Note that `(-3, 4)` and `(5, 0)` are both at distance `5.00`; `(-3, 4)` is shown because it comes first.

Write the solution in `ex3.py`.

## Exercise 4 - Word frequency

Read one line of text. Count how many times each word appears using a **dictionary** (word → count).

Rules:

- Words are separated by spaces.
- Upper and lower case do not matter: `The` and `the` are the same word. Convert every word to lower case.
- Remove the punctuation characters `. , ! ? ; :` from the beginning and end of each word (hint: `word.strip(".,!?;:")`).

Then display:

- the total number of words and the number of different words
- every word with its count, in the order the words **first appeared** in the text
- the most frequent word and its count (if there is a tie, the one that appeared first)
- a list of the words that were used exactly once

Example:

```text
Enter a sentence: The cat and the dog. The dog barked, and the cat ran!
Total words: 12
Unique words: 6
the: 4
cat: 2
and: 2
dog: 2
barked: 1
ran: 1
Most frequent: the (4 times)
Words used once: ['barked', 'ran']
```

Write the solution in `ex4.py`.

## Exercise 5 - Shop inventory

Write a program that manages the stock of a small shop. Keep the stock in a **dictionary** (item name → quantity). The program repeatedly reads a command after the prompt `> ` until the command `end` is entered.

| Command | What it does |
| --- | --- |
| `add <item> <qty>` | Adds `qty` pieces of `item`. If the item is new, it is created. |
| `sell <item> <qty>` | Removes `qty` pieces of `item`. If the quantity becomes `0`, the item is deleted from the dictionary. |
| `show` | Prints every item and its quantity in **alphabetical** order, or `Inventory is empty.` |
| `end` | Stops the program and prints the total number of pieces in stock. |

Errors:

- Selling an item that is not in the dictionary prints `Error: <item> is not in stock.`
- Selling more pieces than available prints `Error: only <n> <item> left.` and changes nothing.
- Any other command prints `Unknown command.`

Item names are single words and quantities are positive integers. Successful `add` and `sell` commands print nothing.

Example:

```text
> add apple 10
> add banana 5
> add apple 3
> sell apple 4
> sell orange 1
Error: orange is not in stock.
> sell banana 7
Error: only 5 banana left.
> sell banana 5
> show
apple: 9
> add cherry 20
> show
apple: 9
cherry: 20
> buy milk 2
Unknown command.
> end
Total items: 29
```

```text
> show
Inventory is empty.
> end
Total items: 0
```

Write the solution in `ex5.py`.

## Exercise 6 - Anagram groups

Two words are **anagrams** if they contain exactly the same letters, possibly in a different order: `listen`, `silent` and `enlist` are anagrams.

Read words, one per line, until an empty line is entered. Ignore upper/lower case when comparing words. If a word was already entered before (ignoring case), print `<word> was already entered.` and skip it.

Group the words that are anagrams of each other using a **dictionary**:

- the **key** is a tuple with the sorted letters of the lower-case word, for example `tuple(sorted("listen"))` → `('e', 'i', 'l', 'n', 's', 't')`
- the **value** is a list of the words (as they were typed) that have this key

Then display:

- every group with **at least two** words, one group per line, words separated by `, `. Groups appear in the order their first word was entered, and words keep their input order. If there are no such groups, print `(none)`.
- the number of such groups
- the words that have no anagram, separated by `, ` (or `(none)`)

Example:

```text
Word (empty line to stop): listen
Word (empty line to stop): silent
Word (empty line to stop): apple
Word (empty line to stop): Enlist
Word (empty line to stop): stone
Word (empty line to stop): dog
Word (empty line to stop): Papel
Word (empty line to stop): tones
Word (empty line to stop): silent
silent was already entered.
Word (empty line to stop): notes
Word (empty line to stop): cat
Word (empty line to stop): act
Word (empty line to stop): bird
Word (empty line to stop):
Anagram groups:
listen, silent, Enlist
apple, Papel
stone, tones, notes
cat, act
Number of groups: 4
No anagrams: dog, bird
```

Write the solution in `ex6.py`.

## Exercise 7 - Grade book

Read grade records, one per line, until `end` is entered. Each record has the form `name subject grade`, for example `Alice math 90`. Names and subjects are single words; grades are integers.

Store the data in a **nested dictionary**: the key is the student name and the value is another dictionary (subject → grade):

```python
{"Alice": {"math": 90, "physics": 85}, "Bob": {...}, ...}
```

If the same student gets a grade for the same subject more than once, keep only the **higher** grade.

Then display:

1. `Students:` followed by one line per student in **alphabetical** order: their subjects with grades (in the order the subjects were first entered for that student) and their average (2 decimal places).
2. `Best per subject:` followed by one line per subject in **alphabetical** order with the student who has the highest grade in it. If two students have the same grade, show the one whose name comes first alphabetically.
3. The student with the highest average (if there is a tie, the one whose name comes first alphabetically).

Example:

```text
Record: Alice math 90
Record: Bob math 78
Record: Alice physics 85
Record: Carol math 95
Record: Bob physics 92
Record: Carol history 88
Record: Alice math 70
Record: Bob history 81
Record: Bob math 85
Record: end
Students:
Alice: math=90, physics=85, average=87.50
Bob: math=85, physics=92, history=81, average=86.00
Carol: math=95, history=88, average=91.50
Best per subject:
history: Carol (88)
math: Carol (95)
physics: Bob (92)
Top student: Carol (91.50)
```

Here `Alice math 70` is ignored because Alice already has 90 in math, while `Bob math 85` replaces Bob's 78.

Write the solution in `ex7.py`.

## Exercise 8 - Travel route

A traveller has `n` train tickets for one continuous trip, but the tickets got mixed up. Each ticket is one line `from to price`, for example `Tashkent Samarkand 120`. City names are single words, and every city is visited at most once.

Read `n` and the `n` tickets. Store them in a **dictionary** where the key is the departure city and the value is a **tuple** `(destination, price)`.

**Part 1 - Rebuild the route.** Find the starting city: it is the only city that appears as a departure but never as a destination. Then follow the tickets from city to city and display:

- the whole route, cities separated by ` -> `
- every leg of the trip, numbered, with its price
- the total cost
- the most expensive leg

**Part 2 - Queries.** After that, repeatedly read queries `A B` until `end` is entered. For each query print:

- `Cost from A to B: <cost>`: the sum of the ticket prices travelling along the route from `A` to `B`
- `Cannot travel from A to B.` if `B` comes **before** `A` on the route
- `Unknown city: <city>` if one of the cities is not on the route (check `A` first)

Example:

```text
Input number of tickets: 4
Ticket 1: Bukhara Khiva 150
Ticket 2: Tashkent Samarkand 120
Ticket 3: Khiva Nukus 90
Ticket 4: Samarkand Bukhara 100
Route: Tashkent -> Samarkand -> Bukhara -> Khiva -> Nukus
Legs:
1. Tashkent -> Samarkand: 120
2. Samarkand -> Bukhara: 100
3. Bukhara -> Khiva: 150
4. Khiva -> Nukus: 90
Total cost: 460
Most expensive leg: Bukhara -> Khiva (150)
Query: Samarkand Khiva
Cost from Samarkand to Khiva: 250
Query: Tashkent Nukus
Cost from Tashkent to Nukus: 460
Query: Khiva Samarkand
Cannot travel from Khiva to Samarkand.
Query: Bukhara Andijan
Unknown city: Andijan
Query: end
```

Write the solution in `ex8.py`.
