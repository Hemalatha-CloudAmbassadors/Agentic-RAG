# Local Agentic RAG System (No API Required)
A simple implementation of a local Retrieval-Augmented Generation (RAG) system with agent-like capabilities.

## Project Overview
```
local_agentic_rag/
│
├── data/
│   └── knowledge.txt          # Initial knowledge base
├── src/
│   ├── __init__.py
│   ├── agent.py              # Agent implementation
│   ├── knowledge_base.py     # Knowledge base management
│   └── utils.py              # Utility functions
├── requirements.txt          # Project dependencies
├── main.py                   # Main application
└── README.md                 # This file
```

## Prerequisites
- Python 3.8 or higher
- Windows/Linux/MacOS

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/local_agentic_rag.git
cd local_agentic_rag
```

2. Create a virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/MacOS
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the application:
```bash
python main.py
```

2. Available Commands:
- Ask any question about the knowledge base
- `exit`: Quit the program
- `load <filename>`: Load additional knowledge from a file
- `history`: Show conversation history

## Example Interactions
```
Your question: What is Python?
Processing...
Answer: Python is a popular programming language created by Guido van Rossum.

Your question: What can I use Python for?
Processing...
Answer: Python can be used for web development, automation, data analysis, and artificial intelligence.
```

## Adding Custom Knowledge

1. Direct file modification:
   - Edit `data/knowledge.txt`
   - Restart the program

2. Loading additional files:
   ```bash
   Your question: load my_new_knowledge.txt
   ```

## Features
- 🚀 Completely local operation (no API keys needed)
- 📚 Expandable knowledge base
- 💬 Conversation history
- 🔄 Context-aware responses
- 🛠 Modular design
- ⚡ Fast response time

## System Requirements
- RAM: Minimum 4GB (8GB recommended)
- Disk Space: ~2GB (for models and dependencies)
- CPU: Any modern processor (GPU not required)

## Customization

### Modifying the Knowledge Base
Create a text file with your custom knowledge:
```text
# custom_knowledge.txt
Your custom information here.
Each sentence will be processed separately.
Add as many sentences as needed.
```

### Adjusting Response Generation
Edit `src/agent.py`:
```python
def _generate_response(self, query, context):
    # Modify this method to customize response generation
    pass
```

### Changing the Embedding Model
Edit `src/knowledge_base.py`:
```python
class KnowledgeBase:
    def __init__(self):
        # Change model name here
        self.model = SentenceTransformer('your-preferred-model')
```

## Troubleshooting

### Common Issues and Solutions

1. Module Not Found Error:
```bash
pip install -r requirements.txt --no-cache-dir
```

2. Memory Issues:
- Reduce knowledge base size
- Use a smaller embedding model

3. Slow Response Time:
- Reduce context window size
- Optimize knowledge base

## Development

### Adding New Features
1. Create new module in `src/`
2. Import in `main.py`
3. Update requirements if needed

### Running Tests
```bash
python -m unittest tests/*.py
```

## Project Structure Details

### agent.py
Handles:
- Query processing
- Response generation
- Conversation management

### knowledge_base.py
Manages:
- Document storage
- Embedding creation
- Similarity search

### utils.py
Provides:
- File operations
- Text processing
- Helper functions
