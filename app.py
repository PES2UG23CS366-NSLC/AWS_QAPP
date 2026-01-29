import streamlit as st
import pandas as pd
from PyPDF2 import PdfReader

st.set_page_config(
    page_title="Action Item Extractor",
    page_icon="📝",
    layout="centered"
)

# ---------------- UI HEADER ----------------
st.title("📝 Action Item Extractor")
st.caption(
    "Upload documents (TXT, PDF, CSV) and automatically extract action items."
)

uploaded_file = st.file_uploader(
    "Upload a TXT, PDF, or CSV file",
    type=["txt", "pdf", "csv"]
)

# ---------------- UTILITY FUNCTIONS ----------------

def extract_text(file):
    if file.name.endswith(".txt"):
        return file.read().decode("utf-8")

    elif file.name.endswith(".pdf"):
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text

    elif file.name.endswith(".csv"):
        df = pd.read_csv(file)
        # Convert rows to free-form text
        text_rows = []
        for _, row in df.iterrows():
            text_rows.append(" ".join(row.astype(str).values))
        return ". ".join(text_rows)

    return ""

def chunk_text(text, chunk_size=400):
    words = text.split()
    return [
        " ".join(words[i:i + chunk_size])
        for i in range(0, len(words), chunk_size)
    ]

def ai_extract_actions(text_chunk):
    """
    Simulated GenAI reasoning layer.
    Designed to be compatible with Amazon PartyRock / Amazon Q.
    """
    sentences = text_chunk.split(".")
    action_sentences = []

    keywords = [
        "will", "should", "must", "need to",
        "responsible for", "assigned to", "by"
    ]

    for sentence in sentences:
        for kw in keywords:
            if kw in sentence.lower():
                clean = sentence.strip()
                if len(clean) > 15:
                    action_sentences.append(clean)
                break

    return action_sentences

# ---------------- MAIN LOGIC ----------------

if uploaded_file:
    with st.spinner("Analyzing document..."):
        raw_text = extract_text(uploaded_file)

        if not raw_text.strip():
            st.error("Could not extract text from the uploaded file.")
        else:
            chunks = chunk_text(raw_text)
            extracted_actions = []

            for chunk in chunks:
                extracted_actions.extend(ai_extract_actions(chunk))

            st.subheader("📌 Extracted Action Items")

            if extracted_actions:
                for i, action in enumerate(extracted_actions, start=1):
                    st.markdown(f"**{i}.** {action}")
            else:
                st.info("No actionable tasks were identified in this document.")

else:
    st.info("Please upload a TXT, PDF, or CSV file to begin.")
