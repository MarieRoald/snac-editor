import sys
modules = sys.modules  # Store this so we can reset the imported modules

import js
from js import document
from functools import wraps


# The builtin Pyodide input method is a bit weird, so we overwrite it with this to make it a bit easier to understand
@wraps(input)
def input(prompt):
    out = js.window.prompt(prompt)
    print(f"{prompt}{out}")
    return out


def get_code():
    """Extract the content from the codemirror editor.
    """
    return js.editor.getValue()


def clear():
    """Clear the PyScript terminal.
    """
    terminals = document.getElementsByClassName("py-terminal")
    if terminals:
        terminals[0].textContent = ""

    for error in document.getElementsByClassName("py-error"):
        error.remove()


def run_code():
    """Reset the terminal and run the code from the editor in an empty scope.
    """
    import sys
    sys.modules = modules  # Reset imported modules

    code = get_code()    
    clear()

    # We put the code in a try-except block so the traceback is printed in the terminal
    try:
        exec(code, {"input": input})
    except Exception as e:
        import traceback
        for tb_line in traceback.format_exception(e):
            print(tb_line, end="")
