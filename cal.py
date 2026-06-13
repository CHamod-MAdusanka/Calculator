import FreeSimpleGUI as FSGUI
def calculate_result(expression):
    try:
        return str(eval(expression))
    except:
        return "Error"
def create_calc_window():
    layout=[
    [FSGUI.InputText(key="-DISPLAY-", size=(20, 1), justification='right')],
    [FSGUI.Button("7"), FSGUI.Button("8"), FSGUI.Button("9"), FSGUI.Button("/")],
    [FSGUI.Button("4"), FSGUI.Button("5"), FSGUI.Button("6"), FSGUI.Button("*")],
    [FSGUI.Button("1"), FSGUI.Button("2"), FSGUI.Button("3"), FSGUI.Button("-")],
    [FSGUI.Button("0"), FSGUI.Button("C"), FSGUI.Button("="), FSGUI.Button("+")]
    ]
    return FSGUI.Window("Simple Calculator", layout)
