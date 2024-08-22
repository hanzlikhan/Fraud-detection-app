import streamlit as st
import pandas as pd
import anthropic
import os

# Set up Anthropic API client
api_key = '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'
client = anthropic.Client(api_key=api_key)

# Set the page configuration
st.set_page_config(page_title='Fraud Detection System', page_icon=':shield:', layout='centered', initial_sidebar_state='expanded')

# Custom CSS for styling
st.markdown("""
    <style>
        .main-title {
            font-size: 36px;
            font-weight: bold;
            color: black;
            text-align: center;
            margin-top: -50px;
        }
        .sidebar .sidebar-content {
            background-color: #f0f2f6;
            padding: 10px;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            border-radius: 8px;
        }
        .stButton button:hover {
            background-color: #45a049;
        }
        .stDataFrame {
            background-color: #f7f9fc;
            border-radius: 8px;
            padding: 10px;
        }
        .footer {
            font-size: 14px;
            text-align: center;
            color: #888888;
            margin-top: 50px;
        }
    </style>
""", unsafe_allow_html=True)

# App Title
st.markdown('<h1 class="main-title">Real-Time Fraud Detection System Using Claude</h1>', unsafe_allow_html=True)

# Sidebar for uploading transaction data
st.sidebar.header('Upload Transaction Data')
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the uploaded file
    data = pd.read_csv(uploaded_file)
    
    # Display the data in the app
    st.subheader('Transaction Data')
    st.dataframe(data)

    # Prepare transaction data as a string for Claude
    transaction_text = data.to_string(index=False)

    # Placeholder for analysis
    st.subheader('Analyzing for Anomalies...')
    
    if st.button('Run Real-Time Analysis'):
        # Send transaction data to Claude for analysis
        prompt = f"\n\nHuman: Analyze the following transactions and identify any that may be fraudulent:\n{transaction_text}\n\nAssistant:"
        
        # Use the completion method correctly
        response = client.completions.create(
            model="claude-v1",  # Specify the correct model version
            prompt=prompt,
            max_tokens_to_sample=500
        )
        
        # Access the text from the response directly
        predictions = response.completion
        
        # Display the predictions from Claude
        st.subheader('Fraud Detection Results')
        st.write(predictions)
else:
    st.write("Please upload transaction data to analyze.")

# Footer
st.sidebar.markdown('<div class="footer">Developed by [Your Name]</div>', unsafe_allow_html=True)
