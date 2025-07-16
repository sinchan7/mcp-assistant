import pywhatkit as kit
import pyautogui
import time

# Decorate message to sound casual
def decorate_message(message):
    templates = [
        f"Yo! {message.capitalize()} 🌞 How was your sleep?",
        f"Hey hey! Just wanted to say: {message.capitalize()} 😎",
        f"Sup! {message.capitalize()} 🤙 Hope you're feeling awesome today.",
        f"Heads up! {message.capitalize()} 🚀 Let’s conquer the day!",
    ]
    return templates[hash(message) % len(templates)]


def send_message(command):
    print("📲 MCP: Who should I send the WhatsApp message to?")
    phone = input("Enter phone number with country code (e.g., +919812345678): ").strip()

    print("📲 MCP: What message do you want to send?")
    message = input("Enter message: ").strip()

    # Decorate the message
    decorated = decorate_message(message)

    try:
        print("📲 MCP: Launching WhatsApp Web...")
        kit.sendwhatmsg_instantly(phone_no=phone, message=decorated, wait_time=15, tab_close=True)
        time.sleep(8)
        pyautogui.press("enter")
        return f"✅ MCP: Message sent to {phone}: {decorated}"
    except Exception as e:
        return f"❌ MCP: Failed to send message: {e}"
