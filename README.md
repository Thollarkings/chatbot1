# Chatbot1 🤖

A streamlined chatbot implementation using **LangGraph** and **Ollama**. This project demonstrates a robust state-managed chat interface powered by local large language models.

## 🌟 Features

- **State-Managed Conversations**: Uses `LangGraph` to manage chat history and state transitions efficiently.
- **Local AI Power**: Integrated with `Ollama` for running models like `llama3.2` locally, ensuring privacy and speed.
- **Interactive CLI**: Easy-to-use command-line interface for real-time interaction.
- **Extensible Architecture**: Built with a modular graph-based design, making it easy to add more complex logic or tools.

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- [Ollama](https://ollama.com/) installed and running.
- The `llama3.2` model pulled:
  ```bash
  ollama pull llama3.2
  ```

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Thollarkings/chatbot1.git
   cd chatbot1
   ```

2. Install dependencies:
   ```bash
   pip install langgraph langchain_ollama
   ```

### Running the Chatbot

Start the interactive session:
```bash
python 1.py
```

## 🛠️ How It Works

The chatbot uses a `StateGraph` to define the flow of messages:
1. **User Input**: Captured via the CLI.
2. **State Update**: Input is added to the message history.
3. **LLM Node**: The graph invokes the Ollama LLM with the current message history.
4. **Response**: The assistant's reply is appended to the state and streamed back to the user.

## 📝 License

Distributed under the MIT License.
