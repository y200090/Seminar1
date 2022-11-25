import PySimpleGUI as sg

layout = [  [sg.Text('Hello')],
            [sg.Text('World')]  ]

window = sg.Window('PySimpleGUI Sample', layout, size=(300, 150))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
window.close()
