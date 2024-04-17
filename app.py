from openai import OpenAI
import streamlit as st

# Read the API key and setup an OpenAI client
f = open('keys/.openai_key2.txt')
key = f.read()
client = OpenAI(api_key = key)

st.title("💻 AI Code Reviewer 🔍")


prompt = st.text_area("Enter your python code here...")

if st.button("Generate") == True:
    response = client.chat.completions.create(
      model="gpt-3.5-turbo-0301",
      messages=[
        {"role": "system", "content": """You are a helpful AI Assistant.
                                    You are an Expert in code review. so find bugs, 
                                    explain the bugs errors and give the corrected code."""},
        {"role": "user", "content": prompt}
      ]
    )
    st.write(response.choices[0].message.content)