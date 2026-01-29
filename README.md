# Action Item Extractor – GenAI Document Assistant

## Overview
Action Item Extractor is a Generative AI–inspired application that automatically identifies actionable tasks from unstructured documents such as meeting notes, emails, and reports. Instead of summarizing text, the application focuses on answering a more practical question: **What needs to be done?**

## Problem Statement
Important action items are often buried inside lengthy documents. Manually scanning documents to find tasks, responsibilities, and deadlines is time-consuming and error-prone. This project automates that process using a prompt-driven Generative AI workflow.

## Solution
The application analyzes uploaded documents and extracts sentences that describe actions to be performed. These action items are presented in a clear, structured, and human-readable format.

## Supported File Types
- TXT files
- PDF documents

## How the Application Works
1. The user uploads a document containing unstructured text.
2. The document text is extracted and split into smaller chunks.
3. Each chunk is analyzed using a Generative AI–style reasoning layer.
4. Sentences indicating actions, responsibilities, or deadlines are identified.
5. The extracted action items are displayed as a clean list.

## Generative AI Architecture
This project follows a prompt-driven GenAI architecture:
- Document ingestion
- Chunking for large inputs
- Language understanding and reasoning
- Action-oriented information extraction
- Human-readable output

The system is designed to be compatible with low-code GenAI platforms such as Amazon PartyRock. The current implementation is provided as a Python-based prototype using Streamlit.

## Example Input
Meeting Notes:
"John will prepare the report by Friday. The HR team should update the onboarding documentation. A follow-up meeting must be scheduled next week."

## Example Output
1. John will prepare the report by Friday  
2. The HR team should update the onboarding documentation  
3. A follow-up meeting must be scheduled next week  

## Tech Stack
- Python
- Streamlit
- PyPDF2

## How to Run Locally
```bash
pip install streamlit PyPDF2
streamlit run app.py
