from pyngrok import ngrok
import os

# Kill any previous tunnels
ngrok.kill()

# Open a tunnel on port 8501
public_url = ngrok.connect(8501, "http")  # ✅ Use int, not string!
print("Streamlit app is live at:", public_url)

# Launch your Streamlit app (this assumes your main file is app.py)
!streamlit run app.py &
