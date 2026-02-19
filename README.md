# Chatbot1 🤖

A web-based chatbot implementation using **Streamlit**, **LangGraph**, and **OpenRouter**. This project demonstrates a robust state-managed chat interface powered by GPT-3.5 Turbo.

## 🌟 Features

- **Web UI**: Built with `Streamlit` for a clean, interactive chat experience.
- **State-Managed Conversations**: Uses `LangGraph` to manage chat history and state transitions efficiently.
- **Cloud-Ready LLM**: Integrated with `OpenRouter` to access GPT-3.5 Turbo, making it easy to deploy without local model requirements.
- **Easy Deployment**: Ready to be hosted on Streamlit Cloud or other web platforms.

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- An [OpenRouter API Key](https://openrouter.ai/keys).

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Thollarkings/chatbot1.git
   cd chatbot1
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Chatbot

1. Create a `.env` file in the root directory and add your API key:
   ```text
   OPENROUTER_API_KEY=your_key_here
   ```
   *(Alternatively, you can enter the key in the sidebar when the app runs.)*

2. Start the Streamlit app:
```bash
streamlit run 1.py
```

## 🛠️ How It Works

The chatbot uses a `StateGraph` to define the flow of messages:
1. **User Input**: Captured via the Streamlit chat input.
2. **State Update**: Input is added to the session state and message history.
3. **LLM Node**: The graph invokes the OpenRouter API with the current message history.
4. **Response**: The assistant's reply is displayed in the UI and saved to the session state.

## 📝 License

Distributed under the MIT License.
