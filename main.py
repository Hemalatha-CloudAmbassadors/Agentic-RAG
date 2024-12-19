# main.py
import os
from src.agent import Agent
from src.utils import ensure_nltk_downloads, load_text_file

def main():
    # Ensure NLTK data is downloaded
    ensure_nltk_downloads()
    
    # Initialize agent
    print("Initializing Agentic RAG system...")
    agent = Agent()
    
    # Load initial knowledge
    try:
        knowledge_text = load_text_file('data/knowledge.txt')
        agent.add_knowledge(knowledge_text)
    except FileNotFoundError:
        print("Warning: knowledge.txt not found. Starting with empty knowledge base.")
    
    print("\nAgentic RAG system ready! Ask questions (type 'exit' to quit)")
    print("Available commands:")
    print("- 'exit': Quit the program")
    print("- 'load <filename>': Load additional knowledge")
    print("- 'history': Show conversation history")
    
    while True:
        user_input = input("\nYour question: ").strip()
        
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        elif user_input.lower() == 'history':
            history = agent.get_conversation_history()
            print("\nConversation History:")
            for role, text in history:
                print(f"{role.capitalize()}: {text}")
            continue
        
        elif user_input.lower().startswith('load '):
            filename = user_input[5:].strip()
            try:
                new_knowledge = load_text_file(filename)
                agent.add_knowledge(new_knowledge)
                print(f"Successfully loaded knowledge from {filename}")
            except FileNotFoundError:
                print(f"Error: File '{filename}' not found.")
            continue
        
        if not user_input:
            print("Please enter a valid question!")
            continue
        
        print("\nProcessing...")
        response = agent.process_query(user_input)
        print(f"\nAnswer: {response}")

if __name__ == "__main__":
    main()