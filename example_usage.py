import os
from dotenv import load_dotenv
from main import AdaptiPersonaAgent

# Ensure .env is loaded if running this example separately
load_dotenv()

def run_adapti_persona_agent_demo():
    print("\n--- Adapti-Persona-Agent Demo ---")
    print("This demo showcases the agent's ability to adapt its persona and use tools based on your input.")
    print("Type 'exit' or 'quit' to end the session.\n")

    try:
        # Initialize the agent. Make sure OPENAI_API_KEY is set in your .env file
        agent = AdaptiPersonaAgent()
        print("Agent initialized and ready to assist!\n")

        while True:
            user_input = input("Your turn (or 'exit'): ")
            if user_input.lower() in ['exit', 'quit']:
                print("Exiting demo. Goodbye!")
                break

            if not user_input.strip():
                print("Please provide some input.")
                continue

            # Run the agent with the user's input
            agent_response = agent.run(user_input)

            print(f"\n--- Adapti-Persona-Agent: ---\n{agent_response}\n")

    except ValueError as e:
        print(f"Configuration Error: {e}\nPlease ensure your .env file is correctly set up with OPENAI_API_KEY.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    run_adapti_persona_agent_demo()
