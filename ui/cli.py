from core.brain import process_command

def main():
    print("🧠 MCP Assistant CLI is ready. Type your commands below.")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("🗣️ You: ").strip()

        if user_input.lower() in ["exit", "quit"]:
            print("👋 MCP: Shutting down CLI.")
            break

        response = process_command(user_input)
        print(f"🤖 MCP: {response}\n")


if __name__ == "__main__":
    main()
