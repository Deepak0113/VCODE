from subprocess import check_call

def open_vscode():
    check_call("code .", shell=True)

def run_python_file(filename:str):
    check_call(f"python {filename}.py", shell=True)