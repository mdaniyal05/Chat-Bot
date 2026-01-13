import anthropic
import os


def main():
    client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

    print("Simple Claude Chatbot")
    print("Type 'quit' or 'exit' to end the conversation\n")

    messages = []

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in ['quit', 'exit']:
            print("Goodbye!")
            break

        if not user_input:
            continue

        messages.append({
            "role": "user",
            "content": user_input
        })

        try:
            response = client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=1000,
                messages=messages
            )

            assistant_message = response.content[0].text

            messages.append({
                "role": "assistant",
                "content": assistant_message
            })

            print(f"\nClaude: {assistant_message}\n")

        except Exception as e:
            print(f"\nError: {e}\n")
            messages.pop()


if __name__ == "__main__":
    main()
