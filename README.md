# Adapti-Persona-Agent 🧠✨

![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/your-username/adapti-persona-agent/main.yml?branch=main) ![License](https://img.shields.io/github/license/your-username/adapti-persona-agent) ![Contributors](https://img.shields.io/github/contributors/your-username/adapti-persona-agent)

Welcome to **Adapti-Persona-Agent**! Your ultimate intelligent assistant that doesn't just answer questions, but *understands your intent*, *adopts the perfect persona*, and *proactively helps you achieve your goals*.

In a world flooded with generic AI, Adapti-Persona-Agent stands out by dynamically shifting its expertise, tone, and available tools based on the nuanced context of your conversation and objectives. Need a software architect to brainstorm system designs? A marketing strategist for campaign ideas? A financial advisor for investment insights? This agent has you covered, adapting on the fly.

## ✨ Features

-   **Dynamic Persona Generation**: Automatically discerns the optimal persona (e.g., Software Architect, Marketing Strategist, Data Scientist) for your query and task, or even generates a new one based on specific needs.
-   **Contextual Tool-Use Orchestration**: Integrates and intelligently leverages a wide array of external tools and APIs (web search, calculators, code interpreters, custom services) relevant to the active persona and goal.
-   **Adaptive Memory & Context**: Utilizes both short-term conversational memory and long-term knowledge retrieval (RAG) to maintain coherence, learn from past interactions, and retrieve relevant information.
-   **Proactive Insights & Suggestions**: Doesn't wait for explicit commands. The agent offers next steps, identifies potential issues, and suggests optimal paths forward to accelerate your workflow.
-   **Modular Architecture**: Easily extendable framework to add new tools, refine persona definitions, integrate different LLMs, and customize memory components.
-   **Goal-Oriented Planning**: Breaks down complex user objectives into manageable sub-tasks, leveraging its personas and tools to systematically work towards completion.

## 🚀 Installation

To get Adapti-Persona-Agent up and running, follow these simple steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/adapti-persona-agent.git
    cd adapti-persona-agent
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up Environment Variables:**
    Create a `.env` file in the root directory and add your API keys:
    ```
    OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
    # Add other API keys for tools like SERPER_API_KEY etc. if you enable them
    ```

## 💡 Usage

To interact with the Adapti-Persona-Agent, you can run the `main.py` script:

```bash
python main.py
```

The agent will start a conversational loop. Type your queries, and observe how it adapts!

**Example Interactions:**

```
User: I need to design a scalable microservices architecture for an e-commerce platform. What are the key considerations?
Agent: (Activates 'Software Architect' persona) Alright, let's break this down. For a scalable e-commerce microservices architecture, we'll need to consider...

User: Can you help me brainstorm some catchy social media campaign ideas for a new eco-friendly skincare line?
Agent: (Activates 'Marketing Strategist' persona) Absolutely! For an eco-friendly skincare line, we could explore themes like 'Glow Green', 'Pure Planet Beauty', or 'Sustainable Radiance'. Let's dive deeper...

User: What's the current stock price of NVIDIA and how has it performed this week?
Agent: (Activates 'Financial Analyst' persona and uses a stock tool) Checking for NVIDIA's stock performance... [Tool Output] NVIDIA (NVDA) is currently at $X.XX, and has seen a Y% change this week. 
```

## 🏗️ Architecture

The Adapti-Persona-Agent is built on a modular, agentic architecture to ensure flexibility and scalability.

```mermaid
graph TD
    A[User Input] --> B{AdaptiPersonaAgent.run()}
    B --> C[Memory Manager]
    C -- Context & History --> D[Persona Manager]
    D -- Suggested Persona & Goal --> E[LLM Core (Agent Executor)]
    E -- Thought, Action, Observation --> F[Tool Orchestrator]
    F -- Tool Call --> G[External Tools / APIs]
    G -- Tool Result --> E
    E -- Final Response --> H[User Output]
    H --> B
    C -- Long-term Memory (Vector Store) --> I[Knowledge Base]
    I -- Retrieval --> E
```

**Key Components:**

1.  **LLM Core (Agent Executor)**: The brain of the operation, powered by a large language model (e.g., GPT-4o). It interprets user input, plans actions, decides which tools to use, and generates responses based on the active persona and available context.
2.  **Persona Manager**: Responsible for analyzing user intent, current context, and historical interactions to dynamically select or generate the most appropriate 'persona' for the task at hand. This involves prompt engineering to guide the LLM into specific roles.
3.  **Tool Orchestrator**: Manages a registry of available tools (web search, calculators, custom APIs). It interfaces with the LLM Core to select and execute the right tools at the right time, parsing their outputs.
4.  **Memory Manager**: Handles both short-term conversational history and long-term memory. Short-term memory keeps track of recent turns, while long-term memory (backed by a vector store like ChromaDB) stores past insights, user preferences, and knowledge snippets for RAG.
5.  **External Tools / APIs**: A collection of external services and functions that the agent can invoke to gather information or perform actions (e.g., Google Search, external databases, calculation engines).

## 🤝 Contributing

We welcome contributions from the community! Whether it's adding new tools, refining persona definitions, improving the core agent logic, or enhancing documentation, your help is appreciated.

Please refer to our [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---