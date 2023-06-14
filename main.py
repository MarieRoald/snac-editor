import sys
__modules = sys.modules  # Store this so we can reset the imported modules

from js import document
from functools import wraps


# The builtin Pyodide input method is a bit weird, so we overwrite it with this to make it a bit easier to understand
@wraps(input)
def input(prompt):
    import js
    out = js.window.prompt(prompt)
    print(f"{prompt}{out}")
    return out


# Two leading underscores to be sure that these are unlikely to be used in the executed code
def __get_code():
    """Extract the content from the codemirror editor.
    """
    import js
    return js.editor.getValue()


def __clear():
    """Clear the PyScript terminal.
    """
    from js import document
    terminals = document.getElementsByClassName("py-terminal")
    if terminals:
        terminals[0].textContent = ""

    for error in document.getElementsByClassName("py-error"):
        error.remove()

del document, wraps, sys  # So these modules are not loaded when the code is run


def run_code():
    """Reset the terminal and run the code from the editor in an empty scope.
    """
    import sys
    sys.modules = __modules  # Reset imported modules
    del sys
    
    code = __get_code()    
    __clear()

    # We put the code in a try-except block so the traceback is printed in the terminal
    try:
        exec(code)
    except Exception as e:
        import traceback
        for tb_line in traceback.format_exception(e):
            print(tb_line, end="")