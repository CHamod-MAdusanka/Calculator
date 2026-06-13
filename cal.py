import FreeSimpleGUI as FSGUI
def calculate_result(expression):
    try:
        return str(eval(expression))
    except:
        return "Error"
 
