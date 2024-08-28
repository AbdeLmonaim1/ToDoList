def main():
    message = '''
    1 - add tasks to a list
    2 - mark tasks as complete
    3 - view tasks
    4 - Quit
    '''
    global tasks
    tasks = []
    while True:
        print(message)
        choice = input("Enter your choice : ")
        if choice == '1':
            addTask()

        elif choice == '2':
            taskComplete()
        elif choice == '3':
            viewTasks()
        elif choice == '4':
            break
        else:
            print("invalid choice try again!")
def addTask():
    task = input("Enter yout task : ")
    taskInfo = {"task":task, "completed":False}
    tasks.append(taskInfo)
    print("Task added to the list successfuly :)")
def taskComplete():
    incomplete_tasks = [task for task in tasks if task["completed"] == False]
    # for task in tasks:
    #     if task["completed"] == False:
    #         incomplete_tasks.append(task)
    if len(incomplete_tasks) == 0:
        print("All tasks are completed or no tasks to mark as complete")
        return
    else:
        for i, task in enumerate(incomplete_tasks):
            print(f'{i + 1} - {task["task"]} - {task["completed"]}')
            print("-" * 30)
        taskNumber = int(input("Choose the task to complete : "))
        incomplete_tasks[taskNumber - 1]["completed"] = True
def viewTasks():
    if not tasks: #tasks emp ty
        print("No tasks added!")
    else:
        for i, task in enumerate(tasks):
            if task["completed"]:
                status = "✅"
            else:
                status = "❌"
            print(f'{i + 1} - {task["task"]} - {status}')
            print("-" * 30)
main()



