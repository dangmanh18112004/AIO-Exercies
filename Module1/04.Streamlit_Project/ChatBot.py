import streamlit as st
from hugchat import hugchat
from hugchat.login import Login

st.title("Chatbot")

with st.sidebar:
	st.title("Huggingface Account")
	hf_email = st.text_input("E-mail")
	hf_pass = st.text_input("Password", type='password')
	
if 'messages' not in st.session_state:
	st.session_state.messages = [{'role': 'assistant', 'content': 'How may I help me?'}]

for message in st.session_state.messages:
	with st.chat_message(message['role']):
		st.write(message['content'])
		
def generate_response(prompt_input, email, passwd):
    # Hugging Face Login
    sign = Login(email, passwd)
    cookies = sign.login()
    # Create ChatBot                        
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
    return chatbot.chat(prompt_input)


if prompt := st.chat_input(disabled=not(hf_email and hf_pass)):
	st.session_state.messages.append({'role': 'user', 'content': prompt})
	with st.chat_message('use'):
		st.write(prompt)
		
# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = generate_response(prompt, hf_email, hf_pass) 
            st.write(response) 
    message = {"role": "assistant", "content": response}
    st.session_state.messages.append(message)