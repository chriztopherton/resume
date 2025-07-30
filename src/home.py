import streamlit as st
import plotly.express as px
import pandas as pd

def home_page(skills_data):
    st.markdown('<h1 class="main-header">Christopher Ton</h1>', unsafe_allow_html=True)
    st.markdown('<p class="contact-info">🚀 Machine Learning & Data Engineer | 📧 christopher.ton@sjsu.edu | 📱 (669) 254-6967</p>', unsafe_allow_html=True)
    
    # Introduction
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### About Me
        I'm a passionate Machine Learning and Data Engineer with expertise in building scalable data solutions, 
        developing AI applications, and driving data-driven insights. Currently working at Genentech, I specialize in:
        
        - **LLM & AI Applications**: Building production-ready RAG systems and chat assistants
        - **Data Engineering**: Designing scalable ETL pipelines and data architectures
        - **Cloud Platforms**: Extensive experience with AWS, Azure, and GCP
        - **ML Operations**: End-to-end ML pipeline development and deployment
        """)
        
    #     # Key metrics
    #     st.markdown("### Key Achievements")
    #     col1, col2, col3 = st.columns(3)
        
    #     with col1:
    #         st.markdown("""
    #         <div class="metric-card">
    #             <h4>20%</h4>
    #             <p>Reduction in resolution times through predictive modeling</p>
    #         </div>
    #         """, unsafe_allow_html=True)
        
    #     with col2:
    #         st.markdown("""
    #         <div class="metric-card">
    #             <h4>30%</h4>
    #             <p>Improvement in data quality through automated workflows</p>
    #         </div>
    #         """, unsafe_allow_html=True)
        
    #     with col3:
    #         st.markdown("""
    #         <div class="metric-card">
    #             <h4>7+</h4>
    #             <p>Global data sources integrated in Snowflake</p>
    #         </div>
    #         """, unsafe_allow_html=True)
    
    # with col2:
    #     st.markdown("### Quick Stats")
        
    #     # Skills visualization
    #     all_skills = []
    #     for category, skills in skills_data.items():
    #         all_skills.extend(skills)
        
    #     # Create a simple skill frequency chart
    #     skill_counts = pd.Series(all_skills).value_counts().head(10)
        
    #     fig = px.bar(
    #         x=skill_counts.values,
    #         y=skill_counts.index,
    #         orientation='h',
    #         title="Top Skills",
    #         labels={'x': 'Frequency', 'y': 'Skills'}
    #     )
    #     fig.update_layout(height=400, showlegend=False)
    #     st.plotly_chart(fig, use_container_width=True) 