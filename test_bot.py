"""Test the conversational bot"""
from bot.conversational_bot import ConversationalKnowledgeBot

def test_basic_conversation():
    """Test basic conversation flow"""
    print("Testing Basic Conversation...")
    bot = ConversationalKnowledgeBot()
    
    test_cases = [
        "Hello, how are you?",
        "What's 15 * 3 + 8?",
        "What's the current time?",
        "Can you search for latest AI news?",
        "What did we talk about earlier?"
    ]
    
    for query in test_cases:
        print(f"\n👤 User: {query}")
        response = bot.process_query(query)
        print(f"🤖 Bot: {response}")
        print("-" * 50)

def test_memory():
    """Test memory functionality"""
    print("\n\nTesting Memory...")
    bot = ConversationalKnowledgeBot()
    
    # First conversation
    print("👤 User: My name is John and I like programming")
    response1 = bot.process_query("My name is John and I like programming")
    print(f"🤖 Bot: {response1}")
    
    # Later, ask about name
    print("\n👤 User: What's my name?")
    response2 = bot.process_query("What's my name?")
    print(f"🤖 Bot: {response2}")

def test_tools():
    """Test tool usage"""
    print("\n\nTesting Tools...")
    bot = ConversationalKnowledgeBot()
    
    # Test calculator
    print("👤 User: Calculate 2 to the power of 10")
    response = bot.process_query("Calculate 2 to the power of 10")
    print(f"🤖 Bot: {response}")
    
    # Test time
    print("\n👤 User: What time is it?")
    response = bot.process_query("What time is it?")
    print(f"🤖 Bot: {response}")

if __name__ == "__main__":
    print("🧪 Testing Conversational Knowledge Bot")
    print("=" * 50)
    
    test_basic_conversation()
    test_memory()
    test_tools()
    
    print("\n✅ All tests completed!")