import PySimpleGUI as sg
layout = [
    [sg.Text("Usuário")],
    [sg.Input(key='Usuário')],
    [sg.Text('Senha')],
    [sg.Input(key='Senha')],
    [sg.Button('Entrar')],
    [sg.Text('', key ='messagem')],
]

window = sg.Window('Exercico_Wagner', layout=layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Entrar':
        usuario_login = 'Beto'
        senha_login = 'admin'
        usuario = values['Usuário']
        senha = values ['Senha']
        if senha == senha_login and usuario == usuario_login:
            window['messagem'].update('Login bem sucedido')
        else:
            window['messagem'].update('Login mal sucedido, senha ou usuário incorreto')

