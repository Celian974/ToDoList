from colorama import Fore
from display_options import display_options
from load_tasks import load_tasks
from save_tasks import save_tasks

def apply_options():

    tasks = load_tasks()
    options = ["add", "rm", "list", "mod", "exit", "help"]

    print(Fore.WHITE + "\nWelcome to To-Do List program !")

    display_options()

    while True:
        choice = input(Fore.MAGENTA + "\nSelect an option : ").strip()

        if choice in options:
            print(Fore.GREEN + f"Selected option : {choice}")

        if choice == "list":

            if tasks:
                print(Fore.CYAN + "\nAdded tasks : \n")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
            else:
                print(Fore.RED + "\nThere are currently no tasks added.")

        elif choice == "add":
            task = input(Fore.MAGENTA + "\nEnter a new task : ").strip()
            tasks.append(task)
            save_tasks(tasks)
            print(Fore.GREEN + f"Task \"{task}\" has been successfully added.")

        elif choice == "rm":

            if tasks:
                while True:
                    try:
                        task_id = int(input(Fore.MAGENTA + "\nEnter the ID of the task to remove : ").strip())

                        if 0 < task_id <= len(tasks):
                            confirmation = input(Fore.YELLOW + "Are you sure that you want to remove this task ? [yes/no] : ")

                            if confirmation == "yes":
                                removed_task = tasks.pop(task_id - 1)
                                save_tasks(tasks)
                                print(Fore.GREEN + f"Task \"{removed_task}\" has been successfully removed.")
                                break

                            elif confirmation == "no":
                                print(Fore.YELLOW + "Aborting...")
                                break

                            else:
                                print(Fore.RED + "Incorrect choice. Aborting...")

                        else:
                            print(Fore.RED + "\nThis ID is incorrect.")

                    except ValueError:
                        print(Fore.RED + "\nInvalid input. Please enter a valid task ID (number).")

            else:
                print(Fore.RED + "\nThere are currently no tasks added.")

        elif choice == "mod":

            if tasks:
                while True:
                    try:
                        task_id = int(input(Fore.MAGENTA + "\nEnter the ID of the task to modify : ").strip())

                        if 0 < task_id <= len(tasks):
                            modified_task = input(Fore.MAGENTA + "\nEnter the new task description : ")
                            confirmation = input(Fore.YELLOW + "Are you sure that you want to modify this task ? [yes/no] : ")

                            if confirmation == "yes":
                                tasks[task_id - 1] = modified_task
                                save_tasks(tasks)
                                print(Fore.GREEN + f"Task \"{tasks[task_id - 1]}\" has been successfully updated to \"{modified_task}\".")
                                break

                            elif confirmation == "no":
                                print(Fore.YELLOW + "Aborting...")
                                break

                            else:
                                print(Fore.RED + "Incorrect choice. Aborting...")
                        else:
                            print(Fore.RED + "\nThis ID is incorrect.")

                    except ValueError:
                        print(Fore.RED + "\nInvalid input. Please enter a valid task ID (number).")

            else:
                print(Fore.RED + "\nThere are currently no tasks added.")

        elif choice == "help":
            display_options()

        elif choice == "exit":
            print(Fore.BLACK + "\nExiting program... Goodbye !\n")
            break

        else:
            print(Fore.RED + "\nThis option is incorrect.")
