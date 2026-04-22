import streamlit as st
from textblob import TextBlob
import PyPDF2

st.title("🧠 Advanced Free AI Summarizer")

# TEXT INPUT
text = st.text_area("Paste your text")

# FILE UPLOAD
file = st.file_uploader("Upload PDF", type=["pdf"])

if file:
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

# LENGTH CONTROL
length = st.slider("Summary Length", 1, 5, 2)

def summarize(text, length):
    sentences = text.split(".")
    return ". ".join(sentences[:length])

# BULLET POINTS
def bullet_summary(text, length):
    sentences = text.split(".")
    return sentences[:length]

# SENTIMENT
def sentiment(text):
    return TextBlob(text).sentiment.polarity

# BUTTON
if st.button("Generate"):
    if text:
        st.subheader("Summary")
        st.write(summarize(text, length))

        st.subheader("Bullet Points")
        for i in bullet_summary(text, length):
            st.write("•", i)

        st.subheader("Sentiment")
        score = sentiment(text)
        if score > 0:
            st.success("Positive 😊")
        elif score < 0:
            st.error("Negative 😠")
        else:
            st.info("Neutral 😐")

    else:
        st.warning("Enter text or upload file")