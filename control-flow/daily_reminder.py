while True:
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ")
    time_bound = input("Is it time-bound? (yes/no): ")
    match priority:
        case "high":
            print()
            if time_bound == "yes":
                print("Reminder: \'" + task + "\' is a high priority task that requires immediate attention today!")
            else:
                print("Note: \'" + task + "\' is a high priority task. Consider completing it when you have free time.")
        case "medium":
            print()
            if time_bound == "yes":
                print("Reminder: \'" + task + "\' is a medium priority task that requires immediate attention today!")
            else:
                print("Note: \'" + task + "\' is a medium priority task. Consider completing it when you have free time.")
        case "low":
            print()
            if time_bound == "yes":
                print("Reminder: \'" + task + "\' is a low priority task that requires immediate attention today!")
            else:
                print("Note: \'" + task + "\' is a low priority task. Consider completing it when you have free time.")
        case _:
            print()
            print("Wrong priority level. Enter again")
