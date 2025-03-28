from colorama import Fore
from display_options import display_options
from load_tasks import load_tasks
from save_tasks import save_tasks

def apply_options():

    tasks = load_tasks()
    options = ["add", "rm", "list", "mod", "exit", "help"]

    print(Fore.WHITE + "\nBienvenue dans le programme To-Do List !")

    display_options()

    while True:
        choice = input(Fore.MAGENTA + "\nSélectionnez une option : ").strip()

        if choice in options:
            print(Fore.GREEN + f"Option sélectionée : {choice}")

        if choice == "list":

            if tasks:
                print(Fore.CYAN + "\nTâches ajoutées : \n")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")

            else:
                print(Fore.RED + "\nIl n'y a actuellement aucune tâche ajoutée.")

        elif choice == "add":
            task = input(Fore.MAGENTA + "\nEntrez une nouvelle tâche : ").strip()
            tasks.append(task)
            save_tasks(tasks)
            print(Fore.GREEN + f"La tâche \"{task}\" a été ajoutée avec succès.")

        elif choice == "rm":

            if tasks:
                while True:
                    try:
                        task_id = int(input(Fore.MAGENTA + "\nEntrez l'identifiant de la tâche à supprimer : ").strip())

                        if 0 < task_id <= len(tasks):
                            confirmation = input(Fore.YELLOW + "Êtes-vous sûr de vouloir supprimer cette tâche ? [oui/non] : ")

                            if confirmation == "oui":
                                removed_task = tasks.pop(task_id - 1)
                                save_tasks(tasks)
                                print(Fore.GREEN + f"La tâche \"{removed_task}\" a été supprimée avec succès.")

                            elif confirmation == "non":
                                print(Fore.YELLOW + "Annulation...")

                            else:
                                print(Fore.RED + "Choix incorrect. Annulation...")

                        else:
                            print(Fore.RED + "Cet identifiant est incorrect.")

                    except ValueError:
                        print(Fore.RED + "\nEntrée incorrecte. Veuillez entrer un identifiant de tâche valide (nombre).")

            else:
                print(Fore.RED + "\nIl n'y a actuellement aucune tâche ajoutée.")

        elif choice == "mod":

            if tasks:
                while True:
                    try:
                        task_id = int(input(Fore.MAGENTA + "\nEntrez l'identifiant de la tâche à modifier : ").strip())

                        if 0 < task_id <= len(tasks):
                            modified_task = input(Fore.MAGENTA + "\nEntrez la nouvelle description de la tâche: ")
                            confirmation = input(Fore.YELLOW + "Êtes-vous sûr de vouloir modifier cette tâche ? [oui/non] : ")

                            if confirmation == "oui":
                                print(Fore.GREEN + f"Task \"{tasks[task_id - 1]}\" a été modifiée en \"{modified_task}\" avec succès.")
                                tasks[task_id - 1] = modified_task
                                save_tasks(tasks)
                                break
                            elif confirmation == "non":
                                print(Fore.YELLOW + "Annulation...")

                            else:
                                print(Fore.RED + "Choix incorrect. Annulation...")

                        else:
                            print(Fore.RED + "Cet identifiant est incorrect.")

                    except ValueError:
                        print(Fore.RED + "\nEntrée incorrecte. Veuillez entrer un identifiant de tâche valide (nombre).")

            else:
                print(Fore.RED + "\nIl n'y a actuellement aucune tâche ajoutée.")

        elif choice == "help":
            display_options()

        elif choice == "exit":
            print(Fore.BLACK + "\nFermeture du programme... Au-revoir !\n")
            break

        else:
            print(Fore.RED + "\nCette option est incorrecte.")
