#!/usr/bin/env python3

import os
from datetime import datetime

# ANSI color codes
CYAN = "\033[96m"
RESET = "\033[0m"

def errors(x):
    error_messages = {
        1: "error: missing 1st argument",
        2: "error: you should provide the 1st argument"
    }
    print(error_messages.get(x, "Unknown error"))

def show_help():
    help_text = """\
    ml      : List directories
    og      : Change directory
    og ..   : Move back a directory
    ogzdr   : Create a folder
    rmogz   : Remove a folder
    vim     : Open file with vim
    python  : Run Python script
    """
    print(help_text)

def list_folder(path="."):
    try:
        with os.scandir(path) as entries:
            for entry in entries:
                print(entry.name)
    except FileNotFoundError:
        errors(1)

def make_folder(path):
    try:
        os.mkdir(path)
    except OSError:
        errors(2)

def remove_folder(path):
    try:
        os.rmdir(path)
    except OSError:
        errors(2)

def change_directory(path):
    try:
        os.chdir(path)
    except OSError:
        print("ERROR: Unable to change directory")

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def open_vim(path):
    os.system(f'vim {path}')

def run_python_script(path):
    if path.endswith('.py'):
        os.system(f'python {path}')
    else:
        print("error: not a Python file")

def run_command(command):
    os.system(command)

def get_current_time():
    now = datetime.now()
    return now.strftime("[%H:%M:%S,%d-%m-%Y] > ")

def main():
    while True:
        current_time = f"{CYAN}{get_current_time()}{RESET}"
        command_input = input(current_time).strip()

        if not command_input:
            continue

        command_parts = command_input.split()
        command = command_parts[0]
        args = command_parts[1:]

        if command == "exit":
            break
        elif command == "clear":
            clear_terminal()
        elif command == "og":
            if not args:
                print("og: missing argument")
            else:
                change_directory(args[0])
        elif command == "ml":
            list_folder(args[0] if args else ".")
        elif command == "ogzdr":
            if not args:
                errors(2)
            else:
                make_folder(args[0])
        elif command == "rmogz":
            if not args:
                errors(2)
            else:
                remove_folder(args[0])
        elif command == "vim":
            if not args:
                errors(1)
            else:
                open_vim(args[0])
        elif command == "python":
            if not args:
                errors(1)
            else:
                run_python_script(args[0])
        elif command == "help":
            show_help()
        elif command == "ls":
            if args:
                run_command(f"tren {args[0]}")
            else:
                run_command("tren")
        else:
            print(f"{command}: command not found, try 'help'")

if __name__ == "__main__":
    main()
