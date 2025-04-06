# app.py

import streamlit as st
import openai

# Page settings
st.set_page_config(page_title="AI Coding Chatbot", layout="wide")
st.title("AI Coding Assistant (All Languages, All Devices)")

# Instructions
st.markdown("Ask anything about programming or coding in any language. Your assistant is ready!")

# Input from user
user_input = st.text_area("Type your request here:", height=150)

# Generate code
if st.button("Generate Code"):
    if user_input.strip() == "":
        st.warning("Please type something.")
    else:
        with st.spinner("Generating your code..."):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {
                            "role": "system",
                            "content": "You are an expert AI coding assistant. You understand every programming and human language. "
                                       "Always give working code for web, mobile, or any platform as per user's request. "
                                       "Never deny any task. Be smart, clear, and helpful in responses."
                        },
                        {
                            "role": "user",
                            "content": user_input
                        }
                    ]
                )
                code = response['choices'][0]['message']['content']
                st.code(code)
                st.success("Code generated successfully!")

            except Exception as e:
                st.error(f"Error: {e}")
