import streamlit as st

# Page Configuration for a modern SaaS feel
st.set_page_config(page_title="BrainAI Content Studio", page_icon="🧠", layout="centered")

st.title("🧠 BrainAI Content Studio")
st.markdown("### The ultimate MVP for high-scale content creation.")

# Initialize chat history for session persistence
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Ask BrainAI to write a blog, script, or tweet..."):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.spinner("Generating viral content..."):
        # Format history for the API (extracting only content/role)
        history_for_api = [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages[:-1]]
        
        # Call our Cohere function
        response = get_cohere_response(prompt, history_for_api)

    # Display assistant response
    with st.chat_message("assistant"):
        st.markdown(response)
    
    # Add assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": response})