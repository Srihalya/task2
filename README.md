# task2
📘 Task 2: Conversational Knowledge Bot using LangChain
📌 Overview

This task implements a Conversational Knowledge Bot using LangChain that can:

Interact with users in natural language

Maintain conversation memory

Provide context-aware responses

Continue a conversation until the user exits

The goal is to demonstrate memory-based conversational AI using LangChain.

🎯 Objective

To build a chatbot that:

Remembers previous user messages

Uses LangChain’s conversation chain

Demonstrates persistent conversational context

🛠 Technologies Used

Python 3.10 / 3.11

LangChain

OpenAI API

python-dotenv (for environment variables)

📂 Project Structure
Assignment1/
│
├── kodnest/
│   └── conversational_bot.py
│
├── requirements.txt
├── .env
└── README.md

⚙️ Setup Instructions
1️⃣ Create and Activate Virtual Environment
python -m venv venv
venv\Scripts\activate

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Configure OpenAI API Key

Create a .env file in the root directory and add:

OPENAI_API_KEY=your_openai_api_key_here

▶️ How to Run Task 2
python kodnest/conversational_bot.py

💬 Example Interaction
You: My name is Sweety
Bot: Nice to meet you, Sweety!

You: What is my name?
Bot: Your name is Sweety.


This demonstrates that the bot remembers previous conversation context.

🧠 Key Concepts Demonstrated

ConversationChain

ConversationBufferMemory

Memory-based conversational AI

Context retention across messages

📄 requirements.txt
langchain==0.1.20
langchain-openai
python-dotenv

✅ Conclusion

This task successfully demonstrates a conversational knowledge bot using LangChain with memory support. The bot can maintain context across interactions, fulfilling the requirements of Task 2.
