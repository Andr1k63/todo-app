import func
import PySimpleGUI as sg


label = sg.Text('Enter a to-do.')
input_box = sg.InputText(tooltip="Enter a todo:", key='todo')
add_button = sg.Button("Add")

window = sg.Window('My App',
                   layout=[[label], [input_box, add_button]],
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
        case sg.WIN_CLOSED:
            break

window.close()
