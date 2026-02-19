import streamlit as st
from typing import List, Dict
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Streamlit Page Config
st.set_page_config(page_title="Chatbot1", page_icon="🤖")
st.title("🤖 Chatbot1")
st.markdown("Powered by LangGraph and OpenRouter (GPT-3.5 Turbo)")

# Configure OpenRouter
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Add a sidebar for API key if not found in env
if not OPENROUTER_API_KEY:
    with st.sidebar:
        OPENROUTER_API_KEY = st.text_input("OpenRouter API Key", type="password")
        st.info("Get your key at [openrouter.ai](https://openrouter.ai/keys)")

if not OPENROUTER_API_KEY:
    st.warning("Please provide an OpenRouter API key to continue.")
    st.stop()

# Initialize the LLM via OpenRouter
llm = ChatOpenAI(
    model="openai/gpt-3.5-turbo",
    openai_api_key=OPENROUTER_API_KEY,
    openai_api_base="https://openrouter.ai/api/v1",
    default_headers={
        "HTTP-Referer": "https://github.com/Thollarkings/chatbot1", # Optional, for OpenRouter rankings
        "X-Title": "Chatbot1", # Optional
    }
)

# Step 1: Define State
class State(Dict):
    messages: List[Dict[str, str]] 

# Step 2: Initialize StateGraph
graph_builder = StateGraph(State)

# Define chatbot function
def chatbot(state: State):
    # Convert state messages to LangChain format for the model
    lc_messages = []
    for m in state["messages"]:
        if m["role"] == "user":
            lc_messages.append(HumanMessage(content=m["content"]))
        else:
            lc_messages.append(AIMessage(content=m["content"]))
    
    response = llm.invoke(lc_messages)
    state["messages"].append({"role": "assistant", "content": response.content})
    return {"messages": state["messages"]}

# Add nodes and edges
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

# Compile the graph
graph = graph_builder.compile()

# Initialize session state for messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if user_input := st.chat_input("Say something..."):
    # Add user message to session state
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Run the graph
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            initial_state = {"messages": st.session_state.messages}
            # We only care about the last message from the final state
            final_state = graph.invoke(initial_state)
            assistant_response = final_state["messages"][-1]["content"]
            st.markdown(assistant_response)
            
    # Update session state with the assistant's response
    st.session_state.messages.append({"role": "assistant", "content": assistant_response})
