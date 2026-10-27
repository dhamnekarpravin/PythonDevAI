Day 1: Python Basics
1. What is a variable in Python?
A variable is a name that stores a value. You can think of it as a labeled box that holds data.

```python
name = "John"
age = 25
```

Python is dynamically typed, meaning you don't need to declare the type - Python figures it out from the value.

**Simple answer:** A variable is like a container with a label that holds data.

========================

2. What are the main data types in Python?
- **int**: Whole numbers (e.g., 5, 10, -3)
- **float**: Decimal numbers (e.g., 3.14, 2.5)
- **str**: Text or strings (e.g., "hello", 'world')
- **bool**: True or False
- **list**: Ordered, changeable collection (e.g., [1, 2, 3])
- **tuple**: Ordered, unchangeable collection (e.g., (1, 2, 3))
- **dict**: Key-value pairs (e.g., {"name": "John", "age": 25})
- **set**: Unique values only (e.g., {1, 2, 3})

**Simple answer:** Different types for different kinds of data - numbers, text, lists of items, etc.

========================

3. What is the difference between list and tuple?
- **List**: Mutable (can be changed), uses square brackets `[]`
- **Tuple**: Immutable (cannot be changed), uses parentheses `()`

```python
my_list = [1, 2, 3]  # Can add/remove/change
my_tuple = (1, 2, 3) # Cannot change after creation
```

**Simple answer:** Lists can be edited; tuples cannot be edited once created.

========================

4. What is a dictionary?
A dictionary stores data in key-value pairs. You use a key to find its value.

```python
person = {
    "name": "John",
    "age": 25
}
print(person["name"])  # Output: John
```

**Simple answer:** Like a contact book - you look up by name (key) to get details (value).

========================

5. What is a function?
A function is a reusable block of code that does a specific task. You give it input, it processes, and returns output.

```python
def add(a, b):
    return a + b

result = add(5, 3)  # Output: 8
```

**Simple answer:** A function is like a machine - you put something in, it does work, and gives something back.

========================

6. Difference between for loop and while loop?
- **for loop**: Used when you know how many times to iterate or what you're iterating over
- **while loop**: Used when you want to repeat until a condition changes

```python
# for loop - go through each item
for item in [1, 2, 3]:
    print(item)

# while loop - repeat until condition is false
while x < 10:
    x += 1
```

**Simple answer:** Use for when you know the items; use while when you repeat until something happens.

========================

7. What is exception handling?
Exception handling prevents your program from crashing when errors occur. You use try-except blocks.

```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Please enter a valid number!")
```

**Simple answer:** It's a safety net - if something goes wrong, your program handles it gracefully instead of crashing.

========================

8. What is the difference between break and continue?
- **break**: Stops the loop completely
- **continue**: Skips the current iteration and moves to the next

```python
for i in range(5):
    if i == 3:
        break  # Loop stops here
    print(i)

for i in range(5):
    if i == 3:
        continue  # Skip 3, continue with 4
    print(i)
```

**Simple answer:** break stops the loop; continue skips to the next round.

========================

9. What is Git and GitHub?
- **Git**: Version control system that tracks changes in your code locally
- **GitHub**: Online platform to store and share Git repositories

**Simple answer:** Git is your local time machine for code; GitHub is the online backup and sharing place.

========================

10. Why use virtual environments?
Virtual environments give each project its own isolated set of packages. This prevents conflicts between projects that need different versions of the same package.

```bash
python -m venv myenv
myenv\Scripts\activate  # Windows
```

**Simple answer:** Each project gets its own toolbox so tools don't interfere with each other.

========================

Day 2: OOP and Modules
11. What is Object-Oriented Programming (OOP)?
OOP is a way to organize code using "objects" that contain both data and behavior. Instead of writing everything as separate functions, you group related data and actions together.

**Simple answer:** Instead of scattered code, you create objects that know their own data and what they can do.

========================

12. What is a class?
A class is a blueprint or template for creating objects. It defines the properties and methods that objects of that class will have.

```python
class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False
```

**Simple answer:** A class is like a design blueprint; objects are the actual things built from that design.

========================

13. What is an object?
An object is an instance of a class. It's a concrete thing created from the class blueprint.

```python
task1 = Task("Learn Python")  # task1 is an object
task2 = Task("Build project") # task2 is another object
```

**Simple answer:** If the class is the blueprint, the object is the actual house built from it.

========================

14. What is __init__?
`__init__` is a special method that runs automatically when you create a new object. It sets up the object's initial data.

```python
def __init__(self, title):
    self.title = title  # Runs when object is created
```

**Simple answer:** It's the setup code that runs when an object is born.

========================

15. What is self?
`self` refers to the current object instance. It lets methods access the object's own data.

```python
def mark_complete(self):
    self.completed = True  # self.completed belongs to this specific object
```

**Simple answer:** self means "this particular object" - it refers to the object calling the method.

========================

16. Difference between class and object?
- **Class**: Blueprint/template, defines structure and behavior
- **Object**: Actual instance created from the class, holds real data

**Simple answer:** Class is the design; object is the real thing made from that design.

========================

17. What is inheritance?
Inheritance lets a child class reuse properties and methods from a parent class. The child can add its own features or change parent behavior.

```python
class Task:
    def __init__(self, title):
        self.title = title

class UrgentTask(Task):  # Inherits from Task
    priority = "high"
```

**Simple answer:** A child class gets all the parent's features and can add its own extras.

========================

18. Why use inheritance?
Inheritance avoids code duplication. If multiple classes share common features, put them in a parent class and let children inherit.

**Simple answer:** Reuse code instead of writing the same thing multiple times.

========================

19. What is a dataclass?
A dataclass is a simplified class for storing data. The `@dataclass` decorator automatically generates common methods like `__init__`, `__repr__`, and `__eq__`.

```python
from dataclasses import dataclass

@dataclass
class Task:
    title: str
    completed: bool = False
```

**Simple answer:** A shortcut class that automatically handles the boring setup code for data storage.

========================

20. When to use dataclass vs normal class?
- **Use dataclass**: When the class mainly stores data with simple behavior
- **Use normal class**: When the class has complex logic or many custom methods

**Simple answer:** Dataclass for storing data; normal class for doing complex work.

========================

21. What is a module?
A module is a single Python file containing code (functions, classes, variables) that can be imported into other files.

```python
from mymodule import my_function
```

**Simple answer:** One Python file that other files can borrow code from.

========================

22. What is a package?
A package is a folder containing multiple related modules. It must have an `__init__.py` file.

```
my_package/
    __init__.py
    module1.py
    module2.py
```

**Simple answer:** A folder of related Python files that work together.

========================

23. Why split code into modules?
- Better organization and readability
- Easier to find and fix bugs
- Reusable code across projects
- Easier for teams to work together
- Simpler testing

**Simple answer:** Don't put everything in one giant file - organize it into smaller, focused files.

========================

24. What is pip?
pip is Python's package installer. It downloads and installs external libraries from the Python Package Index (PyPI).

```bash
pip install requests
```

**Simple answer:** Like an app store for Python packages.

========================

25. What is requirements.txt?
A file that lists all external packages your project needs with their versions.

```
requests==2.32.3
numpy==1.26.0
```

Others can install all dependencies with:
```bash
pip install -r requirements.txt
```

**Simple answer:** Your project's shopping list of required packages.

========================

Project-based questions
26. Why did you use classes in your task tracker?
Classes group related data and behavior together. A `Task` object knows its own title and status, while a `TaskTracker` manages the list. This makes code organized and easier to maintain.

**Simple answer:** Keeps data and actions together instead of scattered everywhere.

========================

27. Why separate CLI from business logic?
Separation of concerns - the CLI handles user input/output, while the tracker handles the actual task operations. This makes the code easier to test and modify.

**Simple answer:** The receptionist talks to users; the manager does the actual work.

========================

28. How would you add a new feature like task priority?
1. Add `priority` field to the Task class
2. Update display logic to show priority
3. Add menu option in CLI for setting priority
4. Add filtering method in tracker if needed

**Simple answer:** Update the data model first, then the behavior, then the user interface.

========================

29. How do you handle invalid user input?
Validate input in the business logic layer and raise appropriate errors. The CLI catches these errors and shows friendly messages to the user.

**Simple answer:** Check the input, catch errors, and show helpful messages instead of crashing.

========================

30. How would you test your task tracker?
Test both happy paths and error cases:
- Add valid task
- Reject empty task title
- Complete a task
- Handle invalid task numbers
- Delete a task
- Display empty list

**Simple answer:** Test what should work and what should fail.

==========================

# Day 3: Git, HTTP, and Web Fundamentals

## 31. What is a Git branch?
A branch is a separate version of your code that lets you work on features without affecting the main code. You can create, switch, and merge branches.

```bash
git branch feature-login    # Create branch
git checkout feature-login  # Switch to branch
git merge feature-login     # Merge branch
```

**Simple answer:** A branch is like a separate workspace where you can experiment without breaking the main code.

---

## 32. What is a Git commit?
A commit saves your changes with a message describing what you did. Each commit is a snapshot of your code at that moment.

```bash
git add .
git commit -m "Add login feature"
```

**Simple answer:** A commit is like saving your work with a note explaining what you changed.

---

## 33. What is a pull request (PR)?
A pull request is a way to propose changes from one branch to another. It lets team members review your code before merging.

**Simple answer:** A PR is asking teammates to review your code before you merge it into the main project.

---

## 34. What are the main HTTP methods?
- **GET**: Retrieve data (e.g., get all tasks)
- **POST**: Create new data (e.g., add a task)
- **PUT/PATCH**: Update existing data (e.g., edit a task)
- **DELETE**: Remove data (e.g., delete a task)

**Simple answer:** GET to read, POST to create, PUT/PATCH to update, DELETE to remove.

---

## 35. What is JSON?
JSON (JavaScript Object Notation) is a lightweight format for storing and exchanging data. It's easy for humans to read and machines to parse.

```json
{
  "title": "Learn Python",
  "completed": false
}
```

**Simple answer:** A simple text format for sending data between servers and apps.

---

## 36. What are HTTP headers?
HTTP headers are extra information sent with requests and responses. They tell the server/client details like content type, authentication, or caching.

```http
Content-Type: application/json
Authorization: Bearer token123
```

**Simple answer:** Metadata about the request/response - like labels on a package.

---

## 37. What is REST?
REST (Representational State Transfer) is an architectural style for APIs. It uses standard HTTP methods and is stateless (each request contains all needed info).

**Simple answer:** A standard way to build APIs using HTTP methods like GET, POST, PUT, DELETE.

---

## 38. What are browser developer tools?
Developer tools are built-in browser features (F12) that let you inspect HTML, debug JavaScript, view network requests, and analyze performance.

**Simple answer:** Tools in your browser to see how websites work and fix problems.

---

## 39. What is the difference between PUT and PATCH?
- **PUT**: Replaces the entire resource with new data
- **PATCH**: Updates only the specified fields of a resource

**Simple answer:** PUT replaces everything; PATCH updates only what you specify.

---

## 40. What makes a good README?
A good README includes:
- Project description and purpose
- Installation instructions
- Usage examples
- Features list
- How to contribute
- License information

**Simple answer:** Clear documentation that helps others understand and use your project.

---

## HTTP Status Codes Reference

| Code                      | Meaning                   | Example                            |
| ------------------------- | ------------------------- | ---------------------------------- |
| 200 OK                    | Success                   | Task list returned                 |
| 201 Created               | New resource created      | New task added                     |
| 400 Bad Request           | Client sent invalid data  | Empty task title                   |
| 401 Unauthorized          | Not logged in             | Missing token                      |
| 403 Forbidden             | Logged in but not allowed | Trying to edit another user's task |
| 404 Not Found             | Resource does not exist   | Invalid task ID                    |
| 500 Internal Server Error | Server-side problem       | Bug in backend code                |

