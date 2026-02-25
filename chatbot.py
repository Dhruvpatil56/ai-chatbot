import os
from groq import Groq
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# System prompt — gives the bot a role/personality
system_prompt = {
    "role": "system",
    "content": "You are a helpful AI assistant. You are smart, concise, and friendly."
}

# Conversation history — this is what makes it remember context
conversation_history = [system_prompt]

def chat(user_message):
    # Add user message to history
    conversation_history.append({
        "role": "user",
        "content": user_message
    })

    # Send full conversation to Groq
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=conversation_history,
        temperature=0.7,
        max_tokens=1024
    )

    # Extract reply
    assistant_message = response.choices[0].message.content

    # Add assistant reply to history so it remembers
    conversation_history.append({
        "role": "assistant",
        "content": assistant_message
    })

    return assistant_message

def main():
    print("="*50)
    print("        AI Chatbot powered by Groq")
    print("="*50)
    print("Type your message and press Enter to chat.")
    print("Type 'exit' or press Ctrl+C to quit.\n")

    while True:
        try:
            user_input = input("You: ").strip()

            # Skip empty inputs
            if not user_input:
                continue

            # Exit condition
            if user_input.lower() in ["exit", "quit", "bye"]:
                print("Bot: Goodbye! Have a great day!")
                break

            # Get response
            response = chat(user_input)
            print(f"\nBot: {response}\n")

        except KeyboardInterrupt:
            print("\n\nBot: Goodbye! Have a great day!")
            break
        except Exception as e:
            print(f"\nError: {e}\n")

if __name__ == "__main__":
    main()
