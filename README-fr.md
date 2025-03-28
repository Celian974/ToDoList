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

    ```
    git clone git@github.com:Celian974/ToDoList.git
    ```

    - Avec HTTPS

    ```
    git clone https://github.com/Celian974/ToDoList.git
    ```
2. Accédez au répertoire **ToDoList** :

    ```
    cd ToDoList
## Utilisation

1. Lancez le programme en exécutant les commandes suivantes :

    ```
    make fr
    ```
    *(si vous souhaitez utiliser l'affichage en **français**)*

    ```
    make en
    ```
    *(si vous souhaitez utiliser l'affichage en **anglais**)*

2. Les options disponibles vous serons montrées, et vous serez invités à en sélectionner une :

    ```
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

```
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