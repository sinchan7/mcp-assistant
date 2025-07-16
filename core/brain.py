from core.agent import decide_task

def process_command(command):
    response = decide_task(command)
    return response or "Sorry, I couldn't understand that."
