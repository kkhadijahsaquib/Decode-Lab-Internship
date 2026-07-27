my_tasks = []

def add_task(task):
    my_tasks.append(task)

def view_tasks():
    for index, task in enumerate(my_tasks):
        print(index, task)

def main():
    while True:
        choice = input("Type 'add' to add a task, 'view' to see tasks, or 'exit' to quit: ")
        if choice == "add":
            task = input("Enter your task: ")
            add_task(task)
        elif choice == "view":
            view_tasks()
        elif choice == "exit":
            break

if __name__ == "__main__":
    main()