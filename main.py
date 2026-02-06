"""Main CLI interface for the conversational bot"""
import os
import sys
from bot.conversational_bot import ConversationalKnowledgeBot
from dotenv import load_dotenv

def clear_screen():
    """Clear terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    """Print welcome banner"""
    banner = """
    ╔══════════════════════════════════════════════════╗
    ║      🤖 CONVERSATIONAL KNOWLEDGE BOT            ║
    ║      Tools + Memory + Knowledge Base            ║
    ╚══════════════════════════════════════════════════╝
    """
    print(banner)

def main():
    """Main function"""
    load_dotenv()
    
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Error: OPENAI_API_KEY not found in .env file")
        print("Please create a .env file with your OpenAI API key")
        return
    
    clear_screen()
    print_banner()
    
    # Initialize bot
    print("🔄 Initializing bot...")
    bot = ConversationalKnowledgeBot()
    
    print("\n" + "="*50)
    print("Available commands:")
    print("  /help    - Show this help message")
    print("  /history - Show conversation history")
    print("  /clear   - Clear conversation memory")
    print("  /add     - Add information to knowledge base")
    print("  /save    - Save conversation to file")
    print("  /exit    - Exit the program")
    print("="*50 + "\n")
    
    # Conversation loop
    while True:
        try:
            # Get user input
            user_input = input("\n👤 You: ").strip()
            
            # Handle commands
            if user_input.lower() == '/exit':
                print("👋 Goodbye!")
                break
            
            elif user_input.lower() == '/help':
                print("\nAvailable commands:")
                print("  /help    - Show help")
                print("  /history - Show conversation history")
                print("  /clear   - Clear memory")
                print("  /add     - Add to knowledge base")
                print("  /save    - Save conversation")
                print("  /exit    - Exit")
                continue
            
            elif user_input.lower() == '/history':
                history = bot.get_conversation_history()
                print("\n📜 Conversation History:")
                print(history if history else "No history yet")
                continue
            
            elif user_input.lower() == '/clear':
                result = bot.clear_memory()
                print(f"✅ {result}")
                continue
            
            elif user_input.lower() == '/save':
                bot.conversation_memory.save_to_file()
                print("✅ Conversation saved to 'conversation.json'")
                continue
            
            elif user_input.lower().startswith('/add'):
                # Extract text after /add
                if len(user_input) > 5:
                    text_to_add = user_input[5:].strip()
                    result = bot.add_to_knowledge_base(text_to_add)
                    print(f"✅ {result}")
                else:
                    print("Please provide text to add: /add [information]")
                continue
            
            # Process normal query
            print("\n🤖 Bot is thinking...")
            response = bot.process_query(user_input)
            
            print(f"\n🤖 Bot: {response}")
            
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error: {str(e)}")

if __name__ == "__main__":
    main()