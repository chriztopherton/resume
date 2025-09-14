import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from datetime import datetime, timedelta
import time

def contact_page():
    st.markdown('<h2 class="section-header">💬 Get In Touch</h2>', unsafe_allow_html=True)
    
    # Interactive contact methods
    st.markdown("### 🔗 Connect With Me")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Enhanced contact information with interactive cards
        st.markdown("""
        <div class="project-card">
            <h3 style="color: #2c3e50; margin-bottom: 1rem;">📧 Email</h3>
            <p style="font-size: 1.2rem; color: #3498db; font-weight: bold;">vchristopherton@gmail.com</p>
            <p style="color: #7f8c8d; margin-top: 0.5rem;">Primary communication method</p>
            <div style="margin-top: 1rem;">
                <a href="mailto:vchristopherton@gmail.com" style="background: #3498db; color: white; padding: 0.5rem 1rem; text-decoration: none; border-radius: 5px;">Send Email</a>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="project-card">
            <h3 style="color: #2c3e50; margin-bottom: 1rem;">📱 Phone</h3>
            <p style="font-size: 1.2rem; color: #3498db; font-weight: bold;"/p>
            <p style="color: #7f8c8d; margin-top: 0.5rem;">Available for calls and texts</p>
            <div style="margin-top: 1rem;">
                <a href="tel:+16692546967" style="background: #27ae60; color: white; padding: 0.5rem 1rem; text-decoration: none; border-radius: 5px;">Call Now</a>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="project-card">
            <h3 style="color: #2c3e50; margin-bottom: 1rem;">🔗 LinkedIn</h3>
            <p style="font-size: 1.2rem; color: #3498db; font-weight: bold;">linkedin.com/in/vchristopherton</p>
            <p style="color: #7f8c8d; margin-top: 0.5rem;">Professional network and updates</p>
            <div style="margin-top: 1rem;">
                <a href="https://linkedin.com/in/vchristopherton" target="_blank" style="background: #0077b5; color: white; padding: 0.5rem 1rem; text-decoration: none; border-radius: 5px;">Connect</a>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="project-card">
            <h3 style="color: #2c3e50; margin-bottom: 1rem;">💻 GitHub</h3>
            <p style="font-size: 1.2rem; color: #3498db; font-weight: bold;">github.com/vchristopherton</p>
            <p style="color: #7f8c8d; margin-top: 0.5rem;">Code portfolio and projects</p>
            <div style="margin-top: 1rem;">
                <a href="https://github.com/vchristopherton" target="_blank" style="background: #24292e; color: white; padding: 0.5rem 1rem; text-decoration: none; border-radius: 5px;">View Profile</a>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    
    # Form with enhanced styling
    with st.form("enhanced_contact_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("👤 Your Name *", placeholder="Enter your full name")
            email = st.text_input("📧 Email Address *", placeholder="your.email@example.com")
            company = st.text_input("🏢 Company/Organization", placeholder="Where do you work?")
        
        with col2:
            phone = st.text_input("📱 Phone Number", placeholder="Optional")
            subject = st.selectbox("📋 Subject *", [
                "Job Opportunity",
                "Project Collaboration", 
                "Technical Discussion",
                "Mentorship Request",
                "General Inquiry",
                "Other"
            ])
            urgency = st.selectbox("⚡ Urgency Level", [
                "Low - General inquiry",
                "Medium - Planning phase", 
                "High - Immediate need",
                "Critical - Urgent requirement"
            ])
        
        message = st.text_area("💭 Message *", height=150, placeholder="Tell me about your project, opportunity, or how I can help you...")
        
        # Additional options
        col1, col2, col3 = st.columns(3)
        with col1:
            preferred_contact = st.radio("📞 Preferred Contact Method", ["Email", "Phone", "LinkedIn"])
        with col2:
            timezone = st.selectbox("🌍 Your Timezone", [
                "PST (Pacific)",
                "MST (Mountain)", 
                "CST (Central)",
                "EST (Eastern)",
                "GMT/UTC",
                "Other"
            ])
        with col3:
            follow_up = st.checkbox("📅 Schedule a follow-up call")
        
        # Submit button with enhanced styling
        submit = st.form_submit_button("🚀 Send Message", type="primary", use_container_width=True)
        
        if submit:
            if name and email and message:
                # Success animation
                st.success("✅ Message sent successfully!")
                
                # Show next steps
                st.info("""
                **📋 Next Steps:**
                - I'll respond within 2 hours during business hours
                - Check your email for confirmation
                - Feel free to follow up if needed
                """)
                
                # Simulate response time
                with st.spinner("Preparing response..."):
                    time.sleep(2)
                
                st.success("📧 Auto-reply sent to your email!")
                
            else:
                st.error("❌ Please fill in all required fields (marked with *)")
    
    # Communication preferences and interests
    st.markdown("### 🎯 What I'm Looking For")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **💼 Professional Opportunities:**
        - Full-time ML/Data Engineering roles
        - Senior/Lead positions
        - Remote or hybrid work arrangements
        - Competitive compensation packages
        
        **🤝 Collaboration Types:**
        - Freelance consulting projects
        - Open-source contributions
        - Technical mentorship
        - Speaking engagements
        """)
    
    with col2:
        st.markdown("""
        **🛠️ Technical Interests:**
        - Large Language Models (LLMs)
        - MLOps and AI infrastructure
        - Data pipeline optimization
        - Cloud-native applications
        
        **🌍 Location Preferences:**
        - Remote-first opportunities
        - US-based positions
        - International projects
        - Travel opportunities
        """)
    
    # Call to action section
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, rgba(52, 152, 219, 0.1), rgba(231, 76, 60, 0.1)); border-radius: 15px;">
        <h2>🚀 Ready to Start a Conversation?</h2>
        <p style="font-size: 1.2rem; margin: 1rem 0;">I'm excited to hear about your opportunities and how we can work together.</p>
        <p style="color: #7f8c8d;">Let's build something amazing together!</p>
    </div>
    """, unsafe_allow_html=True) 