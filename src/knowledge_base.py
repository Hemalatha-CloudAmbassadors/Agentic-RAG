# src/knowledge_base.py
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from .utils import split_into_sentences

class KnowledgeBase:
    def __init__(self):
        print("Initializing knowledge base...")
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.sentences = []
        self.embeddings = None
        print("Knowledge base initialized!")

    def add_text(self, text):
        """Add text to knowledge base"""
        new_sentences = split_into_sentences(text)
        
        if not new_sentences:
            return
        
        # Create embeddings for new sentences
        new_embeddings = self.model.encode(new_sentences)
        
        # Add to existing knowledge base
        if self.embeddings is None:
            self.embeddings = new_embeddings
        else:
            self.embeddings = np.vstack([self.embeddings, new_embeddings])
        
        self.sentences.extend(new_sentences)
        print(f"Added {len(new_sentences)} sentences to knowledge base.")

    def get_relevant_context(self, query, num_results=3):
        """Get most relevant sentences for a query"""
        if not self.sentences:
            return []
        
        # Get query embedding
        query_embedding = self.model.encode([query])
        
        # Calculate similarities
        similarities = cosine_similarity(query_embedding, self.embeddings)[0]
        
        # Get top results
        top_indices = similarities.argsort()[-num_results:][::-1]
        return [self.sentences[i] for i in top_indices]