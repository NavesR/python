import PySimpleGUI as sg 

# Criar as janelas e estilos(layout)
def janela_login():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Nome')],
        [sg.Input()],
        [sg.Button('Continuar')]
    ]
    return sg.Window('Login', layout=layout, finalize=True)
def janela_pedido():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Fazer Pedido')],
        [sg.Checkbox('Pizza', key='pizza'), sg.Checkbox('Hamburguer', key='hamburguer')],
        [sg.Button('Voltar'), sg.Button('Fazer Pedido')]
        
    ]
    return sg.Window('Montar Pedido', layout=layout, finalize=True)
# Criar as janelas iniciais
janela1, janela2 = janela_login(), None
# Criar um loop de leitura de eventos
while True:
    window, event, values = sg.read_all_windows()
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    if window == janela1 and event == 'Continuar':
        janela2 = janela_pedido()
        janela1.hide()
    if window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()
    if window == janela2 and event == 'Fazer Pedido':
        if values['pizza'] == True and values['hamburguer'] == True:
            sg.popup('Foram solicitados uma Pizza e um Hamburguer.')
        elif values['pizza'] == True:
            sg.popup('Foram solicitados uma Pizza.')
        elif values['hamburguer'] == True:
            sg.popup('Foram solicitados um Hamburguer.')
        else:
            sg.popup('Nao foi solicitado nada.')
# Lógica de o que deve acontecer ao clicar os botoes


# pyinstaller --onefile
# pyinstaller --onefile --noconsole ./IFome.py