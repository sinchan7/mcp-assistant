import webbrowser
import urllib.parse

def search_web(command):
    # Remove trigger words
    for trigger in ["search", "google", "look up"]:
        if trigger in command:
            command = command.replace(trigger, "")
    
    query = command.strip()

    if not query:
        return "❌ MCP: What should I search for?"

    url = f"https://www.google.com/search?q={urllib.parse.quote(query)}"
    webbrowser.open(url)
    return f"🌐 MCP: Searching for '{query}' on Google..."
