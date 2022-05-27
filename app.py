import PySimpleGUI as sg

layout = [
[
sg.Text('Info', enable_events= True, key= '-TEXTINFO-'), 
sg.Spin(['item 1', 'item 2'], key='-SELECTITEM-')
], 
[
sg.Button('Cacher', key='-BTNCACHER-'), 
sg.Button('Afficher', key='-BTNAFFICHER-')
],
[sg.Button('Lire', key = '-BTNLIRE-')], 
[sg.Input(key='-INPUT1-')],
[
sg.Text("Valeurs", key='-TTINFO-'), 
sg.Button('Tout lire', key = '-BTNTTLIRE-')
], 
]

window = sg.Window('Converter', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-BTNCACHER-':
        window['-TEXTINFO-'].update(visible = False)
        window['-SELECTITEM-'].update(visible = False)
    
    if event == '-BTNAFFICHER-':
        window['-TEXTINFO-'].update(visible = True)
        window['-SELECTITEM-'].update(visible = True)

    if event == '-BTNLIRE-':
        window['-TEXTINFO-'].update(values['-INPUT1-'])

    if event == '-BTNTTLIRE-':
       window['-TTINFO-'].update(values)

window.close()