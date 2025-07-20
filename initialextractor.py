import streamlit as st

def extract_initials(full_name):
    # Remove leading/trailing spaces and split into words
    words = full_name.strip().split()
    # Extract and capitalize first letters
    initials = ''.join(word[0].upper() for word in words if word)
    return initials

# Streamlit UI
st.set_page_config(page_title="Initial Extractor", page_icon="🔠")

st.title("🔠 Initial Extractor")
st.write("Enter a full name and get the capitalized initials.")

# Input from user
user_input = st.text_input("Enter Full Name:")

# Output display
if user_input:
    initials = extract_initials(user_input)
    st.success(f"🆎 Extracted Initials: {initials}")
