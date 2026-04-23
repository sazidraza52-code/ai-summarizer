import streamlit as st
from PyPDF2 import PdfReader
from PIL import Image
from textblob import TextBlob

st.set_page_config(page_title="AI Summarizer", layout="centered")

# -------- FUNCTIONS --------
def summarize(text, length=2):
    sentences = text.split(".")
    return ". ".join(sentences[:length])

def bullet_points(text, length=3):
    sentences = text.split(".")
    return sentences[:length]

def get_sentiment(text):
    score = TextBlob(text).sentiment.polarity
    if score > 0:
        return "Positive 😊"
    elif score < 0:
        return "Negative 😠"
    else:
        return "Neutral 😐"

def extract_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def extract_image(file):
    return "⚠️ Image OCR not supported in free version"

# -------- MENU --------
menu = st.sidebar.selectbox("Menu", ["Home", "About Us", "Contact", "Privacy Policy"])

# -------- HOME --------
if menu == "Home":
    st.title("🧠 AI Summarizer")

    option = st.selectbox("Choose Input Type", ["Text", "PDF", "Image"])

    text = ""

    if option == "Text":
        text = st.text_area("Paste your text")

    elif option == "PDF":
        file = st.file_uploader("Upload PDF", type=["pdf"])
        if file:
            text = extract_pdf(file)

    elif option == "Image":
        file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])
        if file:
            text = extract_image(file)

    length = st.slider("Summary Length", 1, 5, 2)

    if st.button("Generate Summary"):
        if text:
            st.subheader("Summary")
            st.write(summarize(text, length))

            st.subheader("Bullet Points")
            for i in bullet_points(text, length):
                st.write("•", i)

            st.subheader("Sentiment")
            st.write(get_sentiment(text))
        else:
            st.warning("Please provide input")

    st.markdown("---")
    st.write("Created and developed by Sazid Shaikh")

# -------- ABOUT --------
elif menu == "About Us":
    st.title("About Us")
    st.write("This AI summarizer helps students summarize text, PDFs and images easily.")

# -------- CONTACT --------
elif menu == "Contact":
    st.title("Contact")
    st.write("Email: shazidraja0@gmail.com")

# -------- PRIVACY --------
elif menu == "Privacy Policy":
    st.title("Privacy Policy")
    st.write("We do not store any user data. All processing happens temporarily.")
