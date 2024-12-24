# src/agent.py
from .knowledge_base import KnowledgeBase
import re

class Agent:
    def __init__(self):
        self.knowledge_base = KnowledgeBase()
        self.conversation_history = []
        self.similarity_threshold = 0.3

    def add_text(self, text):
        """Add text to the knowledge base"""
        self.knowledge_base.add_text(text)

    def process_query(self, query):
        """Process a query and generate response"""
        # Preprocess query
        is_valid, processed_query = self._preprocess_query(query)
        if not is_valid:
            response = processed_query
            self.conversation_history.append(("user", query))
            self.conversation_history.append(("agent", response))
            return response
            
        # Add query to conversation history
        self.conversation_history.append(("user", query))
        
        # Get relevant context
        relevant_context = self.knowledge_base.get_relevant_context(query)
        
        # Generate response based on context
        response = self._generate_response(query, relevant_context)
        
        # Add response to conversation history
        self.conversation_history.append(("agent", response))
        
        return response

    def _preprocess_query(self, query):
        """Preprocess the query to determine if it's answerable"""
        query = query.lower()
        
        # List of topics we can answer about
        known_topics = ['python', 'programming', 'code', 'developer', 'syntax']
        
        # Check if query contains any known topics
        contains_known_topic = any(topic in query for topic in known_topics)
        
        if not contains_known_topic:
            return False, "I can only answer questions about Python programming language."
        
        return True, query

    def _generate_response(self, query, context):
        """Generate response based on query and context"""
        if not context:
            return "I apologize, but I don't have any relevant information about that topic in my knowledge base. I can only answer questions about Python programming language based on my current knowledge."
        
        # Extract key terms from query
        query_terms = set(query.lower().split())
        relevant_terms = {'python', 'programming', 'language', 'code', 'syntax', 
                         'developer', 'development', 'library', 'package'}
        
        # Check if query is relevant to our knowledge domain
        if not any(term in query_terms for term in relevant_terms):
            return "I apologize, but I can only answer questions about Python programming language based on my current knowledge."
        
        # Your existing response generation logic
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