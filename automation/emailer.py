import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv, find_dotenv
from tools.brainstorm import generate_ideas
from tools.file_writer import format_email  # assume this generates a polished email

load_dotenv(find_dotenv())

YOUR_NAME = "Sinchan"  # ✅ Customize this

def send_email(command):
    sender = os.getenv("MCP_EMAIL_SENDER")
    password = os.getenv("MCP_EMAIL_PASSWORD")

    print("📧 MCP: Who should I send the email to?")
    receiver = input("Enter recipient email: ")

    print("👤 MCP: What is the recipient's name?")
    recipient_name = input("Enter recipient name: ")

    print("📧 MCP: What's the subject?")
    subject = input("Enter subject: ")

    # Extract body idea from command
    raw_idea = command.replace("send email", "").strip()
    if not raw_idea:
        print("🧠 MCP: What should the email be about?")
        raw_idea = input("Enter topic or idea: ")

    # Brainstorm ideas and format them
    idea_text = generate_ideas(raw_idea)
    body = format_email(subject, idea_text, recipient_name, YOUR_NAME)

    # Create the email
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)
        server.send_message(msg)
        server.quit()
        return "✅ MCP: Email sent successfully."
    except Exception as e:
        return f"❌ MCP: Failed to send email: {e}"
