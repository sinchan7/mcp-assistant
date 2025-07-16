from automation import apps, browser, whatsapp, emailer, system
from tools import summarizer, brainstorm, file_writer
def decide_task(command):
    command = command.lower()

    if "open" in command:
        return apps.open_app(command)

    elif "search" in command:
        return browser.search_web(command)

    elif any(x in command for x in ["send whatsapp", "whatsapp message", "send message"]):
        return whatsapp.send_message(command)

    elif any(x in command for x in ["send email", "email"]):
        return emailer.send_email(command)

    elif any(x in command for x in ["shutdown", "shut down", "exit program", "terminate"]):
        return system.shutdown()

    elif "summarize" in command:
        return summarizer.summarize(command)

    elif "brainstorm" in command:
        return brainstorm.generate_ideas(command)

    elif "write" in command:
        return file_writer.write_to_file(command)
    
    elif "remind me" in command or "set reminder" in command:
        return system.set_reminder()

    

    return "❌ MCP: No known task matched your command."
