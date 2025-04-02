# ToDoList

## Description

This is a terminal-based application that allows users to create a to-do-list and manage their tasks efficiently by adding, removing, modifying, listing their tasks. Tasks are stored in a JSON file to ensure persistence across sessions.

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

    ```bash
    git clone git@github.com:Celian974/ToDoList.git
    ```

    - Using HTTPS

    ```bash
    git clone https://github.com/Celian974/ToDoList.git
    ```
2. Navigate to **ToDoList** directory :

    ```bash
    cd ToDoList
## Usage

1. Run the program by running the following commands :

    ```bash
    make fr
    ```
    *(if you want to use the **french** display)*

    ```bash
    make en
    ```
    *(if you want to use the **english** display)*

2. You will be shown the available options, and prompted to select one :

    ```bash
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

```bash
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

# ToDoList

## Description

Il s'agit d'une application de terminal permettant aux utilisateurs de créer une liste de tâches et de gérer efficacement leurs tâches en les ajoutant, supprimant, modifiant, et listant. Les tâches sont stockées dans un fichier JSON file pour assurer la persistence entre les sessions.

## Fonctionnalités

- Ajouter une nouvelle tâche
- Supprimer une tâche (avec confirmation)
- Modifier une tâche existante (avec confirmation)
- Lister toutes les tâches
- Menu d'aide pour afficher les options disponibles
- Option de sortie pour quitter le programme (les tâches restent enregistrées)
- Interface avec code couleur pour améliorer la lisibilité

## Installation

### Prérequis

Assurez-vous que *python3* est installé sur votre système. Vous avez également besoin du module *colorama* pour l'affichage en couleur.

### Étapes

1. Clonez ce dépot :
    - Avec SSH

    ```bash
    git clone git@github.com:Celian974/ToDoList.git
    ```

    - Avec HTTPS

    ```bash
    git clone https://github.com/Celian974/ToDoList.git
    ```
2. Accédez au répertoire **ToDoList** :

    ```bash
    cd ToDoList
## Utilisation

1. Lancez le programme en exécutant les commandes suivantes :

    ```bash
    make fr
    ```
    *(si vous souhaitez utiliser l'affichage en **français**)*

    ```bash
    make en
    ```
    *(si vous souhaitez utiliser l'affichage en **anglais**)*

2. Les options disponibles vous serons montrées, et vous serez invités à en sélectionner une :

    ```bash
    ➜  ToDoList git:(main) ✗ make en
    /bin/python3 src/en/to_do_list.py

    Bienvenue dans le programme To-Do List !

    Options disponibles :

    1. "list" - Lister les tâches
    2. "add" - Ajouter une tâche
    3. "rm" - Supprimer une tâche
    4. "mod"- Modifier une tâche
    5. "help" - Afficher les options disponibles
    6. "exit" - Quitter le programme

    Sélectionnez une option :
    ```
3. Choisissez **add** pour créer une nouvelle tâche, **rm** pour supprimer une tâche, **list** pour lister les tâches existantes, etc. Vous pouvez utiliser l'option **help** si vous avez besoin d'afficher les option disponibles

### Exemple de session

```bash
➜  ToDoList git:(main) ✗ make fr
/bin/python3 src/en/to_do_list.py

Sélectionnez une option : add
Option sélectionnée : add

Entrez une nouvelle tâche : test
La tâche "test" a été ajoutée avec succès.

Sélectionnez une option : list

Tâches ajoutées :

1. test

Sélectionnez une option :

```
