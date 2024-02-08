import func
import PySimpleGUI as sg


label = sg.Text('Enter a to-do.')
input_box = sg.InputText(tooltip="Enter a todo:", key='todo')
add_button = sg.Button("Add")
list_box = sg.Listbox(values=func.get_todos(), key='todos',
                      enable_events=True, size=[45,10])

edit_button = sg.Button("Edit")

window = sg.Window('My App',
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=('Helvetica', 16))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = func.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            func.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = func.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            func.write_todos(todos)
            window['todos'].update(values=todos)
        case "todos":
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()
