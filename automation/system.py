import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def shutdown():
    print("⚠️ MCP: Are you sure you want to shut down? (yes/no)")
    choice = input("Confirm: ").lower()
    if choice == "yes":
        os.system("shutdown /s /t 1")
        return "🛑 MCP: Shutting down the system."
    return "❌ MCP: Shutdown cancelled."

def set_reminder():
    sender = os.getenv("MCP_EMAIL_SENDER")
    password = os.getenv("MCP_EMAIL_PASSWORD")
    receiver = sender  # send reminder to yourself

    print("📅 MCP: What should I remind you about?")
    body = input("Reminder text: ")

    print("🕐 MCP: When should I remind you? (Just for the record, not timed)")
    time_info = input("Enter time/date info: ")

    subject = f"⏰ Reminder: {time_info}"

    # Compose the email
    msg = EmailMessage()
    msg.set_content(f"Hey, here's your reminder:\n\n{body}\n\n-- MCP Assistant")
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)
        server.send_message(msg)
        server.quit()
        return "✅ MCP: Reminder sent to your email."
    except Exception as e:
        return f"❌ MCP: Failed to send reminder: {e}"
