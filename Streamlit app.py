!pip install streamlit
!pip install pyngrok
!pip install requests

%%writefile app.py
import streamlit as st
import requests

# Replace with your API Gateway Invoke URL
api_url = "Replace with your API Gateway Invoke URL"

# Streamlit app UI
st.title("Audiobook Recommendation")

query = st.text_input("Enter your query:")
if query:
    # Sending the user input query to the API Gateway (Lambda function)
    response = requests.post(api_url, json={"query": query})

    # Check if the response is successful
    if response.status_code == 200:
        data = response.json()
        recommendations_text = data.get("recommendations", "")
    if recommendations_text:
        st.write("Top 3 Recommended Books:")
        st.markdown(recommendations_text)
    else:
        st.write("No recommendations found.")


