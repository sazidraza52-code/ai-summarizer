import streamlit as st
from PyPDF2 import PdfReader

st.set_page_config(page_title="AI Summarizer", layout="centered")

# ---------- SIDEBAR ----------
menu = st.sidebar.selectbox("Menu", [
    "Home",
    "About Us",
    "Contact",
    "Privacy Policy",
    "Terms & Conditions"
])

st.sidebar.markdown("---")
st.sidebar.write("👑 Premium Unlock Required for Image Upload")

# ---------- FUNCTIONS ----------

def summarize(text, length=3):
    sentences = text.split(".")
    return ". ".join(sentences[:length])

def extract_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def image_premium():
    return "⚠️ Image summarization is a PREMIUM feature. Please upgrade."

# ---------- HOME ----------
if menu == "Home":
    st.title("🧠 AI Summarizer")
    st.write("✨ Created and developed by Sazid Shaikh")

    option = st.radio("Choose Input Type", ["Text", "PDF File", "Image (Premium)"])

    length = st.slider("Summary Length", 1, 10, 3)

    text_data = ""

    if option == "Text":
        text_data = st.text_area("Paste your text here")

    elif option == "PDF File":
        file = st.file_uploader("Upload PDF", type=["pdf"])
        if file:
            text_data = extract_pdf(file)

    elif option == "Image (Premium)":
        file = st.file_uploader("Upload Image", type=["jpg", "png"])
        if file:
            st.error(image_premium())

    if st.button("Summarize"):
        if text_data:
            summary = summarize(text_data, length)
            st.subheader("📌 Summary")
            st.write(summary)

            st.download_button("Download Summary", summary)

        else:
            st.warning("Please enter or upload data")

# ---------- ABOUT ----------
elif menu == "About Us":
    st.title("About Us")
    st.write("""
This AI Summarizer helps users quickly convert long text into short summaries.

🔹 Free Features:
- Text summarization
- PDF summarization
- Adjustable summary length

🔹 Premium Features:
- Image summarization (OCR)
- Advanced AI summaries
""")

# ---------- CONTACT ----------
elif menu == "Contact":
    st.title("Contact Us")
    st.write("📧 Email: shazidraja0@gmail.com")

# ---------- PRIVACY ----------
elif menu == "Privacy Policy":
    st.title("Privacy Policy")
    st.write("""
We respect your privacy.

✔ We do NOT store your data  
✔ All processing is temporary  
✔ No personal data is saved  
""")

# ---------- TERMS ----------
elif menu == "Terms & Conditions":
    st.title("Terms & Conditions")
    st.write("""
By using this website, you agree:

✔ Do not misuse the tool  
✔ No illegal content  
✔ Premium features require payment  

We are not responsible for misuse of generated summaries.
""")
