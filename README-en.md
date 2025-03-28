# ToDoList

## Description

This is a terminal-based application that allows users to create a To-Do List and manage their tasks efficiently by adding, removing, modifying, listing their tasks. Tasks are stored in a JSON file to ensure persistence across sessions.

## Features

- Add a new task
- Delete a task (with confirmation)
- Modify an existing task (with confirmation)
- List all tasks
- Help menu to display available options
- Exit option to quit the program at any time (with tasks remaining saved)
- Color-coded interface to improve readability

## Installation

### Prerequisistes

Make sure you have *python3* installed on your system. You also need *colorama* module for colored output.

### Steps

1. Clone this repository :
    - Using SSH

    ```
    git clone git@github.com:Celian974/ToDoList.git
    ```

    - Using HTTPS

    ```
    git clone https://github.com/Celian974/ToDoList.git
    ```
2. Navigate to **ToDoList** directory :

    ```
    cd ToDoList
## Usage

1. Run the program by running the following commands :

    ```
    make fr
    ```
    *(if you want to use the **french** display)*

    ```
    make en
    ```
    *(if you want to use the **english** display)*

2. You will be shown the available options, and prompted to select one :

    ```
    ➜  ToDoList git:(main) ✗ make en
    /bin/python3 src/en/to_do_list.py

    Welcome to To-Do List program !

    Available options :

    1. "list" - List tasks
    2. "add" - Add a task
    3. "rm" - Remove a task
    4. "mod"- Modify a task
    5. "help" - Display available options
    6. "exit" - Exit program

    Select an option :
    ```
3. Choose **add** to create a new task, **rm** to delete a task, **list** to display the existing tasks, and so on. You can use **help** option when prompted to choose an option if you need to look at the available optîons.

### Example session

```
➜  ToDoList git:(main) ✗ make en
/bin/python3 src/en/to_do_list.py

Select an option : add
Selected option : add

Enter a new task : test
Task "test" has been successfully added.

Select an option : list

Added tasks :

1. test

Select an option :

```