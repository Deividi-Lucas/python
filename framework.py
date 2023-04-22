import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [
    [sg.Text('some text on row 1')],
    [sg.Text('Enter something on row 2')],

    [sg.Button('Ok')],
    [sg.Button('Cancel')]

]

window = sg.Window('My first App', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'cancel':
        break
    print('you Enterd', values[0])

window.close()
