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
def main():
    window = create_calc_window()
    current_expression = ""
    while True:
        event, values = window.read()
        if event == FSGUI.WIN_CLOSED:
            break
        elif event == "C":
            current_expression = ""
        elif event == "=":
            current_expression = calculate_result(current_expression)
        else:
            current_expression += event
        window["-DISPLAY-"].update(current_expression)
    window.close()
if __name__ == "__main__":    main()    



