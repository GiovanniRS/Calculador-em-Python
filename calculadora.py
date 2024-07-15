import PySimpleGUI as sg

def soma(n1, n2):
    return n1 + n2

def subtracao(n1, n2):
    return n1 - n2

def multiplicacao(n1, n2):
    return n1 * n2

def divisao(n1, n2):
    return n1 / n2

sg.theme('Reddit')

layout = [
    [sg.Text('', font=('Helvetica', 8), key='conta')],
    [sg.Text('0', font=('Helvetica', 20), key='digitando')],
    [sg.Button('', size=(12,2), disabled=True), sg.Button('', size=(12,2), disabled=True), sg.Button('=', size=(12,2)),sg.Button('Limpar', size=(12,2))],
    [sg.Button('7', size=(12,2)),sg.Button('8', size=(12,2)),sg.Button('9', size=(12,2)), sg.Button('/', size=(12,2))],
    [sg.Button('4', size=(12,2)),sg.Button('5', size=(12,2)),sg.Button('6', size=(12,2)), sg.Button('-', size=(12,2))],
    [sg.Button('1', size=(12,2)),sg.Button('2', size=(12,2)),sg.Button('3', size=(12,2)), sg.Button('+', size=(12,2))],
    [sg.Button('', size=(12,2), disabled=True),sg.Button('0', size=(12,2)),sg.Button(',', size=(12,2)), sg.Button('X', size=(12,2))],
]

window = sg.Window('Calculadora', layout)

primeiro_numero = ''
operador = ''
segundo_numero = ''
resultado = ''
while True:
    evento, valor = window.read()

    if evento == sg.WIN_CLOSED:
        break

    if evento == 'Limpar':
        window['conta'].update('')
        window['digitando'].update('0')
        primeiro_numero = ''
        operador = ''
        segundo_numero = ''
        resultado = ''

    elif evento not in ('+', '-', 'X', '/', '=') and operador == '':
        primeiro_numero += evento
        window['digitando'].update(primeiro_numero)

    elif evento in ('+', '-', 'X', '/') and segundo_numero == '':
        window['conta'].update(primeiro_numero)
        operador = evento
        window['digitando'].update(operador)

    elif evento not in ('+', '-', 'X', '/', '='):
        window['conta'].update(primeiro_numero+operador)
        segundo_numero += evento
        window['digitando'].update(segundo_numero)
    
    elif evento == '=':
        window['conta'].update(primeiro_numero+operador+segundo_numero+'=')
        primeiro_numero = float(primeiro_numero)
        segundo_numero = float(segundo_numero)
        if operador == "+":
            resultado = soma(primeiro_numero, segundo_numero)
        if operador == "-":
            resultado = subtracao(primeiro_numero, segundo_numero)
        if operador == "X":
            resultado = multiplicacao(primeiro_numero, segundo_numero)
        if operador == "/":
            resultado = divisao(primeiro_numero, segundo_numero)
        window['digitando'].update(resultado)

    print(f'O primeiro numero é: {primeiro_numero}')
    print(f'O operador numero é: {operador}')
    print(f'O segundo numero é: {segundo_numero}')
    print(resultado)