# src/agent.py
from .knowledge_base import KnowledgeBase
import re

class Agent:
    def __init__(self):
        self.knowledge_base = KnowledgeBase()
        self.conversation_history = []

    def add_knowledge(self, text):
        """Add knowledge to the agent"""
        self.knowledge_base.add_text(text)

    def process_query(self, query):
        """Process a query and generate response"""
        # Add query to conversation history
        self.conversation_history.append(("user", query))
        
        # Get relevant context
        relevant_context = self.knowledge_base.get_relevant_context(query)
        
        # Generate response based on context
        response = self._generate_response(query, relevant_context)
        
        # Add response to conversation history
        self.conversation_history.append(("agent", response))
        
        return response

    def _generate_response(self, query, context):
        """Generate response based on query and context"""
        if not context:
            return "I don't have enough information to answer that question."
        
        # Simple response generation based on context
        if "what" in query.lower():
            return " ".join(context)
        elif "how" in query.lower():
            return " ".join(context)
        elif "who" in query.lower():
            for sentence in context:
                if "by" in sentence or "created" in sentence:
                    return sentence
            return context[0]
        else:
            return context[0]

    def get_conversation_history(self):
        """Get conversation history"""
        return self.conversation_history