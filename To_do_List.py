def main():
    tasks = [] #Create an empty list to store tasks


    while True: # Show menu
        print("\n==== To-Do List ====")
        print("1. Add Task")
        print("2. Show Task")
        print("3. Mark Task as Done")
        print("4. Exit")

        choice = input("Enter Your Choice: ") # Get user choice

         # Process the choice

          # Add tasks

        if choice == '1':
            print()
            n_tasks = int(input("How many task you want to Add: "))

            for i in range(n_tasks):
                task = input("Enter the task: ")
                tasks.append({"task": task, "Done": False})
                print("Task added!")

                 # Show tasks

        elif choice == '2':
            print("\nTasks:")
            for index, task in enumerate(tasks):
                status = "Done" if task["Done"] else "Not Done"
                print(f"{index + 1}. {task['task']} - {status}")


# Mark task as done
        elif choice == '3':
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["Done"] = True
                print("Task marked as done!")
            else:
                print("Invalid task number")



        elif choice == '4':
            print("Exiting the To-Do List")
            break  # Exit the loop


        
        else:
            print("Invalid choice. Please try again")


if __name__ == "__main__":
    main()