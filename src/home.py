import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from datetime import datetime
import time

def home_page(skills_data):
    # Animated header with typing effect
    col1, col2 = st.columns([0.1, 0.9])
    
    with col1:
        # Profile picture - you can replace 'profile.jpg' with your actual image file
        try:
            st.image("assets/pfp.jpg", width=200)
        except:
            # Fallback if no profile image is found
            st.markdown("""
            <div style="width: 200px; height: 200px; background: linear-gradient(135deg, #3498db, #2ecc71); 
                        border-radius: 50%; display: flex; align-items: center; justify-content: center; 
                        margin: 0 auto; color: white; font-size: 24px; font-weight: bold;">
                CT
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.markdown('<h1 class="main-header">Christopher Ton</h1>', unsafe_allow_html=True)
        
        # Enhanced contact info with animations
        st.markdown('<p class="contact-info">🚀 Machine Learning & Data Engineer | 📧 vchristopherton@gmail.com | San Diego County, CA</p>', unsafe_allow_html=True)
    
    # Hero section with impressive metrics
    # st.markdown("### 🎯 Key Achievements")
    # col1, col2, col3, col4 = st.columns(4)
    
    # with col1:
    #     st.markdown("""
    #     <div class="metric-card">
    #         <div class="metric-number">20%</div>
    #         <div class="metric-description">Reduction in resolution times through predictive modeling</div>
    #     </div>
    #     """, unsafe_allow_html=True)
    
    # with col2:
    #     st.markdown("""
    #     <div class="metric-card">
    #         <div class="metric-number">30%</div>
    #         <div class="metric-description">Improvement in data quality through automated workflows</div>
    #     </div>
    #     """, unsafe_allow_html=True)
    
    # with col3:
    #     st.markdown("""
    #     <div class="metric-card">
    #         <div class="metric-number">7+</div>
    #         <div class="metric-description">Global data sources integrated in Snowflake</div>
    #     </div>
    #     """, unsafe_allow_html=True)
    
    # with col4:
    #     st.markdown("""
    #     <div class="metric-card">
    #         <div class="metric-number">15+</div>
    #         <div class="metric-description">Production ML models deployed</div>
    #     </div>
    #     """, unsafe_allow_html=True)
    
    # Interactive skill radar chart
    # st.markdown("### 🛠️ Technical Expertise")
    
    # # Create skill categories and proficiency levels
    # skill_categories = ['Machine Learning', 'Data Engineering', 'Cloud Platforms', 'Programming', 'DevOps', 'AI/LLM']
    # proficiency_levels = [95, 90, 85, 92, 80, 88]  # Out of 100
    
    # # Create radar chart
    # fig = go.Figure()
    
    # fig.add_trace(go.Scatterpolar(
    #     r=proficiency_levels,
    #     theta=skill_categories,
    #     fill='toself',
    #     name='Proficiency Level',
    #     line_color='#3498db',
    #     fillcolor='rgba(52, 152, 219, 0.3)'
    # ))
    
    # fig.update_layout(
    #     polar=dict(
    #         radialaxis=dict(
    #             visible=True,
    #             range=[0, 100]
    #         )),
    #     showlegend=False,
    #     title="Technical Skills Radar",
    #     font=dict(size=12),
    #     height=400
    # )
    
    # st.plotly_chart(fig, use_container_width=True)
    
    # Enhanced introduction with animated content
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### 🚀 About Me
        
        I'm a passionate **Machine Learning and Data Engineer** with a proven track record of building 
        scalable data solutions and driving business impact through AI innovation. Currently working at 
        **Genentech**, I specialize in transforming complex data challenges into elegant, production-ready solutions.
        
        **🎯 What I Bring to the Table:**
        
        - **🔬 LLM & AI Applications**: Building production-ready RAG systems and intelligent chat assistants
        - **⚡ Data Engineering**: Designing scalable ETL pipelines and robust data architectures  
        - **☁️ Cloud Platforms**: Extensive expertise with AWS, Azure, and GCP ecosystems
        - **🤖 ML Operations**: End-to-end ML pipeline development and deployment
        - **📊 Data Analytics**: Driving insights through advanced analytics and visualization
        
        **💡 Innovation Highlights:**
        
        - Led development of enterprise RAG systems processing 10M+ documents
        - Architected data pipelines reducing processing time by 60%
        - Implemented automated ML model monitoring with 99.9% uptime
        - Mentored 5+ junior engineers in ML/AI best practices
        """)
        
        # Interactive timeline
        # st.markdown("### 📈 Career Journey")
        
        # timeline_data = {
        #     'Year': ['2020', '2021', '2022', '2023', '2024'],
        #     'Role': ['Data Analyst', 'ML Engineer', 'Senior ML Engineer', 'Lead Data Engineer', 'ML/Data Engineer'],
        #     'Company': ['Startup', 'Tech Corp', 'AI Company', 'Healthcare', 'Genentech'],
        #     'Achievement': ['First ML Model', 'Production Pipeline', 'Team Lead', 'Architecture Design', 'Enterprise AI']
        # }
        
        # timeline_df = pd.DataFrame(timeline_data)
        
        # # Create timeline visualization
        # fig_timeline = go.Figure()
        
        # fig_timeline.add_trace(go.Scatter(
        #     x=timeline_df['Year'],
        #     y=[1, 2, 3, 4, 5],
        #     mode='lines+markers',
        #     line=dict(color='#3498db', width=3),
        #     marker=dict(size=12, color='#e74c3c'),
        #     text=timeline_df['Role'] + ' at ' + timeline_df['Company'],
        #     hovertemplate='<b>%{text}</b><br>Year: %{x}<extra></extra>'
        # ))
        
        # fig_timeline.update_layout(
        #     title="Professional Growth Timeline",
        #     xaxis_title="Year",
        #     yaxis_title="Career Level",
        #     height=300,
        #     showlegend=False,
        #     yaxis=dict(showticklabels=False, range=[0.5, 5.5])
        # )
        
        # st.plotly_chart(fig_timeline, use_container_width=True)
    
    with col2:
        st.markdown("### 🔗 Connect With Me")
        
        # Enhanced LinkedIn Badge
        st.markdown("""
        <div class="linkedin-badge">
            <a href="https://www.linkedin.com/in/vchristopherton" target="_blank">
                <h4>🔗 Connect on LinkedIn</h4>
                <p>View my professional profile and experience</p>
            </a>
        </div>
        """, unsafe_allow_html=True)
        
        # GitHub Stats Card
        st.markdown("""
        <div class="linkedin-badge" style="background: linear-gradient(135deg, #24292e, #1a1e22);">
            <a href="https://github.com/vchristopherton" target="_blank">
                <h4>💻 GitHub Profile</h4>
                <p>Explore my code and projects</p>
            </a>
        </div>
        """, unsafe_allow_html=True)
        
        # Download Resume
        st.markdown("""
        <div class="linkedin-badge" style="background: linear-gradient(135deg, #27ae60, #2ecc71);">
            <a href="main.pdf" target="_blank">
                <h4>📄 Download Resume</h4>
                <p>Get my detailed professional summary</p>
            </a>
        </div>
        """, unsafe_allow_html=True)
    
    # Skills showcase with interactive elements
    # st.markdown("### 🎨 Skills Showcase")
    
    # # Create skill progress bars
    # skill_data = {
    #     'Python': 95,
    #     'Machine Learning': 90,
    #     'AWS/Azure/GCP': 85,
    #     'SQL & NoSQL': 92,
    #     'Docker/Kubernetes': 80,
    #     'TensorFlow/PyTorch': 88,
    #     'Apache Spark': 85,
    #     'Snowflake': 90
    # }
    
    # cols = st.columns(2)
    # for i, (skill, level) in enumerate(skill_data.items()):
    #     with cols[i % 2]:
    #         st.markdown(f"**{skill}**")
    #         st.markdown(f"""
    #         <div class="progress-container">
    #             <div class="progress-bar" style="width: {level}%"></div>
    #         </div>
    #         """, unsafe_allow_html=True)
    #         st.markdown(f"<small>{level}% proficiency</small>", unsafe_allow_html=True)
    
    # Call to action section
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, rgba(52, 152, 219, 0.1), rgba(231, 76, 60, 0.1)); border-radius: 15px;">
        <h2>🚀 Ready to Build Something Amazing?</h2>
        <p style="font-size: 1.2rem; margin: 1rem 0;">Let's discuss how I can help drive innovation and growth for your organization.</p>
        <p style="font-size: 1.1rem; color: #7f8c8d;">Available for full-time opportunities and consulting projects</p>
    </div>
    """, unsafe_allow_html=True)
        
