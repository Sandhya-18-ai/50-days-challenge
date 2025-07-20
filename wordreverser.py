import streamlit as st

def reverse_words(sentence):
    words = sentence.strip().split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)

# Streamlit UI
st.set_page_config(page_title="Word Reverser", page_icon="🔁")

st.title("🔁 Word Reverser App")
st.write("This app reverses **individual words** in the sentence.")

user_input = st.text_input("Enter a sentence:")

if user_input:
    output = reverse_words(user_input)
    st.success(f"🔄 Reversed Words: {output}")
