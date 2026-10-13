# Laboratory Practice n. 5 - Python (Exercises 1-8)

Turin Polytechnic University in Tashkent - Course of Computer Science

Topics: **lists**, **tuples** and **dictionaries**.

## How to start

1. Open this repository in a Codespace: **Code → Codespaces → Create codespace on main**.
2. Wait. Python is installed automatically.
3. Open the file for the exercise, for example `ex1.py`.
4. Write your code below the comment `# Write your solution below.`
5. Click the **Run Python File** button (top-right of the editor). The output shows in the terminal.

You can also run a file in the terminal:

```bash
python ex1.py
```

Do not rename the files. Some files already contain data. Use this data in your solution.

## How to submit

Run these commands in the terminal:

```bash
git add .
git commit -m "Solve lab 5"
git push
```

We grade only the code on GitHub.

## Useful reminders

```python
for name, mark in results:      # take the two values from each tuple
d.get(key, 0)                   # value for key, or 0 if the key is not there
for key, value in d.items():    # go through a dictionary
", ".join(["a", "b"])           # 'a, b'
sorted(my_list, reverse=True)   # new list, from biggest to smallest
f"{25.2857:.1f}"                # '25.3'
```

---

## Exercise 1 - Weather

You have the temperatures for one week. The data is in `ex1.py`:

```python
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temps = [24, 27, 22, 31, 29, 19, 25]
```

1. Find the hottest day and the coldest day. Use a loop. Do not use `max()` or `min()`.
2. Calculate the average temperature. Print it with 1 decimal.
3. Make a list of the days that are warmer than the average. Print the list.

Output:

```text
Hottest day: Thu (31)
Coldest day: Sat (19)
Average: 25.3
Warmer than average: ['Tue', 'Thu', 'Fri']
```

## Exercise 2 - Shopping list

Help a friend make a shopping list.

1. Read items from the user. Stop when the user types `done`.
2. Do not add the same item two times. Print a message.
3. Print the list with numbers.
4. Read one item to remove. Remove it and print the list again.
5. If the item is not in the list, print a message.

Example:

```text
Add item (done to stop): bread
Add item (done to stop): milk
Add item (done to stop): eggs
Add item (done to stop): milk
milk is already in the list.
Add item (done to stop): apples
Add item (done to stop): done
Your list:
1. bread
2. milk
3. eggs
4. apples
Remove item: eggs
Your list:
1. bread
2. milk
3. apples
```

## Exercise 3 - Exam results

Each tuple has a student name and an exam mark. The data is in `ex3.py`:

```python
results = [
    ("Aziz", 78),
    ("Malika", 92),
    ("Javohir", 55),
    ("Dilnoza", 85),
    ("Sardor", 47),
    ("Nigora", 92),
]
```

1. Make a list of students who passed (mark 60 or more). Make a list of students who failed.
2. Find the best mark. Print all students with the best mark.
3. Print the ranking from the highest mark to the lowest.

Tip for step 3: make a list of `(mark, name)` tuples and sort it. Python sorts tuples by the first value.

Output:

```text
Passed: ['Aziz', 'Malika', 'Dilnoza', 'Nigora']
Failed: ['Javohir', 'Sardor']
Best mark: 92
Best students: ['Malika', 'Nigora']
Ranking:
1. Nigora - 92
2. Malika - 92
3. Dilnoza - 85
4. Aziz - 78
5. Javohir - 55
6. Sardor - 47
```

If two students have the same mark, any order is OK.

## Exercise 4 - English-Uzbek dictionary

Make a small translator. The data is in `ex4.py`:

```python
words = {
    "apple": "olma",
    "book": "kitob",
    "water": "suv",
    "house": "uy",
    "friend": "do'st",
}
```

1. Read an English word. Change it to lower case.
2. If the word is in the dictionary, print the translation.
3. If the word is not in the dictionary, ask for the Uzbek word. Add the new word to the dictionary.
4. Do steps 1-3 again. Stop when the user types `exit`.
5. Print the number of words in the dictionary.

Example:

```text
English word: book
book = kitob
English word: Cat
I do not know cat. Uzbek word: mushuk
Saved.
English word: cat
cat = mushuk
English word: exit
The dictionary has 6 words.
```

## Exercise 5 - Class election

The class chooses a leader. Each item in the list is one vote. The data is in `ex5.py`:

```python
votes = ["Malika", "Aziz", "Malika", "Sardor", "Aziz", "Malika",
         "Dilnoza", "Aziz", "Malika", "Sardor", "Aziz", "Malika"]
```

1. Count the votes for each person. Use a dictionary: name → number of votes.
2. Print each person, the votes and the percent (1 decimal).
3. Print the winner.

Output:

```text
Malika: 5 (41.7%)
Aziz: 4 (33.3%)
Sardor: 2 (16.7%)
Dilnoza: 1 (8.3%)
Winner: Malika
```

## Exercise 6 - Cafe order

You work in a cafe. The menu is in `ex6.py`:

```python
menu = {
    "plov": 35000,
    "lagman": 30000,
    "somsa": 8000,
    "salad": 15000,
    "tea": 5000,
}
```

1. Print the menu.
2. Read a dish and a quantity. Stop when the user types `done`.
3. If the dish is not on the menu, print a message.
4. Keep the order in a dictionary: dish → quantity. If the user orders the same dish again, add to the quantity.
5. Print the receipt and the total.
6. If the total is 100000 or more, give a 10% discount.

Example:

```text
Menu:
plov - 35000
lagman - 30000
somsa - 8000
salad - 15000
tea - 5000
Dish (done to finish): plov
Quantity: 2
Dish (done to finish): pizza
Sorry, we do not have pizza.
Dish (done to finish): tea
Quantity: 3
Dish (done to finish): plov
Quantity: 1
Dish (done to finish): done
Receipt:
plov x 3 = 105000
tea x 3 = 15000
Total: 120000
Discount 10%: 12000
To pay: 108000
```

## Exercise 7 - Students by city

Each tuple has a student name and a home city. The data is in `ex7.py`:

```python
students = [
    ("Aziz", "Tashkent"),
    ("Malika", "Samarkand"),
    ("Javohir", "Tashkent"),
    ("Dilnoza", "Bukhara"),
    ("Sardor", "Samarkand"),
    ("Nigora", "Tashkent"),
    ("Bekzod", "Fergana"),
]
```

1. Make a dictionary: city → list of student names.
2. Print the cities in alphabetical order. For each city, print the number of students and their names.
3. Print the city with the most students.

Output:

```text
Bukhara (1): Dilnoza
Fergana (1): Bekzod
Samarkand (2): Malika, Sardor
Tashkent (3): Aziz, Javohir, Nigora
Biggest group: Tashkent
```

## Exercise 8 - Grade book

Each student has marks for three subjects. The data is in `ex8.py`:

```python
grades = {
    "Aziz":    {"math": 85, "physics": 72, "english": 90},
    "Malika":  {"math": 95, "physics": 88, "english": 79},
    "Javohir": {"math": 64, "physics": 91, "english": 71},
    "Dilnoza": {"math": 78, "physics": 81, "english": 96},
}
```

1. Print the average mark of each student (1 decimal).
2. Print the student with the highest average.
3. For each subject, print the student with the best mark.
4. Make a dictionary: subject → average mark. Print it (1 decimal).

Output:

```text
Student averages:
Aziz: 82.3
Malika: 87.3
Javohir: 75.3
Dilnoza: 85.0
Top student: Malika
Best in each subject:
math: Malika (95)
physics: Javohir (91)
english: Dilnoza (96)
Subject averages:
math: 80.5
physics: 83.0
english: 84.0
```
