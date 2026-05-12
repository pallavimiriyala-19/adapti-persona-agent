import os
import json
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.tools import tool
from langchain.memory import ConversationBufferWindowMemory

# Load environment variables
load_dotenv()

# --- 1. Define Tools ---
@tool
def search_web(query: str) -> str:
    """Searches the web for information using a hypothetical search engine."""
    # In a real scenario, this would integrate with a search API like Serper, Google Search, etc.
    # For demonstration, we'll return a mock result.
    print(f"[Tool Call: Searching web for '{query}']")
    mock_results = {
        "scalable microservices": "Key considerations: loose coupling, stateless services, API gateway, containerization (Docker, Kubernetes), message queues, distributed tracing, robust monitoring.",
        "eco-friendly skincare campaign ideas": "'Glow Green' (sustainability focus), 'Pure Planet Beauty' (natural ingredients), 'Sustainable Radiance' (long-term benefits, eco-packaging). Highlight cruelty-free, vegan, organic aspects.",
        "NVIDIA stock performance": "NVIDIA (NVDA) stock price: $925.30. Weekly performance: +3.5%. Market cap: $2.3T.",
        "latest AI trends 2026": "Multi-modal LLMs, embodied AI, personalized adaptive agents, explainable AI, secure federated learning, quantum-AI hybrid solutions."
    }
    for keyword, result in mock_results.items():
        if keyword in query.lower():
            return result
    return f"No specific search result found for '{query}'."

@tool
def calculate(expression: str) -> str:
    """Evaluates a mathematical expression."""
    print(f"[Tool Call: Calculating '{expression}']")
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error evaluating expression: {e}"

@tool
def get_current_date() -> str:
    """Returns the current date in YYYY-MM-DD format."""
    from datetime import date
    print(f"[Tool Call: Getting current date]")
    return date.today().strftime("%Y-%m-%d")

# List of all available tools
available_tools = [search_web, calculate, get_current_date]

# --- 2. Persona Definitions (Implicit via Prompt Templates) ---
# The persona is primarily guided by the system message and user input interpretation.
# We'll use a dynamic system message that the agent can update or infer.

# --- 3. AdaptiPersonaAgent Class ---
class AdaptiPersonaAgent:
    def __init__(self, llm_model: str = "gpt-4o", temperature: float = 0.7, memory_k: int = 5):
        if not os.getenv("OPENAI_API_KEY"):
            raise ValueError("OPENAI_API_KEY environment variable not set.")

        self.llm = ChatOpenAI(model=llm_model, temperature=temperature)
        self.memory = ConversationBufferWindowMemory(memory_key="chat_history", return_messages=True, k=memory_k)

        self.system_message = (
            "You are Adapti-Persona-Agent, a highly intelligent and adaptive AI assistant. "
            "Your core function is to infer the user's implicit persona needs and current goal, "
            "then adopt the most suitable expert persona (e.g., Software Architect, Marketing Strategist, Financial Analyst) "
            "to provide proactive, accurate, and insightful assistance. "
            "You have access to a suite of tools to help you. Always strive to understand the user's true intent and provide the most helpful response, even if it requires clarifying questions or suggesting next steps. "
            "Maintain context from our conversation and reference past interactions when relevant. "
            "Begin by stating which persona you are adopting or creating, and why, based on the user's request."
        )

        self.prompt = ChatPromptTemplate.from_messages(
            [
                ("system", self.system_message),
                MessagesPlaceholder(variable_name="chat_history"),
                ("human", "{input}"),
                MessagesPlaceholder(variable_name="agent_scratchpad"),
            ]
        )

        self.agent = create_openai_tools_agent(self.llm, available_tools, self.prompt)
        self.agent_executor = AgentExecutor(agent=self.agent, tools=available_tools, verbose=True, memory=self.memory)

    def run(self, user_input: str) -> str:
        print(f"\n--- User Input: {user_input} ---")
        try:
            response = self.agent_executor.invoke({"input": user_input, "chat_history": self.memory.load_memory_variables({})["chat_history"]})
            return response["output"]
        except Exception as e:
            return f"An error occurred: {e}"

# --- 4. Example Usage ---
if __name__ == "__main__":
    print("Initializing Adapti-Persona-Agent... (This may take a moment)")
    agent = AdaptiPersonaAgent()
    print("Agent ready! Type 'exit' to quit.")

    while True:
        user_query = input("\nYour turn: ")
        if user_query.lower() == 'exit':
            print("Exiting Adapti-Persona-Agent. Goodbye!")
            break

        agent_response = agent.run(user_query)
        print(f"\n--- Adapti-Persona-Agent: ---\n{agent_response}")

        # Optional: Save chat history (already handled by memory object, but could be persisted externally)
        # print("\n--- Current Chat History (last k messages): ---")
        # for msg in agent.memory.load_memory_variables({})["chat_history"]:
        #     print(f"{msg.type.capitalize()}: {msg.content}")

