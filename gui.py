import func
import PySimpleGUI as sg
import time

sg.theme("GreenMono")
clock_label = sg.Text("",key='clock')


label = sg.Text("Enter a to-do.")
input_box = sg.InputText(tooltip="Enter a todo:", key='todo')
add_button = sg.Button("Add", size=8)
list_box = sg.Listbox(values=func.get_todos(), key='todos',
                      enable_events=True, size=(40, 6))

edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
window = sg.Window("My App",
                   layout=[[clock_label],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 16))

while True:
    event, values = window.read(timeout=1000)
    window['clock'].update(value=time.strftime('%B %d, %Y %H:%M:%S'))

    #  print(event)
    #  print(values)
    #  print(values['todos'])

    match event:
        case "Add":
            todos = func.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            func.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = func.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                func.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select item first.", font=('Helvetica', 20))

        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = func.get_todos()
                todos.remove(todo_to_complete)
                func.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select item first.", font=('Helvetica', 20))

        case "Exit":
            break
        case "todos":
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()
