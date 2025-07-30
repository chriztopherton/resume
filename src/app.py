import streamlit as st
from streamlit_option_menu import option_menu

# Import modularized pages
from home import home_page
from experience import experience_page
from skills import skills_page
from projects import projects_page
from education import education_page
from contact import contact_page

# Import data
from data import experience_data, skills_data, projects_data

# Import chatbot
from chatbot import render_chatbot
from chatbot_floating import render_floating_chatbot
from ai_chatbot import render_ai_chatbot, render_floating_ai_chatbot

# Page configuration
st.set_page_config(
    page_title="Christopher Ton - ML/Data Engineer",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 1rem;
    }
    .section-header {
        font-size: 2rem;
        font-weight: bold;
        color: #2c3e50;
        border-bottom: 3px solid #3498db;
        padding-bottom: 0.5rem;
        margin-bottom: 1.5rem;
    }
    .job-title {
        font-size: 1.3rem;
        font-weight: bold;
        color: #34495e;
    }
    .company-name {
        font-size: 1.1rem;
        color: #7f8c8d;
    }
    .skill-badge {
        background-color: #3498db;
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 15px;
        font-size: 0.9rem;
        margin: 0.2rem;
        display: inline-block;
    }
    .metric-card {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #3498db;
        margin: 0.5rem 0;
    }
    .contact-info {
        text-align: center;
        font-size: 1.1rem;
        color: #7f8c8d;
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# Navigation
selected = option_menu(
    menu_title=None,
    options=["Home", "Experience", "Projects", "Education", "Contact"],
    icons=["house", "briefcase", "tools", "folder", "mortarboard", "envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "#3498db", "font-size": "18px"},
        "nav-link": {
            "font-size": "16px",
            "text-align": "left",
            "margin": "0px",
            "--hover-color": "#3498db",
        },
        "nav-link-selected": {"background-color": "#3498db"},
    }
)





# Main app logic
if selected == "Home":
    home_page(skills_data)
elif selected == "Experience":
    experience_page(experience_data)
# elif selected == "Skills":
#     skills_page(skills_data)
elif selected == "Projects":
    projects_page(projects_data)
elif selected == "Education":
    education_page()
elif selected == "Contact":
    contact_page()

# Render chatbot (always visible)
# Choose which chatbot to use:
# Option 1: AI-powered sidebar chatbot (recommended)
render_ai_chatbot()

# Option 2: Original rule-based chatbot
# render_chatbot()

# Option 3: Floating AI chatbot (uncomment to use instead)
# render_floating_ai_chatbot()

# Option 4: Original floating chatbot
# render_floating_chatbot()
