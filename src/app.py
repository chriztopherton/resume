import streamlit as st
from streamlit_option_menu import option_menu

from ai_chatbot import render_ai_chatbot

# Import chatbot
from contact import contact_page

# Import data
from data import experience_data, skills_data
from education import education_page
from experience import experience_page

# Import modularized pages
from home import home_page

# Page configuration
st.set_page_config(
    page_title="Christopher Ton - ML/Data Engineer",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded",
)

# Enhanced Custom CSS with animations and modern design
st.markdown(
    """
<style>
    /* Modern gradient background */
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        min-height: 100vh;
    }

    /* Animated header with typing effect */
    .main-header {
        font-size: 3.5rem;
        font-weight: bold;
        text-align: center;
        background: linear-gradient(45deg, #ff6b6b, #4ecdc4, #45b7d1, #96ceb4);
        background-size: 400% 400%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: gradientShift 3s ease-in-out infinite, fadeInUp 1s ease-out;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }

    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    /* Enhanced section headers with hover effects */
    .section-header {
        font-size: 2.2rem;
        font-weight: bold;
        color: #2c3e50;
        border-bottom: 3px solid #3498db;
        padding-bottom: 0.5rem;
        margin-bottom: 1.5rem;
        position: relative;
        transition: all 0.3s ease;
    }

    .section-header:hover {
        transform: translateX(10px);
        border-bottom-color: #e74c3c;
    }

    .section-header::after {
        content: '';
        position: absolute;
        bottom: -3px;
        left: 0;
        width: 0;
        height: 3px;
        background: linear-gradient(90deg, #3498db, #e74c3c);
        transition: width 0.3s ease;
    }

    .section-header:hover::after {
        width: 100%;
    }

    /* Enhanced job cards with hover animations */
    .job-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
        border-left: 4px solid #3498db;
    }

    .job-card:hover {
        transform: translateY(-5px) scale(1.02);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
        border-left-color: #e74c3c;
    }

    .job-title {
        font-size: 1.4rem;
        font-weight: bold;
        color: #34495e;
        margin-bottom: 0.5rem;
        transition: color 0.3s ease;
    }

    .job-card:hover .job-title {
        color: #e74c3c;
    }

    .company-name {
        font-size: 1.2rem;
        color: #7f8c8d;
        font-weight: 500;
    }

    /* Enhanced skill badges with animations */
    .skill-badge {
        background: linear-gradient(135deg, #3498db, #2980b9);
        color: white;
        padding: 0.4rem 1rem;
        border-radius: 20px;
        font-size: 0.9rem;
        margin: 0.3rem;
        display: inline-block;
        transition: all 0.3s ease;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        cursor: pointer;
    }

    .skill-badge:hover {
        transform: translateY(-2px) scale(1.05);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        background: linear-gradient(135deg, #e74c3c, #c0392b);
    }

    /* Enhanced metric cards with pulse animation */
    .metric-card {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        padding: 1.5rem;
        border-radius: 15px;
        border-left: 4px solid #3498db;
        margin: 0.5rem 0;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }

    .metric-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.1);
    }

    .metric-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
        transition: left 0.5s ease;
    }

    .metric-card:hover::before {
        left: 100%;
    }

    .metric-number {
        font-size: 2.5rem;
        font-weight: bold;
        color: #3498db;
        text-align: center;
        margin-bottom: 0.5rem;
    }

    .metric-description {
        text-align: center;
        color: #7f8c8d;
        font-size: 0.9rem;
    }

    /* Enhanced contact info */
    .contact-info {
        text-align: center;
        font-size: 1.2rem;
        color: #7f8c8d;
        margin-bottom: 2rem;
        padding: 1rem;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        backdrop-filter: blur(10px);
        animation: fadeInUp 1s ease-out 0.5s both;
    }

    /* Enhanced LinkedIn badge with 3D effect */
    .linkedin-badge {
        background: linear-gradient(135deg, #0077b5, #005885);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        margin: 1rem 0;
        box-shadow: 0 8px 25px rgba(0, 123, 181, 0.3);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }

    .linkedin-badge::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(45deg, transparent 30%, rgba(255,255,255,0.1) 50%, transparent 70%);
        transform: translateX(-100%);
        transition: transform 0.6s ease;
    }

    .linkedin-badge:hover {
        transform: translateY(-5px) scale(1.02);
        box-shadow: 0 12px 35px rgba(0, 123, 181, 0.4);
    }

    .linkedin-badge:hover::before {
        transform: translateX(100%);
    }

    .linkedin-badge h4 {
        margin: 0 0 0.5rem 0;
        font-size: 1.3rem;
        position: relative;
        z-index: 1;
    }

    .linkedin-badge p {
        margin: 0;
        font-size: 1rem;
        opacity: 0.9;
        position: relative;
        z-index: 1;
    }

    .linkedin-badge a {
        color: white;
        text-decoration: none;
        display: block;
        position: relative;
        z-index: 1;
    }

    .linkedin-badge a:hover {
        color: #e1f5fe;
    }

    /* Project cards with glassmorphism effect */
    .project-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2rem;
        margin: 1.5rem 0;
        border: 1px solid rgba(255, 255, 255, 0.2);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }

    .project-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, #3498db, #e74c3c, #f39c12);
        transform: scaleX(0);
        transition: transform 0.3s ease;
    }

    .project-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
    }

    .project-card:hover::before {
        transform: scaleX(1);
    }

    /* Animated progress bars */
    .progress-container {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
        backdrop-filter: blur(10px);
    }

    .progress-bar {
        height: 8px;
        background: linear-gradient(90deg, #3498db, #e74c3c);
        border-radius: 4px;
        transition: width 1s ease;
        position: relative;
        overflow: hidden;
    }

    .progress-bar::after {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
        animation: shimmer 2s infinite;
    }

    @keyframes shimmer {
        0% { left: -100%; }
        100% { left: 100%; }
    }

    /* Floating action button */
    .fab {
        position: fixed;
        bottom: 30px;
        right: 30px;
        width: 60px;
        height: 60px;
        background: linear-gradient(135deg, #3498db, #e74c3c);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 24px;
        cursor: pointer;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        transition: all 0.3s ease;
        z-index: 999;
    }

    .fab:hover {
        transform: scale(1.1);
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
    }

    /* Loading animation */
    .loading {
        display: inline-block;
        width: 20px;
        height: 20px;
        border: 3px solid rgba(255,255,255,.3);
        border-radius: 50%;
        border-top-color: #fff;
        animation: spin 1s ease-in-out infinite;
    }

    @keyframes spin {
        to { transform: rotate(360deg); }
    }

    /* Responsive design */
    @media (max-width: 768px) {
        .main-header {
            font-size: 2.5rem;
        }
        .section-header {
            font-size: 1.8rem;
        }
    }


</style>
<script type="text/javascript" src="https://platform.linkedin.com/badges/js/profile.js" async defer></script>
""",
    unsafe_allow_html=True,
)

# Enhanced Navigation with animations
selected = option_menu(
    menu_title=None,
    options=["Home", "Experience", "Education", "Contact"],
    icons=["house", "briefcase", "tools", "folder", "mortarboard", "envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {
            "padding": "0!important",
            "background-color": "#ffffff",
            "border-radius": "10px",
            # "margin": "1rem 0",
            "box-shadow": "0 2px 10px rgba(0, 0, 0, 0.1)",
        },
        # "icon": {"color": "#3498db", "font-size": "18px"},
        "nav-link": {
            "font-size": "16px",
            "text-align": "center",
            "margin": "0px",
            # "--hover-color": "#e74c3c",
            "border-radius": "10px",
            "transition": "all 0.3s ease",
            "padding": "0.75rem 1rem",
        },
        "nav-link-selected": {
            "background-color": "#3498db",
            # "color": "white"
        },
    },
)

# Add floating action button for quick contact
st.markdown(
    """
<div class="fab" onclick="window.open('mailto:vchristopherton@gmail.com')">
    Email
</div>
""",
    unsafe_allow_html=True,
)

# Main app logic with enhanced user experience
if selected == "Home":
    home_page(skills_data)
elif selected == "Experience":
    experience_page(experience_data)
# elif selected == "Projects":
#     projects_page(projects_data)
elif selected == "Education":
    education_page()
elif selected == "Contact":
    contact_page()

# Render AI-powered chatbot (always visible)
render_ai_chatbot()
