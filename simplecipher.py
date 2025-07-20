import streamlit as st

def shift_letter(letter):
    if letter.isalpha():
        base = ord('A') if letter.isupper() else ord('a')
        return chr((ord(letter) - base + 1) % 26 + base)
    return letter

def shift_text(text):
    return ''.join(shift_letter(char) for char in text)

# Streamlit App UI
st.set_page_config(page_title="Simple Cipher", page_icon="🔐")

st.title("🔐 Simple Caesar Cipher (Shift by 1)")
st.write("This app shifts each letter by 1 position in the alphabet (A→B, Z→A).")

# Input
user_input = st.text_input("Enter a word or sentence:")

# Output
if user_input:
    shifted_output = shift_text(user_input)
    st.success(f"🔁 Shifted Output: {shifted_output}")
