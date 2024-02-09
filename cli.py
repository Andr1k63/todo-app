#  from func import get_todos, write_todos
import func
import time

now = time.strftime('%B %d, %Y %H:%M:%S')

print(f"It is:{now}")

while True:
    user_action = input("Type add,show,edit,complete or exit:")
    user_action = user_action.strip()  # or another title()-every word cap()

    if user_action.startswith('add') or user_action.startswith('new'):
        todo = user_action[4:]

        todos = func.get_todos()

        todos.append(todo + '\n')

        func.write_todos(todos)
    elif user_action.startswith('show'):

        todos = func.get_todos()
        # new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)
            number = number-1

            todos = func.get_todos()

            new_todo = input("Enter new todo:")
            todos[number] = new_todo + '\n'

            func.write_todos(todos)

        except ValueError:
            print("You enter a valid command.Try again!")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = func.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            func.write_todos(todos)

            message = f"Todo {todo_to_remove} is removed from the list."
            print(message)

        except IndexError:
            print("This number isn't at list")
            continue
    elif user_action.startswith('exit'):
        break
    else:
        print("Command isn't valid.")

print("Bye!")
