import subprocess

def open_app(command):
    if "chrome" in command:
        subprocess.Popen("start chrome", shell=True)
        return "Opening Chrome..."
    elif "notepad" in command:
        subprocess.Popen("notepad.exe")
        return "Opening Notepad..."
    return "App not recognized."
