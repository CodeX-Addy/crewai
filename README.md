# CrewAI

CrewAI is a project that simulates an interactive Q&A system using Crew AI and Langraph, where a student agent asks popular questions about generative AI, and a teacher agent provides automated responses. The system uses the Gemini API as the backend large language model.

## Requirements

Ensure you have the following installed:

- Python 3.8+
- Crew AI and Langraph packages
- Gemini API (configured and authorized)
- Any necessary Python libraries (see the `requirements.txt`)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/CodeX-Addy/crewai.git
   cd crewai
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows
   ```
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Gemini API**:
   ```bash
   export GEMINI_API_KEY="your_api_key_here"  # On Linux/Mac
   set GEMINI_API_KEY="your_api_key_here"     # On Windows
   ```
5. **Run the main script**:
   ```bash
   python crew.py
   ```

