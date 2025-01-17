import streamlit as st
from dotenv import dotenv_values

# Load environment
env = dotenv_values(".env")

# Streamlit Page Properties
page_title = env["PAGE_TITLE"]
title = env["TITLE"]

st.set_page_config(page_title=page_title, page_icon="🚀")

# Custom CSS to enhance the UI
st.markdown("""
    <style>
        /* Page Title Styling */
        .css-1v3fvcr { color: #1F77B4; font-family: 'Arial', sans-serif; }
        
        /* Custom Markdown Style */
        .markdown-text-container {
            background-color: #F0F8FF;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }

        /* Sidebar Styling */
        .css-1v0mbdj { background-color: #222222; color: white; padding: 15px; }

        .css-1vq4g9d {
            background-color: #9C27B0;
            color: white;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Set the title and subtitle for the main page
st.title(f"<span style='color:#4B9CD3;'>{title}</span>", unsafe_allow_html=True)

# Sidebar with a welcome message and cool accent colors
st.sidebar.markdown("""
    <div style="background-color: #333333; padding: 20px; color: white; border-radius: 8px;">
        <h3>Welcome to SnapLogic Gen AI Builder!</h3>
        <p style="font-size: 14px;">Choose from a variety of demos to see the potential of our tool.</p>
        <p><strong>📚 Learn More:</strong></p>
        <ul style="font-size: 14px; line-height: 1.8;">
            <li><a href="https://www.snaplogic.com/products/agent-creator" target="_blank" style="color: #9C27B0;">Agent Creator</a></li>
            <li><a href="https://docs-snaplogic.atlassian.net/wiki/spaces/SD/overview?homepageId=34537" target="_blank" style="color: #9C27B0;">Documentation</a></li>
            <li><a href="https://community.snaplogic.com" target="_blank" style="color: #9C27B0;">Community</a></li>
        </ul>
    </div>
""", unsafe_allow_html=True)

# Main content with a nice background
st.markdown("""
    <div class="markdown-text-container">
        ## 🚀 SnapLogic Gen AI Builder
        Allows you to create LLM-based applications in no time!
        ### **⬅️ Select a demo from the sidebar** to see some examples of what Gen AI Builder can do!
    </div>
""", unsafe_allow_html=True)

# Add a sample button for interaction
if st.button("🔍 Explore Demos"):
    st.markdown("""
        <div style="background-color: #9C27B0; color: white; padding: 10px; border-radius: 8px; text-align: center;">
            <h3>Choose a demo to begin!</h3>
            <p>Click on one of the demos in the sidebar to explore different features and functionalities.</p>
        </div>
    """, unsafe_allow_html=True)
